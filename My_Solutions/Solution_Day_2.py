# Take a **name as input** and print a greeting message for that name

# x = input("Enter you name : ")
# print(f"Hello , {x} welcome to my DSA Challenge")

# -------------------------------------------------------------------------------------------------------

# Input **Principal (P), Time (T), Rate (R)** from the user and calculate **Simple Interest**.

# p = int(input("Enter the principal : "))
# t = int(input("Enter the time : "))
# r = int(input("Enter the rate : "))

# SI = (p * t * r) / 100
# print(f"The Simple intrest is : {SI}")

# -------------------------------------------------------------------------------------------------------

# Take two numbers and an **operator (+, -, *, /)** as input and calculate the result using if conditions.

# x = int(input("Enter a number : "))
# y = int(input("Enter a number : "))

# a = x + y
# b = x - y
# c = x * y
# d = x / y

# print( a  , b , c , d)

# -----------------------------------------------------------------------------------------------------

# Take **2 numbers** as input and print the **largest**.

# x = int(input("Enter the number : "))
# y = int(input("Enter the number : "))

# if x > y :
#     print(f"The given {x} is largest")
# else:
#     print(f"The given {y} is largest")

# ------------------------------------------------------------------------------------------------

# Input an amount in **Indian Rupees** and convert it to **USD**.

# x = int(input("Enter price in Indian Rupees : "))
# y = x / 83.5
# print(f"The amount in $ is {y}")

# -------------------------------------------------------------------------------------------

#  Print the **Fibonacci Series** up to n numbers

# x = int(input("Enter the place : "))
# a = 0
# b = 1
# c = 0
# while c < x:
#     print(a)
#     n = a + b
#     a = b
#     b = n
#     c += 1

# -------------------------------------------------------------------------------------

# Check whether a given **String is a Palindrome** or not

# x = int(input("Enter a string : "))
# temp = x
# rev = 0
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# if(rev == x):
#     print(f"The given string is palindrome : {x}")
# else:
#     print("the given string is not palindrome.")


# x = input("Enter a string : ")
# rev = x[::-1]
# if x == rev:
#     print(f"The given string is palindrome : {x}")
# else:
#     print("the given string is not palindrome.")

# Find all **Armstrong Numbers** between two given numbers.

x = int(input("Enter a number : "))

temp = x
y = 0
while temp > 0:
    z = temp % 10
    z = z * z * z # ( z ** 3)
    y = y + z
    temp //= 10

if y == x : 
    print(f"the given number {x} is armstrong.")
else:
    print(f"the given number is not armstrong")
