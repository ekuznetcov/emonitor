<template>
  <div>
     <v-container
            class = "spacing-playground pa-6"
            fluid
            v-if = "selected.length<2"
          >
            <v-sheet  
              v-for="data, i of coresWorkloadData"
              :key="i"
              min-height="250" class="fill-height" color="transparent"
            >
              <v-lazy 
                v-model="coresWorkloadStat[i].isActive" 
                :options="{
                            threshold: .5
                  }"
                class="fill-height"
              >
                <line-chart-container
                  :data="coresWorkloadData[i]"
                  :stat="coresWorkloadStat[i]"
                  :type="'core'"
                  :path="`Core ${i}`"
                >
                </line-chart-container>
              </v-lazy>
            </v-sheet>
          </v-container>
          <data-table
            v-else
            :items="cpuBusyStat"
          />
  </div>
</template>

<script>

import LineChartContainer from '@/components/ChartContainer.vue'
import DataTable from '@/components/DataTable.vue'

export default {
  components:{
    LineChartContainer, DataTable
  },

  data: ()=>({

  }),

  props:{
    selected: Array,
  },

  computed:{
      cpuBusyStat(){
        if(!this.selected.length) return undefined
        let cpuStat = []
        let statData = this.getData()
        for(let path of this.selected){
          if(path in statData){
            cpuStat.push(statData[path].cpu_stat[1])
          }
          else{
            console.log(path)
          }
        }
        return cpuStat
      },

      coresWorkloadStat(){
        if(!this.selected.length) return undefined
        let cpuStat=[]
        let statData = this.getData()
        for(let path of this.selected){
          if(path in statData){
            cpuStat = statData[path].cpu_stat[0]
          }
          else{
            console.log(path)
          }
        }
        return cpuStat
      },

      coresWorkloadData(){
        if(!this.selected.length) return undefined
        let cpuData = []
        let statData = this.getData()
        for(let path of this.selected){
          if(path in statData){
            cpuData = statData[path].cpu_data
          }
          else{
            console.log(path+" not loaded")
          }
        }
        return cpuData
      },
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
