
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter tempurture in f : "))
# and when we use f string and got some space in output we can use round example
c = f_to_c(f)
print(f"{round(c,2)}c")