def print_table(table_data):
    col_widths = [0] * len(table_data)
    new_table = {k:[] for k in range(len(table_data[0]))}
    
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            if len(table_data[i][j]) > col_widths[i]: 
                col_widths[i] = len(table_data[i][j])
            new_table[j].append(table_data[i][j])
    
    for i in range(len(new_table)):
        for j in range(len(new_table[i])):
            print(new_table[i][j].rjust(col_widths[j]), end=' ')
        print()
    


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(tableData)