from bs4 import BeautifulSoup


html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
# </table>
# '''

soup = BeautifulSoup(html, 'html.parser')
columns = soup.select('tr:nth-of-type(1) > th')
tds = soup.select('td')

# for column in columns:
# 	column =  column.text
# 	print(column)



column = soup.select_one('table > tr:nth-of-type(1)')
# column = soup.select('table > tr:nth-of-type(1) > th')
row =  soup.select('table > tr > th:nth-of-type(1)')
# td1s = tr.select ('tr:nth-of-type(1) > td')
# td2s = soup.select('talbe > tr:nth-of-type(2) > td')
# td3s = soup.select('talbe > tr:nth-of-type(3) > td')
# td4s = soup.select('talbe > tr:nth-of-type(4) > td')

# tdlist = []
for td in tds:
	print(td)
	td1s = td.select('tr:nth-of-type(1) > td')
	print(td1s)
	
# append(td.text)


# print(column.text)

# for i in column:
# 	columns = i.text
# 	print(columns)

# def text(variable):
# 	for i in variable:
# 		a = i.text
# 		print(a)

# text(row)
# text(td1s)
# text(td3s)
# text(td4s)



# print(ths, td1s, td2s, td3s, td4s)



# a = {'region' : 'seoul' }
# b = {'total staff': '130' }
# c = {'tel': '010-222-3333'}
# d = {'email': 'a@b.com'}
# companies = {A:[a,b,c,d],B:[a,b,c,d],C:[a,b,c,d]}

# A = 회사

# print(companies['A'][0])

# # def update(company, row, value):
# # 	companies[compnay: []]

# companies = {}
# companies['A'] = {'region': '서울', 'staff':'30명', 'tel': '02-2345-2323', 'email': 'a@a.com'}
# companies['B'] = {'region': '강원도', 'staff':'55명', 'tel': '033-223-2323', 'email': 'b@b.com'}

# print(companies)

# # item = sorted(companies.items(), key=lambda x : x[1]['region'])

# print(companies['A']['region'])

# companies['C'] = {'staff':'200명'}

# print(companies['C'])
# # print(item)