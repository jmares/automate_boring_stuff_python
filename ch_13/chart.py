import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):
    sheet['A' + str(i)] = i

ref = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1,max_row=10)
series = openpyxl.chart.Series(ref, title='First Series')

chart_obj = openpyxl.chart.BarChart()
chart_obj.title = 'My Chart'
chart_obj.append(series)

sheet.add_chart(chart_obj, 'C5')
wb.save('samplechart.xlsx')