#!/usr/bin/env python3
import requests

proxies = {
    # "https": "http://proxy.example.com:3128/",
    # "http": "http://proxy.example.com:3128/",
}


def main():
    res = requests.get("https://www.google.com/", proxies=proxies)
    print(res)
    print(res.url)
    print(res.headers)
    print(res.status_code)
    print(res.text)


if __name__ == "__main__":
    main()
