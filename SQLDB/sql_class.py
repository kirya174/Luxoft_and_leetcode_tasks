import config
from contextlib import closing
from psycopg2 import sql, connect
from datetime import datetime


class SqlTable:
    def __init__(self, name: str):
        self.__fields = None
        self.__name = name

    def create_table(self, fields: dict):
        """ Создание таблицы в БД """
        self.__fields = fields.keys()
        create_query = f"""CREATE TABLE IF NOT EXISTS public.{self.__name} """
        fields_query = f"{self.__name}_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,"
        for field in fields.keys():
            fields_query += f"{field} {fields[field]},"
        sql_query = f"""{create_query}
                    (
                    {fields_query[:-1]}
                    );"""
        self.execute_and_commit(sql_query)
        print(f'table "{self.__name}" has been created')

    def add_items(self, items_to_add):
        """ Добавление элементов в таблицу """
        function = "add"
        ids = []
        if self.__fields is None:
            self.get_field_names()
        columns = self.__fields
        for item in items_to_add:
            if item is not None:
                sql_query = sql.SQL("INSERT INTO public.{}({}) VALUES({}) RETURNING {}"). \
                    format(sql.Identifier(self.__name),
                           sql.SQL(',').join(map(sql.Identifier, columns)),
                           sql.SQL(',').join(map(sql.Literal, item)),
                           sql.SQL(f'{self.__name}_id')
                           )
                ids.append(self.execute_and_commit(sql_query, function))

    # def __del__(self):
    #     """ Удаление таблицы из БД при удалении объекта класса """
    #     sql_query = sql.SQL("DROP TABLE public.{}").format(sql.Identifier(self.__name))
    #     self.execute_and_commit(sql_query)
    #     print(f'table "{self.__name}" has been deleted')

    def get_all_items(self):  # JOIN с другой таблицей доделать
        if self.__fields is None:
            self.get_field_names()
        function = "get"
        sql_query = sql.SQL("SELECT * FROM public.{};").format(sql.Identifier(self.__name))
        entries = self.execute_and_commit(sql_query, function)
        elems = []
        for entry in entries:
            entry_dict = {}
            for key, elem in zip(self.__fields, entry[1:]):
                entry_dict[key] = elem
            elems.append(entry_dict)
        return elems

    def get_field_names(self):
        function = "field_names"
        sql_query = sql.SQL("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {};").\
            format(sql.Literal(self.__name))
        self.__fields = self.execute_and_commit(sql_query, function)

    @staticmethod
    def execute_and_commit(sql_query, function=None):
        # print(f"execute SQL:{sql_query}")
        with closing(connect(**config.dbparam)) as db:
            with db.cursor() as cursor:
                cursor.execute(sql_query)
                db.commit()
                match function:
                    case "add":
                        entry_id = cursor.fetchone()[0]
                        return entry_id
                    case "get":
                        entries = cursor.fetchall()
                        return entries
                    case "field_names":
                        fields = [field[0] for field in cursor.fetchall()]
                        return fields[1:]


table_name = "schedule"
table_fields = {
    "id_departure": "bigint NOT NULL",
    "id_destination": "bigint NOT NULL",
    "departure_time": "timestamp",
    "arrival_time": "timestamp"
}

test_table = SqlTable(table_name)
test_table.create_table(table_fields)

items = [(3, 4, datetime(2020, 5, 16), datetime(2021, 5, 18))]
test_table.add_items(items)

schedule = test_table.get_all_items()
for departure in schedule:
    print(departure)



# def get_all_schedules():
#     with closing(connect(**config.dbparam)) as db:
#         with db.cursor() as cursor:
#             sql_query = """
#             SELECT departure.title, destination.title, departure_time, arrival_time
#             FROM public.schedule
#             LEFT JOIN public.stations as departure ON departure.id = public.schedule.id_departure
#             LEFT JOIN public.stations as destination ON destination.id = public.schedule.id_destination
#             """
#             cursor.execute(sql_query)
#             db.commit()
#             recordset = cursor.fetchall()
#             return recordset
#
# schedules = get_all_schedules()
# for c in schedules:
#     print(f"departure {c[0]} {c[2]} arrival {c[1]} {c[3]}")