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