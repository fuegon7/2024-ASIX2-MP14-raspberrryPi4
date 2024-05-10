<template>
  <div class="container">
    <Line v-if="loaded" :data="chartData" />
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
      const lastMinuteData = newData.filter(item => {
        return Date.now() - new Date(item.date).getTime() < 60000;
      });
      
    
      if (lastMinuteData.length > 0) {
        const avgTemp = lastMinuteData.reduce((sum, item) => sum + item.temperature, 0) / lastMinuteData.length;
        const avgHumi = lastMinuteData.reduce((sum, item) => sum + item.humidity, 0) / lastMinuteData.length;
        let newChartData = JSON.parse(JSON.stringify(this.chartData)); // Crea una copia de this.chartData
        newChartData.labels.push(new Date().toLocaleTimeString());
        newChartData.datasets[0].data.push(avgTemp);
        newChartData.datasets[0].data.push(avgHumi);
        this.chartData = newChartData; // Asigna la copia actualizada a this.chartData
      }
    }, 5000);

  }
}

</script>
  