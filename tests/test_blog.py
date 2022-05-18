import unittest
from app.models import Blog_post

class BlogTest(unittest.TestCase):
    '''
    test Class to test the behaviour of the Blog-post class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_blogs = Blog_post(id = 1, content='test-content', author = 'test-author',category='test-category')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_blogs, Blog_post))