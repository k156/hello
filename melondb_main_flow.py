import melondb_func as mf
import melondb_rank as mr
import melondb_album as ma
import melondb_singer as ms
import melondb_song as mso



mr.get_rank_data()
ma.get_album_data()
ms.get_singer_data()
ms.get_song_data()


sql_rank_insert = "insert into SongRank(song_no, rank, rank_dt, like_cnt) values(%s,%s,%s,%s)"
sql_album_insert = "insert ignore into Album(album_no, album_name, publisher, likecnt, rating) values(%s,%s,%s,%s,%s)
"
sql_singer_insert1 = "insert ignore into Singer(singer_no, singer_name, label) values(%s,%s,%s)"
sql_singer_insert2 = "insert ignore into Singer(singer_no, singer_name) values(%s,%s)"
    
sql_song_insert = "insert ignore into Song(song_no, song_name, genre) values(%s,%s,%s)"


mf.save_data(sql_rank_insert, SongRank_insert_list)
mf.save_data(sql_album_insert, album_insert_lst)

mf.save_data(sql_singer_insert1, singer_insert_lst_1)
mf.save_data(sql_singer_insert2, singer_insert_lst_2)

mf.save_data(sql_song_insert, sss)
