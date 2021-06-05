<template>
    <v-row>
      <v-col
        cols="12"
      >
        <v-card
          class="pa-2"
          outlined
          tile
        >
          <line-chart
            :chartData="chartdata"
            :title="path"
          />
          
          <!-- <v-skeleton-loader
            class="mx-auto"
            type="card"
          ></v-skeleton-loader> -->
        </v-card>
      </v-col>
      <stat-bar
        :statistics="stat"
      />
    </v-row>
</template>

<script>
import LineChart from './Chart.vue'
import StatBar from './StatBar.vue'

export default {
  name: 'LineChartContainer',
  components: { LineChart, StatBar,  },
  props:{
      data:Array,
      stat:Object,
      path:String,
      type: String
  },

  data: () => ({
    labels: {energy:'Energy consumption (J)', core:'Core workload (%)'}
  }),

  computed:{
      chartdata(){
        return {
          labels: Array(this.data.length).fill(1).map((_, i)=>i+1),
          datasets:[{
          label: this.labels[this.type],
          data: this.data
          }]
        };  
      }
    }, 
}
</script>

