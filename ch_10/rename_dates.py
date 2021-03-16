#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.”
import shutil, os, re

# Before running this script, create some files with USA dates 
# in the same directory as the script
# Examples: 01-25-1985spam.txt, spam4-5-1999.txt, 09-11-2010eggs.txt

# Create a regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year (must start with 19 or 20)
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.

for usa_filename in os.listdir('.'):
    mo = datePattern.search(usa_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename.
    eu_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths.
    abs_workingdir = os.path.abspath('.')
    usa_filename = os.path.join(abs_workingdir, usa_filename)

    # Rename the files.
    eu_filename = os.path.join(abs_workingdir, eu_filename)
    print(f'Renaming "{usa_filename}" to "{eu_filename}" ...')
    shutil.move(usa_filename, eu_filename)

