import openpyxl


book = openpyxl.Workbook()
sheet = book.active
sheet.title = '시트'


# insert image
imgFile = 'C:\workspace\hello\images\download.jpg'
img = openpyxl.drawing.image.Image(imgFile)
sheet.add_image(img, 'B5')



from PIL import Image

# resize image
img2 = Image.open(imgFile)
new_img = img2.resize((30, 30))
new_img.save('new.png')
img3 = openpyxl.drawing.image.Image('new.png')
sheet.add_image(img3, 'A5')


book.save("./image.xlsx")


#chart
rows = [
    ['김일수', 11],
    ['김이수', 22],
    ['김삼수', 33],
    ['김사수', 15],
    ['김오수', 11],
]

for row in rows:
    sheet.append(row)

datax = Reference(sheet, min_col=2, 
		min_row=1, max_col=2, max_row=5)
categs = Reference(sheet, min_col=1,
				 min_row=1, max_row=5)

chart = BarChart()
chart.add_data(data=datax)
chart.set_categories(categs)

chart.legend = None  # 범례
chart.varyColors = True
chart.title = "차트 타이틀"

sheet.add_chart(chart, "A8")