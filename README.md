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

Read March 2-5, 2021

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

Optional matching with a question mark

```python
bat_regex = re.compile(r'Bat(wo)?man')
```
This regex will search for Batman or Batwoman.

Matching zero or more with the star

```python
bat_regex = re.compile(r'Bat(wo)*man')
```

Matching one or more with the plus

```python
bat_regex = re.compile(r'Bat(wo)+man')
```

Matching specific repititions with braces

```python
ha_regex = re.compile(r'(Ha){3}')
```

Greedy and nog-greedy matching. Python regex are greedy by default

```python
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```

While `search()` will return a Match object of the first matched text in the searched string, the `findall()` method will return a list of strings if there are no groups in the regular expression. Otherwise it will return a list of tuples.

```python
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
```

Shorthand | Represents
:---|:---
\d | Any numeric digit from 0 to 9.
\D | Any character that is not a numeric digit from 0 to 9.
\w | Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W | Any character that is not a letter, numeric digit, or the underscore character.
\s | Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S | Any character that is not a space, tab, or newline.

```python
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

Making your own character classes.

Example: the character class [aeiouAEIOU] will match any vowel.    
Other example: the character class [a-zA-Z0-9] will match lowercase letters, uppercase letters, and numbers.   
Inside a character class, you don't need to escape characters.  
By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class.

Using the caret symbol (^) at the start of a regex indicates that a match must occur at the beginning of the searched text. Using a dollar sign ($) at the end of a regex indicates that a match must occur at the end of the searched text.

The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

A dot-star (.\*) matches everything. To make it non-greedy, add a question mark (.\*?).

The dot-star will match everything, except a newline. By passing `re.DOTALL` as the second argument to the `re.compile()` method, the dot-star will now match all characters.

**Summary**

- The ? matches zero or one of the preceding group.
- The * matches zero or more of the preceding group.
- The + matches one or more of the preceding group.
- The {n} matches exactly n of the preceding group.
- The {n,} matches n or more of the preceding group.
- The {,m} matches 0 to m of the preceding group.
- The {n,m} matches at least n and at most m of the preceding group.
- {n,m}? or *? or +? performs a non-greedy match of the preceding group.
- ^spam means the string must begin with spam.
- spam$ means the string must end with spam.
- The . matches any character, except newline characters.
- \d, \w, and \s match a digit, word, or space character, respectively.
- \D, \W, and \S match anything except a digit, word, or space character, respectively.
- [abc] matches any character between the brackets (such as a, b, or c).
- [^abc] matches any character that isn’t between the brackets.

To make regex case-insensitive, you can pass `re.IGNORECASE` or `re.I` as the second argument to the `re.compile()` method.

Substituting strings with the `sub()` method.

```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

```python
“>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
'A**** told C**** that E**** knew B**** was a double agent.'
```

By passing the variable `re.VERBOSE` as the second argument to `re.compile()` you are telling it to ignore whitespace and comments.

Complex regex can be spread over multiple lines with comments.

Even though `re.compile()` takes only a single value as its second argument, you can combine multiple values with the pipe character.

```python
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```

Didn't make any projects, because I didn't have the time for it. This is probably the 5th ot 6th time that I study regex in the past 25 years and I never had a use for it, so I always forgot. I can always revisit this chapter when needed.

### Chapter 08: Input Validation

Read March 6-7, 2021

### Chapter 09: Reading and Writing Files

Read March 8-11, 2021

```python
from pathlib import Path
```

Current working directory: `Path.cwd()`

To change directory: `os.chdir()`

To make a directory with `os`: `os.mkdirs('C:\\delicious\\walnut\\waffles')`

To make a directory with `pathlib`: Path(r'C:\delicious\walnut\waffles').mkdir()

The difference between `os.mkdirs()` and `Path().mkdir()` is that the latter can only make 1 directory, while the former can make multiple (delicious, walnut, waffles).

Path can be used to extract the different parts of a directory: achor, drive, parent (list of the directories int the path), name, stem and suffix.

If you want to get the contents of a folder or the size of a file, you have to use `os`: `os.listdir(path)` and `os.path.getsize(path)`.

For modifying a list of files, use the `glob()` method from `Path` instead of `os.listdir()`.

Path objects have methods to check validity: `.exists()`, `.is_file()` and `.is_dir()`.

In the chapter "Opening Files with the `open()` Function" I made a change to the code

```python
# helloFile = open(Path.home() / 'hello.txt')
helloFile = open(Path.cwd() / 'hello.txt')
```
Needed some help with the Mad Libs project. Me and regular expressions still don't get along.

### Chapter 10: Organizing Files

Read March 16, 2021

```python
import shutil    # shell utilities module, to be used with the pathlib module
```

Copy a single file: `shutil.copy()`    
Copy an entire folder with every subfolder and file in it: `shutil.coputree()`    
Moving and renaming files and folders: `shutil.move()`    
Delete the file at *path*: `os.unlink(path)`    
Delete the **empty** folder at *path*: `os.rmdir(path)`   
Delete the folder at *path* including all subfolders and files: `shutil.rmtree(path)`    

The above mentioned delete method will irreversibly delete files and folders.

The `send2trash` module will send files and folders to the computer's trash or recycle bin: `send2trash.send2trash()`

Walking a directory tree with `os.walk()`:

```python
for foldername, subfolders, filenames in os.walk(path):
    ...
```

Working with ZIP-files: the `zipfile` module

A ZipFile object represents an entire archive file.    
A ZipInfo object holds useful information about a single file in the archive.   

Didn't make the practice projects, because I already have one: replace the bash scripts I currently use to backup sites and databases with a python script.

### Chapter 11: Debugging

Read March 22- , 2021

Not impressed by the traceback and assertions chapters.