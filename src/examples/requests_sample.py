#!/usr/bin/env python3
import requests
from requests.sessions import session
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

proxies = {
    # "https": "http://proxy.example.com:3128/",
    # "http": "http://proxy.example.com:3128/",
}


def get_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


def main():
    url = "https://www.google.com/"
    res = requests.get(url, proxies=proxies)
    print(res)
    print(res.url)
    print(res.headers)
    print(res.status_code)
    print(res.text)

    session = get_session()
    res = session.get(url, proxies=proxies)
    res.raise_for_status()
    print(res)


if __name__ == "__main__":
    main()
