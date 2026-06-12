const mysql = require('mysql2');

function newConn()
{
    let conn = mysql.createConnection({
        host:'lg7j30weuqckmw07.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        user: 'kive3rcqiam2uci0',
        password:'ajsz1u4maufeqx8u',
        database:'t650mhy2tt432hkp'
    });
    // let conn = mysql.createConnection({
    //     host:'localhost',
    //     user: 'root',
    //     password:'password',
    //     database:'candy_retail'
    // });
    return conn;
}
module.exports = newConn;