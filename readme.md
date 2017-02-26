# Social Media Finder
This python script goes to a website and looks for external links to known social media domains. Each result is stored in a dictionary and the result is printed.

## Installation Guide
___
Python 3.5 on OS: Ubuntu 16.04

- Clone repo
```
$git clone 'https://github.com/path/to/repo'
```
- Create virtualenv
```
$virtualenv env
```
- Activate it
```
$source env/bin/activate
```
  - Download Geckodriver

    [geckodriver](https://github.com/mozilla/geckodriver/releases)

    [geckodriver-v0.14.0-linux64.tar.gz](https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz)
  - Place the driver in your virtualenv directory

    ```
    /env/bin/<geckodriver-goes-here>
    ```

- Install dependencies
```
$pip install -r requirements.txt
```
- collect data
```
$python getsocial.py 'http://www.example.com'
```

## Credits

Copyright (c) 2017 [Kevin Tarvin](http://www.kevintarvin.com/)
