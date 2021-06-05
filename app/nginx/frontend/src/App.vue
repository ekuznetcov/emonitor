<template>
  <v-app >
    <v-navigation-drawer 
    app
    v-model="drawer"  
    >
      <dirrectory-tree 
      @update-active="updateActive"
      @update-selected="updateSelected"
      :loading.sync="loading"
      >
      </dirrectory-tree>
    </v-navigation-drawer>

    <v-app-bar app class="deep-purple accent-3 white--text headline" dark flat>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <span>EMonitor</span>
        <v-tabs
          v-model="tabs"
          slider-color="white"
          right
        >
          <v-tab to="/energy">
            Energy
          </v-tab >

          <v-tab to="/cpu" >
            CPU
          </v-tab>
        </v-tabs>
        <v-progress-linear
          :active="loading"
          :indeterminate="loading"
          absolute
          bottom
          color="white"
        >
        </v-progress-linear>        
    </v-app-bar>

    <v-main>
      <router-view
        v-if="selected.length" 
        :selected="selected">
      </router-view>
      <v-alert
      v-model="!selected.length"
      border="left"
      close-text="Close Alert"
      colored-border
      color="deep-purple accent-3"
      type="warning"
      dismissible
      >
        You have not yet selected files. Please select file or dirrectory
      </v-alert>
    </v-main>

    <v-footer app>
      &copy;2021 — <strong>Ekuznetcov</strong>
    </v-footer>
  </v-app>

</template>

<script>
import LineChartContainer from './components/ChartContainer.vue';
import DoughnatChartContainer from './components/DoughnatChartContainer.vue';
import DirrectoryTree from './components/DirrectoryTree.vue'
import DataTable from './components/DataTable.vue';
import StatBar from './components/StatBar.vue';
import Energy from './views/Energy.vue';

  export default {
    components:{
        LineChartContainer, DirrectoryTree, DoughnatChartContainer,
        DataTable, StatBar, Energy
    },

    data: () => ({
      active: [],
      selected: [],
      selectedSumDict: {},
      tabs: "energy",
      loading: false,
      drawer: false,
    }),

    computed:{
      // selected(){
      //   if(!this.$router.query) return []
      //   return this.$router.query.files
      // },


      cpuBusyStat(){
        if(this.selected.length>0) return undefined
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
      filter(db, keys){
       return keys.reduce((a, key) => (a[key] = db[key], a), {})
      },

      updateActive(newActive){
        this.path = newActive.path;
        this.active = newActive.active;
      },

      updateSelected(newSelected){
        this.selected = newSelected;
      },

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
    },
  }

</script>

<style>
.v-navigation-drawer ::-webkit-scrollbar {
    width: 0px;
}
</style>