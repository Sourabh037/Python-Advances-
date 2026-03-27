# create a file or either write something in

st = "hello i am learning pyhton"

f = open("myfile.txt", "w")

f.write(st)

# add something at the end of file

st = "from harrywithcode"

f = open("myfile.txt", "a")

f.write(st)

f.close()