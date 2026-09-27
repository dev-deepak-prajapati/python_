import keyword

# 1. keyword.kwlist: Returns a list containing all the keywords defined for Python
all_keywords = keyword.kwlist
print("Total number of keywords:", len(all_keywords))
print("Keywords List:", all_keywords)

# 2. keyword.iskeyword(s): Returns True if the string 's' is a Python reserved keyword
print(keyword.iskeyword("if"))       # Output: True
print(keyword.iskeyword("lambda"))   # Output: True
print(keyword.iskeyword("hello"))    # Output: False
print(keyword.iskeyword("for"))      # Output: True

# 3. keyword.issoftkeyword(s): Returns True if the string is a 'soft' keyword (Python 3.9+)
# Soft keywords (like 'match', 'case', or '_') act as keywords in specific contexts 
# but can still be used as regular variable names elsewhere.
print(keyword.issoftkeyword("match")) # Output: True
print(keyword.issoftkeyword("case"))  # Output: True
print(keyword.issoftkeyword("if"))    # Output: False (it's a hard keyword, not a soft one)

# 4. keyword.softkwlist: Returns a set containing all the soft keywords (Python 3.9+)
print("Soft Keywords:", keyword.softkwlist)
