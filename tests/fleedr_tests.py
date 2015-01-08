import unittest
import json

import header

import fleedr

class FleedrTestCase(unittest.TestCase):

    def setUp(self):
        fleedr.app.config['TESTING'] = True
        self.app = fleedr.app.test_client()

    def test_search_no_tags(self):
        '''Test search URL without tags.

        Return value should be in JSON format
        '''

        rv = self.app.get('/_search')
        self.assertTrue(json.loads(rv.data))

    def test_search_with_tags(self):
        '''Test search URL with tags.

        Return value should be in JSON format
        '''

        tags = 'meme, rage face'
        rv = self.app.get('/_search', data=dict(tags=tags))
        self.assertTrue(json.loads(rv.data))


if __name__ == '__main__':
    unittest.main()
