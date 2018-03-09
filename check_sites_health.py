import sys
import whois
import requests
import datetime


def load_urls4check(path_to_urls):
    with open(path_to_urls, 'r', encoding='utf8') as file_with_urls:
        list_urls = file_with_urls.readlines()
        return list(map(lambda x: x.rstrip(), list_urls))


def is_server_respond_with_200(url):
    try:
        status_code = requests.get(url, timeout=5).status_code
        return status_code == 200
    except requests.RequestException:
        return False


def get_expiration_date(domain_name):
    whois_data = whois.whois(domain_name)
    expiration_date = whois_data.expiration_date
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[0]
    return expiration_date


def is_expiration_date_more_month(expiration_date):
    if expiration_date is None:
        return None
    remaining_days = expiration_date - datetime.datetime.now()
    return remaining_days > datetime.timedelta(days=31)


def print_server_status(server_status):
    message = 'OK' if server_status else 'Error'
    print('URL status: {0}'.format(message))


def print_domain_status_expiration(status_expiration):
    if status_expiration:
        message = 'OK'
    elif status_expiration is None:
        message = 'No information'
    else:
        message = 'Need payment'
    print('Domain status expiration: {0}'.format(message))


def test_urls(list_urls):
    for url in list_urls:
        try:
            delimiter = '-' * 50
            print(delimiter, url, sep='\n')
            print_server_status(is_server_respond_with_200(url))
            expiration_date = get_expiration_date(url)
            status_expiration = is_expiration_date_more_month(expiration_date)
            print_domain_status_expiration(status_expiration)
        except whois.parser.PywhoisError:
            print('No information about domain')


if __name__ == '__main__':
    try:
        path_to_urls = sys.argv[1]
        urls4check = load_urls4check(path_to_urls)
        test_urls(urls4check)
    except FileNotFoundError as text_error:
        exit(text_error)
    except IndexError:
        exit('No directory path. Try again entering the path')
