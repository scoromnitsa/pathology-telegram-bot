import os
import random
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database_macro import session as macro_session, QuizQuestion as MacroQuizQuestion
from database_micro import session as micro_session, QuizQuestion as MicroQuizQuestion

bot = telebot.TeleBot('')

user_data = {}

# Главное меню
@bot.message_handler(commands=['start'])
def start(message):
    buttons = [
        ("Список препаратов", "list"),
        ("Алгоритмы описания препаратов", "algorythm"),
        ("Похожие препараты", "similar"),
        ("Синонимичные названия", "synonim"),
        ("Тест", "test"),
        ("Проверка с ручным вводом", "writing_check")
    ]
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(*[InlineKeyboardButton(text, callback_data=callback) for text, callback in buttons])

    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)

# Команды меню
@bot.callback_query_handler(func=lambda call: call.data in ["similar", "synonim"])
def handle_menu_commands(call):
    responses = {
        "similar": "Раздел в разработке",
        "synonim": "Раздел в разработке",
    }
    bot.send_message(call.message.chat.id, responses.get(call.data, "Неизвестная команда"))

@bot.callback_query_handler(func=lambda call: call.data == "list")
def send_list(call):
    chat_id = call.message.chat.id
    file_path = "C:/pathology_test_bot/files/список-препаратов (Сеченова 24-25).docx" 
    
    with open(file_path, 'rb') as file:
        bot.send_document(chat_id, file)

@bot.callback_query_handler(func=lambda call: call.data == "algorythm")
def send_algorythm(call):
    chat_id = call.message.chat.id
    image_paths = [
        'C:/pathology_test_bot/images/menu/macro_algorythm.jpg',
        'C:/pathology_test_bot/images/menu/micro_algorythm.jpg'
    ]
    
    for img_path in image_paths:
        with open(img_path, 'rb') as img_file:
            bot.send_photo(chat_id, img_file)

# Рукописная проверка
@bot.callback_query_handler(func=lambda call: call.data == "writing_check")
def start_check(call):
    chat_id = call.message.chat.id
    user_data[chat_id] = {
        "current_question": 0,
        "answered_questions": [],
        "test_type": "writing_check",
        "waiting_for_answer": False
    }


    macro_questions = random.sample(macro_session.query(MacroQuizQuestion).all(), 13)
    micro_questions = random.sample(micro_session.query(MicroQuizQuestion).all(), 12)
    all_questions = macro_questions + micro_questions
    random.shuffle(all_questions)

    user_data[chat_id]["all_questions"] = all_questions

    bot.send_message(chat_id, "Тест с ручным вводом начался! Напишите ответ на каждый вопрос.")
    send_writing_question(chat_id)


def send_writing_question(chat_id):
    user = user_data.get(chat_id)
    if not user:
        return

    question_index = user["current_question"]
    all_questions = user.get("all_questions")
    if not all_questions or question_index >= len(all_questions):
        bot.send_message(chat_id, "❌ Тест завершен!")
        user_data.pop(chat_id, None)
        return

    question = all_questions[question_index]
    user["waiting_for_answer"] = True

    
    if os.path.exists(question.image_path):
        with open(question.image_path, "rb") as image_file:
            # Кнопка пропуска в рукописной проверке
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("⏭️ Пропустить вопрос", callback_data="skip_question"))
            bot.send_photo(chat_id, image_file, caption="Напишите ответ:", reply_markup=markup)
    else:
        bot.send_message(chat_id, "❌ Ошибка: Картинка не найдена.")
        user["current_question"] += 1
        send_writing_question(chat_id)

# Рукописный ответ
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("waiting_for_answer", False))
def handle_written_answer(message):
    chat_id = message.chat.id
    user = user_data.get(chat_id)
    if not user or not user.get("waiting_for_answer"):
        return

    question_index = user["current_question"]
    question = get_question_by_index(question_index, chat_id)
    if not question:
        return

    
    options = eval(question.options_json)
    correct_answer = options[question.correct_option]

    
    user_answer = message.text.strip().lower()
    correct_answer_lower = correct_answer.strip().lower()
    
    if user_answer == correct_answer_lower:
        response = "✅ Верно!"
    else:
        response = f"❌ Неверно! Правильный ответ: {correct_answer}"

    bot.send_message(chat_id, response)
    user["waiting_for_answer"] = False
    user["current_question"] += 1
    
    
    show_next_question_button(chat_id)

# Кнопка пропуска
@bot.callback_query_handler(func=lambda call: call.data == "skip_question")
def skip_question(call):
    chat_id = call.message.chat.id
    user = user_data.get(chat_id)
    if not user:
        return

    question_index = user["current_question"]
    question = get_question_by_index(question_index, chat_id)
    if question:
        options = eval(question.options_json)
        correct_answer = options[question.correct_option]
        bot.send_message(chat_id, f"❓ Пропущено! Правильный ответ: {correct_answer}")

    user["waiting_for_answer"] = False
    user["current_question"] += 1
    show_next_question_button(chat_id)


def show_next_question_button(chat_id):
    user = user_data.get(chat_id)
    if not user:
        return

    markup = InlineKeyboardMarkup()
    if user["current_question"] < len(user["all_questions"]):
        markup.add(InlineKeyboardButton("➡️ Следующий вопрос", callback_data="next_writing_question"))
    else:
        markup.add(InlineKeyboardButton("🏠 Завершить тест", callback_data="back_to_menu"))

    bot.send_message(chat_id, "Выберите действие:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "next_writing_question")
def handle_next_writing_question(call):
    chat_id = call.message.chat.id
    send_writing_question(chat_id)


def get_question_by_index(index, chat_id):
    user = user_data.get(chat_id)
    if not user:
        return None

    all_questions = user.get("all_questions")
    if all_questions and index < len(all_questions):
        return all_questions[index]

    return None

# Меню тестов
@bot.callback_query_handler(func=lambda call: call.data == "test")
def select_test(call):
    chat_id = call.message.chat.id
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🧪 Макропрепараты", callback_data="test_macro"),
        InlineKeyboardButton("🦠 Микропрепараты", callback_data="test_micro"),
        InlineKeyboardButton("🔍 Общий тест", callback_data="test_all"),
        InlineKeyboardButton("🏠 Вернуться к разделам", callback_data="back_to_menu")
    )
    bot.send_message(chat_id, "Выберите тест:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["test_macro", "test_micro", "test_all"])
def start_quiz(call):
    chat_id = call.message.chat.id
    test_type = call.data
    user_data[chat_id] = {"current_question": 0, "test_type": test_type}

    if test_type == "test_all":
        # Get all questions from both databases
        macro_questions = macro_session.query(MacroQuizQuestion).all()
        micro_questions = micro_session.query(MicroQuizQuestion).all()


        all_questions = macro_questions + micro_questions
        random.shuffle(all_questions)


        user_data[chat_id]["all_questions"] = all_questions
    elif test_type == "test_macro":
        macro_questions = macro_session.query(MacroQuizQuestion).all()
        random.shuffle(macro_questions)
        user_data[chat_id]["all_questions"] = macro_questions
    elif test_type == "test_micro":
        micro_questions = micro_session.query(MicroQuizQuestion).all()
        random.shuffle(micro_questions)
        user_data[chat_id]["all_questions"] = micro_questions

    bot.send_message(chat_id, "Бот будет отправлять фото препарата с вариантами ответа.")
    send_question(chat_id)


def send_question(chat_id):
    user = user_data.get(chat_id)
    if not user:
        return

    question_index = user["current_question"]
    question = get_question_by_index(question_index, chat_id)
    if not question:
        bot.send_message(chat_id, "❌ Вопросов больше нет.")
        return

    markup = InlineKeyboardMarkup(row_width=1)
    options = eval(question.options_json)
    markup.add(*[InlineKeyboardButton(option, callback_data=f"quiz,{question_index},{i}") 
                 for i, option in enumerate(options)])

    if os.path.exists(question.image_path):
        with open(question.image_path, "rb") as image_file:
            bot.send_photo(chat_id, image_file, reply_markup=markup)
    else:
        bot.send_message(chat_id, f"❌ Ошибка: Картинка не найдена: {question.image_path}")


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    user = user_data.get(chat_id)
    if not user:
        return

    data = call.data.split(",")
    command = data[0]

    if command == "quiz":
        handle_quiz_response(call, user, data)
    elif command == "explain":
        question_index = int(data[1])
        question = get_question_by_index(question_index, chat_id)
        if question:
            bot.send_message(chat_id, question.description)
    elif command == "details":
        question_index = int(data[1])
        question = get_question_by_index(question_index, chat_id)
        if question:
            with open(question.description_image_path, "rb") as image_file:
                bot.send_photo(chat_id, image_file, caption=question.image_details)
    elif command == "next_question":
        user["current_question"] += 1
        send_question(chat_id)
    elif command == "back_to_menu":
        bot.send_message(chat_id, "Вы вернулись в главное меню.")
        user_data.pop(chat_id, None)
        start(call.message)


def handle_quiz_response(call, user, data):
    chat_id = call.message.chat.id
    question_index, selected_option = map(int, data[1:])
    question = get_question_by_index(question_index, chat_id)
    if not question:
        return

    options = eval(question.options_json)
    if question.correct_option == selected_option:
        bot.answer_callback_query(call.id, "✅ Верно!")
        
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("📖 Описание препарата", callback_data=f"explain,{question_index}"))
        if user["test_type"] == 'test_micro':
            markup.add(InlineKeyboardButton("✏️ Препарат с подписью", callback_data=f"details,{question_index}"))
        if get_question_by_index(question_index + 1, chat_id):
            markup.add(InlineKeyboardButton("➡️ Следующий препарат", callback_data="next_question"))
        else:
            markup.add(InlineKeyboardButton("🏠 Вернуться к разделам", callback_data="back_to_menu"))

        bot.send_message(chat_id, f"✅ Верно! Это *{options[selected_option]}*", parse_mode="Markdown", reply_markup=markup)
    else:
        bot.answer_callback_query(call.id, "❌ Неверно, попробуй еще раз.")

bot.polling()