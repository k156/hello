db.test.update({singer: 'singer3'}, 
{
    $push: {albums : 10}
})