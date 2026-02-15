# to define a dictionary we use {} and it's unordered
# dictionary is mutable you can write the items in both int ot srt
# left side is keys and right side is value 
# as for empty dictionary you use d = {}

marks =  {"sourabh" : 70,
           "rohan" : 20,
           "shubham" : 100,
            0 : "you"
         }

# in dictionary value are store in two pair one is key other value 
# there can't be two duplicate keys and it is indexed means
# it not going to check one by one once given a key it will directly jump there

print(marks, type(marks))
print(marks["rohan"])