from bs4 import BeautifulSoup

html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

# dic = {}
soup = BeautifulSoup(html, 'html.parser')
# dt = soup.select("dl > dt")
# dd = soup.select("dl > dd")

# for i, t in enumerate(dt):
#     print(t.text)

# for i, d in enumerate(dd):
#     print(d.text)

col_names = {'국적': 'nation', '활동유형': 'act_type', '활동연대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth'}

dl = soup.find('dl')
dts = []
dds = []
for d in dl:
    if not d.name: continue

    if d.name == 'dt':
        if not col_names.get(d.text): continue

        dts.append(col_names[d.text])
    else:
        span = d.select_one('span')
        if span != None:
            print("ssssssssssssS>>", span.text.replace('\n', ''))
            dds.append(span.next.strip())
        else:
            dds.append(d.text)

vals = {}
for i in range(len(dts)):
    vals[dts[i]] =  dds[i]
print(vals)