import webbrowser, sys, pyperclip

print(sys.argv)
if len(sys.argv) > 1:
    ## get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

