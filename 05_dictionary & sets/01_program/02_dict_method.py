marks =  {"sourabh" : 70,
           "rohan" : 20,
           "shubham" : 100,
            0 : "you"
         }

# it will show all the item in form of list and the item will be shown as tuple
print(marks.items())

# it will show all the keys
print(marks.keys())

# it will show all the values
print(marks.values())

# it will update the value
marks.update("sourabh" : 75, "remuru" : 100)
print(marks)

# the difference is first one show none and other an error why bcz key doesn't exist
print(marks.get("sourabh1")) 
print(marks["sourabh1"])
