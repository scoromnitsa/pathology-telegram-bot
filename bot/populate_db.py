from database_macro import session, QuizQuestion
import json

questions = [
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_1.jpg',
        'options': ['Первично-сморщенная почка', 'Большая пестра почка', 'Церебоспинальный гнойный менингит'],
        'correct_option': 0,
        'description': '''Почки уменьшены в размерах, плотной консистенции, с мелкозернистой поверхностью, мелкими кистами с прозрачным содержимым, на разрезе корковое (особенно) и мозговое вещество истончено, увеличен объем жировой клетчатки ворот почек. 
        
Бугристая поверхность - последствие инфарктов почки с последующей их организацией (замещением на соединительную ткань).'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_2.jpg',
        'options': ['Кровоизлияние в головном мозге', 'Цереброспинальный гнойный менингит', 'Эмболический гнойный нефрит'],
        'correct_option': 1,
        'description': '''Мягкие мозговые оболочки утолщены, тусклые, пропитаны гнойным экссудатом зеленовато – серого цвета, борозды и извилины сглажены. 
        
Гной скапливается в субарахноидальном пространстве (лептоменингит).'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_3.jpg',
        'options': ['Рак молочной железы', 'Мелкоузловой цирроз печени', 'Большая пестрая почка'],
        'correct_option': 2,
        'description': '''Почки увеличены в размерах, дряблой консистенции. Поверхность серо-розового цвета с красным крапом. 
        
На разрезе корковый слой широкий, набухший, с красным крапом на сероватом фоне. Мозговое вещество почки темно – красное.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_4.jpg',
        'options': ['Узловой зоб', 'Рак тела матки', 'Центральный рак лёгкого'],
        'correct_option': 0,
        'description': '''Щитовидная железа увеличена в размерах, поверхность ее бугристая, с узлами разной величины, консистенция плотная, капсула гладкая, сквозь нее просвечивают очаги кровоизлияний, склероза. 
        
На разрезе желатинообразная.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_5.jpg',
        'options': ['Септический эндометрит', 'Рак тела матки', 'Фиброзно-кавернозный туберкулез легких'],
        'correct_option': 2,
        'description': '''Имеется полость неправильной формы, стенки ее толстые, плотные, не спадаются и представлены белесоватой тканью, сообщается с бронхом. Изнутри полость покрыта крошащимися желто-серыми казеозными массами, гноевидным налетом. '
        
Бронхи и кровеносные сосуды склерозированы. 
        
За пределами полости очаги казеозного некроза желто – серого цвета.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_6.jpg',
        'options': ['Первичный легочный туберкулезный комплекс', 'Милиарный туберкулез легких', 'Фиброзно-кавернозный туберкулез легких'],
        'correct_option': 0,
        'description': '''Под плеврой виден очаг казеозного некроза, желто – серого цвета (первичный аффект). Плевра над этим участком покрыта фибринозными наложениями. 
       
Первичный аффект связан с корнем легкого тяжем из мелких, просовидных, желто – серых бугорков (лимфангит). 
        
Бифуркационные лимфоузлы увеличены, округлой формы, на разрезе суховаты, желто – серого цвета (казеозный лимфаденит). 
        
Первичного туберкулезный комплекс состоит из  
1)первичного аффекта(очаг Гона)
2)туберкулезного лимфангита
3)лимфаденита (очаг казеозного некроза в регионарных лимфоузлах).'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_7.jpg',
        'options': ['Возвратно-бородавчатый эндокардит', 'Инфаркт миокарда', 'Легочное сердце'],
        'correct_option': 2,
        'description': '''Сердце увеличено в размерах и массе, гипертрофия преимущественно стенок правого желудочка. 
        
Миокард дряблой консистенции, глинистого вида (жировая дистрофия кардиомиоцитов). 
        
*патология связана с заболеваниями легких.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_8.jpg',
        'options': ['Инфаркт миокарда', 'Бронхоэктазы и пневносклероз', 'Полипнозно-язвенный эндордит'],
        'correct_option': 0,
        'description': '''Очаг некроза (сосудистый некроз) неправильной формы, пестрого вида, желтовато-серого цвета с красными очагами, дряблой консистенции, западает на разрезе, окружен геморрагическим венчиком темно-красного цвета (зона демаркационного воспаления). 
        
Вид инфаркта - белый с геморрагическим венчиком.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_9.jpg',
        'options': ['Первичный легочный туберкулезный комплекс', 'Милиарный туберкулез легких', 'Крупноузловой цирроз печени'],
        'correct_option': 1,
        'description': '''Легкие повышенной воздушности. 
        
На разрезе видны многочисленные, мелкие, просовидные бугорки желто – серого цвета. 
        
*при хронической форме бугорки рубцуются (мелкоочаговый и диффузный пневмосклероз), развивается легочное сердце.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_10.jpg',
        'options': ['Атеросклероз аорты', 'Флегмонозный аппендицит', 'Артериолосклеротический нефросклероз'],
        'correct_option': 1,
        'description': '''Червеобразный отросток увеличен в размерах, его серозная оболочка тусклая, полнокровная, с мелкоточечными кровоизлияниями, белесоватыми нитевидными и пленчатыми фибринозными наложениями. 
        
Стенка отростка утолщена, диффузно пропитана гноем. В просвете гнойный экссудат (при надавливании из просвета отростка выделяется гной). 
        
Брыжейка отростка полнокровна, с очагами нагноения, кровоизлияний.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_11.jpg',
        'options': ['Аммилоидоз почек', 'Бронхоэктазы и пневмосклероз', 'Крупозная пневмония'],
        'correct_option': 0,
        'description': '''Доля легкого увеличена в размере, плотной консистенции, серого цвета. Плевра утолщена за счет наложений тусклых пленок фибрина (фибринозный плеврит). 
        
На разрезе легочная ткань всей пораженной доли серого цвета, маловоздушная, по виду и консистенции напоминает печень (стадия серого опеченения). 
        
Крупозное фибринозное воспаление паренхимы легких может сопровождаться воспалением плевры (плевропневмония). 
        
Синонимы - лобарная пневмония, плевропневмония, фибринозная пневмония.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_12.jpg',
        'options': ['Диффузный рак желудка', 'Блюдцеобразный рак желудка', 'Флегмонозный аппендицит'],
        'correct_option': 0,
        'description': '''Стенка желудка диффузно утолщена (в участках роста опухоли), уплотнена, на разрезе белесовато-серого цвета. 
        
Слизистая оболочка неровная, ее рельеф сглажен, складки различной толщины, иногда с эрозиями. 
        
Просвет желудка сужен.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_13.jpg',
        'options': ['Мелкоузловой цирроз печени', 'Крупноузловой цирроз печени', 'Рак тела матки'],
        'correct_option': 0,
        'description': '''Печень увеличена в размерах, жетоватая, плотной консистенции, с равномерной мелкобугристой (мелкоузловой) поверхностью. 
        
Узлы в диаметре менее 3 мм, ярко-желтого цвета, разделены тонкими прослойками соединительной ткани. 
        
*темный орган - селезенка *соответствует микропрепарату “Алкогольный монолобулярный цирроз печени”'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_14.jpg',
        'options': ['Мелкоузловой цирроз печени', 'Крупноузловой цирроз печени', 'Милиарный туберкулез легких'],
        'correct_option': 1,
        'description': 'Печень уменьшена в размерах, плотной консистенции, поверхность печени неровная крупноузловая. На разрезе узлы разных размеров в диаметре более 3 мм, разделены широкими сероватыми прослойками соединительной ткани.'
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_15.jpg',
        'options': ['Диффузный рак желудка', 'Атеросклероз аорты', 'Блюдцеобразный рак желудка'],
        'correct_option': 2,
        'description': '''Крупное образование на широком основании блюдцеобразной формы с приподнятыми валикообразными неровными краями и опущенным изъязвленным дном. 
        
Ткань образования белесоватого цвета, плотной консистенции, прорастает все слои стенки желудка.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_16.jpg',
        'options': ['Возвратно-бородавчатый эндокардит', 'Легочное сердце', 'Полипозно-язвенный эндокардит'],
        'correct_option': 0,
        'description': '''Сердце увеличено в размерах и массе (гипертрофия миокарда).Отмечаются мелкие тромботические наложения красного цвета - “бородавки”, по свободному краю склерозированных, деформированных, частично сращенных и петрифицированных створок митрального клапана (в очагах повреждения эндокарда створок клапана). 
        
Хорды утолщены, сращены, укорочены (ревматический порок сердца).'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_17.jpg',
        'options': ['Возвратно-бородавчатый эндокардит', 'Инфаркт миокарда', 'Полипозно-язвенный эндокардит'],
        'correct_option': 2,
        'description': '''Сердце увеличено в размерах и массе, камеры расширены, стенки левого желудочка утолщены (гипертрофированы). 
        
Створки митрального и аортального клапанов утолщены, с крупными изъязвлениями, которые закрыты легко отделяемыми, крупными крошащимися полиповидными темно-красного и серовато-красного цвета тромботическими наложениями с очагами обызвествления (полипозно-язвенный эндокардит). 
        
Изьязвления с тромботическими наложениями переходят и на пристеночный эндокард.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_18.jpg',
        'options': ['Рак молочной железы', 'Септический эндометрит', 'Рак тела матки'],
        'correct_option': 1,
        'description': '''Матка увеличена в размерах, дряблой консистенции. 
        
Эндометрий неравномерной толщины, грязного зелено – серого цвета, местами покрыт гнойным налетом.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_19.jpg',
        'options': ['Бронхоэктазы и пневмосклероз', 'Мелкоузловой цирроз печени', 'Милиарный туберкулез легких'],
        'correct_option': 0,
        'description': '''Бронхи расширены (в виде цилиндров), их стенки утолщены, уплотнены, выступают над поверхностью разреза, в просвете гной (цилиндрические бронхоэктазы). 
        
В окружающей ткани легкого усилен диффузный сетчатый рисунок (тонкие прослойки соединительной ткани серого цвета), расширена перибронхиальная соединительная ткань серого цвета (диффузный сетчатый и перибронхиальный пневмосклероз). 
        
Плевра утолщена, склерозирована'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_20.jpg',
        'options': ['Большая пестрая почка', 'Вторично-сморщенная почка', 'Большая сальная почка'],
        'correct_option': 2,
        'description': '''Почки увеличены, уплотнены, со слабо зернистой матовой поверхностью, бледного желтовато-серого цвета. 
        
На разрезе корковое вещество широкое и матовое, а мозговое серо-розовое (отмечается сальный блеск). 
        
Синонимы - большая сальная почка, большая белая амилоидная почка.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_21.jpg',
        'options': ['Рак молочной железы', 'Рак тела матки', 'Инфаркт миокарда'],
        'correct_option': 0,
        'description': '''Молочная железа увеличена в размерах, плотной консистенции, кожа бугристая, в области соска втянута в ткань железы. 
        
На разрезе узел плотной консистенции, зернистого вида, без четких границ, серовато-белого цвета.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_22.jpg',
        'options': ['Рак тела матки', 'Рак молочной железы', 'Узловой зоб'],
        'correct_option': 0,
        'description': '''Матка увеличена в размерах. 
        
На разрезе обнаруживается опухолевидное образование, растущее из слизистой оболочки сосочкового вида, не имеющие четких границ, буроватого цвета, с изъязвлениями и кровоизлияниями.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_23.jpg',
        'options': ['Атеросклероз аорты', 'Крупноузловой цирроз печени', 'Флегмонозный аппендицит'],
        'correct_option': 0,
        'description': '''Стенка аорты деформирована, каменистой плотности, желтовато-белого цвета, образует выпячивания (атеросклеротические бляшки). 
        
На интиме аорты отмечаются липидные пятна (желтого цвета). 
        
Осложненные поражения - множественные изъязвления фиброзных бляшек, пристеночные тромбы с характерной гофрированной поверхностью, кальциноз.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_24.jpg',
        'options': ['Цереброспинальный гнойный менингит', 'Кровизлияние в головном мозге', 'Полипозно-язвенный эндокардит'],
        'correct_option': 1,
        'description': '''В ткани мозга– скопление свернувшейся крови буровато-красного цвета.
        
В области кровоизлияния вещество мозга разрушено (гематома). 
        
Ткань мозга отечна, полнокровна, желудочки расширены, в ликворе примесь крови.'''
    },
    {
        'image_path': 'C:/pathology_test_bot/images/macro/image_25.jpg',
        'options': ['Рак легкого', 'Бронхоэктазы и пневмосклероз', 'Крупозная пневмония'],
        'correct_option': 0,
        'description': '''В области корня легкого виден узел серовато-белого цвета, не имеет четких границ (опухоль исходит из стенки бронхов).
        
Перибронхиальные лимфатические узлы увеличены, замещены опухолевой тканью плотной консистенции, серовато-белого цвета - лимфогенные метастазы рака легкого.'''
    }
    ]
    
    


for q in questions:
    question_entry = QuizQuestion(
        image_path=q["image_path"],
        options_json=json.dumps(q["options"]),
        correct_option=q["correct_option"],
        description=q["description"]
    )
    session.add(question_entry)

session.commit()
print("Questions added to the database!")