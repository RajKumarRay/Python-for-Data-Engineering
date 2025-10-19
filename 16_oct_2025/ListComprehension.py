# what is list Comprehension ? 
# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering items based on a condition. It replaces longer for loops with single expressive line. 

# Syntax of List Comprehension:
# new_list = [expression for item in iterable if condition]

thisList=["apple", "banana", "cherry", "kiwi", "mango"]

# Replacing the list with upper case in List Comprehension
upperList=[x.upper() for x in thisList]
print(upperList)



# Replacing the list with value more vowels or more consonants
categoryList = [
	"MORE VOWELS" if sum(ch in 'aeiou' for ch in set(i)) > len(set(i))//2 else "MORE CONSONANTS"
    for i in thisList
]
print(categoryList)

# Output:
['MORE VOWELS', 'MORE CONSONANTS', 'MORE CONSONANTS', 'MORE CONSONANTS', 'MORE CONSONANTS']


# Flattening the list of characters from each string in the list
dummyList = [
	ch
    for i in thisList
    for ch in set(i)
]
print(dummyList)

# Output: ['a', 'e', 'p', 'n', 'a', 'b', 'r', 'c', 'e', 'h', 'y', 'w', 'i', 'k', 'a', 'o', 'g', 'n', 'm']


# Flattening and getting only uniques. 
    
uqdummyList = [
	uq for uq in set(ch
    for i in thisList
    for ch in set(i))
]

# or 

uqdummyList = [
	uq for uq in {ch # Third for loop
    for i in thisList # first for loop
    for ch in set(i) # second for loop}
    }
]
print(uqdummyList)
# Output: ['a', 'e', 'p', 'n', 'b', 'r', 'c', 'h', 'y', 'w', 'i', 'k', 'o', 'g', 'm']



# in Below two examples, see the way of use of if and how they differ.

# this will give the whole list. 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ["Not apple" if x!='apple' else "Apple" for x in fruits]
print(newlist)

# Output: ['Apple', 'Not apple', 'Not apple', 'Not apple', 'Not apple']

# this will give the list without apple.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Output: ['banana', 'cherry', 'kiwi', 'mango']




# Python doesn’t have direct elif in list comprehension,
# but you can nest conditional expressions like this:

newlist = [
    "contains both a and e" if "a" in x and "e" in x
    else "contains a" if "a" in x
    else "contains e" if "e" in x
    else "no a or e"
    for x in fruits
]
print(newlist)


# 🟢 Output:
['contains both a and e', 'contains a', 'contains e', 'no a or e', 'contains a']

# ✅ Equivalent normal for loop:
newlist = []
for x in fruits:
    if "a" in x and "e" in x:
        newlist.append("contains both a and e")
    elif "a" in x:
        newlist.append("contains a")
    elif "e" in x:
        newlist.append("contains e")
    else:
        newlist.append("no a or e")

print(newlist)