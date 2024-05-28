import express from 'express';
import mariadb from 'mariadb';
import dotenv from 'dotenv';

dotenv.config();

const pool = mariadb.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
});

async function connectToDatabase() {
  let conn;
  try {
    conn = await pool.getConnection();
    console.log('Conexión a la base de datos MariaDB establecida');
    return conn;
  } catch (err) {
    console.error('Error al conectar a la base de datos:', err);
    throw err;
  }
}

const api = express();

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
    if (conn) conn.end();
  }
});

const port = process.env.API_PORT || 3000;
api.listen(port, () => {
  console.log(`Servidor de API iniciado en http://localhost:${port}`);
});
