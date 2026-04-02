'''
f took data form the file and give it to data
and data got print
and you can read it without write a read function it's a default 
'''


f = open("file.txt")
data = f.read()
print(data)
f.close()
# .......