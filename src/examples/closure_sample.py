#!/usr/bin/env python3
import configparser
from pathlib import Path


def get_func():
    # Config caching
    config = None

    def get(key):
        nonlocal config
        # Lazy loading
        if config is None:
            print("Loading config.ini ...")
            config = configparser.ConfigParser()
            config.read(Path(__file__).parent / "config.ini")

        return config["test"][key]

    return get


get = get_func()


def main():
    print(get("name"))
    print(get("key-a"))
    print(get("key-b"))


if __name__ == "__main__":
    main()
