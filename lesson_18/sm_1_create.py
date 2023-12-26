import psycopg2
from config import host, user, password, db_name

connection = None

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT version()"""
        )
        print(f"server version: {cursor.fetchall()}")

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            foreign_id integer unique not null,
            name varchar(50)  not null,
            email varchar(50) not null ,
            CONSTRAINT proper_email CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
            age integer check(age > 0) not null)"""
        )

        print("[Info] Table  created")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE country(
            id serial PRIMARY KEY,
            foreign_id integer unique not null,
            name varchar(50)  not null)"""
        )

        print("[Info] Table  created")

        with connection.cursor() as cursor:
            cursor.execute(
                """Create table user_country(
            user_id integer references users(id),
            country_id integer references country(id)
            )"""
            )

        print("[Info] Table  created")

except Exception as _ex:
    print("[Info]  Error", _ex)
finally:
    if connection:
        connection.close()
        print("[Info] PSQL connection close")
