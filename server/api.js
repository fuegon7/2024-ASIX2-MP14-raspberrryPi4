// Importar las librer�as necesarias
import express from 'express';
import mariadb from 'mariadb';
import dotenv from 'dotenv';

// Configurar las variables de entorno
dotenv.config();

// Crear una nueva pool de conexiones
const pool = mariadb.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
});

// Crear una funci�n para manejar la conexi�n de la base de datos
async function connectToDatabase() {
  let conn;
  try {
    conn = await pool.getConnection();
    console.log('Conexi�n a la base de datos MariaDB establecida');
    return conn;
  } catch (err) {
    console.error('Error al conectar a la base de datos:', err);
    throw err;
  }
}

// Iniciar la aplicaci�n express
const api = express();

// Ruta para obtener los datos de la tabla temperature
api.get('/api/data', async (req, res) => {
  let conn;
  try {
    conn = await connectToDatabase();
    const rows = await conn.query('SELECT * FROM temperature');
    res.json(rows);
  } catch (err) {
    console.error('Error al obtener datos de la base de datos:', err);
    res.status(500).json({ error: 'Error al obtener datos de la base de datos' });
  } finally {
    if (conn) conn.end(); // Cerrar la conexi�n cuando hayamos terminado
  }
});

// Iniciar el servidor
const port = process.env.API_PORT || 3000;
api.listen(port, () => {
  console.log(`Servidor de API iniciado en http://localhost:${port}`);
});
