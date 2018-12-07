def a():
    return sum_2num(2,3)
def sum_2num(a,b):
    if not isinstance(a,int):
        return a
    elif not isinstance(b,int):
        return b
    sums = a+b
    return sums

print(a())
