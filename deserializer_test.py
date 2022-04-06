import deserializer

buffer = input(">") # key1:value1:key2:value2:key3:value3

data_list = buffer.split(':')

data = ((data_list[i],data_list[i+1]) for i in range(0, len(data_list), 2))

x = deserializer.get_object(data)

for key,value in data:

    v = getattr(x,key,None)

    if v != value:

        raise Exception()

print("ok")

