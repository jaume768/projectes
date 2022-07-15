
// tot aixo per poder fer consultes a la base de dades
const mysql = require('mysql');
const { promisify } = require('util');
const {database } = require('./keys');

const pool = mysql.createPool(database);

pool.getConnection((err, connection) =>{
    if (err){
       if(err.code === 'PROTOCOL_CONNECTION_LOST') {
           console.error('Conexión con la base de datos perdida');
       } 
       if (err.code == 'ER_CON_COUNT_ERROR'){
            console.error('La base de datos tiene muchas conexiones');
       }
       if (err.code == 'ECONNREFUSED'){
            console.error('Conexión rechazada');
       }
    } else {
        console.log('Conectado a la base de datos');
    }

    if (connection) connection.release();
    
});

pool.query = promisify(pool.query);

module.exports = pool;