def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum


def display(**kwargs):
    ls=[]
    for key,value in kwargs.items():
       ls.append(f"{key} : {value}")
    return ls