from urllib.parse import urlsplit

def get_base_url(url):
    parsed = urlsplit(url)
    return parsed.scheme + '://' + parsed.netloc + parsed.path