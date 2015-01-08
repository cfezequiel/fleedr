# Fleedr
Web app that shows images from Flickr Public Feed.
Allows images to be liked, and specific images to be searched using keywords.
Built using Python Flask.

## Files

- `fleedr.py`: Main server application
- `flickr_util.py`: Contains utility methods for interacting with Flickr API
- `/tests`: Test files
    - `header.py`: Defines sys.path extensions for importing code-under-test
    - `*_tests.py`: Test corresponding **.py* code 
- `/templates`: HTML templates (Jinja2 format)
    - `layout.html`: Top-level template extended in other templates
    - `index.html`: Front page template
- `/static`: Static files
    - `style.css`: CSS style file

## Deployment

To start the web server, go to the top directory and call:
```
$ python fleedr.py
```

## Third-party libraries

- *lxml*: XML processing (http://lxml.de/)
