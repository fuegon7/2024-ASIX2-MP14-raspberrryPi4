<template>
  <div class="chart-container">
    <canvas id="myChart"></canvas>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      chartData: [] // Aquí almacenaremos los datos de la API
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/api/data'); // Cambia la URL según tu ruta de API
        this.chartData = response.data; // Almacena los datos en chartData
        this.createChart(); // Llama a la función para crear el gráfico
      } catch (error) {
        console.error('Error al obtener datos de la API:', error);
      }
    },
    createChart() {
    }
  }
};
</script>

<!-- createChart() {
      const ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar', // Tipo de gráfica (puedes cambiarlo a 'line', 'pie', etc.)
        data: {
          labels: ['Enero', 'Febrero', 'Marzo'], // Etiquetas en el eje X
          datasets: [
            {
              label: 'Ventas 2024', // Etiqueta para el dataset
              data: [100, 150, 120], // Datos para la gráfica
              backgroundColor: 'rgba(75, 192, 192, 0.6)' // Color de las barras
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    } -->