import openpyxl

book = openpyxl.Workbook()
sheet1 = book.active
sheet1.title = '첫번째 시트'
sheet1.cell(row=1, column =1).value = 'yeahyeah'

sheet2 = book.creat_sheet()
sheet2.title = '두번째 시트'
sheet2.cell['A1'] = 'heyhey'

book.save("./output.xlsx")