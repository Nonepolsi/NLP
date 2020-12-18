import unittest
import module_gordeevmv

# Почти все изменения делал для работаспособности тестов с моим модулем, суть не изменилась.

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = module_gordeevmv.NERModule()

    def test_one(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('комсомольский', 'проспект'), (res.Street.name, res.Street.street_type))
        self.assertEqual('50', res.House.name)


    def test_second(self):
        testing_address = 'город липецк улица катукова 36 а'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('липецк', 'город'), (res.City.name, res.City.city_type))
        self.assertEqual(('катукова', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('36 а', res.House.name) # Не знаю, специально или нет, но "а" была латинская


    def test_third(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('сургут', None), (res.City.name, res.City.city_type))
        self.assertEqual(('рабочая', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('31а', res.House.name)


    def test_fouth(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('липецк', 'город'), (res.City.name, res.City.city_type))
        self.assertEqual(('доватора', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('18', res.House.name)

    def test_behtereva(self):
        testing_address =  'ну бехтеева 9 квартира 310'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('бехтеева', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('9',res.House.name)
        self.assertEqual(('310', 'квартира'), (res.Appartment.name, res.Appartment.appartment_type))

    def test_moskovskaya(self):
        testing_address =  'московская 34б'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('московская', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('34б', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_minina(self):
        testing_address =  'улица минина дом 1'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('минина', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('1', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_30_let_victory(self):
        testing_address =  'сколько улица 30 лет победы 50 46'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('30 лет победы', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('50', res.House.name)
        self.assertEqual('46', res.Appartment.name)

    def test_tract(self):
        testing_address = 'тюменский тракт 10'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('тюменский', 'тракт'), (res.Street.name, res.Street.street_type))
        self.assertEqual('10', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_beregovaya(self):
        testing_address =  'береговая 43 береговая 43 сургут'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('сургут', None), (res.City.name, res.City.city_type))
        self.assertEqual(('береговая', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('43', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_yuogorskaya(self):
        testing_address =  'сургут югорская 30/2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('сургут', None), (res.City.name, res.City.city_type))
        self.assertEqual(('югорская', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('30/2', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_index(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.predictAdress(testing_address)
        self.assertEqual([], res)

    def test_salmanova(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('сургут', 'город'), (res.City.name, res.City.city_type))
        self.assertEqual(('фармана салманова', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('4', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_vidnoe(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('видное', 'город'), (res.City.name, res.City.city_type))
        self.assertEqual( ('зеленые аллеи', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('8', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_zelinskogo(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('зелинского', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('2', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_kuskovaya_corpus(self):
        testing_address = 'Кусковская 19 корпус 1 '
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('Кусковская', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('19', res.House.name)
        self.assertEqual(('1', 'корпус'), (res.Building.name, res.Building.building_type))
        self.assertEqual(None, res.Appartment)

    def test_shosse(self):
        testing_address = 'москва щелковское шоссе 35'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('москва', None), (res.City.name, res.City.city_type))
        self.assertEqual(('щелковское', 'шоссе'), (res.Street.name, res.Street.street_type))
        self.assertEqual('35', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_park(self):
        testing_address = 'город москва марьинский парк дом 25 корпус 2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('москва', 'город'), (res.City.name, res.City.city_type))
        self.assertEqual(('марьинский парк', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('25', res.House.name)
        self.assertEqual(('2', 'корпус'), (res.Building.name, res.Building.building_type))
        self.assertEqual(None, res.Appartment)

    def test_gai(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('Старый Гай', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('1', res.House.name)
        self.assertEqual(('2', 'корпус'), (res.Building.name, res.Building.building_type))
        self.assertEqual(None, res.Appartment)

    def test_third_post(self):
        testing_address = 'улица 3 почтовое отделение дом 62'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(None, res.City)
        self.assertEqual(('3 почтовое отделение', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('62', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_july_Street(self):
        testing_address = 'нижний новгород улица июльских дней 19'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('нижний новгород', None), (res.City.name, res.City.city_type))
        self.assertEqual(('июльских дней', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('19', res.House.name)
        self.assertEqual(None, res.Appartment)

    def test_val(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('москва', None), (res.City.name, res.City.city_type))
        self.assertEqual(('хамовнический вал', None), (res.Street.name, res.Street.street_type))
        self.assertEqual(None, res.House)
        self.assertEqual(None, res.Appartment)

    def test_semen_bilecky(self):
        testing_address = 'город сургут улица семена билецкого 1'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('сургут', 'город'), (res.City.name, res.City.city_type))
        self.assertEqual(('семена билецкого', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('1', res.House.name)
        self.assertEqual(None, res.Appartment)


    def test_critical(self):
        testing_address = 'улица значит антонова овсиенко дом 19/2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('антонова овсиенко', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('19/2', res.House.name)

    def test_critical0(self):
        testing_address = 'улица генерала армии епишева дом 9'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('генерала армии епишева', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('9', res.House.name)


    def test_critical1(self):
        testing_address = 'улица академика байкова дом 9'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual('9', res.House.name)
        self.assertEqual(('академика байкова', 'улица'), (res.Street.name, res.Street.street_type))

    def test_critical2(self):
        testing_address = 'улица академика байкова дом дом дом 9'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual('9', res.House.name)
        self.assertEqual(('академика байкова', 'улица'), (res.Street.name, res.Street.street_type))

    def test_critical2_3(self):
        testing_address = 'улица подзаборного байкова дом дом дом 9'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual('9', res.House.name)
        self.assertEqual(('подзаборного байкова', 'улица'), (res.Street.name, res.Street.street_type))

    def test_critical2_4(self):
        testing_address = 'улица монтажника байкова дом дом дом 9'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual('9', res.House.name)
        self.assertEqual(('монтажника байкова', 'улица'), (res.Street.name, res.Street.street_type))

    def test_critical3(self):
        testing_address = 'такзначит у меня дом номер 12 а улица джона рида'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('джона рида', 'улица'), (res.Street.name, res.Street.street_type))
        self.assertEqual('12', res.House.name)

if __name__ == '__main__':
    unittest.main()