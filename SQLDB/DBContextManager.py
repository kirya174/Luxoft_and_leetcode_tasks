import config
import psycopg2
from psycopg2 import sql
from contextlib import closing
from datetime import datetime

class Context(object):
    def __init__(self, sql):        
        self.__sql_query = sql
        self.__conn = psycopg2.connect(**config.dbparam2)
        self.__cur = self.__conn.cursor()

    def __enter__(self):        
        self.__cur.execute(self.__sql_query)
        self.__conn.commit()
        return self

    def fetchone(self):
        return self.__cur.fetchone()[0]

    def fetchall(self):
        return self.__cur.fetchall()


    def __exit__(self,type,value,trace):
        self.__cur.close()
        self.__conn.close()         

def create_table():
    sql_query = """            
            CREATE TABLE public.products
            (
                id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
                title varchar(50) NOT NULL
            );

            CREATE TABLE public.price
            (
                id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
                id_product int NOT NULL,
                price int NOT NULL
            )
            """
    with Context(sql_query) as f: pass    


def insert_products(products):        
    ids = []
    for product in products:     
        sql_query = sql.SQL("INSERT INTO public.products (title) VALUES ({}) RETURNING id ").\
        format(sql.Literal(product))
        with Context(sql_query) as f:                             
            print(f"execute SQL: {sql_query}")                
            ids.append(f.fetchone())
    return ids        


def insert_price(prices):
    cols = ("id_product","price")
    sql_query = sql.SQL("INSERT INTO public.price ({}) VALUES ({}) RETURNING ID").\
            format(
                sql.SQL(',').join(map(sql.Identifier,cols)),
                sql.SQL(',').join(map(sql.Literal,prices))
                )    
    with Context(sql_query) as f:
        return f.fetchone()


def get_all_schedule():
    sql_query = """
            SELECT departure.title, departure_time, arrival.title, arrival_time FROM public.schedules 
            LEFT JOIN public.stations as departure ON departure.id = public.schedules.id_departure
            LEFT JOIN public.stations as arrival ON arrival.id = public.schedules.id_destination
            """
    with Context(sql_query) as f:  
        recordset = f.fetchall()
        return recordset



# # create_table()
# # insert_products(['egg1', 'egg2','egg3'])
# insert_price((12,400))