s = "Deepak Prajapati"
print(s) # Deepak Prajapati

# return string lenght
lenght = len(s)
print(lenght) # 16


#-------- formatting methods ----------
name = "Ram"
print(f"Hii, {name}") # Hii, Ram
print(f"{name=}") # name='Ram'

# ------------------------------------
PI = 3.14159

print(f"{PI=}") # PI=3.14159

print(f"{PI:.2f}") # 3.14

# ------------------------------------
nums = 1143.34234

print(f"{nums:,.3f}") # 1,143.342

print(f"{nums:.3e}") # 1.143e+03

# -------------------------------
roll_no = 101
salary = 12312342

print(f"{roll_no:07}") # 0000101

print(f"{salary:,}") # 12,312,342

print(f"{salary:_}") # 12_312_342

# -------------------------------
number = 142 

print(f"{number:b}") # 10001110 (convert in binary)
print(f"{number:o}") # 216 (convert in octal)
print(f"{number:x}") # 8e (convert in hexadecimal)

# -------------------------------
num = 42

# Right-aligned inside a 10-character box
print(f"|{num:>10}|")  # |        42|

# Center-aligned inside a 10-character box
print(f"|{num:^10}|")  # |    42    |

# Left-aligned inside a 10-character box
print(f"|{num:<10}|")  # |42        |





''' STRING METHODS LIST '''



# Dynamically formats placeholders within a string.
s = "Hello , {}".format("ram")
print(s) # Hello , ram


#-------- case conversion methods ----------

#convert in lowercase  
s = "RAM".lower()
print(s) # ram

#convert in uppercase  
s = "ram".upper()
print(s) # RAM

#first character in capital and other wrords in lowercase  
s = "ramKumar".capitalize()
print(s) # Ramkumar

#first character in capital of each words.  
s = "ramKumar".title()
print(s) # Ramkumar

# convert in toggle word.  
s = "RamKumar".swapcase()
print(s) # rAMkUMAR


#-------- alignment and padding methods ----------

# center the string fill by a specified character.  
s = "ram".center(7,'-')
print(s) # --ram--

# left justify the string fill by a specified character.  
s = "ram".ljust(7,'-')
print(s) # ram----

# right justify the string fill by a specified character.  
s = "ram".rjust(7,'-')
print(s) # ----ram

# fill zeros on the left of the string ,with given width.  
s = "68".zfill(7)
print(s) # 0000068


#-------- searching and counting methods ----------

# count the substring.  
s = "ramkumar ramji ramnarayan rameshewar".count("ram")
print(s) # 4 times occurs

# gives the index of first occured substring, otherwise -1 .
s = "ramkumar".find("a")
print(s) # 1 

# gives the index of last occured substring, otherwise -1 .
s = "ramkumar".rfind("a")
print(s) # 6 

# same as find() method, but it gives ValueError if substring not found.  
s = "ramkumar".index("a")
print(s) # 1

# same as rfind() method, but it gives ValueError if substring not found.  
s = "ramkumar".rindex("a")
print(s) # 6


#-------- splitting and joining methods ----------

# join the string character using given separator.
# join/merge the iterable elements {like string,list,tuple} using separator.
s = "-".join("ram")
print(s) # r-a-m

s = "-".join(("ram","is","good","boy"))
print(s) # ram-is-good-boy

# splits the string the fisrt occurence of separator and return a 3-tuple
s = "a-b-c-d".partition("-")
print(s) # ('a', '-', 'b-c-d')

# splits the string the last occurence of separator and return a 3-tuple
s = "a-b-c-d".rpartition("-")
print(s) # ('a-b-c', '-', 'd')

# splits a string into a list using a delimiter, by default maxsplit = -1.
# maxsplit means Maximum number of splits.
# maxsplit = -1 (the default value) means no limit.
s = "hii this is deepak prajapati".split(" ")
print(s) # ['hii', 'this', 'is', 'deepak', 'prajapati']

# splits a string into a list from right, using a delimiter, by default maxsplit = -1.
s = "hii this is deepak prajapati".rsplit(" ",maxsplit = 2)
print(s) # ['hii this is', 'deepak', 'prajapati']

# splits a string at line breaks
s = "ram\nis\ngood\nboy".splitlines()
print(s) # ['ram', 'is', 'good', 'boy']


#-------- cleaning and modifying methods ----------

# Replaces \t tab characters with spaces.
s = "ram\tis\tgood\tboy".expandtabs(10)
print(s) # ram       is        good      boy

# Removes a specified prefix if it exists.
s = "ramkumaryadav".removeprefix("ram")
print(s) # kumaryadav

# Removes a specified suffix if it exists.
s = "ramkumaryadav".removesuffix("yadav")
print(s) # ramkumar

# Replaces occurrences of a substring with a new one.
s = "mohan is good boy".replace("o","0")
print(s) # m0han is g00d b0y

# Remove/trim whitespaces or specified character from both side.
s = "   shyam   ".strip()
print(s) # ram

s = "bbbbbbbbbrambbbbbbbbb".strip("b")
print(s) # ram

# Remove/trim whitespaces or specified character from left side.
s = "bbbbbbbbbrambbbbbbbbb".lstrip("b")
print(s) # rambbbbbbbbb

# Remove/trim whitespaces or specified character from right side.
s = "bbbbbbbbbrambbbbbbbbb".rstrip("b")
print(s) # bbbbbbbbbram



#-------- boolen evaluation methods (Returns True or Fasle) ---------

# Checks if the string begins with the specified value.
s = "python".startswith("py")
print(s) # True

# Checks if the string ends with the specified value.
s = "python".endswith("on")
print(s) # True

#  Returns True if all characters are alphanumeric (letters or numbers).
s = "python123".isalnum()
print(s) # True

#  Returns True if all characters belong to the ASCII character set.
s = "python".isascii()
print(s) # True

# Returns True if all characters are basic decimals (0-9).
s = "123456".isdecimal()
print(s) # True

#  Returns True if all characters are digits (includes superscripts).
s = "123²".isdigit()  
print(s) # True

# Returns True if all characters are numeric (includes fractions like ½).
s = "½".isnumeric()  
print(s) # True

# Returns True if the string is a valid variable name in Python.
s = "my_var1".isidentifier()  # Output: True
print(s) # True

# Returns True if  if all cased characters are lowercase.
s = "ram".islower()
print(s) # True

# Returns True if  if all cased characters are uppercase.
s = "RAM".isupper()
print(s) # True

# Returns True if the string follows title-case rules.
s = "Ram Kumar".istitle()
print(s) # True

# Returns True if the string contains only whitespace characters.
s = "  \t\n".isspace()
print(s) # True

#  Returns True if all characters can be printed (returns False for \n, \t).
s = "hello".isprintable()
print(s) # True





