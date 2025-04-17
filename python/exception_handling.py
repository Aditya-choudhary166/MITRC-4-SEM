#exception handling-->(try,except,else,finally)
#try-->jo bhi code likenge try mai 
#except---> try code ke andar error handle karega usse except handle karega
#else-->jb try ke andar error nhi ayegi tb chalega
#finally-->chaelga hi

try:
    print(10/0)
except Exception as e :#-->sari error hai Exception ke andar
     print(e)
else:
     print("hello")
finally:
     print("world")