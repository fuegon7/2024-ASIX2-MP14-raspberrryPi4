<template>
  <div class="container">
    <Line v-if="loaded" :data="chartData" :options="chartOptions"/>
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
  Legend,
  scales
} from 'chart.js'
import { Line } from 'vue-chartjs'
import axios from 'axios';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

var numsamples = 10;
var AvgTemperatureChartOptions

export default {
  name: 'LineChart',
  components: { Line },
  data: () => ({
      loaded: false,
      chartData: null,
      originalData: [],
      tempSum: 0,
      count: 0,
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
        },
      ]
      };
      this.chartOptions = {
        showLines: true,
        animation: {
          duration: 1000,
          easing: 'linear'
        },
        tooltips: {
          enabled: false
        },
        responsive: true,
        scales: {
          xAxis: [{
            id: 'temperature',
            position: 'left',
            gridLines: {
              drawTicks: false
            },
            ticks: {
              fontSize: 10,
              max: 100,
              min: 0,
              stepSize: 25,
            }
          }]
        }
      }
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
  