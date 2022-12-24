const mysql = require('mysql');

function newConn()
{
    let conn = mysql.createConnection({
        host:'us-cdbr-east-06.cleardb.net',
        user: 'b81cfff364960c',
        password:'9d994542',
        database:'heroku_ffb9511d068313f'
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