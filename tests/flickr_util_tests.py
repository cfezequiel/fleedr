import unittest 

import flickr_util

class FlickrUtilTestCase(unittest.TestCase):

    def test_get_public_feed_no_tags(self):
        data = flickr_util.get_public_feed()
        self.assertTrue(data)

    def test_get_public_feed_with_tags(self):
        tags = 'rage face, meme'
        data = flickr_util.get_public_feed()
        self.assertTrue(data)


if __name__ == '__main__':
    unittest.main()

