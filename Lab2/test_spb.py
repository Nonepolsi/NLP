import unittest
import module_gordeevmv

# Все изменения делал для работаспособности тестов с моим модулем, суть не изменилась.

class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = module_gordeevmv.NERModule()

    def test_shkolnaya(self):
        testing_address = 'санкт-петербург школьная 20'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('санкт-петербург', None), (res.City.name, res.City.city_type))
        self.assertEqual(('школьная', None), (res.Street.name, res.Street.street_type))
        self.assertEqual('20', res.House.name)

    def test_full_gagarina(self):
        testing_address = 'санкт-петербург юрия гагарина 22 к2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('санкт-петербург', None), (res.City.name, res.City.city_type))
        self.assertEqual(('юрия гагарина', None), (res.Street.name, res.Street.street_type))
        self.assertEqual(('2', 'корпус'), (res.Building.name, res.Building.building_type))
        self.assertEqual('22', res.House.name)

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        #self.assertEqual(('санкт-петербург', None), res.City) комментарий не мой
        self.assertEqual(('гагарина', None), (res.Street.name, res.Street.street_type))
        self.assertEqual(('2', 'корпус'), (res.Building.name, res.Building.building_type))
        self.assertEqual('22', res.House.name)

    def test_untolovsky(self):
        testing_address = "санкт-петербург;юнтоловский 43 корпус 1"
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('санкт-петербург', None), (res.City.name, res.City.city_type))
        self.assertEqual(('юнтоловский', None), (res.Street.name, res.Street.street_type))
        self.assertEqual(('1', 'корпус'), (res.Building.name, res.Building.building_type))
        self.assertEqual('43', res.House.name)


    def test_untolovsky_str(self):
        testing_address = "санкт-петербург;юнтоловский 43 строение 1"
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('санкт-петербург', None), (res.City.name, res.City.city_type))
        self.assertEqual(('юнтоловский', None), (res.Street.name, res.Street.street_type))
        self.assertEqual(('1', 'строение'), (res.Building.name, res.Building.building_type))
        self.assertEqual('43', res.House.name)

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(('юнтоловский', None), (res.Street.name, res.Street.street_type))
        self.assertEqual(('1', 'строение'), (res.Building.name, res.Building.building_type))
        self.assertEqual('43', res.House.name)
