###modes--> 
# r -- open the file in reading mode
#w --overite
#a-->append
##b-->binary files
##+ --read and write 
##r+-->read the write in reading mode
# file=open("demo.txt","r")
# print(file.read())
# file.close()


# ##2 way --with statement --close need nhi hoti hai
# # with open("demo.txt","r") as file:
# #  print(file.readline())#read single line
# #  print(file.readlines())#return a list

# # 
# with open("demo.txt","w") as file:
#  print(file.write(""))#read single line
 

#  ##json file
# import json
# data={
#    "name":"aditya",
#     "year": 2020
#  }
# with open ("data.json","w") as file:
#   json.dump(data,file)

# with open("data.json","r") as file:
#      content=json.load(file)
#      print(content)


##create a file in csv format;[home work]
import pandas as pd

# Load CSV file
df = pd.read_csv('Used_Bikes[1].csv')


# Display the first few rows
print(df.head())




 