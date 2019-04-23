#_*_coding=utf-8_*_

print('\n\n unittest use')
import unittest
from C03UnitTestBase import Dict

class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))
		
	def setUp(self):
		print('setUp')
		
	def tearDown(self):
		print('tearDown')
		
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key, 'value')
		
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')
		
	def test_keyerror(self):
		d=Dict()
		print('test_keyerror')
		with self.assertRaises(KeyError):
			value = d['empty']
			
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
		
	
print('\n\n	对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：')

from C03UnitTestBase import Student 
		
class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

#if __name__ == '__main__':
 #   unittest.main()