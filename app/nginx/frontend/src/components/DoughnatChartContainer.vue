<template>
  <div class=" mb-10">
    <v-banner
      overflow: auto
    >
  <div class="chartAreaWrapper">
    <doughnat-chart
      style=" width: 200%;"
      :chartData="chartData"
    >
    </doughnat-chart>
  </div>
    <stat-bar
      :statistics="statDict"
    >
    </stat-bar>
    </v-banner>
  </div>
</template>

<script>
import DoughnatChart from '@/components/DoughnatChart'
import StatBar from './StatBar.vue';

export default {
  components: {
    DoughnatChart, StatBar
  },
  props:{
    data:Object
  },

  methods:{
    getRandomInt(max) {
      return Math.floor(Math.random() * max);
    },

    getRandomColor(index) {

      let colors = [
        `rgba(255, 99, 132, ${index})`, //"Red", "Pinc","Blue", "Yellow", "Green", "Purple", "Orange"
        `rgba(255, 51, 51, ${index})`,
        `rgba(255, 0, 153, ${index})`,
        `rgba(54, 162, 235, ${index})`,
        `rgba(102, 255, 255, ${index})`,
        `rgba(255, 206, 86, ${index})`,
        `rgba(75, 192, 192, ${index})`,
        `rgba(153, 102, 255, ${index})`,
        `rgba(255, 159, 64, ${index})`
      ]

      let borderColors = [
        `rgba(255, 99, 132, ${index + 1})`, //"Red", "Pinc","Blue", "Yellow", "Green", "Purple", "Orange"
        `rgba(255, 0, 153, ${index + 1})`,
        `rgba(54, 162, 235, ${index + 1})`,
        `rgba(255, 206, 86, ${index + 1})`,
        `rgba(75, 192, 192, ${index + 1})`,
        `rgba(153, 102, 255, ${index + 1})`,
        `rgba(255, 159, 64, ${index + 1})`
      ]

      let number = this.getRandomInt(colors.length)
      
      return {backgroundColor: colors[number], borderColor: borderColors[number]}
    }
  },

  computed:{
    statDict(){
      if(!Object.values(this.data).length) return 0
      return {
        Max: this.max,
        Min: this.min,
        Sum: this.sum,
      }
    },

    sum(){
      if(!Object.values(this.data).length) return 0
      let statData = Object.values(this.data)
      statData = statData.filter((number)=>(!isNaN(Number(number))))
      return Math.round(statData.reduce((sum, value)=>(sum+value), 0))
    },

    min(){
      if(!Object.values(this.data).length) return 0
      let statData = Object.values(this.data)
      statData = statData.filter((number)=>(!isNaN(Number(number))))
      let min = Math.min(...statData)
      // let match  = Object.keys(this.data).filter((y) => ( this.data[y] === min ));
      // return {[match]: min}
      return min
    },

    max(){
      if(!Object.values(this.data).length) return 0
      let statData = Object.values(this.data)
      statData = statData.filter((number)=>(!isNaN(Number(number))))
      return Math.max(...statData)
    },

    chartData() {
          if(!Object.keys(this.data).length) return undefined
          let colorsArr = Array.from({length: Object.keys(this.data).length}, () => this.getRandomColor(0.4)["backgroundColor"])
          return {
            labels: Object.keys(this.data),
            datasets: [{
              borderWidth: 1,
              borderColor: colorsArr,
              backgroundColor: colorsArr,
              data: Object.values(this.data)
            }]
          }
        },
  }
}
</script>

<style >
  .chartAreaWrapper {
     overflow-x: scroll;
  }


</style>