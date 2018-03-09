

def load_urls4check(path_to_urls):
    with open(path_to_urls, 'r', encoding='utf8') as file_with_urls:
        list_urls = file_with_urls.readlines()
        return list(map(lambda x: x.rstrip(), list_urls))


def is_server_respond_with_200(url):
    pass


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    path_to_urls = 'urls'
    urls4check = load_urls4check(path_to_urls)
