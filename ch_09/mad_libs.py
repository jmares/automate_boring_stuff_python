import sys, re
regex = re.compile('ADJECTIVE|VERB|NOUN|ADVERB')

try:
    f = open(sys.argv[1])
except IndexError:
    print("IndexError: Specify a file to open as in 'python mad_libs.py myfile.txt'.")
    sys.exit(1)
except FileNotFoundError:
    print(f"FileNotFoundError: The file {sys.argv[1]} could not be found.")
    sys.exit(1)

text = f.read()
f.close()
print(text)
matches = regex.findall(text)

for match in matches:
    replace = input(f'Enter a new {match.lower()}: ')
    text = text.replace(match, replace, 1)
print(text)

f = open(f'new_{sys.argv[1]}', 'w')
f.write(text)
f.close()

