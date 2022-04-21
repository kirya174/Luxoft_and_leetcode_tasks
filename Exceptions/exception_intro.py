def make_error(x):
    if x > 5:
        return x / 0
    else:
        return x * 2
def make_syntax_error(x):
    if x > 5:
        print__(x)
            
try:

    print(make_error(3))
    print(make_error(6))
    print(make_error(2))
   
except ZeroDivisionError:
    print("Ooops!")

try:
    
    make_syntax_error(6)

except NameError as e:
    print(f"Error in call unknow function {e.args[0]}")
