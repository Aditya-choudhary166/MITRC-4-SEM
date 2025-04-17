# def square(input):
#     return input**2
# square(3)

# ##map --(function,iterable)


# #### with the help of lambda function
# l=[2,3,4,5,6]
# newl=list(map(lambda a:a*a,l))
# print(newl)

# ###passing square in map
# l=[2,3,4,5,6]
# newl=list(map(square,l))
# print(newl)

# ##filter --(function,iterable)
def ff(a):
    return a%2==0
l=[2,3,4,5,6]
newl=list(filter(ff,l))
print(newl)



#reduce --(function,iterable)
from functools import reduce 
l=[2,3,4,5,67,8]
newl=reduce(lambda x,y : x+y,l)
print(newl)


##enumerate---provide a index to each number
name=["python","java","c"]
enumate_list=list(enumerate(name))
enumate_list
print(enumate_list)




