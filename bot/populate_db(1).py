from database_micro import session, QuizQuestion
import json

questions_micro = [
    {
        'image_path': 'C:/pathology_test_bot/images/micro/question_images/image_1.jpg',
        'options' : ['Атеросклероз венечной артерии с тромбом', 'Аденокарцинома желудка', 'Септический эндометрит'],
        'correct_option': 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_1.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_2.jpg',
        'options' : ['Щитовидная железа при болезни Грейвса', 'Крупноочаговый (постинфарктный) кардиосклероз', 'Экстракапиллярный пролиферативный гломерулонефрит'],
        'correct_option' : 1,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_2.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_3.jpg',
        'options' : ['Крупозная пневмония', 'Милиарный туберкулез легких', 'Тиреоидит Хишимото'],
        'correct_option' : 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_3.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_4.jpg',
        'options' : ['Щитовидная железа при болезни Грейвса', 'Крупноочаговый(постинфарктный) кардиосклероз', 'Экстракапиллярный пролиферативный гломерулонефрит'],
        'correct_option' : 0,
        'description' : '''1. Фолликулы неправильной формы выстланы высоким гиперплазированным эпителием. 

2. Коллоид ярко-розовый, вакуолизирован. 

3. Встроме местами виден лимфо-макрофагальный инфильтрат.

Синонимы - диффузный токсический зоб, Базедова болезнь.''',

        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_4.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_5.jpg',
        'options' : ['Щитовидная железа при болезни Грейвса', 'Аденокарциома желудка', 'Плоскоклеточный рак легкого с ороговением'],
        'correct_option' : 2,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_5.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_6.jpg',
        'options' : ['Щитовидная железа при болезни Грейвса', 'Диабетический гломерулосклероз', 'Теоридит Хашимото'],
        'correct_option' : 2,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_6.jpg',
        'image_details' : '1 - лимфоидный фолликул'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_7.jpg',
        'options' : ['Флегмонозно-язвенный аппендицит', 'Теоридит Хашимото', 'Бронхопневмония'],
        'correct_option' : 0,
        'description' : '''1. Все слои стенки аппендикса диффузно инфильтрированы полиморфно-ядерными лейкоцитами.

2. В слизистой оболочке- фокусы некроза и изъязвления. 

3. Сосуды полнокровны.''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_7.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_8.jpg',
        'options' : ['Бронхопневмония', 'Вирусный мультилобулярный цирроз печени', 'Алкогольный монобулярный цирроз печени'],
        'correct_option' : 2,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_8.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_9.jpg',
        'options' : ['Вирусный мультилобулярный цирроз печени', 'Алкогольный монобулярный цирроз печени', 'Инфаркт миокарда'],
        'correct_option' : 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_9.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_10.jpg',
        'options' : ['Некроз эпителия канальцев проксимальных и дистальных отделов нефрона', 'Амилоидоз почек', 'Эмболический гнойный нефрит'],
        'correct_option' : 0,
        'description' : '''В извитых канальцах признаки кариолизиса, клетки набухшие, цитоплазма гомогенная розового цвета, просвет канальцев сужен или не определяется, в нем видны признаки плазморексиса. В некоторых канальцах видна фрагментация базальной мембраны – тубулорексис.

Эпителий прямых канальцев, собирательных трубочек и нисходящей части петли Генле сохранен. 

Интерстиций отечен, со слабо выраженной диффузной лейкоцитарной инфильтрацией. 

Сосуды мозгового вещества полнокровны.''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_10.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_11.jpg',
        'options' : ['Инфаркт миокарда', 'Эмболический гнойный нефрит', 'Аденокарцинома желудка'],
        'correct_option' : 0,
        'description' : '''1) Зона некроза мышечных клеток (кариолизис, плазмокоагуляция), образование некротического детрита. 

2) По периферии зоны некроза отмечается демаркационное воспаление — расширенные полнокровные тонкостенные кровеносные сосуды, инфильтрация полиморфно-ядерными лейкоцитами.''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_11.jpg',
        'image_details' : '''1 - зона некроза кардиомиоцитов
2 - демаркационная зона воспаления (зона грануляционной ткани)'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_12.jpg',
        'options' : ['Амилоидоз почек(конго красный)', 'Бронхопневмония', 'Хроническая язва желудка в период обострения'],
        'correct_option' : 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_12.jpg',
        'image_details' : '''красным окрашен амилоид в 
1-клубочке
2-капилляре
3-канальцах'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_13.jpg',
        'options' : ['Хроническая язва желудка в период обострения', 'Флегмонозно-язвенный аппендицит', 'Плоскоклеточный рак легкого с ороговением'],
        'correct_option' : 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_13.jpg',
        'image_details' : '''1-фибринозно-гнойный экссудат
2-фибриноидный некроз
3-грануляционная ткань
4-рубцовая ткань

справа обрывки мышечной ткани'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_14.jpg',
        'options' : ['Бронхопневмония', 'Хроническая обструктивная эмфизема легких', 'Крупозная пневмония'],
        'correct_option' : 1,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_14.jpg',
        'image_details' : '''1-альвеола
2-замыкательные пластинки в виде булавовидных утолщений
3-кровеносные капилляры'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_15.jpg',
        'options' : ['Экстракапиллярный пролиферативный гломерулонефрит', 'Диабетический гломерулосклероз', 'Атеросклероз венечной артерии с тромбом'],
        'correct_option' : 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_15.jpg',
        'image_details' : '''1-наружный листок капсулы Шумлянского-Боумена
2-мезангий
3-канальцы'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_16.jpg',
        'options' : ['Крупнозная пневмония', 'Тиреоидит Хашимото', 'Бронхопневмония'],
        'correct_option' : 2,
        'description' : '''1. В просвете мелкого бронха- скопление лейкоцитов, которые инфильтрируют все слои стенки бронха и разрушают ее (деструктивный панбронхит). 

2. В прилежащих альвеолах виден экссудат, состоящий из нейтрофилов, фибрина и слущенного эпителия. 

3. Окружающие альвеолы расширены заполнены воздухом (перифокальная эмфизема).''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_16.jpg',
        'image_details' : '''1-просвет бронха
2-экссудат в альвеоле
3-перифокальная эмфизема'''
    }, 
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_17.jpg',
        'options' : ['Флегмонозно-язвенный аппендицит', 'Гриппозная бронхопневмония', 'Вирусный мультилобулярный цироз печени'],
        'correct_option' : 1,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_17.jpg',
        'image_details' : '''1-просвет бронха
2-стенка бронха
3-перибронхиальные альвеолы'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_18.jpg',
        'options' : ['Диабетическая гломерулосклероз', 'Неинвазивный протоковый рак молочной железы', 'Аденокарцинома тела матки в соскобе'],
        'correct_option' : 0,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_18.jpg',
        'image_details' : '''1-гломерулосклероз
2-мезангий
3-артериолы'''
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_19.jpg',
        'options' : ['Эмболический гнойный нефрит', 'Тиреоидит Хашимото', 'Бронхопневмония'],
        'correct_option' : 0,
        'description' : '''Ткань почки в очагах гнойного воспаления (абсцессах) в состоянии гнойного расплавления.

В центре очагов видны мелкие сосуды, просветы которых обтурированы микробными эмболами.''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_19.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_20.jpg',
        'options' : ['Аденокарцинома желудка', 'Диабетический гломерулосклероз', 'Неинвазивный протоковый рак молочной железы'],
        'correct_option' : 2,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_20.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_21.jpg',
        'options' : ['Аденокарцинома тела матки в соскобе', 'Плоскоклеточный рак легкого с ороговением', 'Крупноочаговый (постинфарктный) кардиосклероз'],
        'correct_option' : 0,
        'description' : '''Клетки цилиндрические, располагаются одно- или многорядно. Их полиморфизм незначителен. 

Ядра удлиненные, гиперхромные.

Опухоль представлена атипичными железистыми комплексами разной величины и формы, построенными из атипичных эпителиальных клеток эндометриоидного типа.''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_21.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_22.jpg',
        'options' : ['Атеросклероз венечной артерии с тромбом', 'Экстракапиллярный пролиферативный гломерулонефрит', 'Септический эндометрит'],
        'correct_option' : 2,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_22.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_23.jpg',
        'options' : ['Бронхопневмония', 'Милиарный туберкулез легких', 'Аденокарцинома желудка'],
        'correct_option' : 1,
        'description' : 'Описание',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_23.jpg',
        'image_details' : 'Подпись'
    },
    {
        'image_path' : 'C:/pathology_test_bot/images/micro/question_images/image_24.jpg',
        'options' : ['Аденокарцинома желудка', 'Аденокарцинома тела матки в соскабе', 'Диабетический гломерулосклероз'],
        'correct_option' : 0,
        'description' : '''В стенке желудка разрастания атипичных железистых структур различной величины и формы, построенных из атипичных полиморфных клеток, ядра крупные и гиперхромные.''',
        'description_image_path' : 'C:/pathology_test_bot/images/micro/description_images/image_24.jpg',
        'image_details' : 'Подпись'
    }     

]

for q in questions_micro:
    question_entry = QuizQuestion(
        image_path=q["image_path"],
        options_json=json.dumps(q["options"]),
        correct_option=q["correct_option"],
        description=q["description"],
        description_image_path=q["description_image_path"],
        image_details=q["image_details"]
    )
    session.add(question_entry)

session.commit()
print("Questions added to the database!")