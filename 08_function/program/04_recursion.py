''' factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X........3 X 2 X 1
factorial(n) = n * factorial(n-1) '''
                    # |___________this is the formula we used in recursion

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("enter a number : "))
# print(f"the factorial of this number is : {factorial(n)}")

# next example
# sum(6) = 1 + 2 + 3 + 4 + .......n-1 + n
# sum(n) = sum(n-1) + n
# so the formula work likes 
# sum(3) = sum(3-1) + 3 => 2 + 3 but n = 2 why bcz sum(n) now
# sum(2) = sum(2-1) + 5 why 5 bcz addtion

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) +n

print(sum(4))