<template>
  <div>
    <v-container
      class="spacing-playground pa-6"
      fluid
    >
        <doughnat-chart-container
          :data="energyConsumptionSum"
        >
        </doughnat-chart-container>
        <v-sheet  
          v-for="path, i of selected"
          :key="i"
          min-height="250" class="fill-height" color="transparent"
        >
        <v-lazy 
          v-model="energyConsumptionStat[path].isActive" 
          :options="{
                threshold: .5
          }"
          class="fill-height">
          <line-chart-container
            :data="energyConsumptionData[path]"
            :stat="energyConsumptionStat[path]" 
            :type="'energy'"
            :path="path"
          >
          </line-chart-container>
        </v-lazy>
      </v-sheet>
    </v-container>
  </div>
</template>

<script>

import LineChartContainer from '@/components/ChartContainer.vue'
import DoughnatChartContainer from '@/components/DoughnatChartContainer.vue'

export default {
  components:{
    LineChartContainer, DoughnatChartContainer
  },

  data: ()=>({

  }),

  props:{
    selected: Array,
  },

  computed:{
    energyConsumptionData(){
        if(!this.selected.length) return undefined
        let energyData = {}
        let statData = this.getData()
        for(let path of this.selected){
          if(path in statData){
            energyData[path]=statData[path].energy_data
          }
          else{
            console.log(path+" not loaded")
          }
        }
        return energyData
      },

      energyConsumptionStat(){
        if(!this.selected.length) return undefined
        let energyStat = {}
        let statData = this.getData()
        for(let path of this.selected){
          if(path in statData){
            energyStat[path] = statData[path].energy_stat[1]
          }
          else{
            console.log(path+" not loaded")
          }
        }
        return energyStat
      },

      energyConsumptionSum(){
        if(!this.selected.length) return undefined
        let sumDict = {}
        let statData = this.getData()
        for(let path of this.selected){
          sumDict[path] = statData[path].energy_stat[1]['Sum']
        }
        return sumDict
      }
  },

  methods:{
    getData(){        
        let statData = {}
        if (localStorage.getItem("statData")){
            try{
              statData = JSON.parse(localStorage.getItem("statData"))
            }
            catch(e){
              localStorage.removeItem("statData")
            }
        }
        return statData
      },
  }

}
</script>
