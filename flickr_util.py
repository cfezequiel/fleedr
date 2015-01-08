import urllib2
from lxml import objectify
from werkzeug.urls import url_fix

URL_PUBLIC_FEED = 'https://api.flickr.com/services/feeds/photos_public.gne'

def get_public_feed(tags=None):
    '''Retrieve images from Flickr feed

    Returns
        List of tuples, where each tuple contains image title and URL respectively

    '''

    # Read web page
    url = URL_PUBLIC_FEED
    if tags:
        url = url_fix(url + '?tags=' + tags)
    response = urllib2.urlopen(url)
    data = response.read()

    # Used XML instead of JSON response from Flickr since Flickr JSON
    # escape format seems to be unsupported by Python json decoder 
    root = objectify.fromstring(data)

    # Parse data
    image_data = []
    for i, entry in enumerate(root.entry):
        # Get image ID
        #id_ = entry.id.text
        id_ = str(i) 

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

# Quick test for checking data
if __name__ == '__main__':
    image_data = get_public_feed()
    print image_data[0]


'''
            car 

            $('#search').click(function() {
                    $.getJSON($SCRIPT_ROOT + '/_search', {
                        tags: $('input[name="search"]').val()
                        }, function(data) {
                        });
                    return false;
                    });
'''

'''
<!-- 
{% for image in images %}
<div class="photo" id="{{ image.id }}">
    <img src="{{ image.url }}" alt="{{ image.title }}">
    <p><span class="like">Like</span></p>
</div>
{% else %}
    <em>Unbelievable! No images! </em>
{% endfor %}
-->
'''
