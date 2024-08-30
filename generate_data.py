import random
import faker
import psycopg2
import os


fake = faker.Faker('ru_RU')
conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
cursor = conn.cursor()

kazakh_first_names = [
    "Ерасыл", "Кайрат", "Нурсултан", "Ержан", "Тимур", "Санжар", "Жанибек", "Азамат", "Данияр", "Бекжан",
    "Айбек", "Бакытжан", "Куаныш", "Алихан", "Аскар", "Жасулан", "Максат", "Бауыржан", "Алмас", "Дархан",
    "Саян", "Мурат", "Аслан", "Жандос", "Еркебулан", "Ануар", "Ринат", "Мадияр", "Арман", "Ермек"
]
kazakh_last_names = [
    "Абдрахманов", "Алибаев", "Байсултанов", "Жанатов", "Иманбеков", "Карабаев", "Нурмагамбетов", "Садыков",
    "Тлеубаев", "Умиров", "Шарипов", "Ыдырысов", "Аманжолов", "Ермуханов", "Кенжебаев", "Муслимов", "Нуртаев",
    "Оразбаев", "Сариев", "Уразалин", "Токтасынов", "Каратаев", "Жумагалиев", "Асанов", "Баймуратов"
]
kazakh_middle_names = [
    "Ержанович", "Кайратович", "Маратбекович", "Нурланович", "Серикович", "Тимурович", "Уланович", "Шакенович",
    "Арманович", "Бекетович", "Даулетович", "Жанибекович", "Куанышевич", "Нурсултанович", "Рустемович",
    "Сапарбекович", "Талгатович", "Шахметович", "Темирболатович"
]

russian_first_names = [
    "Александр", "Андрей", "Дмитрий", "Иван", "Максим", "Николай", "Владимир", "Алексей", "Сергей", "Константин",
    "Павел", "Виктор", "Георгий", "Григорий", "Денис", "Евгений", "Олег", "Петр", "Федор", "Юрий",
    "Михаил", "Владислав", "Станислав", "Борис", "Илья", "Кирилл", "Вячеслав", "Егор", "Аркадий", "Анатолий"
]
russian_last_names = [
    "Иванов", "Петров", "Сидоров", "Алексеев", "Морозов", "Новиков", "Федоров", "Васильев", "Смирнов", "Кузнецов",
    "Соколов", "Попов", "Волков", "Зайцев", "Семенов", "Егоров", "Михайлов", "Крылов", "Никитин", "Романов",
    "Соловьев", "Воробьев", "Мельников", "Савельев", "Щербаков", "Голубев", "Овчинников", "Панфилов", "Мартынов", "Козлов"
]
russian_middle_names = [
    "Александрович", "Дмитриевич", "Иванович", "Петрович", "Владимирович", "Андреевич", "Николаевич", "Сергеевич",
    "Павлович", "Викторович", "Константинович", "Федорович", "Георгиевич", "Михайлович", "Юрьевич",
    "Борисович", "Кириллович", "Анатольевич", "Станиславович", "Владиславович"
]

schools = [
    "РГУ 'Алматинская республиканская школа 'Жас Улан' имени Б.Момышулы' МО РК",
    "Военный колледж имени Ш.Уалиханова",
    "РГУ 'Карагандинская республиканская школа 'Жас Улан' имени Дважды Героя Советского Союза Т.Я. Бегельдинова' МО РК",
    "РГУ 'Шымкентская республиканская школа 'Жас улан' имени Героя Советского Союза С.Рахимова' МО РК",
    "Военный колледж имени Героя Советского Союза Халық Қаһарманы генерал-армии С.Қ. Нұрмағамбетова",
    "'Назарбаев' интеллектуальные школы",
    "РФМШ г.Астана", "РФМШ г. Алматы", "«Дарын»", "«Білім инновация лицейі»",
    "КТЛ", "Гимназия №1", "Гимназия №5", "Школа-лицей №36", "Школа-лицей №92"
]

universities = [
    "Назарбаев университет", "КазНУ им. Аль-Фараби", "ЕНУ", "МУИТ", "СДУ", "КБТУ",
    "ALMAU", "Университет Международного Бизнеса", "КарГТУ", "АУЭС им. Даукеева",
    "Астана IT-университет", "КазНТУ им. К. Сатпаева", "МГУ им. Ломоносова", "Томский Политехнический Университет"
]

foreign_universities = [
    "Harvard University", "Stanford University", "Massachusetts Institute of Technology", "University of Oxford",
    "California Institute of Technology", "University of Cambridge", "Princeton University", "University of Chicago",
    "Columbia University", "University of Pennsylvania", "Yale University", "University of Toronto"
]

specialties = [
    "Иностранный язык: два иностранных языка", "переводческое дело", "Иностранная филология: английский язык",
    "Международные отношения", "Международное право", "Программная инженерия", "Информационные системы",
    "Информационная безопасность", "Компьютерные науки", "Мехатроника", "Биоинформатика", "Кибербезопасность",
    "Искусственный интеллект", "Робототехника", "Экономика", "Менеджмент"
]

academic_degrees = ["кандидат наук", "PhD", "магистр наук", "доктор наук"]

international_olympiads = [
    "Международная олимпиада по физике", "Международная олимпиада по математике", "Международная олимпиада по информатике",
    "Международная олимпиада по химии", "Международная олимпиада по биологии", "Международная олимпиада по экономике"
]

republican_olympiads = [
    "Республиканская олимпиада по физике", "Республиканская олимпиада по математике", "Республиканская олимпиада по информатике",
    "Республиканская олимпиада по химии", "Республиканская олимпиада по биологии", "Республиканская олимпиада по литературе"
]

regional_city_olympiads = [
    "Городская олимпиада по физике", "Городская олимпиада по математике", "Городская олимпиада по информатике",
    "Городская олимпиада по химии", "Городская олимпиада по биологии", "Городская олимпиада по истории"
]

republican_sports_competitions = [
    "Республиканские соревнования по футболу", "Республиканские соревнования по баскетболу",
    "Республиканские соревнования по волейболу", "Республиканские соревнования по плаванию",
    "Республиканские соревнования по легкой атлетике", "Республиканские соревнования по дзюдо"
]

regional_city_sports_competitions = [
    "Городские соревнования по футболу", "Городские соревнования по баскетболу", "Городские соревнования по волейболу",
    "Городские соревнования по плаванию", "Городские соревнования по легкой атлетике", "Городские соревнования по дзюдо"
]

for _ in range(50000):
    year = random.randint(1993, 2008)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    
    year_prefix = f"{year % 100:02d}"
    month_prefix = f"{month:02d}"
    day_prefix = f"{day:02d}"
    random_digits = ''.join(random.choices('0123456789', k=6))
    
    iin = f"{year_prefix}{month_prefix}{day_prefix}{random_digits}"

    if random.random() < 0.75:
        first_name = random.choice(kazakh_first_names)
        last_name = random.choice(kazakh_last_names)
        middle_name = random.choice(kazakh_middle_names)
    else:
        first_name = random.choice(russian_first_names)
        last_name = random.choice(russian_last_names)
        middle_name = random.choice(russian_middle_names)

    full_name = f"{last_name} {first_name} {middle_name}"

    school = random.choice(schools)
    university = random.choice(universities)
    foreign_university = random.choice(foreign_universities) if random.random() > 0.8 else None
    specialty = random.choice(specialties) if random.random() > 0.3 else None
    academic_degree = random.choice(academic_degrees) if random.random() > 0.9 else None

    international_olympiad = random.choice(international_olympiads) if random.random() > 0.9 else None
    republican_olympiad = random.choice(republican_olympiads) if random.random() > 0.9 else None
    regional_city_olympiad = random.choice(regional_city_olympiads) if random.random() > 0.5 else None

    republican_sports_competition = random.choice(republican_sports_competitions) if random.random() > 0.8 else None
    regional_city_sports_competition = random.choice(regional_city_sports_competitions) if random.random() > 0.8 else None

    cursor.execute("""
        INSERT INTO candidates (
            iin, full_name, school, university, foreign_university,
            specialty, academic_degree, international_olympiads,
            republican_olympiads, regional_city_olympiads,
            republican_sports_competitions, regional_city_sports_competitions
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (iin, full_name, school, university, foreign_university,
          specialty, academic_degree, international_olympiad,
          republican_olympiad, regional_city_olympiad,
          republican_sports_competition, regional_city_sports_competition))

conn.commit()
cursor.close()
conn.close()

print("Данные успешно вставлены.")
