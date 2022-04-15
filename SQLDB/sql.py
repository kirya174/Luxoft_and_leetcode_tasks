import config
import psycopg2
from contextlib import closing
from psycopg2 import sql
from datetime import datetime


def create_table():
    with closing(psycopg2.connect(**config.dbparam)) as db:
        with db.cursor() as cursor:
            sql_query = """
            CREATE TABLE public.stations 
            (
                id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
                title varchar(50) NOT NULL
            );
            CREATE TABLE public.schedule
            (
                id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
                id_departure bigint NOT NULL,
                id_destination bigint NOT NULL,
                departure_time timestamp,
                arrival_time timestamp
            )
            """
            cursor.execute(sql_query)
            db.commit()


def insert_stations(stations):
    ids = []
    with closing(psycopg2.connect(**config.dbparam)) as db:
        with db.cursor() as cursor:
            for station in stations:
                sql_query = sql.SQL("INSERT INTO public.stations (title) VALUES({}) RETURNING id"). \
                    format(sql.Literal(station))
                print(f"execute SQL:{sql_query}")
                cursor.execute(sql_query)
                db.commit()
                ids.append(cursor.fetchone()[0])
    return ids


def insert_schedule(schedule):
    with closing(psycopg2.connect(**config.dbparam)) as db:
        columns = ("id_departure", "id_destination", "departure_time", "arrival_time")
        with db.cursor() as cursor:
            sql_query = sql.SQL("INSERT INTO public.schedule ({}) VALUES({}) RETURNING id"). \
                format(
                sql.SQL(',').join(map(sql.Identifier, columns)),
                sql.SQL(',').join(map(sql.Literal, schedule))
            )
            cursor.execute(sql_query)
            db.commit()
            return cursor.fetchone()[0]


def get_all_schedules():
    with closing(psycopg2.connect(**config.dbparam)) as db:
        with db.cursor() as cursor:
            sql_query = """
            SELECT departure.title, destination.title, departure_time, arrival_time
            FROM public.schedule
            LEFT JOIN public.stations as departure ON departure.id = public.schedule.id_departure
            LEFT JOIN public.stations as destination ON destination.id = public.schedule.id_destination
            """
            cursor.execute(sql_query)
            db.commit()
            recordset = cursor.fetchall()
            return recordset


# print(insert_stations(["SPB", "Chelyabinsk"]))
# print(insert_schedule((1, 2, datetime(2022, 4, 15), datetime(2022, 4, 16))))
schedules = get_all_schedules()
for c in schedules:
    print(f"departure {c[0]} {c[2]} arrival {c[1]} {c[3]}")
