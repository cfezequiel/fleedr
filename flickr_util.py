import urllib2
from lxml import objectify

URL_PUBLIC_FEED = 'https://api.flickr.com/services/feeds/photos_public.gne'

def get_public_feed():
    '''Retrieve images from Flickr feed URL

    Returns
        List of tuples, where each tuple contains image title and URL respectively

    '''

    # Read web page
    response = urllib2.urlopen(URL_PUBLIC_FEED)
    data = response.read()
    root = objectify.fromstring(data)

    # Parse data
    image_data = []
    for entry in root.entry:
        # Get image ID
        id_ = entry.id.text

        # Get image title
        title = entry.title.text

        # Get image URL
        link = entry.link[1]
        url = ''
        if link.get('rel') == 'enclosure':
            url = link.get('href')
        else:
            continue

        # Get image tags
        tags = []
        for cat in entry.category:
            tags.append(cat.get('term'))

        # Store extracted data in dictionary
        image_data.append(dict(id=id_, title=title, url=url, tags=tags))

    return image_data

if __name__ == '__main__':
    image_data = get_public_feed()
    print image_data[0]


