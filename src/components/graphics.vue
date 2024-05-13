<template>
  <div class="container">
    <Line v-if="loaded" :data="chartData" :options="chartOptions"/>
    <button model="chart_id" :value=1 @click="label_timeset(1)">Horas</button>
    <button disabled model="chart_id" :value=2 @click="label_timeset(2)">Dias</button>
    <button disabled model="chart_id" :value=3 @click="label_timeset(3)">Semana</button>
    <button disabled model="chart_id" :value=4 @click="label_timeset(4)">Mes</button>
    <button disabled model="chart_id" :value=5 @click="label_timeset(5)">Año</button>
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'
import axios from 'axios';
import Utils from 'Utils';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
  name: 'LineChart',
  components: { Line },
  data: () => ({
      loaded: false,
      chartData: null,
      originalData: [],
      chartOptions: {
        animation: {
        duration: 2000, // Duración de la animación en milisegundos
        },
        responsiveAnimationDuration: 0, // Desactiva las animaciones al cambiar el tamaño
        scales: {
          x: {
            type: 'realtime', // Habilita la escala de tiempo en tiempo real
            realtime: {
              delay: 2000, // Retraso de la animación en milisegundos
            },
          },
        },
      tempSum: 0,
      count: 0,
    }
  }),
  async mounted() {
    this.loaded = false
    try {
      const response = await axios.get('/api/data');
      this.originalData = response.data;
      this.chartData = {
        labels: [],
        datasets: [
        {
          label: 'Temperatura',
          backgroundColor: 'red',
          fill: false,
          cubicInterpolationMode: 'monotone',
          data: []
        },
        {
          label: 'Humetat',
          backgroundColor: 'blue',
          data: response.data.map(item => item.humidity)
        }]
      };
      this.loaded = true
    } catch (e) {
      console.error(e)
    }

    // Actualiza el gráfico cada 5 segundos
    setInterval(async () => {
      const response = await axios.get('/api/data');
      const newData = response.data;
      const lastData = newData[newData.length - 1]; // Obtiene el último dato
    
      if (lastData) {
        let newChartData = JSON.parse(JSON.stringify(this.chartData)); // Crea una copia de this.chartData
        newChartData.labels.push(new Date(lastData.date).toLocaleTimeString());
        newChartData.datasets[0].data.push(lastData.temperature);
        newChartData.datasets[1].data.push(lastData.humidity);
        this.chartData = newChartData; // Asigna la copia actualizada a this.chartData

        if (newChartData.labels.length > 10) {
          newChartData.labels.shift(); // Elimina el primer elemento de labels
          newChartData.datasets[0].data.shift(); // Elimina el primer elemento de data de temperatura
          newChartData.datasets[1].data.shift(); // Elimina el primer elemento de data de humedad
        }

        this.chartData = newChartData; // Asigna la copia actualizada a this.chartData
      }
    }, 5000);
  }
}

</script>
  