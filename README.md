# Sites Monitoring Utility

This script tests URLs into a file:
1. The response of the status code of the HTTP server is 200
1. Domain expiration term ends in more than a month


# How to install
Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt
```
# Quick start

```bash
$ python3 check_sites_health.py <filepath_with_urls>
```

Running on Windows is similar.

*(Possibly requires call of 'python' executive instead of just 'python3'.)*

# Example

Use [this list urls](https://www.dropbox.com/s/gza2mhx5v7tzahg/urls?dl=0) for script test.

```bash
$ python3 check_sites_health.py test/urls 
--------------------------------------------------
http://grawlix.nl
URL status: Error
Domain status expiration: No information
--------------------------------------------------
http://f63.net
URL status: OK
Domain status expiration: Need payment
--------------------------------------------------
http://kgb.su
URL status: Error
Domain status expiration: OK
--------------------------------------------------
http://chronicle.su
URL status: Error
Domain status expiration: OK
--------------------------------------------------
http://nic.re
URL status: OK
Domain status expiration: OK
--------------------------------------------------
http://ersi.se
URL status: Error
No information about domain
```

# Possible answers
1. ```URL status: OK``` - URL status is 200
1. ```URL status: Error``` - URL status isn't 200 or an error occurred
1. ```Domain status expiration: OK``` - domain's expiration date is more than 1 month
1. ```Domain status expiration: Need payment``` - domain's expiration date is more than 1 month
1. ```Domain status expiration: No information``` - expiration date unknown
1. ```No information about domain```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
