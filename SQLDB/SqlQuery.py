class Entity:
    def __str__(self):
        result = ""
        for key, val in self.__dict__.items():
            result += f'field = {key} with value {val}\n'
        return result

    def get_createtable_query(self):
        fields = []
        for field_name, field_value in self.__dict__.items():
            if field_name == "ID":
                fields.append(f"{field_name} bigint NOT NULL GENERATED ALWAYS AS IDENTITY")
            elif type(field_value) == int:
                fields.append(f"{field_name} bigint NOT NULL")
            elif type(field_value) == str:
                fields.append(f"{field_name} varchar(50) NOT NULL")
        return f"CREATE TABLE public.{type(self).__name__} ({fields});"

    def get_inserttable_query(self):
        values = ["'" + str(val) + "'" for val in self.__dict__.values()]
        fields = [key for key in self.__dict__.keys()]
        return f"INSERT INTO {type(self).__name__} ({','.join(fields)}) VALUES ({','.join(values)})"


class Person(Entity):
    def __init__(self, ID, first_name, last_name, age):
        self.id = ID
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


peter = Person("0", "Peter I", "Romanov", 30)
print(peter)
print(peter.get_createtable_query())
print(peter.get_inserttable_query())
