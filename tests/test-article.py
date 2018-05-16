import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
	'''
	Test Class to test the behaviour of the Article class
	'''
    def setUp(self):
        '''
		Set up method that will run before every Test
		'''
        self.new_article = Articles()

    def test_instance(self):
        '''
		A method that will run to test whether an instance is of Article class.
		'''
        self.assertTrue(isinstance(self.new_article,Articles))

