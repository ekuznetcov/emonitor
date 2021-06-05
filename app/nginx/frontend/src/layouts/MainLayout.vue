<template>
  <v-app >
    <v-navigation-drawer 
    app
    v-model="drawer"  
    >
      <dirrectory-tree 
      @update-active="updateActive"
      @update-selected="updateSelected"
      >

      </dirrectory-tree>
    </v-navigation-drawer>

    <v-app-bar app class="deep-purple accent-3 white--text headline" dark flat>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <span>EMonitor</span>

        <v-tabs
          v-model="tab"
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
					<v-btn icon>
						<v-icon>mdi-plus</v-icon>
					</v-btn>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
        <!-- If using vue-router -->
        <!-- <router-view></router-view> -->
    </v-main>

    <v-footer app>
      &copy;2021 — <strong>Ekuznetcov</strong>
    </v-footer>
  </v-app>

</template>


<script>
import DirrectoryTree from './components/DirrectoryTree.vue'

  export default {
    components:{
      DirrectoryTree,
    },

    data: () => ({
      files: [],
      selected: [],
      active: [],
      selectedSumDict: {},
      drawer: false,
    }),

    computed:{
      select(){
        if(!this.selected.length) return undefined
        return this.filter(this.selectedSumDict, this.selected)
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
    },

  }

</script>

<style>
  ::-webkit-scrollbar {
    width: 0px;
}
</style>