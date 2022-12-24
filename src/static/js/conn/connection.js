const mysql = require('mysql');

function newConn()
{
    let conn = mysql.createConnection({
        host:'localhost',
        user: 'root',
        password:'password',
        database:'candy_retail'
    });
    return conn;
}
module.exports = newConn;