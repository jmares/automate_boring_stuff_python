# Automate the Boring Stuff with Python, 2nd Ed.

Practical Programming for Total Beginners by Al Sweigart   
Published by **no starch press** in November 2019, 592 pp.   
ISBN-13: 9781593279929

Started reading/studying this book on Februari 1, 2021.

Exercises and notes from the book Automate the Boring Stuff with Python

## PART I: Python Programming Basics

### Chapter 01: Python Basics

Read Februari 1, 2021

### Chapter 02: Flow Control

Read Februari 4, 2021

### Chapter 03: Functions

Read Februari 10, 2021.

Keyword arguments are often used for optional arguments. The print function has two optional arguments: `end` and `sep`.

Example with `end`:

```python
print("Hello")
print("World")

# Output:
# Hello
# World

print("Hello", sep='') # an empty string replaces the default newline character
print("World")

# Output:
# HelloWorld
```

Example with `sep`: 

```python
print('cats', 'dogs', 'mice')

# Output:
# cats dogs mice

print('cats', 'dogs', 'mice', sep=', ')

# Output:
# cats, dogs, mice
```

How to catch a keyboard interrupt exception caused by pressing CTRL-C?

```python
    ...
    except KeyboardInterrupt:
        sys.exit()
```


### Chapter 04: Lists

Read Februari 13, 2021.

Multiple assignment or tuple unpacking is a technique I always forget exists:

```python
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
```

Enumerate-function:

```python
for index, item in enumerate(supplyList):
```

Random choice: return a randomly selected item from a list

```python
pet = random.choice(pets)
```

Random shuffle: reorders the items in a list. It modifies the list in place, it doesn't return a new list.

```python
random.shuffle(pets)
```

The augmented assignment statements `+=` and `*=` can be used on lists as well.

Removing values from a list:

```python
del pets[2]
pets.remove('cat')
```

The sort method is case sensitive: 'Z' comes before 'a'. Want to sort a list of strings in alphabetical order:

```python
pets.sort(key=str.lower)
```

If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses.

```python
fruits = ('apple', )
```

Converting

```python
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```
