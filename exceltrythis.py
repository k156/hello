import openpyxl
import csv, codecs
from bs4 import BeautifulSoup
import requests
from openpyxl.chart import (
    Reference, BarChart, Series, ScatterChart
)
import os
import os.path as path
import urllib.parse as parse
from PIL import Image


# 1) 지난 시간에 작성한 meltop100.csv 파일을 읽어, meltop100.xlsx 로 저장하시오.
#  (단, 랭킹, 좋아요, 좋아요차이 컬럼은 숫자형식으로 저장 할 것!)


fp = codecs.open("meltop100.csv", "r", encoding = "MS949")

reader = csv.reader(fp, delimiter=',', quotechar='"')

book = openpyxl.Workbook()
sheet1 = book.active
sheet1.title = "첫번째 시트"

for i, cells in enumerate(reader):
	for j, col in enumerate(cells):
		tcell = sheet1.cell(row = (i+1), column = (j+1))
		if i > 0 and (j == 0 or j > 2) and col.isnumeric():
			tcell.number_format
			tcell.value = int(col)
		else: tcell.value = col


            
# 2) 멜론 Top100 곡들의 `앨범 재킷파일`을 다운받아, meltop100.xlsx 파일의 두번째 시트에 랭킹순으로 작성하시오.
# 	(단, 이미지파일의 크기는 축소하여 보기 좋게 작성 할 것!)

sheet2 = book.create_sheet()
sheet2.title = "두번째 시트"

os.makedirs('melonimages', exist_ok = True)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url = "https://www.melon.com/chart/index.htm"

html = requests.get(url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')
links = soup.select('tr > td:nth-of-type(4) > div > a > img[src]')

i= 1

for l in links:
	link = l.get('src')
	print(link)
	img = requests.get(link).content
	saveFile = "./images/{}.png".format(i)
	with open(saveFile, mode="wb") as file:
		file.write(img)
	i += 1


for i in range(1, 101):
	imgFile = './images/{}.png'.format(i)
	img = openpyxl.drawing.image.Image(imgFile)
	img2 = Image.open(imgFile)
	new_img = img2.resize((20, 20))
	new_img.save('./images/new{}.png'.format(i))
	img3 = openpyxl.drawing.image.Image('new{}.png'.format(i))
	sheet2.add_image(img3, 'B{}'.format(i))




# 3) 상위 Top10의 `좋아요 수`는 BarChart로, `좋아요 차이 수`는 ScatterChart로 세번째 시트에 작성하시오.


sheet3 = book.create_sheet()
sheet3.title = "세번째 시트"

data = Reference(sheet1, min_col=4,
        min_row=2, max_col=4, max_row=11)
categ = Reference(sheet1, min_col=2,
                 min_row=2, max_row=11)

chart = BarChart()
chart.add_data(data=data)
chart.set_categories(categ)

chart.legend = None 
chart.varyColors = True
chart.title = "Top10 좋아요 차이 수"

sheet3.add_chart(chart, "A2")




chart = ScatterChart()
chart.style = 13
chart.x_axis.title = 'likes'
chart.y_axis.title = 'titles'

xvalues = Reference(sheet1, min_col=2,
             min_row=2, max_row=11)


values = Reference(sheet1,
            min_col=5,
            min_row=2,
            max_row=11)
series = Series(values, xvalues,
            title = "Top10 좋아요 수")
chart.series.append(series)

sheet3.add_chart(chart, "A18")




book.save("exceltrythis.xlsx")


