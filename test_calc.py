import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_oper(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(4, 2,"^"), 16)
        
    def test_add_neg(self):
        """Символы вместо чисел (a+2)"""
        self.assertEqual(calc_me("a", 2, "+"), "ERROR: now it is does not supported")

    def test_add_neg1_null(self):
        """Функция без первой переменной (None+2)"""
        self.assertEqual(calc_me(None, 2, "+"), "ERROR: send me Number1")        

    def test_add_neg2_null(self):
        """Функция без второй переменной (2+None)"""
        self.assertEqual(calc_me(2, None, "+"), "ERROR: send me Number2")        

if __name__ == '__main__':
    unittest.main(verbosity=2)