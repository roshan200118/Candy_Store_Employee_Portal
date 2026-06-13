const mysql = require('mysql');

function newConn()
{
    let conn = mysql.createConnection({
        host: process.env.DB_HOST || 'us-cdbr-east-06.cleardb.net',
        user: process.env.DB_USER || 'b81cfff364960c',
        password: process.env.DB_PASSWORD || '9d994542',
        database: process.env.DB_NAME || 'heroku_ffb9511d068313f'
    });
    return conn;
}
module.exports = newConn;