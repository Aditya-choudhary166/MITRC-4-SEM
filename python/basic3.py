#set---unordered,duplicate not ,immutable;
st={"hello",1,2,True,"hello"} #1=true,0=false if we runt the code 1,is print but true is not print
print(st)
print(type(st))    #add and remove kr skte hai


#dictionary -indexing not allowed 
##
dt={
    "name": "upflairs",
    "year": 2023,
}
print(dt)
print(type(dt))
dt["name"]
print(dt["name"])

dt["name"]="google"#update the value in dict.
print(dt["name"])
dt.get("name")


#dictionary constructor
dt1=dict(name="upflairs",year=2023)
print(dt1)

#item-key or value pair 
dt.get("name")
dt.items()
dt.pop("name") #pop delete the elements
dt.update({"name":"amazon","address":"xyz"})
print(dt.update({"name":"amazon","address":"xyz"}))
print(dt.items())

