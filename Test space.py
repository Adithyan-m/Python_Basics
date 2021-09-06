"""

#lists

num = [4, 8, 9, 7, 5, 2]
friendds = ["Alex","Jim","Harold","suzi","Philip","alfred"]
print(friendds)
print(friendds[0])              #accesing list elements using index
print(friendds[-1])             #accessing from the back
print(friendds[1:])             #open range
print(friendds[1:4])            #closed range
print("\n")

#tuples

coordinate = (4 , 5)            #they cant be changes or modified
print(coordinate[0])
print("\n")

#functions

def say_hi(name):
    print("hello " + name)

say_hi("mike")
print("\n")


def calculator(a,b):
    result = a + b
    return result

ans = calculator ( int ( input ( "enter one number : " ) ) ,int ( input ( "enter another number : " ) ) )
print(ans)
print("\n")

#if statements

is_Male = True
is_tall = True

if is_Male and is_tall:                      #can be replaced with "or" or "=="
    print("you are privilaged")
elif is_Male and not(is_tall):
    print("you are sort of privilaged")
elif is_tall and not(is_Male):
    print("you are sort of privilaged")
else:
    print("you are not privilaged")


#finding maximum of three numbers

def max_num(a,b,c):
    if a >= b and a >= c :
        return a
    elif b >= c and b >= a :
        return b
    else:
        return c

print(max_num(1,2,3))



#dictionaries

Monthconv = {
    "jan":"January",
    "feb":"February",
    "mar":"March",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    "aug":"August",
    "sep":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December"
}

print(Monthconv["nov"])
print(Monthconv.get("luv","not a valid key"))     #seconf premeter is a default return



#while loop

i = 1
while i <= 10:
    print(i)
    i +=1

print("loop terminated")



#for loops

for letters in "hello this is pc":
    print(letters)

ar1 = [1, 2, 3, 34, 5, 64, 5, 45, 6, 7, 5, 4, 6, 78]
for num in ar1:
    print("hello world")

for index in range(len(ar1)):       #accessing items using index and len
    print(ar1[index])

i = 1
for index in range(15):
    print(f"my age is {i}")          #f string formating
    i +=1

for index in range(5):               #applying logic
    if index == 0:
        print("first one")
    else:
        print("next one")

#exponent function
print (2**3)       #2^3

#custon exponent function

def expo(base,power):
    result = 1
    for num in range(power):
        result *= base
    return result


a = float(input("enter base :"))
b = int(input("enter power : "))
print(expo(a,b))


# try/except
try:
    num = int(input("enter a number : "))       #if a int is not entered then expcept block code will be run
    number = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("pls make sure entered number is true")

 #or

try:
    num = int(input("enter a number : "))  # if a int is not entered then expcept block code will be run
    number = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError as errr:
    print(errr)



#files

with open("sample3.txt","r+") as f:
    for lines in f.readlines():
        print(lines)

with open("sample3.txt","r+") as f:
    print(f.readlines()[2])

with open("sample3.txt","r+") as f:
    print(f.read())

with open("sample3.txt","r+") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())             #reads one line at a time and moves it to

with open("sample3.txt","r+") as f:     #adds text to end
    f.write("toby - alfred\n")
    print(f.readlines())


with open("sample3.txt","r+") as f:         #if we use "w" instead, it will overight current file, or it will create file if it doesnt exist
    f.seek(4)       #moving text to particular line
    print(f.readline())
"""


