# # # # a=int(input("enter the number user"))
# # # # b=int(input("enter the number user"))
# # # # import math
# # # # z=math.lcm(a,b)
# # # # print(z)

# # # # a=int(input("enter the number"))
# # # # print() #print is used to give the space
# # # # print()
# # # # b=int(input("enter the number"))
# # # # print(a,b)

# # # # x=5
# # # # y=9
# # # # print(x,y,sep=' & ')

# # # # x=6
# # # # bin(x)
# # # # print(bin(x))


# # # company="upflairs"
# # # company.upper()
# # # company.lower()
# # # # print(y.upper().title())
# # # # print(x)

# # # print(company.upper().title())
# # # print(company.replace("upflairs","Adi"))

# # # a="aditya is a good boy"
# # # a.upper().title()
# # # print(a.capitalize().title())
# # # print(a[3])

# # # h="aditya company"
# # # g=h[::-1]
# # # print(g)

# # # l=[18,34,323,1]
# # # l.sort(reverse=True)
# # # print(l)

# # # t1=(1,55,23,45,2)
# # # # t1.sort()
# # # t2=list(t1)

# # # t2.sort()
# # # print(t2)
# # # t3=tuple(t2)
# # # print(t3)

# # # marks={
# # #    "harry":100,
# # #    "aditya":95,
# # #    "rohan":89
# # # }
# # # print(marks["aditya"])
# # # print(type(set()))


# # # s={1,4,2,45,45,"adi"}
# # # h=s.add(556)
# # # print(s)

# # # s1={1,2,34,22,3}
# # # s2={23,23,2,34,2,32,32,}
# # # print(s1.intersection(s2))

# # # #dictionary constructor
# # # dt1=dict(name="upflairs",year=2023)
# # # print(dt1)

# # # marks1=int(input("enter the marks 1:"))
# # # marks2=int(input("enter the marks 2:"))
# # # marks3=int(input("enter the marks 3:"))

# # # #check for total percentage
# # # total_percentage=(100*(marks1+marks2+marks3))/300
# # # if(total_percentage>=40):
# # #     print("you are pass",total_percentage)
# # # else:
# # #     print("you failed ",total_percentage)




# # # p1="make a lot of money"
# # # p2="buy now"
# # # p3="click this"

# # # message=input("enter your comment:")
# # # if((p1 in message) or (p2 in message) or (p3 in message)):
# # #     print("this comment is a spam")
# # # else:
# # #     print("this is not a spam")



# # # user_name=input("enter the username")
# # # if(len(user_name)<10):
# # #     print("user name is contain 10 characters")
# # # else:
# # #     print("nothing")


# # # l=["harry","rohan","shubham","aditya"]
# # # name=input("enter your name:")
# # # if(name in l):
# # #     print("your name in the list")
# # # else:
# # #     print("not")
# # # for i in range(1,101):
# # #     print(i)

# # # p=1
# # # while(p<100):
# # #     print(p)
# # #     p+=1

# # # l=["adi",False,"rohan","shubham"]
# # # i=0
# # # while(i<len(l)):
# # #     print(l[i])
# # #     i+=1
# # l=[1,7,8]
# # for item in l:
# #     print(item)
# # else:
# #     print("done") #this is print when loop is exhaust


# # for i in range(10):
# #     if(i==5):#exit the loop right now
# #         break
# #     print(i)


# # for i in range(10):
# #     if(i==5):#skip the iteration
# #         continue
# #     print(i)

# # def greet():
# #     print("good day")
# # greet()


# # def average(input):
# #     return sum(input)/len(input)
# # print(average)
   

# # average([1,2,34,4,5])
# # print(average)

# # # lst=[1,2,3,4,2]
# # # temp=[]
# # # for i in lst:
# # #     temp.append(i*i)
# # # print(temp)



# # # x=lambda a : a+10
# # # print(x(5))

# # # y=lambda a,b,c : a+b+c
# # print(y(5,7,9))


# # def a_o_c():
# #     pi=3.14
# #     a_o_c=pi*radius*radius
# #     return a_o_c

# # radius=int(input("enter the radius : "))
# # a = a_o_c()
# # print("the radius of circle is",a)

# # x=lambda a : a+10
# # print()


# def ff(a):
#     return a%2==0
# l=[2,3,4,5,6]
# newl=list(filter(ff,l))
# print(newl)

# l=[2,3,4,5,6]
# newl=list(filter(lambda a : a%2==0,l))
# print(newl)



# name=["python","java","c"]
# a=list(enumerate(name))
# # enumate_list
# print(a)

import os

if os.path.exists("data.json"):
    print("File mil gayi!")
else:
    print("File nahi mili 😅")
