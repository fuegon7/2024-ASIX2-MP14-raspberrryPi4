import express from 'express';
import mysql from 'mysql';
import dotevn from 'dotenv'
dotevn.config()

const api = express();

// Buscar los datos para la conneixion
const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
});

connection.connect(err => {
  if (err) {
    console.error('Error al conectar a la base de datos:', err);
    return;
  }
  console.log('Conexión a la base de datos MySQL establecida');
});

// Query para obtener la tabla users.
api.get('/api/users', (req, res) => {
  const query = 'SELECT * FROM users';
  connection.query(query, (err, results) => {
    if (err) {
      console.error('Error al obtener usuarios:', err);
      res.status(500).json({ error: 'Error al obtener usuarios' });
      return;
    }
    res.json(results);
  });
});

// Iniciar el servidor
api.listen(port, () => {
  console.log(`Servidor de API iniciado en http://localhost:${port}`);
});