# # i=1
# # while i<=10:
# #     print(i)
# #     i+=1

# # 
# #i=1
# # while i<6:
# #     i+=1
# #     if i==3:
# #         continue
# #     print(i)
# i=1
# while i<6:
#     print(i)
#     i+=1
#     if(i==3):
#         print(i)
#         break
#         i+=1

# #reverse while loop
# i=10
# while i>=0:
#     print(i)
#     i-=1

#check how many times a given number can be divided by 3 before 
#it is less than or equal to 10
# count=0
# number=100
# while number>10:
#     number=number/3
#     count+=1
# print("total iteration",count)  

#iterate a list with the help of while loop

# lst=[1,2,3,4,5,6,7]

# size=len(lst)
# i=0
# while i<size:
#     print(lst[i])
#     i+=1


# def hello():
#     #block of code
#     print("hellofrom function")
# hello()

##parameters and argumments
#parameters="jb function banate hai tb value pass krna"
#arguments="calling ke krte smay value pass krna"

# def name(fname):
#     print("hello my name is",fname)

# name("adi")

def goodday(name):
    print("good day, "  + name)
goodday("aditya")


##arbitary arguments --args--*
##jb apan ko nhi pta hota number of arguments kitne pass honge
#example:::--
# def my_fun(*kids):
#     print("the youngest child is "+kids[2])
# my_fun("mohan","rohan","aditya")

# age=10
# text="my name is"+age  #it gives error because we can concatenate string and integer
# print(text)

#formatted strings
# age=10
# text=f"my age is {age}"
# print(text)



##keyword arguments --jaha aap argument ki value
#as a key value pair pass karta ho

# def children(child1,child2,child3):
#     print("the youngest child is" +child2)
# children(child2="mohan",child1="rohan",child3="rohit")



##arbitary keyword arguments --kwargs--**
# def children(**child):
#     print("the youngest child is" +child["fname"] +child["lname"])
# children(fname="rohan",lname="sharma")


# ##default parameter value

# def country(name="india"):
#     print("my country is",name)
# country() #we also pass 

#avg

def average(input):
    return sum(input)/len(input)
a=average([1,2,34,4,5])
print(a)


##list---square--list
# lst=[1,2,3,4,3,4]

##square
# lst=[1,2,3,4,2]
# temp=[]
# for i in lst:
#     temp.append(i*i)
# print(temp)


##lambda function --small function--
#multiple arguments but one expression

# x=lambda a : a+10
# print(x(5))


# x=lambda a,b,c: a+b+c
# print(x(5,2,3))

def add(input):
    return sum(input)
a=add([1,2,3,4,5])
print(a)




    

