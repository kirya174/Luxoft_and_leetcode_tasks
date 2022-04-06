def my_sum(source, p):
    sum_out = 0
    for elem in source:
        if p(elem):
            sum_out += elem
    return sum_out


def mul(param):
    def decorator(func):
        def wrapped(source, p):
            return func(source, p) * param
        return wrapped
    return decorator
