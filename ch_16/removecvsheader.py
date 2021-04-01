import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# this exercise assumes that every csv file has a header

for filename in os.listdir('./removeCsvHeader'):
    if not filename.endswith('.csv'):
        continue
    print('Removing header from ' + filename + ' ...')

    rows = []
    csvfile = open(os.path.join('removeCsvHeader', filename))
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        rows.append(row)
    csvfile.close()

    csvfile = open(os.path.join('headerRemoved', filename), 'w', newline='')
    csvwriter = csv.writer(csvfile)
    for row in rows:
        csvwriter.writerow(row)
    csvfile.close()
