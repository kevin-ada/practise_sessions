import unittest
from class_employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start")

    @classmethod
    def tearDownClass(cls):
        print("End")


    def setUp(self):
        print('Setup')
        self.emp1 = Employee(first='Jim', last='Codes', pay=6000)
        self.emp2 = Employee(first='Kim', last='Codes', pay=8000)

    def tearDown(self):
        print('Tear Down')
        pass

    def testFullname(self):
        print('name')
        self.assertEqual(self.emp1.get_full_name(), 'JimCodes')
        self.assertEqual(self.emp2.get_full_name(), 'KimCodes')

    def testEmail(self):
        print('email')
        self.assertEqual(self.emp1.get_email(), 'JimCodes@example.com')
        self.assertEqual(self.emp2.get_email(), 'KimCodes@example.com')

    def testPay(self):
        print('epay')
        self.assertEqual(self.emp1.raise_pay(), 6300)
        self.assertEqual(self.emp2.raise_pay(), 8400)

    def test_monthly_Schedule(self):
        with patch('class_employee.requests.get') as mock:
            mock.return_value.ok = True
            mock.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('June')
            mock.assert_called_with('https://company.com/Codes/June')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()
