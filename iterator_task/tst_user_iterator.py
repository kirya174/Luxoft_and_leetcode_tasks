import user_iterator

buffer = input(">")

p = input(">")

lst = ( int(x) for x in buffer.split(' '))

exec("predicate = lambda x: " + p)

it = user_iterator.get_object(lst, predicate)

for c in it:

    if c != None:

        print(c,end=' ')

    else:

        print('----NoneType----')


"""
Sample input:
-1 2 -5 5 -4 -3 2 3 5 6 -10
x>0
Sample output:
2 5 2 3 5 6 
"""