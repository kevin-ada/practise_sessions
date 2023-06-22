import unittest
from main import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("Start of the tests")
        self.empl1 = Employee(first='Kim', last='Codes', pay=8000)
        self.empl2 = Employee(first='Jim', last='Codes', pay=8000)


    def tearDown(self):
        print("End of the Test")
        pass




    def testFullname(self):
        print("Testing the full name")
        self.assertEqual(self.empl2.get_full_name, 'JimCodes')
        self.assertEqual(self.empl1.get_full_name, 'KimCodes')

        self.empl1.first = 'Kevin'
        self.empl1.last = 'Koech'

        self.empl2.first = 'Kim'
        self.empl2.last = 'Codes'

        self.assertEqual(self.empl1.get_full_name, 'KevinKoech')
        self.assertEqual(self.empl2.get_full_name, 'KimCodes')

    def testEmail(self):
        print('Testing email')
        self.assertEqual(self.empl1.get_email, 'KimCodes@company.com')
        self.assertEqual(self.empl2.get_email, 'JimCodes@company.com')




