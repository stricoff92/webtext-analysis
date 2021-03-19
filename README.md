# Webtext Analysis

## About
This application scrapes text from the web. You can choose to scrape with a simple crawler or a headless browser.
Currently the app supports 2 contents types: `text/plain` and `text/html`.

![](https://i.imgur.com/rt4tnEDh.jpg)

## Requirements
1. Linux or MacOS is recommended
2. Python3.6.X or better
3. Node.js 8 or Better

## Installation
4. Install Python 3.6.X or Better
5. Initialize you python environment and install dependancies
```bash
# Using virtualenv

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
6. (Optional) Install MySQL and create a database for this app
```bash
# Using docker
$ docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=YOUR_PASSWORD_GOES_HERE -v /tmp:/tmp --name YOUR_DATABASE_NAME_GOES_HERE -d mysql --default-authentication-plugin=mysql_native_password
```
7. (Optional) If you want to scrape with a headless browser you will need to install Google Chrome and download a webdriver for chrome [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
8. Create `applocals.py` file.
```bash
$ touch webtext/webtext/applocals.py
```

```python
# Example `applocals.py` file

# DO NOT COMMIT THIS FILE

SECRET_KEY = 'ADD YOUR SECRET KEY HERE'

ENV = "DEV"

ALLOWED_HOSTS = ["*"]

# TO USE MySQL
MYSQL_DB_NAME = "YOUR_DATABASE_NAME_GOES_HERE"
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = "3306"
MYSQL_USER = "DB USER NAME GOES HERE"
MYSQL_PASS = "YOUR PASSWORD GOES HERE"

# OR TO USE SQLITE
USE_SQLITE = True

# Optional
CHROME_DRIVER_PATH = "/home/path/chromedriver_linux64/chromedriver"
```
To generate secret keys
```bash
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
9. Initialize Your database and add a super user
```bash
$ ./manage.py migrate
$ ./manage.py createsuperuser

# Start the development server
$ ./manage.py runserver
```
10. Install Node.js 8 or better. Install NPM.
11. Install Node dependancies
```bash
$ cd webtext/website/appclient
$ npm install
```
12. Build Angular Assets
```bash
# Build assets once
$ ng build --output-hashing all --base-href /static/

# Build and watch for changes
$ ng build --watch --output-hashing all --base-href /static/
# or
$ npm run-script builddev
```