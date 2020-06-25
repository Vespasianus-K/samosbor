#-------------------------------------------------------------------------
# Опции:

# Гигацикл начала отсчёта.
CYCLE_START = 1000
# До какого возраста исследовать:
AGE_END = 25

# Численность населения в гигацикл начала отсчёта:
POPULATION = 15000000
# Уровень рождаемости (например: 0.05 значит 5%
# или 50 новорожденных на 1000 населения в гигацикл):
FERTILITY_RATE = 0.05
# Уровень смертности, аналогично:
MORTALITY_RATE = 0.047

# Переменные для расчёта военной экономики:
# Количество концентрата в год на душу населения
GDP_RATE = 13000
# Гигацикловой рост доходов-расходов
GDP_GROWTH = 0.03
# Доля расходов на ликвидаторов из всех расходов строения. 0.2 - 20%
GDP_ARMY = 0.2

# Компонент Мейкхама, независимый от возраста риск:
COMPONENT_A = 0.03
# Коэффициент b:
COEFFICIENT_B = 0.000350
# Коэффициент c:
COEFFICIENT_C = 1.08

# Распределение полов.
MALE_NAME = 'Мужчины'
MALE_PERCENT = 0.6
FEMALE_NAME = 'Женщины'
FEMALE_PERCENT = 0.4

# Армия:
prof_percent = 0.5
# Профессиональный риск, изменение компонента Мейкхама:
# (0.4 = 40% риск смерти каждый гигацикл)
prof_hazard = 0.4
# Ликвидаторы обоих полов? 0 - нет; 1 - да
prof_male_switch = 1
prof_female_switch = 1
# Возраст вступления в ликвидаторы:
prof_age_apprentice = 17
# Возраст перехода в запас:
prof_age_expert = 20
# Возраст отставки:
prof_age_retiree = 40
prof_name_apprentice = 'Ликвидаторы'
prof_name_expert = 'Запасники'
prof_name_retiree = 'Отставники'


#-------------------------------------------------------------------------
# Список видов войск. Используется базой данных военной техники,
# Смотри параметр 'gsl_troops_type'.

# Для замены хорошо подойдут регулярные выражения, например в Vim'е:
# %s/'РВ'/'РВСН'/g — подправит всю базу данных. Кавычки важны.
dict_troops_types = {
        # Формат:
        # 'Вид_войск':процент,
        # Военно-промышленный комплекс (боеприпасы):
        'ВПК':1,
        # Полевая ликвидация:
        'ПЛ':0.5,
        # Огневая поддержка:
        'ОП':0.15,
        # Ополченцы:
        'Ополчение':0.2,
        # Инженерные войска:
        'ИВ':0.15,
        }


#-------------------------------------------------------------------------
# База данных оружия. Двумерный массив.

# Дополняется блоками, без ограничений и очень легко. Пользуйтесь этим.

# Создаётся объединённый словарь — строки массива.
metadict_gsl = {}

# Выбирается первый из ключей — номер столбца.
dict_gsl_key = 0
dict_gsl = {
    "gsl_name":"Штурмовые винтовки",
    "gsl_name_comment":"Рабочая лошадка ликвидаторов-регуляров. Надёжные и убойные.",
    "gsl_troops_type":"ПЛ",
    "gsl_cost":2500,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_cost_maintenance":0.05,
    "gsl_budget":0.01,
    "gsl_name_new":"Автоматы Ералашникова модернизированные (АЕМ)",
    "gsl_name_mid":"Автоматы Ералашникова, модель 47 (АЕ-47)",
    "gsl_name_old":"Опытные образцы автоматических винтовок под списание",
    "gsl_age_mid":6,
    "gsl_age_old":25,
    "gsl_a":0.1,
    "gsl_b":0.04,
    "gsl_c":1.1,
    "gsl_ammo_1_name":"Патроны 5.45х39",
    "gsl_ammo_1_capacity":30, # Магазин
    "gsl_ammo_1_expense":14000, # Расход в гигацикл
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Магазинные винтовки",
    "gsl_name_comment":"Стреляют медленно, но далеко и точно более мощным патроном.",
    "gsl_troops_type":"ПЛ",
    "gsl_cost":1750,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_cost_maintenance":0.025,
    "gsl_budget":0.0075,
    "gsl_name_new":"Трёхлинейные винтовки Слизнева-Щерского",
    "gsl_name_mid":"Трёхлинейные винтовки Слизнева (устаревшие)",
    "gsl_name_old":"Трёхлинейные винтовки Слизнева (под списание",
    "gsl_age_mid":8,
    "gsl_age_old":25,
    "gsl_a":0.075,
    "gsl_b":0.02,
    "gsl_c":0.88,
    "gsl_ammo_1_name":"Патроны 7.62х54",
    "gsl_ammo_1_capacity":5,
    "gsl_ammo_1_expense":3000,
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Ручные пулемёты",
    "gsl_name_comment":"Основное оружие поддержки. Стреляет далеко и точно, но о надёжности лучше забыть.",
    "gsl_troops_type":"ПЛ",
    "gsl_cost":4500,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_cost_maintenance":0.05,
    "gsl_budget":0.0125,
    "gsl_name_new":"Ручные пулемёты Ералашникова-Гермова",
    "gsl_name_mid":"Ручные пулемёты Ералашникова",
    "gsl_name_old":"Станковые пулемёты (под списание)",
    "gsl_age_mid":4,
    "gsl_age_old":12,
    "gsl_a":0.12,
    "gsl_b":0.035,
    "gsl_c":2.1,
    "gsl_ammo_1_name":"Патроны 5.45х39",
    "gsl_ammo_1_capacity":45,
    "gsl_ammo_1_expense":15000,
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Огнемёты",
    "gsl_name_comment":"Жги, детка, жги! Ранцевый огнемёт выбрасывает струю смеси на 45-60 метров, зачищая всё в радиусе видимости.",
    "gsl_troops_type":"ИВ",
    "gsl_cost":7200,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_cost_maintenance":0.1,
    "gsl_budget":0.0075,
    "gsl_name_new":"Ранцевые огнемёты Изийского модернизированные",
    "gsl_name_mid":"Ранцевые огнемёты Изийского РОИ-2",
    "gsl_name_old":"Стационарные огнемёты (под списание)",
    "gsl_age_mid":4,
    "gsl_age_old":12,
    "gsl_a":0.1,
    "gsl_b":0.045,
    "gsl_c":1.4,
    "gsl_ammo_1_name":"Огнесмесь (литры)",
    "gsl_ammo_1_capacity":6,
    "gsl_ammo_1_expense":1400,
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Грабли ликвидаторские",
    "gsl_name_comment":"Символ ликвидаторов. Просты в использовании и всегда под рукой.",
    "gsl_troops_type":"ПЛ",
    "gsl_cost":550,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_cost_maintenance":0.005,
    "gsl_budget":0.05,
    "gsl_name_new":"Грабли новые",
    "gsl_name_mid":"Грабли потрёпанные",
    "gsl_name_old":"Грабли списанные",
    "gsl_age_mid":1,
    "gsl_age_old":5,
    "gsl_a":0.25,
    "gsl_b":0.05,
    "gsl_c":0.75,
    "gsl_ammo_1_name":"Запасные зубцы к граблям",
    "gsl_ammo_1_capacity":12,
    "gsl_ammo_1_expense":120,
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Патроны 5.45х39",
    "gsl_name_comment":"Патроны к Ералашникову. Начальная скорость - 860 м/с, дульная энергия - 1100 Дж.",
    "gsl_troops_type":"ВПК",
    "gsl_cost":0.6,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_cost_maintenance":0.02,
    "gsl_budget":0.035,
    "gsl_name_new":"Патроны 5.45х39 новые",
    "gsl_name_mid":"Патроны 5.45х39 с запасных складов",
    "gsl_name_old":"Патроны 5.45х39 под списание",
    "gsl_age_mid":3,
    "gsl_age_old":5,
    "gsl_a":0.09,
    "gsl_b":0.01,
    "gsl_c":0.75,
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Запасные зубцы к граблям",
    "gsl_name_comment":"Без сомнения, самый важный продукт производства.",
    "gsl_troops_type":"ВПК",
    "gsl_cost":0.15,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_budget":0.0005,
    "gsl_name_new":"Запасные зубцы к граблям (новые)",
    "gsl_name_mid":"Запасные зубцы к граблям, немного ржавые",
    "gsl_name_old":"Запасные зубцы к граблям списанные",
    "gsl_age_mid":2,
    "gsl_age_old":5,
    "gsl_a":0.05,
    "gsl_b":0.005,
    "gsl_c":0.6,
    }
metadict_gsl[dict_gsl_key] = dict_gsl

dict_gsl_key = dict_gsl_key + 1
dict_gsl = {
    "gsl_name":"Огнесмесь (литры)",
    "gsl_name_comment":'Смесь горючих жидкостей, отлично "работающая" по всем целям',
    "gsl_troops_type":"ВПК",
    "gsl_cost":15,
    "gsl_cost_currency":"грамм концентрата",
    "gsl_budget":0.015,
    "gsl_name_new":"Огнесмесь (новая, литры)",
    "gsl_name_mid":"Огнесмесь (со складов, литры)",
    "gsl_name_old":"Огнесмесь списанная (литры)",
    "gsl_age_mid":1,
    "gsl_age_old":3,
    "gsl_a":0.15,
    "gsl_b":0.009,
    "gsl_c":0.9,
    }
metadict_gsl[dict_gsl_key] = dict_gsl
#-------------------------------------------------------------------------
# Внутренние переменные.

# Создаём рабочие переменные на основе данных из опций (для удобства):
cycle_real = CYCLE_START
age_real = AGE_END
pop = POPULATION
fert = FERTILITY_RATE
mort = MORTALITY_RATE
a = COMPONENT_A
b = COEFFICIENT_B
c = COEFFICIENT_C


#-------------------------------------------------------------------------
# Функции, подпрограммы. Последующие вызывают предыдущие.

def population_size(cycle):
    """Вычисляем численность популяции.

    Рост популяции, это геометрическая прогрессия, например:
    100000*1.002^(100-1)=121872
    Начальная численность, гигацикловой прирост, период в сто лет.
    Функция вычисляет исходную численность, зная конечную:
    121872*1.002^(1-100)=100000
    """
    population = POPULATION * ((FERTILITY_RATE - MORTALITY_RATE + 1) ** (-cycle))
    # Округляем число
    population = round (population)
    return population
 
def generation_size(cycle, percent):
    """Определяем численность поколения.

    Поколение, это процент от популяции, например, если рождаемость 0.02:
    121872*1.002^(1-100)*0.02=2000 (2% новорожденных в популяции)
    Точно так же можно определить число умерших, прирост населения, состав:
    121872*1.002^(1-100)*0.02*0.5=1000 (50% новорожденных мужского пола)
    """
    generation = round(population_size(cycle) * percent)
    return generation

def GDP_size(cycle):
    """ВВП страны в определённый гигацикл.

    Рост благосостояния, это та же геометрическая прогрессия:
    10000*1.03^(1-100)=536
    В данном случае от 536$ за столетие ВВП вырос до 10 000$
    """
    GDP_in_cycle = GDP_RATE * ((GDP_GROWTH + 1) ** (-cycle)) * population_size(cycle)
    GDP_in_cycle = round (GDP_in_cycle)
    return GDP_in_cycle

def gompertz_distribution(a, b, c, age):
    """Распределение Гомпертца. Риск смерти в зависимости от возраста.

    Распределение Гомпертца-Мейкхама неплохо работает в
    демографических расчётах для самых разных популяций.
    Единственный недостаток — оно склонно занижать
    смертность в начале и завышать в конце (экспонента, что поделать).
    Для популяции людей даёт хорошие результаты в диапазоне — 30-70 лет.
    Формула: p=a+b*(c^x)
    Где:
    p — вероятность смерти в процентах
    a — независимый от возраста риск (0.002%)
    b — коэффициент 2 (0.000350)
    c — коэффициент 3 (1.08)
    x — возраст в гигациклах
    Коэффициенты подобраны с учётом исследования:
    "Parametric models for life insurance mortality data: gompertz's law over time".
    """
    chance_of_dying = a + b * (c ** age)
    # Проверка. Если получилось больше 1, значит 100% смерть.
    if (chance_of_dying > 1):
        chance_of_dying = 1
    return chance_of_dying


def generation_alive(generation, a, b, c, age_real):
    """Число живых в поколении.

    Каждый гигацикл умирает некий процент из поколения.
    Этот цикл вычисляет точное число живых в определённый гигацикл.
    """
    # Задаём рабочую переменную для цикла:
    age = 0
    # Из численности поколения вычитаем число погибших в первый гигацикл:
    generation_survivors = generation - \
            generation * \
            gompertz_distribution(a, b , c, age)
    # Далее это вычитание продолжается циклично.
    while (age <= age_real):
        age = age + 1
        generation_survivors = generation_survivors - \
                generation_survivors * \
                gompertz_distribution(a, b, c, age)
        # Проверка. Если число выживших уходит в минус, значит все мертвы.
        if (generation_survivors <= 0):
            generation_survivors = 0
            break
    # Округляем число
    generation_survivors = round(generation_survivors)
    return generation_survivors


def generation_profession(prof_percent, prof_hazard):
    """Число представителей определённой профессии, с учётом риска."""
    prof_number = 0
    if (prof_male_switch != 0):
        # Берём из словаря численность живых в нужном поколении
        # и пропускаем через ещё один цикл, чтобы учесть риск профессии.
        prof_number = prof_number + \
                generation_alive(dict_population['generation_alive'] * MALE_PERCENT * prof_percent,
                        # Отчёт начинается с возраста профессии.
                        prof_hazard, b, c, age_real - prof_age_apprentice)
    if (prof_female_switch != 0):
        prof_number = prof_number + \
                generation_alive(dict_population['generation_alive'] * FEMALE_PERCENT * prof_percent,
                        prof_hazard, b, c, age_real - prof_age_apprentice)
    return prof_number



#-------------------------------------------------------------------------
# Главный цикл скрипта.

# Эта база данных станет индексом для словарей.
metadict = {}

# Рабочие переменные:
progression_cycle = 0
cycle = 0

# Цикл перебирает гигациклы, уходя в прошлое,
# пока возраст популяции не сравняется с возрастом конца исследования.
while (progression_cycle <= AGE_END):
    # Определяем текущий гигацикл (для прогрессии роста населения).
    cycle = AGE_END - progression_cycle
    cycle_real = CYCLE_START - cycle

    # Создаём основной словарь (базу данных) для этого возраста:
    dict_population = {
            'age_real':age_real,
            'cycle_real':cycle_real,
            'population_size':population_size(cycle),
            'generation_size':generation_size(cycle, fert),
            'generation_alive':generation_alive(generation_size(cycle, fert), a, b, c, age_real),
            'GDP_size':GDP_size(cycle)
            }

    # Определяем численность призывников:
    prof_number_apprentice = 0
    if (prof_age_apprentice <= age_real < prof_age_expert):
        prof_number_apprentice = prof_number_apprentice + \
                generation_profession(prof_percent, prof_hazard)
    # Определяем численность резервистов:
    prof_number_expert = 0
    if (prof_age_expert <= age_real < prof_age_retiree):
        prof_number_expert = prof_number_expert + \
                generation_profession(prof_percent, prof_hazard)
    # И, наконец, пенсионеры:
    prof_number_retiree = 0
    if (prof_age_retiree <= age_real):
        prof_number_retiree = prof_number_retiree + \
                generation_profession(prof_percent, prof_hazard)

    # Создаём временный словарь гендеров и профессий:
    dict_demography = {
            MALE_NAME:generation_alive(generation_size(cycle, fert * MALE_PERCENT), a, b, c, age_real),
            FEMALE_NAME:generation_alive(generation_size(cycle, fert * FEMALE_PERCENT), a, b, c, age_real),
            prof_name_apprentice:prof_number_apprentice,
            prof_name_expert:prof_number_expert,
            prof_name_retiree:prof_number_retiree,
            }
 
    # Дополняем первый словарь вторым
    dict_population.update(dict_demography)
    # Создаём объединённый словарь,
    # он будет пополняться при каждом проходе цикла:
    metadict[age_real] = dict_population

    # Завершение главного цикла:
    progression_cycle = progression_cycle + 1
    age_real = age_real - 1


#-------------------------------------------------------------------------
# Модуль. Вычисляет производство и количество оружия в войсках.

# Произведённое оружие:
metadict_equipment_create = {}
# Уцелевшее оружие:
metadict_equipment_alive = {}

# Исследование объединённого словаря. Создание баз данных оружия.
# Перебираем вложенные словари начиная с последнего:
for meta_key in sorted(metadict.keys(), reverse=True):
    # Временный словарь вооружений (за один гигацикл):
    dict_equipment_create = {}
    dict_equipment_alive = {}
    # Перебираем опции из базы данных вооружений:
    for gsl_key in sorted(metadict_gsl.keys()):
        # Количество созданных машин, это бюджет на них, делённый на стоимость.
        gsl_create = round(metadict[meta_key]['GDP_size'] * GDP_ARMY * \
                metadict_gsl[gsl_key]['gsl_budget'] / metadict_gsl[gsl_key]['gsl_cost'])
        gsl_alive = generation_alive(gsl_create,
                metadict_gsl[gsl_key]['gsl_a'],
                metadict_gsl[gsl_key]['gsl_b'],
                metadict_gsl[gsl_key]['gsl_c'],
                metadict[meta_key]['age_real'])
        # Создаём временный словарь:
        dict_equipment_create[metadict_gsl[gsl_key]['gsl_name']] = gsl_create
        dict_equipment_alive[metadict_gsl[gsl_key]['gsl_name']] = gsl_alive
    # Объединяем временные словари в базу данных:
    metadict_equipment_create[meta_key] = dict_equipment_create
    metadict_equipment_alive[meta_key] = dict_equipment_alive

# Далее, вычисляем общее число вооружений на складах:
dict_equipment_all = {}
for gsl_key in sorted(metadict_gsl.keys()):
    equipment_all = 0
    for meta_key in sorted(metadict_equipment_alive.keys()):
        equipment_all = equipment_all + metadict_equipment_alive[meta_key][metadict_gsl[gsl_key]['gsl_name']]
    dict_equipment_all[metadict_gsl[gsl_key]['gsl_name']] = equipment_all


#-------------------------------------------------------------------------
# Вывод результатов.

# Вывод по гигациклам:
for meta_key in sorted(metadict.keys(), reverse=True):
    # Вывод данных о населении:
    print('гигацикл:', metadict[meta_key]['cycle_real'],
            'Возраст:', metadict[meta_key]['age_real'],
            'Родившиеся:', metadict[meta_key]['generation_size'],
            'Живые:', metadict[meta_key]['generation_alive'])
    print(MALE_NAME, metadict[meta_key][MALE_NAME],
            FEMALE_NAME, metadict[meta_key][FEMALE_NAME])
    # Вывод данных о солдатах:
    if (prof_age_apprentice <= metadict[meta_key]['age_real'] < prof_age_expert):
        print(prof_name_apprentice, metadict[meta_key][prof_name_apprentice])
    if (prof_age_expert <= metadict[meta_key]['age_real'] < prof_age_retiree):
        print(prof_name_expert, metadict[meta_key][prof_name_expert])
    if (prof_age_retiree <= metadict[meta_key]['age_real']):
        print(prof_name_retiree, metadict[meta_key][prof_name_retiree])
    # Вывод данных о вооружении:
    for gsl_key in sorted(metadict_gsl.keys()):
        # Отмена вывода, если число машинок по нулям.
        if (metadict_equipment_alive[meta_key][metadict_gsl[gsl_key]['gsl_name']] != 0):
            if (metadict[meta_key]['age_real'] < metadict_gsl[gsl_key]['gsl_age_mid']):
                print(metadict_gsl[gsl_key]['gsl_name_new'],
                        ' (Создано: ',
                        # Обращение аж к двум словарям, одно вложено в другое.
                        metadict_equipment_create[meta_key][metadict_gsl[gsl_key]['gsl_name']], ')',
                        ' Уцелело: ',
                        metadict_equipment_alive[meta_key][metadict_gsl[gsl_key]['gsl_name']], sep='')
            if (metadict_gsl[gsl_key]['gsl_age_mid'] <= metadict[meta_key]['age_real'] <
                    metadict_gsl[gsl_key]['gsl_age_old']):
                print(metadict_gsl[gsl_key]['gsl_name_mid'],
                        ' (Создано: ',
                        metadict_equipment_create[meta_key][metadict_gsl[gsl_key]['gsl_name']], ')',
                        ' Уцелело: ',
                        metadict_equipment_alive[meta_key][metadict_gsl[gsl_key]['gsl_name']], sep='')
            if (metadict_gsl[gsl_key]['gsl_age_old'] <= metadict[meta_key]['age_real']):
                print(metadict_gsl[gsl_key]['gsl_name_old'],
                        ' (Создано: ',
                        metadict_equipment_create[meta_key][metadict_gsl[gsl_key]['gsl_name']], ')',
                        ' Уцелело: ',
                        metadict_equipment_alive[meta_key][metadict_gsl[gsl_key]['gsl_name']], sep='')
    print('------------------------------------------------------------')

# Подведение итогов:
print('Ожидаемая численность:', POPULATION)
population_alive = 0
army_soldiers= 0
army_reservists = 0
for meta_key in sorted(metadict.keys()):
    population_alive = population_alive + metadict[meta_key]['generation_alive']
    army_soldiers = army_soldiers + metadict[meta_key][prof_name_apprentice]
    army_reservists = army_reservists + metadict[meta_key][prof_name_expert]
print('Численность населения:', population_alive)
print(prof_name_apprentice, 'и', prof_name_expert, 'по видам войск:')
for troop_key in sorted(dict_troops_types.keys()):
    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%) ',
            round(army_soldiers * dict_troops_types[troop_key]),
            ' — ', round((army_soldiers + army_reservists) * dict_troops_types[troop_key]), sep='')
print('Несчастные случаи (в гигацикл):', round(POPULATION * COMPONENT_A))
print('Потери: ', round(army_soldiers * prof_hazard),
        ' (', round(army_soldiers * prof_hazard / (POPULATION * COMPONENT_A) * 100),
        '% от несчастных случаев)', sep='')
print('------------------------------------------------------------')


#-------------------------------------------------------------------------
# И наконец, суммируем всё вооружение, вычисляем отношение единиц оружия к числу солдат,
# потребность армии в боеприпасаха, а также суммарный бюджет на вооружения и бюджеты по видам войск:

budget_percent = 0
budget_troops_percent = 0
# База данных потребностей в боеприпасах:
ammunition_needs = {}
# Названия боеприпасов превращаем в ключи базы данных:
for gsl_key in sorted(metadict_gsl.keys()):
    if metadict_gsl[gsl_key].get('gsl_ammo_1_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_1_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_2_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_2_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_3_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_3_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_4_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_4_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_5_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_5_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_6_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_6_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_7_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_7_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_8_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_8_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_ammo_9_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_9_name']] = 0
    if metadict_gsl[gsl_key].get('gsl_fuel_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_fuel_name']] = 0
# База данных бюджета по видам войск:
# Создаётся рабочий словарь, обнуляются значения:
budget_troops_types = {}
budget_troops_types.update(dict_troops_types)
for troop_key in budget_troops_types:
    budget_troops_types[troop_key] = 0
# База данных стоимости обслуживания по видам войск:
# Создаётся рабочий словарь, обнуляются значения:
maintenance_troops_types = {}
maintenance_troops_types.update(dict_troops_types)
for troop_key in budget_troops_types:
    maintenance_troops_types[troop_key] = 0

# Перебор столбцов в базе данных оружия:
for gsl_key in sorted(metadict_gsl.keys()):
    equipment_all = 0
    # Затем перебор по гигациклам:
    for meta_key in sorted(metadict_equipment_alive.keys()):
        equipment_all = equipment_all + metadict_equipment_alive[meta_key][metadict_gsl[gsl_key]['gsl_name']]
    # Если есть проект, значит есть оружие, хотя бы один экземпляр:
    if (equipment_all < 1):
        equipment_all = 1
        print('Не хватает бюджета на',metadict_gsl[gsl_key]['gsl_name'])
    # Вывод суммы оружия, сохранившегося за все гигациклы:
    print(metadict_gsl[gsl_key]['gsl_troops_type'], metadict_gsl[gsl_key]['gsl_name'], '—' , equipment_all, end=' ')
    # Вывод отношения числа вооружений к числу солдат определённых видов войск:
    army_type_percent = dict_troops_types[metadict_gsl[gsl_key]['gsl_troops_type']]
    print('на', round(army_soldiers * army_type_percent / equipment_all),
            prof_name_apprentice, metadict_gsl[gsl_key]['gsl_troops_type'],
            'или на', round((army_reservists + army_soldiers) * army_type_percent / equipment_all),
            prof_name_apprentice, '+',
            prof_name_expert, metadict_gsl[gsl_key]['gsl_troops_type'])
    # Вывод описания вооружения:
    print('    ', metadict_gsl[gsl_key]['gsl_name_comment'])
    # Подсчитываем, сколько оружия создано за гигацикл:
    gsl_create = round(GDP_size(0) * GDP_ARMY * \
                metadict_gsl[gsl_key]['gsl_budget'] / metadict_gsl[gsl_key]['gsl_cost'])
    # Расходы на проект:
    print('        Расходы: ',
            round(metadict_gsl[gsl_key]['gsl_budget'] * 100, 3),'% бюджета ',
            '(', metadict_gsl[gsl_key]['gsl_cost'] * gsl_create / (10 ** 9),
            ' млрд ', metadict_gsl[gsl_key]['gsl_cost_currency'], ') ', sep='')
    # Подсчитываем потери (без учёта старения оружия):
    print('        Создано:', gsl_create)
    print('        Потери:', round(gsl_create * metadict_gsl[gsl_key]['gsl_a'] + \
            equipment_all * metadict_gsl[gsl_key]['gsl_a']))
    print('        ---')
    # Считаем потребность в боеприпасах (максимум 9 видов оружия) и топливо:
    if metadict_gsl[gsl_key].get('gsl_ammo_1_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_1_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_1_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_1_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_2_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_2_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_2_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_2_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_3_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_3_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_3_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_3_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_4_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_4_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_4_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_4_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_5_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_5_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_5_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_5_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_6_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_6_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_6_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_6_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_7_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_7_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_7_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_7_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_8_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_8_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_8_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_8_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_ammo_9_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_9_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_ammo_9_name']] + \
                metadict_gsl[gsl_key]['gsl_ammo_9_expense'] * equipment_all
    if metadict_gsl[gsl_key].get('gsl_fuel_name'):
        ammunition_needs[metadict_gsl[gsl_key]['gsl_fuel_name']] = \
                ammunition_needs[metadict_gsl[gsl_key]['gsl_fuel_name']] + \
                metadict_gsl[gsl_key]['gsl_fuel_expense'] * equipment_all
    # Считаем общий бюджет и бюджет по родам войск:
    budget_percent = budget_percent + metadict_gsl[gsl_key]['gsl_budget']
    for troop_key in budget_troops_types:
        if troop_key == metadict_gsl[gsl_key]['gsl_troops_type']:
            budget_troops_types[troop_key] = budget_troops_types[troop_key] + \
                    metadict_gsl[gsl_key]['gsl_budget'] * 100
    # Считаем расходы на обслуживание данного вида оружия:
    # Стоимость оружия * процент обслуживания * штук на складах
    # Если строка 'gsl_maintenance' не указана, тогда обслуживание бесплатно
    gsl_maintenance_all = metadict_gsl[gsl_key]['gsl_cost'] * \
            metadict_gsl.get(gsl_key, 0).get('gsl_maintenance', 0)  * \
            dict_equipment_all.get(metadict_gsl[gsl_key]['gsl_name'])
    # Теперь распределяем расходы на обслуживание по родам войск:
    for troop_key in maintenance_troops_types:
        if troop_key == metadict_gsl[gsl_key]['gsl_troops_type']:
            maintenance_troops_types[troop_key] = maintenance_troops_types[troop_key] + \
                    gsl_maintenance_all

# Сумма бюджета всех проектов из базы данных оружия:
print('Расходы военного бюджета на закупки и производство:')
for troop_key in sorted(budget_troops_types.keys()):
    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%)',
            ' — ', round(budget_troops_types[troop_key], 2), '%', sep='')
print('Использовано ', round(budget_percent * 100, 2), '% расходов ликвидации',
        ' (или ', round(GDP_ARMY * budget_percent * 100, 2), '% расходов гигаблока)',
        sep='')
print('        ---')

# Расходы на обслуживание оружия по видам войск:
maintenance_percent_sum = 0
print('Расходы ликвидаторского бюджета на техническое обслуживание:')
for troop_key in sorted(maintenance_troops_types.keys()):
    maintenance_percent = maintenance_troops_types[troop_key] / (GDP_size(0) * GDP_ARMY)
    maintenance_percent_sum = maintenance_percent_sum + maintenance_percent
    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%)',
            ' — ', round(maintenance_percent * 100, 2), '%', sep='')
print('Использовано ', round(maintenance_percent_sum * 100, 2), '% расходов ликвидации',
        ' (или ', round(maintenance_percent_sum * GDP_ARMY * 100, 2), '% расходов гигаблока)',
        sep='')
print('        ---')

# Соотношение производства боеприпасов и потребности в них:
print('Боеприпасы на складах (на гигацикл войны):')
for ammo_key in sorted(ammunition_needs.keys()):
    # (ammo_key, 0) — значит, если нет ключа, брать ноль.
    print('   ', ammo_key, ' — ', dict_equipment_all.get(ammo_key, 0), ' (',
            round(dict_equipment_all.get(ammo_key, ammunition_needs[ammo_key]) / \
                    ammunition_needs[ammo_key] * 100), '%)', sep='')

