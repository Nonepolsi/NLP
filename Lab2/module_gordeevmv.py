# Импортирую все, что понадобится
from yargy import (
    Parser,
    rule, or_,
    and_, not_
)
from yargy.predicates import (
    eq, type, length_eq,
    is_capitalized, gram,
    lte, gte, tag, in_,
    in_caseless, dictionary,
    normalized, caseless,
    is_title
)
from yargy.interpretation import fact
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline
from yargy.tokenizer import QUOTES

# Несколько констант для более чистого кода
DASH = eq('-')
DOT = eq('.')
SEMICOLON = eq(';')
SPACEBAR = eq(' ')

ADJF = gram('ADJF')
NOUN = gram('NOUN')
INT = type('INT')
GEN = gram('gent')
APRO = gram('Apro')
PREP = gram('PREP')
CONJ = gram('CONJ')

# А творение ниже сделано для критикалов и береговой
SIMPLE_WILDCARD = rule(
  NOUN.repeatable().optional(),
  ADJF.optional(),
  INT.optional()
)

TITLE = is_title()
ANUM = rule(
    INT,
    DASH.optional(),
    in_caseless({
        'я', 'й', 'е',
        'ое', 'ая', 'ий', 'ой'
    })
)

# # # # # # # # # Адрес # # # # # # # # # # #

Address = fact(
    'Address',
    ['City', 'Street',
     'House', 'Building',
     'Appartment']
)

# # # # # # # # # Города # # # # # # # # # # #

# Сначала беру готовые списки названий городов + добавляю пару своих
City = fact(
    'City',
    ['name', 'city_type']
)

CITY_COMPLEX = morph_pipeline([
    'санкт-петербург',
    'нижний новгород',
    'н.новгород',
    'ростов-на-дону',
    'набережные челны',
    'улан-удэ',
    'нижний тагил',
    'комсомольск-на-амуре',
    'йошкар-ола',
    'старый оскол',
    'великий новгород',
    'южно-сахалинск',
    'петропавловск-камчатский',
    'каменск-уральский',
    'орехово-зуево',
    'сергиев посад',
    'новый уренгой',
    'ленинск-кузнецкий',
    'великие луки',
    'каменск-шахтинский',
    'усть-илимск',
    'усолье-сибирский',
    'кирово-чепецк',
])

CITY_SIMPLE = dictionary({
    'москва',
    'новосибирск',
    'екатеринбург',
    'казань',
    'самара',
    'омск',
    'челябинск',
    'уфа',
    'волгоград',
    'пермь',
    'красноярск',
    'воронеж',
    'саратов',
    'краснодар',
    'тольятти',
    'барнаул',
    'ижевск',
    'ульяновск',
    'владивосток',
    'ярославль',
    'иркутск',
    'тюмень',
    'махачкала',
    'хабаровск',
    'оренбург',
    'новокузнецк',
    'кемерово',
    'рязань',
    'томск',
    'астрахань',
    'пенза',
    'липецк',
    'тула',
    'киров',
    'чебоксары',
    'калининград',
    'брянск',
    'курск',
    'иваново',
    'магнитогорск',
    'тверь',
    'ставрополь',
    'симферополь',
    'белгород',
    'архангельск',
    'владимир',
    'севастополь',
    'сочи',
    'курган',
    'смоленск',
    'калуга',
    'чита',
    'орёл',
    'волжский',
    'череповец',
    'владикавказ',
    'мурманск',
    'сургут',
    'вологда',
    'саранск',
    'тамбов',
    'стерлитамак',
    'грозный',
    'якутск',
    'кострома',
    'петрозаводск',
    'таганрог',
    'нижневартовск',
    'братск',
    'новороссийск',
    'дзержинск',
    'шахта',
    'нальчик',
    'орск',
    'сыктывкар',
    'нижнекамск',
    'ангарск',
    'балашиха',
    'благовещенск',
    'прокопьевск',
    'химки',
    'псков',
    'бийск',
    'энгельс',
    'рыбинск',
    'балаково',
    'северодвинск',
    'армавир',
    'подольск',
    'королёв',
    'сызрань',
    'норильск',
    'златоуст',
    'мытищи',
    'люберцы',
    'волгодонск',
    'новочеркасск',
    'абакан',
    'находка',
    'уссурийск',
    'березники',
    'салават',
    'электросталь',
    'миасс',
    'первоуральск',
    'рубцовск',
    'альметьевск',
    'ковровый',
    'коломна',
    'керчь',
    'майкоп',
    'пятигорск',
    'одинцово',
    'копейск',
    'хасавюрт',
    'новомосковск',
    'кисловодск',
    'серпухов',
    'новочебоксарск',
    'нефтеюганск',
    'димитровград',
    'нефтекамск',
    'черкесск',
    'дербент',
    'камышин',
    'невинномысск',
    'красногорск',
    'мур',
    'батайск',
    'новошахтинск',
    'ноябрьск',
    'кызыл',
    'октябрьский',
    'ачинск',
    'северск',
    'новокуйбышевск',
    'елец',
    'евпатория',
    'арзамас',
    'обнинск',
    'каспийск',
    'элиста',
    'пушкино',
    'жуковский',
    'междуреченск',
    'сарапул',
    'ессентуки',
    'воткинск',
    'ногинск',
    'тобольск',
    'ухта',
    'серов',
    'бердск',
    'мичуринск',
    'киселёвск',
    'новотроицк',
    'зеленодольск',
    'соликамск',
    'раменский',
    'домодедово',
    'магадан',
    'глазов',
    'железногорск',
    'канск',
    'назрань',
    'гатчина',
    'саров',
    'новоуральск',
    'воскресенск',
    'долгопрудный',
    'бугульма',
    'кузнецк',
    'губкин',
    'кинешма',
    'ейск',
    'реутов',
    'железногорск',
    'чайковский',
    'азов',
    'бузулук',
    'озёрск',
    'балашов',
    'югра',
    'кропоткин',
    'клин',
    'нижний',
    'питер',
    'сургут'
})

CITY_ABBREVIATION = in_caseless({
    'спб',
    'мск',
    'нск',
    'нн',
    'нино'
})

# Теперь делаю более общее правило. Названием города может быть что-то из сетов сверху
CITY_NAME = or_(
    rule(CITY_SIMPLE),
    rule(CITY_COMPLEX),
    rule(CITY_ABBREVIATION)
).interpretation(
    City.name
)

# Однако есть много городов, которых нет в списке, их нужно попытаться обработать
# Названиями могут быть существительные и прилагательные, регистр мне не будет важен
# Пример: Инженерный, Сургут (которого реально нет в списках сверху)
CITY_PROBABLY = or_(
    NOUN,
    ADJF
).interpretation(
    City.name
)

# Готовим варианты ключего слова
CITY_KEYWORD = or_(
    rule(normalized('город')),
    rule(
        caseless('г'),
        DOT.optional()
    )
).interpretation(
    City.city_type.const('город')
)

# Два основных условия: либо слово из списков назаний, тогда "ключ" не важен
# Или мы считаем названием города сущ. или прил. с "ключом"
# Поскольку "ключ" во втором случае не опционале, то регистр не так важен
CITY = or_(
    rule(CITY_KEYWORD, CITY_PROBABLY),
    rule(CITY_KEYWORD.optional(), CITY_NAME)
).interpretation(
    City
)

# # # # # # # # # Улицы # # # # # # # # # # #

# Тут мои силы писать подробные комментарии закончились.
# А еще пришло осознание того, что универсальное нечто сделать у меня не получится.
# Еще немного пытался, но потом решил просто делать то, что работает.

Street = fact(
    'Street',
    ['name', 'street_type']
)

# Сначала длеаю обрабочтик для названий улиц с именами
# Сразу снизу слово для "подзаборынх академиков"
WITH_NAME = or_(
    and_(ADJF, not_(APRO)),
    and_(NOUN, GEN)
)

# Одна буковка, совсем одна
SINGLE = length_eq(1)

# Мои попытки сделать универсальный парсер, а именно "двойные стандарты".
# То, что с заглавной буквы может быть названием улицы без ключевого слова.
# То, что без регистра должно иметь хоть какой-то ключ. 
# Позже увидел тесты и забил на все это.
PART_UPPER = and_(
    TITLE,
    or_(
        gram('Name'),
        gram('Surn')
    )
)

PART_NOCASE = or_(
    gram('Name'),
    gram('Surn')
)

# Дальше зрелище не для слабонервных. Я сам сдался и не трогаю это.
PERSON_NAME = or_(
    rule(SINGLE, '.', TITLE),
    rule(SINGLE, '.', SINGLE, '.', TITLE),
    rule(TITLE, SINGLE, '.', SINGLE, '.'),
    rule(PART_NOCASE, PART_NOCASE),
    rule(TITLE, PART_NOCASE),
    rule(PART_NOCASE, TITLE),
    rule(WITH_NAME, PART_UPPER),
    rule(PART_UPPER, WITH_NAME),
    rule(WITH_NAME, PART_NOCASE),
    rule(PART_NOCASE, WITH_NAME),
    rule(SINGLE, '.', WITH_NAME),
    rule(SINGLE, '.', SINGLE, '.', WITH_NAME),
    rule(WITH_NAME, SINGLE, '.', SINGLE, '.')
)

PERSON_NAME_WITH_KEY = or_(
    rule(WITH_NAME, PART_NOCASE),
    rule(PART_NOCASE, PART_NOCASE),
    rule(PART_NOCASE, WITH_NAME),
    rule(SINGLE, '.', WITH_NAME),
    rule(SINGLE, '.', SINGLE, '.', WITH_NAME),
    rule(WITH_NAME, SINGLE, '.', SINGLE, '.')
)

# Теперь список "титулов" для человека-улицы
POSITION_WORDS = or_(
    rule(
        dictionary({
            'мичман',
            'геолог',
            'подводник',
            'краевед',
            'снайпер',
            'штурман',
            'бригадир',
            'учитель',
            'политрук',
            'военком',
            'ветеран',
            'историк',
            'пулемётчик',
            'авиаконструктор',
            'адмирал',
            'академик',
            'актер',
            'актриса',
            'архитектор',
            'атаман',
            'врач',
            'воевода',
            'генерал',
            'губернатор',
            'хирург',
            'декабрист',
            'разведчик',
            'граф',
            'десантник',
            'конструктор',
            'скульптор',
            'писатель',
            'поэт',
            'капитан',
            'князь',
            'комиссар',
            'композитор',
            'космонавт',
            'купец',
            'лейтенант',
            'лётчик',
            'майор',
            'маршал',
            'матрос',
            'подполковник',
            'полковник',
            'профессор',
            'сержант',
            'старшина',
            'танкист',
            'художник',
            'герой',
            'княгиня',
            'строитель',
            'дружинник',
            'диктор',
            'прапорщик',
            'артиллерист',
            'графиня',
            'большевик',
            'патриарх',
            'сварщик',
            'офицер',
            'рыбак',
            'брат',
        })
    ),
    rule(normalized('генерал'), normalized('армия')),
    rule(normalized('герой'), normalized('россия')),
    rule(
        normalized('герой'),
        normalized('российский'), normalized('федерация')),
    rule(
        normalized('герой'),
        normalized('советский'), normalized('союз')
    ),
)

# Правила для человека-улицы
PERSON_PROBABLY = or_(
    rule(PERSON_NAME),
    rule(POSITION_WORDS, PERSON_NAME),
    rule(POSITION_WORDS, TITLE),
    rule(POSITION_WORDS, WITH_NAME),
    rule(POSITION_WORDS, PERSON_NAME_WITH_KEY)
)

# Теперь если есть ключевое слово "имени"
# Сами слова
IN_NAME_WORDS = or_(
    rule(
        caseless('им'),
        DOT.optional()
    ),
    rule(caseless('имени'))
)

# Правила для улицы имени человека
IN_NAME_RULES = or_(
    rule(
        IN_NAME_WORDS.optional(),
        PERSON_PROBABLY
    ),
    rule(
        IN_NAME_WORDS,
        TITLE
    )
)

# Если есть ключевое слово лет
# Сами слова
YEARS_OF_WORDS = or_(
    rule(caseless('лет')),
    rule(
        DASH.optional(),
        caseless('летия')
    )
)

# Лет чего
YEARS_OF_LIST = in_caseless({
    'влксм',
    'ссср',
    'алтая',
    'башкирии',
    'бурятии',
    'дагестана',
    'калмыкии',
    'колхоза',
    'комсомола',
    'космонавтики',
    'москвы',
    'октября',
    'пионерии',
    'победы',
    'приморья',
    'района',
    'совхоза',
    'совхозу',
    'татарстана',
    'тувы',
    'удмуртии',
    'улуса',
    'хакасии',
    'целины',
    'чувашии',
    'якутии',
})

# Правила для улицы лет
YEARS_OF = rule(
    INT,
    YEARS_OF_WORDS,
    YEARS_OF_LIST
)

# Слова модификаторы, которые, емнип, не используются.
MODIFIER_WORDS_ = rule(
    dictionary({
        'большой',
        'малый',
        'средний',

        'верхний',
        'центральный',
        'нижний',
        'северный',
        'дальний',

        'первый',
        'второй',

        'старый',
        'новый',

        'красный',
        'лесной',
        'тихий',
    }),
    DASH.optional()
)

ABBR_MODIFIER_WORDS = rule(
    in_caseless({
        'б', 'м', 'н'
    }),
    DOT.optional()
)

SHORT_MODIFIER_WORDS = rule(
    in_caseless({
        'больше',
        'мало',
        'средне',

        'верх',
        'верхне',
        'центрально',
        'нижне',
        'северо',
        'дальне',
        'восточно',
        'западно',

        'перво',
        'второ',

        'старо',
        'ново',

        'красно',
        'тихо',
        'горно',
    }),
    DASH.optional()
)

MODIFIER_WORDS = or_(
    MODIFIER_WORDS_,
    ABBR_MODIFIER_WORDS,
    SHORT_MODIFIER_WORDS,
)

# А теперь идет настоящее волшебство!
# Время собрать все, что выше в название улицы
# Тут заготовка для "обычных" названий
STREET_PROBABLY_UPPER = and_(
    or_(
        and_(ADJF, not_(APRO)),
        and_(NOUN, GEN),
    ),
    TITLE
)

STREET_PROBABLY_CASELESS = or_(
        and_(ADJF, not_(APRO)),
        and_(NOUN, GEN),
)

# Тут мои правки и легаси
# Доработал первое правило, чтобы отсеить "мусор"
COMPLEX = or_(
    rule(
        and_(ADJF, not_(APRO)),
        and_(NOUN, GEN)
    ),
    rule(
        TITLE,
        DASH.optional(),
        TITLE
    ),
)

# Исключения, которые не нужны
EXCEPTION = dictionary({
    'арбат',
    'варварка',
    'таганка',
    'покровка',
})

# Исключения, которые нужны
COMPLEX_EXCEPTION_WORDS = in_caseless({
    'гай',
    'вал',
    'аллея',
    'парк',
})

# Кейсы для валов, гаев, аллей, парков
COMPLEX_EXCEPTION = or_(
    rule(
        STREET_PROBABLY_CASELESS,
        COMPLEX_EXCEPTION_WORDS
    ),
    rule(
        STREET_PROBABLY_CASELESS,
        COMPLEX_EXCEPTION_WORDS
    ),
)

# "3 почтовое отделение", добавить нечего)
EXCEPTION_OTHER = rule(
    INT,
    ADJF,
    NOUN
).interpretation(
    Street.name
)

# Собираем название улицы первый раз
STREET_NAME = or_(
    rule(COMPLEX_EXCEPTION),
    rule(EXCEPTION),
    rule(COMPLEX),
    rule(STREET_PROBABLY_UPPER),
    rule(STREET_PROBABLY_CASELESS)
)

# Собираем название улицы второй раз
NAME = or_(
    YEARS_OF,
    IN_NAME_RULES,
    STREET_NAME
)

# Third time is the charm
ADDR_NAME = rule(
    MODIFIER_WORDS.optional(),
    NAME
)

# А теперь определяем тип
# Просто улица
# Слова-ключи
STREET_WORDS = or_(
    rule(normalized('улица')),
    rule(
        caseless('ул'),
        DOT.optional()
    )
).interpretation(
    Street.street_type.const('улица')
)

# Название
STREET_NAME_L = ADDR_NAME.interpretation(
    Street.name
)

# Кейсы
STREET = or_(
    rule(STREET_WORDS, EXCEPTION_OTHER),
    rule(STREET_WORDS, (gram('VERB')).optional(), STREET_NAME_L),
    rule(STREET_NAME_L, STREET_WORDS),
    STREET_NAME_L
).interpretation(
    Street
)

# Микрорайон
SUBDISTRICT_WORDS = or_(
    rule(
        in_caseless({'мкр', 'мик'}),
        DOT.optional()
    ),
    rule(
        caseless('мкр'),
        DASH,
        in_caseless({'н', 'он'}),
        DOT.optional()
    ),
    rule(normalized('микрорайон'))
).interpretation(
    Street.street_type.const('микрорайон')
)

SUBDISTRICT_NAME = ADDR_NAME.interpretation(
    Street.name
)

SUBDISTRICT = or_(
    rule(SUBDISTRICT_WORDS, SUBDISTRICT_NAME),
    rule(SUBDISTRICT_NAME, SUBDISTRICT_WORDS)
).interpretation(
    Street
)

# Проспект
AVENUE_WORDS = or_(
    rule(
        in_caseless({'пр', 'просп'}),
        DOT.optional()
    ),
    rule(
        caseless('пр'),
        DASH,
        in_caseless({'кт', 'т'}),
        DOT.optional()
    ),
    rule(normalized('проспект'))
).interpretation(
    Street.street_type.const('проспект')
)

AVENUE_NAME = ADDR_NAME.interpretation(
    Street.name
)

AVENUE = or_(
    rule(AVENUE_WORDS, AVENUE_NAME),
    rule(AVENUE_NAME, AVENUE_WORDS)
).interpretation(
    Street
)

# Проезд
DRIVEWAY_WORDS = or_(
    rule(caseless('пр'), DOT.optional()),
    rule(
        caseless('пр'),
        DASH,
        in_caseless({'зд', 'д'}),
        DOT.optional()
    ),
    rule(normalized('проезд'))
).interpretation(
    Street.street_type.const('проезд')
)

DRIVEWAY_NAME = ADDR_NAME.interpretation(
    Street.name
)

DRIVEWAY = or_(
    rule(DRIVEWAY_WORDS, DRIVEWAY_NAME),
    rule(DRIVEWAY_NAME, DRIVEWAY_WORDS)
).interpretation(
    Street
)

# Переулок
LANE_WORDS = or_(
    rule(
        caseless('п'),
        DOT
    ),
    rule(
        caseless('пер'),
        DOT.optional()
    ),
    rule(normalized('переулок'))
).interpretation(
    Street.street_type.const('переулок')
)

LANE_NAME = ADDR_NAME.interpretation(
    Street.name
)

LANE = or_(
    rule(LANE_WORDS, LANE_NAME),
    rule(LANE_NAME, LANE_WORDS)
).interpretation(
    Street
)

# Площадь
SQUARE_WORDS = or_(
    rule(
        caseless('пл'),
        DOT.optional()
    ),
    rule(normalized('площадь'))
).interpretation(
    Street.street_type.const('площадь')
)

SQUARE_NAME = ADDR_NAME.interpretation(
    Street.name
)

SQUARE = or_(
    rule(SQUARE_WORDS, SQUARE_NAME),
    rule(SQUARE_NAME, SQUARE_WORDS)
).interpretation(
    Street
)

# Шоссе
HIGHWAY_WORDS = or_(
    rule(
        caseless('ш'),
        DOT
    ),
    rule(normalized('шоссе'))
).interpretation(
    Street.street_type.const('шоссе')
)

HIGHWAY_NAME = ADDR_NAME.interpretation(
    Street.name
)

HIGHWAY = or_(
    rule(HIGHWAY_WORDS, HIGHWAY_NAME),
    rule(HIGHWAY_NAME, HIGHWAY_WORDS)
).interpretation(
    Street
)

# Тракт
TRACT_WORDS = rule(normalized('тракт')).interpretation(
    Street.street_type.const('тракт')
)

TRACT_NAME = ADDR_NAME.interpretation(
    Street.name
)

TRACT = or_(
    rule(TRACT_WORDS, TRACT_NAME),
    rule(TRACT_NAME, TRACT_WORDS)
).interpretation(
    Street
)

# Набережная
EMBANKMENT_WORDS = or_(
    rule(
        caseless('наб'),
        DOT.optional()
    ),
    rule(normalized('набережная'))
).interpretation(
    Street.street_type.const('набережная')
)

EMBANKMENT_NAME = ADDR_NAME.interpretation(
    Street.name
)

EMBANKMENT = or_(
    rule(EMBANKMENT_WORDS, EMBANKMENT_NAME),
    rule(EMBANKMENT_NAME, EMBANKMENT_WORDS)
).interpretation(
    Street
)

# Бульвар
BOULEVARD_WORDS = or_(
    rule(
        caseless('б'),
        DASH,
        caseless('р')
    ),
    rule(
        caseless('б'),
        DOT
    ),
    rule(
        caseless('бул'),
        DOT.optional()
    ),
    rule(normalized('бульвар'))
).interpretation(
    Street.street_type.const('бульвар')
)

BOULEVARD_NAME = ADDR_NAME.interpretation(
    Street.name
)

BOULEVARD = or_(
    rule(BOULEVARD_WORDS, BOULEVARD_NAME),
    rule(BOULEVARD_NAME, BOULEVARD_WORDS)
).interpretation(
    Street
)

# А теперь собираем "финальную версию" улицы
STREET_FINAL = or_(
    AVENUE,
    SUBDISTRICT,
    DRIVEWAY,
    LANE,
    SQUARE,
    HIGHWAY,
    EMBANKMENT,
    BOULEVARD,
    TRACT,
    STREET
).interpretation(
    Address.Street
)

# # # # # # # # # От дома до квартиры # # # # # # # # # # #

# Считаем номер "дома"/"квартиры"
LETTER = in_caseless(set('абвгдежзиклмнопрстуфхшщэюя'))
QUOTE = in_(QUOTES)

# Буква в номере
LETTER = or_(
    rule(LETTER),
    rule(QUOTE, LETTER, QUOTE)
)

# Разделители
SEP = in_({'-', '/', '\\'})

# Разные кейсы номера дома №1
VALUE = or_(
  rule(
    INT,
    SPACEBAR,
    LETTER
  ),
  rule(
    INT,
    SEP.optional(),
    LETTER.optional()
  )
)

# Разные кейсы номера дома №2
VALUE = or_(
    rule(VALUE, SEP, VALUE),
    rule(VALUE, SEP, LETTER),
    rule(VALUE)
)

# №
ADDR_VALUE = rule(
    eq('№').optional(),
    VALUE
)

# А теперь считаем номер дома
House = fact(
    'House',
    ['name', 'house_type']
)

# "Домашние" слова
HOUSE_WORDS = or_(
    rule(normalized('дом')),
    rule(
        caseless('д'),
        DOT
    ),
    rule(normalized('дом номер'))
).interpretation(
    House.house_type.const('дом')
)

# Сам номер дома
HOUSE_VALUE = ADDR_VALUE.interpretation(
    House.name
)

# И кейсы, которые мы рассматриваем
HOUSE = or_(
    rule(
      HOUSE_WORDS,
      HOUSE_VALUE
    ),
    HOUSE_VALUE
).interpretation(
    House
)

# Теперь в случае, если номер дома составной, то нужно распарсить номер и тип
Building = fact(
    'Building',
    ['name', 'building_type']
)

# Слова для коппуса
HOUSING_WORDS = or_(
    rule(
        in_caseless({'корп', 'кор', 'к'}),
        DOT.optional()
    ),
    rule(normalized('корпус'))
).interpretation(
    Building.building_type.const('корпус')
)

# Номер корпуса
HOUSING_VALUE = ADDR_VALUE.interpretation(
    Building.name
)

# Кейсы для корпуса
HOUSING = or_(
    rule(
        HOUSING_WORDS,
        HOUSING_VALUE
    ),
    rule(
        HOUSING_VALUE,
        HOUSING_WORDS
    )
).interpretation(
    Building
)

# То же, сто делали для корпуса, деламе и для строения
BUILDING_WORDS = or_(
    rule(
        caseless('стр'),
        DOT.optional()
    ),
    rule(
        caseless('ст'),
        DOT.optional()
    ),
    rule(normalized('строение'))
).interpretation(
    Building.building_type.const('строение')
)

# Номер
BUILDING_VALUE = ADDR_VALUE.interpretation(
    Building.name
)

# Кейсы
BUILDING = rule(
    BUILDING_WORDS,
    BUILDING_VALUE
).interpretation(
    Building
)

# Сохраняем то, что получили
BUILDING_FINAL = or_(
    HOUSING,
    BUILDING
).interpretation(
    Address.Building
)

# Теперь определяем квартира или офис
Appartment = fact(
    'Appartment',
    ['name', 'appartment_type']
)

# Слова для офиса
OFFICE_WORDS = or_(
    rule(
        caseless('оф'),
        DOT.optional()
    ),
    rule(normalized('офис'))
).interpretation(
    Appartment.appartment_type.const('офис')
)

# Номер офиса
OFFICE_VALUE = ADDR_VALUE.interpretation(
    Appartment.name
)

# Кейсы
OFFICE = or_(
    rule(
        OFFICE_WORDS,
        OFFICE_VALUE
        ),
    OFFICE_WORDS
).interpretation(
    Appartment
)

# Теперь квартира
APPARTMENT_WORDS = or_(
    rule(
        caseless('кв'),
        DOT.optional()
    ),
    rule(normalized('квартира'))
).interpretation(
    Appartment.appartment_type.const('квартира')
)

# Номер
APPARTMENT_VALUE = ADDR_VALUE.interpretation(
    Appartment.name
)

# Кейсы
APPARTMENT = or_(
    rule(
        APPARTMENT_WORDS,
        APPARTMENT_VALUE
    ),
    APPARTMENT_VALUE
).interpretation(
    Appartment
)

# Сохраняем нужное
APPARTMENT_FINAL = or_(
    OFFICE,
    APPARTMENT
).interpretation(
    Address.Appartment
)

# # # # # # # # # Главное правило # # # # # # # # # # #

# Теперь приводим все в финальный вид
CITY_FINAL = rule(
    CITY
).interpretation(
    Address.City
)

HOUSE_FINAL = rule(
    HOUSE
).interpretation(
    Address.House
)

# И вот главный кейссет-парсер
# Не самое красивое решение, кое-где костыли
# Но зато работает на тестовых данных
ADDRESS = or_(
    rule(
        CITY_FINAL,
        SEMICOLON.optional(),
        STREET_FINAL,
        HOUSE_FINAL,
        BUILDING_FINAL.optional(),
        APPARTMENT_FINAL.optional()
    ),
    rule(
        SIMPLE_WILDCARD.optional(),
        STREET_FINAL,
        HOUSE_FINAL,
        BUILDING_FINAL.optional(),
        APPARTMENT_FINAL.optional(),
        CITY_FINAL
    ),
    rule(
        CITY_FINAL,
        STREET_FINAL,
        HOUSE_FINAL.optional(),
        BUILDING_FINAL.optional(),
        APPARTMENT_FINAL.optional()
    ),
    rule(
        STREET_FINAL,
        CITY_FINAL,
        HOUSE_FINAL,
        BUILDING_FINAL.optional(),
        APPARTMENT_FINAL.optional()
    ),
    rule(
        CITY_FINAL.optional(),
        STREET_FINAL,
        SIMPLE_WILDCARD.optional(),
        HOUSE_FINAL,
        BUILDING_FINAL.optional(),
        APPARTMENT_FINAL.optional()
    ),
    rule(
        HOUSE_FINAL,
        CONJ,
        STREET_FINAL,
        BUILDING_FINAL.optional(),
        APPARTMENT_FINAL.optional()
    )
).interpretation(
    Address
)

# # # # # # # # # ФИО # # # # # # # # # # #

# Теперь парсер для распознавания ФИО
Name = fact(
    'Name',
    ['first', 'middle', 'last']
)

# Непотраченное согласование в падежах
gnc = gnc_relation()

# Неизвестные пайморфи фамилии
LAST = (type('RU')).interpretation(
    Name.last.inflected()
).match(gnc)

# Известные пайморфи фамилии
LAST_STD = and_(
    gram('Surn'),
    not_(PREP)
  ).interpretation(
    Name.last.inflected()
).match(gnc)

# Известные пайморфи имена
FIRST = gram('Name').interpretation(
    Name.first.inflected()
).match(gnc)

# Известные пайморфи отчества
MIDDLE = gram('Patr').interpretation(
    Name.middle.inflected()
).match(gnc)

# Если есть сокращения
ABBR = and_(
    length_eq(1),
    is_capitalized()
)

# Для имени
FIRST_ABBR = ABBR.interpretation(
    Name.first.custom(str.lower)
)

# Для отчества
MIDDLE_ABBR = ABBR.interpretation(
    Name.middle.custom(str.lower)
)

# Много-много правил
NAME = or_(
    rule(
        LAST,
        FIRST_ABBR, DOT,
        MIDDLE_ABBR, DOT
    ),
    rule(
        FIRST_ABBR, DOT,
        MIDDLE_ABBR, DOT,
        LAST
    ),
    rule(
        LAST,
        FIRST_ABBR, DOT
    ),
    rule(
        FIRST_ABBR, DOT,
        LAST
    ),
    rule(
        FIRST,
        MIDDLE,
        LAST
    ),
    rule(
        LAST,
        FIRST,
        MIDDLE
    ),
    rule(
        FIRST,
        MIDDLE
    ),
    rule(
        LAST,
        FIRST
    ),
      rule(
        LAST_STD,
        FIRST_ABBR, DOT,
        MIDDLE_ABBR, DOT
    ),
    rule(
        FIRST_ABBR, DOT,
        MIDDLE_ABBR, DOT,
        LAST_STD
    ),
    rule(
        LAST_STD,
        FIRST_ABBR, DOT
    ),
    rule(
        FIRST_ABBR, DOT,
        LAST_STD
    ),
    rule(
        FIRST,
        MIDDLE,
        LAST_STD
    ),
    rule(
        LAST_STD,
        FIRST,
        MIDDLE
    ),
    rule(
        LAST_STD,
        FIRST
    ),
    rule(
        FIRST
    ),
    rule(
        LAST_STD
    )
).interpretation(
    Name
)

# # # # # # # # # Модуль # # # # # # # # # # #

# Работает просто — инициализируем, вызываем из юниттестов нужный метод
# Он берет строчку, подставляет "шаблон" и ищет совпадения
# Возвращает массив, ибо может быть несколько совпадений
# В тестах этого либо нет, либо попадает мусор
# Поэтому в униттестах всегда беру первый элемент
class NERModule:
  def __init__(self):
        self.person_model = NAME
        self.address_model = ADDRESS

  def predictPerson(self, data_to_parse): # Для ФИО
    parser_person = Parser(self.person_model)
    matches = []
    for match in parser_person.findall(data_to_parse):
      matches.append(match.fact)
    return matches

  def predictAdress(self, data_to_parse): # Для адреса
    parser_address = Parser(self.address_model)
    matches = []
    for match in parser_address.findall(data_to_parse):
      matches.append(match.fact)
    return matches