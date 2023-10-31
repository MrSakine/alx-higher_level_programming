0x09. Python - Everything is object

# 0-answer.txt
function to get the type of an object

# 1-answer.txt
function to get get the variable identifier (which is the memory address in the CPython implementation)

# 2-answer.txt
```
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100
```

# 3-answer.txt
```
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89
```

# 4-answer.txt
```
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a
```

# 5-answer.txt
```
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a + 1
```

# 6-answer.txt
```
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

# 7-answer.txt
```
What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

# 8-answer.txt
```
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

# 9-answer.txt
```
What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

# 10-answer.txt
```
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

# 11-answer.txt
```
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

# 12-answer.txt
```
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

# 13-answer.txt
```
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

# 14-answer.txt
```
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

# 15-answer.txt
```
What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

# 16-answer.txt
```
What does this script print?
def increment(n):
  n += 1
a = 1
increment(a)
print(a)
```

# 17-answer.txt
```
What does this script print?
def increment(n):
  n.append(4)
l = [1, 2, 3]
increment(l)
print(l)
```

# 18-answer.txt
```
What does this script print?
def assign_value(n, v):
  n = v
l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

# 19-copy_list.py
a function def copy_list(l): that returns a copy of a list

# 20-answer.txt
```
a = ()
Is a a tuple? Answer with Yes or No.
```

# 21-answer.txt
```
a = (1, 2)
Is a a tuple? Answer with Yes or No.
```

# 22-answer.txt
```
a = (1)
Is a a tuple? Answer with Yes or No.
```

# 23-answer.txt
```
a = (1, )
Is a a tuple? Answer with Yes or No.
```

# 24-answer.txt
```
What does this script print?
a = (1)
b = (1)
a is b
```

# 25-answer.txt
```
What does this script print?
a = (1, 2)
b = (1, 2)
a is b
```

# 26-answer.txt
```
What does this script print?
a = ()
b = ()
a is b
```

# 27-answer.txt
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
```

# 28-answer.txt
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
```
