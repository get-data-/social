# Social Media Finder
This python script goes to a website and looks for external links to known social media domains. Each result is stored in a dictionary and the result is printed.

## Installation Guide
___
Python 3.5 on OS: Ubuntu 16.04

1. Clone repo
```
$git clone 'https://github.com/path/to/repo'
```
2. Create virtualenv
```
$virtualenv env
```
3. Activate it
```
$source env/bin/activate
```
  1. Download Geckodriver

    [geckodriver](https://github.com/mozilla/geckodriver/releases)

    [geckodriver-v0.14.0-linux64.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz)

  2. Place the driver in your virtualenv directory
    ```
    /env/bin/<geckodriver-goes-here>
    ```

4. Install dependencies
```
$pip install -r requirements.txt
```

5. collect data
```
$python getsocial.py 'http://www.example.com'
```

## Credits

Copyright (c) 2017 [Kevin Tarvin](http://www.kevintarvin.com/)
