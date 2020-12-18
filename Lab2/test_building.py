import unittest
import module_gordeevmv

# Почти все изменения делал для работаспособности тестов с моим модулем, суть не изменилась.

class TestHome(unittest.TestCase):
    def setUp(self):
        self.NERInstance = module_gordeevmv.NERModule()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '50')

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 а'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '36 а') # Не знаю, специально или нет, но "а" была латинская

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '31а')

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '18')

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '9')

    def test_6(self):
        testing_address = 'артема 32 квартира 8'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '32')

    def test_7(self):
        testing_address = 'город липецк полиграфическая дом 4'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '4')

    def test_8(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '55')
        self.assertEqual((res.Building.name, res.Building.building_type), ('1', 'корпус'))

    def test_9(self):
        testing_address = 'люберцы октябрьский проспект 10 корпус 1'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '10')
        self.assertEqual((res.Building.name, res.Building.building_type), ('1', 'корпус'))

    def test_10(self):
        testing_address = 'бульвар миттова 24'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '24')

    def test_11(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res = self.NERInstance.predictAdress(testing_address)
        res = res[0]
        self.assertEqual(res.House.name, '78')


if __name__ == '__main__':
    unittest.main()
