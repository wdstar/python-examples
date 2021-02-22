#!/usr/bin/env python3
import pymysql
import pymysql.cursors


def main():
    connection = pymysql.connect(
        host="localhost",
        user="user",
        password="passwd",
        database="db",
        cursorclass=pymysql.cursors.DictCursor,
    )

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO `users` (`account`, `email`) VALUES (%s, %s)",
                (
                    "alice",
                    "alice@example.com",
                ),
            )
        connection.commit()

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT `id`, `account`, `email` FROM `users` WHERE `account` = %s",
                ("alice",),
            )
            result = cursor.fetchone()
            print(result)


if __name__ == "__main__":
    main()
