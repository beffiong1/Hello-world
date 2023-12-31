print("This line will be printed")
#if statements 
x= 1 
if x==1:
      #indented four spaces
    print ("x is 1.")
print("Goodbye World")


#variables and types
  #numbers
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

#strings
mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)
mystring = "Dont worry about apostrophes"
print(mystring)
#combinatorsß
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
#assignments
a, b = 3, 4
print(a, b)

# #mixing operators
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# mylist = [1,2,3]
# print(mylist[10])

#Exercise
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = []
strings.append("hello world")

names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#basic operators
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3

print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

#Exercise

x = (1, 2, 3)
y = (4,5,6)

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


#string formating
name = "john"
print("hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

#Exercise

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s your current balance is $%s "

print( format_string % data)



#still string operations
astring = "Hello world!"
astring2 = 'Hello world!'

astring = "Hello world!"
print("single quotes are '  ' " )
print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring =  "Hello world!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

astring = "Hello world!"
print(astring[::-1])

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

astring = "Hello world!"
afewwords = astring.split(" ")

#exercise

s = "Hey there! what should this string be?"

# Length should be 34 (not 20)
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 13 (not 8)
print("The first occurrence of the letter a = %d" % s.index("a"))

# Slicing the string into bits

# The first five characters are 'Hey t' (not 'Hey there!')
print("The first five characters are '%s'" % s[:5]) # Start to 5

# The next five characters are 'here!' (not ' what')
print("The next five characters are '%s'" % s[5:10]) # 5 to 10

# The thirteenth character is 'h' (not 't')
print("The thirteenth character is '%s'" % s[12]) # Just number 12

# The characters with odd index are 'e hr!wa hudti tigb?' (not 'e  etrwhta hsi tigb')
print("The characters with odd index are '%s'" %s[1::2]) # (0-based indexing)

# The last five characters are 'g be?' (not 'g this string be?')
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())


#conditions
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
