<template>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
import axios from 'axios';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data: () => ({
      loaded: false,
      chartData: null,
  }),
  async mounted() {
    this.loaded = false
    try {
      const response = await axios.get('/api/data');
      this.chartData = {
        labels: response.data.map(item => item.date),
        datasets: [{
          data: response.data.map(item => item.temperature)
        }]
      };
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
  