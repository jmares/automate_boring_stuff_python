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

Two copy methods: `copy.copy()` makes a copy of a list and `copy.deepcopy()` makes a copy of a list containing lists.

I do not make every exercise, only the ones that I can't figure out right away.    

I now understand why a lot of people didn't make the *Coin Flip Streaks* project. I made it, but I didn't understand the outcome. I had no idea what to expect.

I am not the only who commits his exercises from courses and books (including this one) to GitHub, but this specific project was missing with a lot of fellow learners. I found a solution on Gist, which had an impossible answer (> 140%) (see file `coinflips2.py`). Found some on StackOverFlow that were similar to mine, but still left me with questions. Then I found a solution on [StackExchange CodeReview](https://codereview.stackexchange.com/questions/247936/coin-flip-streaks-correct-streak-condition) (see file `coinflips3.py`). I am not going to go into details about optimizing my code, PEP8, the pythonic way, and the statistics, but I immediately spotted the two mistakes that I and others made. 

First mistake: it is not the numbers of streaks that you should count, but the sets of 100 tosses that have at least one streak of 6. As soon as you find a streak of 6 heads or tails: abort (`break`) the loop.

Second mistake: if you are looking for a streak of 6 heads or tails pay attention to the initialization of the variable. I initialized the variable `streak` by setting it to 0 and I increased it untill it had reached 6. That is actually a streak of 7. So, either you set the initial value to 0 and count until it reaches 5, or you set the initial value to 1 and count until it reaches 6.

### Chapter 05: Dictionaries and Structuring Data

Read Februari 18 - 19, 2021.

While they’re still not ordered and have no “first” key-value pair, dictionaries in Python 3.7 and later will remember the insertion order of their key-value pairs if you create a sequence value from them.

Import the `pprint` module for pretyy printing a dictionary. Two methods: `pprint` and `pformat`.

### Chapter 06: Manipulating Strings

Read Februari 22 - 23, 2021.

A *raw string* completely ignores all escape characters and prints any backslash that appears in the string. Helpful if you have to printing Windows file paths.

```python
print(r'C:\Users\Al\Desktop\test\new')
```

Multiline string

```python
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```

Single line comment starts with: **#**

Multiline comment starts and ends with: **"""**

Reversing the order in a string

```python
spam = 'abcdefghij'
spam[::-1]
```

String interpolation & f-strings:

```python
print('My name is %s. I am %s years old.' % (name, age))
print(f'My name is {name}. Next year I will be {age + 1}.”)
```

Some lesser know methods:

- isalpha(): true if only letters and not blank
- isalnum(): true if only letters and numbers, and not blank
- isdecimal(): true, if only numeric characters and not blank
- isspace(): true, if only spaces, tabes and newlines, and not blank
- istitle(): true, if words start with uppercase letter followed by only lowercase letters, and not blank

The `.partition()` method splits a string into the text before and after the separator string.

```python
>>> 'Hello, world!'.partition('w')
('Hello, ', 'w', 'orld!')
>>> 'Hello, world!'.partition('world')
('Hello, ', 'world', '!') 
```

I spent more time on the *Table Printer* project than anticipated, so I skipped the *Zombie Dice Bots* project (for now).

## PART II: Automating Tasks 

### Chapter 07: Pattern Matching with regular Expressions 

Read March 2, 2021

Import the regular expresssion module

```python
import re
```

Create a RegEx object (use a raw string):

```python
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # or
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
```

Search for the pattern:

```python
mo = phone_num_regex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
# Phone number found: 415-555-4242
```

The `search` method will only return the first occurence. If you want them all, use the `findall` method.

Web-based regular expression tester: [pythex](https://pythex.org/)

Grouping with ():

```python
phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_regex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group(1) + ' - ' + mo.group(2))
# Phone number found: 415 - 555-4242
```

```python
print(mo.groups())
# ('415', '555-4242')
```

If you want to search for the following characters `.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )` you will need to escape them in the raw string: `\$`

Matching multiple groups with the pipe

```python
bat_regex = re.compile(r'Bat(man|woman|mobile|copter|boat)')
```
This regex will search for the first occurence of Batman, Batwoman, Batmobile, Batcopter or Batboat.

```python
bat_regex = re.compile(r'Bat(wo)?man')
```
This regex will search for Batman or Batwoman.