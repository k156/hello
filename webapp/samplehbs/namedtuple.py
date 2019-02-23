from collections import namedtuple
# namedtuple('Type', 'col1 col2 col3')
Song = namedtuple('Song', 'songno title likecnt')
# set
s1 = Song(123, '만남', 100)
s2 = Song(songno=222, title='강남스타일', likecnt=200)
# getattr    cf. s1.title
title = getattr(s2, 'title')

print(title)

# _fields
print("FFFFFFFFFFF>>", s2._fields)
# _make()
s3 = Song._make([333, 'Radio ga ga', 300])
# _asdict() : cast to OrderedDict
d1 = s1._asdict()
# _replace()
s2 = s2._replace(likecnt=201)

print('s1>>>>>>>>', s1)
print('d1>>>>>>>>>>>>>>>',d1)

