import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
	Test Class to test the behaviour of the Source class
	'''

    def setUp(self):     
        '''
		Set up method that will run before every Test Case
		'''
        self.new_source = Source("ars-technica", "ars-technica", "it", "http://arstechnica.com", "general", "it", "us", )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))