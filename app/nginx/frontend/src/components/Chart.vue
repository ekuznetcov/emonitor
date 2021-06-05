<script>

import { Line, mixins } from 'vue-chartjs'

const { reactiveProp } = mixins

export default {
  extends: Line,
  mixins: [reactiveProp],
  props: ["title"],

  mounted(){  
    let options = { 
      decimation:{
          enabled: true, 
          algorithm: "lttb",
          samples: 50,
        },
      responsive: true,
      maintainAspectRatio: false,
      title: {
        display: true,
        text: this.title,
      },
      plugins: {
        legend: {
          labels: {
            usePointStyle: true,
          },
        },
        
      },
    }; 
    this.renderChart(this.chartData, options);   
  }
}
</script>