const mysql = require('mysql2');

function newConn()
{
    let conn = mysql.createConnection({
        host: process.env.DB_HOST || 'lg7j30weuqckmw07.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        user: process.env.DB_USER || 'kive3rcqiam2uci0',
        password: process.env.DB_PASSWORD || 'ajsz1u4maufeqx8u',
        database: process.env.DB_NAME || 't650mhy2tt432hkp'
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