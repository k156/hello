// for (let i = 0; i < 100; i++ ) {
//     db.test.insert({singer: 'singer'+i, company: 'company'+i , likecnt : '1'})
// }

var t = db.test.findOne({singer: 'singer1'})
t.albums = [1,2,3]
db.test.save(t)


// db.test.update({})