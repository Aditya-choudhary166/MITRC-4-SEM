# # print("hello world")
# # a=10
# # print(type(a))
# a="aditya"
# print(type(a))
# l=[12,44,556,4]
# h=l.sort()
# for i in l:
#     print(i) #multiple line comment

company=" upflairs"
company.upper()
company.lower()

print(company.upper().title())#first letter capital or small
print(company.upper())
print(company.replace("upflairs","adi"))

# company="upflairs companyyyyyyyyyyyy"
# print(company.count("y"))

# company="upflairs company"
# print(company.removeprefix("upflairs"))
# print(company.removesuffix("company"))

# print(company[0])
# print(company[-10])

# a="aditya company"
# #silicing [start:stop:skip]
# #list--mutuable



# lst=[12,34,22,44,56,34,"hello","true"]
# print(type(lst))

# lst=["red","black","blue"]
# h=lst.append("green")
# for i in lst:
#     print(i)
#print(lst)
# lst.clear()#clear kr dega list ko khali

# print(lst)

# print(lst.extend(["green","yellow"])) #elements ko list mai aur extend ke liye
# print(lst)
# lst.index("red")

lst=[12,34,56,45,33]
lst.sort(reverse=True)#reverse the list
print(list)

#without list method reverse a list
# lst[::-1]
# print(lst)

lst.append("adi") #append last mai append krta hai
print(lst)

lst.insert(2,"hello") #insert take two arguments we can insert element at any position
print(lst)

lst.pop(1)
print(lst)

# lst.remove("red")#remove the element
# print(lst)

# lst1=lst.copy()
# print(lst1)

# tpl=(1,2,45,33,2,3,4,2)
# print(type(tp1))

tp=("hello",) #single element tupple
print(type(tp))

a=(2,3,4,5)
repeated=a *3 #repeat the value 3 times
print(repeated)

t=(1,2,3,4,5)
print(1 in t) #returns true or false


