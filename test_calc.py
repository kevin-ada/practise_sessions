import unittest
import main


class Testfunctons(unittest.TestCase):
    def testadd(self):
        result = main.add(10, 5)
        self.assertEqual(result, 15)

    def testsub(self):
        self.assertEqual(main.sub(10, 5), 5)
        self.assertEqual(main.sub(-1, -1), 0)

    def testmul(self):
        self.assertEqual(main.mul(10, 5), 50)
        self.assertEqual(main.mul(-1, -1), 1)

    def testdiv(self):
        result = main.div(10, 5)
        self.assertEqual(result, 2)
        self.assertRaises(ZeroDivisionError, main.div, 10, 0)










if __name__ == '__main__':
    unittest.main()