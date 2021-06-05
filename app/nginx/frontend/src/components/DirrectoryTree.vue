<template>
  <div>
    <v-sheet class="deep-purple accent-3 pa-4 " >
      <v-text-field
        v-model="search"
        label="Search Statistics File"
        dark
        flat
        solo-inverted
        hide-details
        clearable
        clear-icon="mdi-close-circle-outline"
      ></v-text-field>
      <v-checkbox
        prepend-icon="mdi-poll"
        v-model="isSelected"
        dark
        hide-details
        label="Select to compair"
      ></v-checkbox>
      <span class="d-flex flex-row">
          <v-file-input mt-10 mb-0 
          dark flat
          v-model="files"
          @change="addFile"
          hide-details
          multiple
          placeholder="Select your files"
          prepend-icon="mdi-file-plus-outline"
          >
        </v-file-input>
      </span>
    </v-sheet>
      <v-treeview class="text-truncate"
      v-model="selected"
      :active.sync="active"
      :open.sync="open"
      :items="items"
      :search="search"
      :filter="filter"
      :selectable="isSelected"
      item-key="path"
      color="deep-purple accent-3"
      transition
      open-on-click
      hoverable
      dense
    >
      <template v-slot:prepend="{ item, open }">
        <v-icon v-if="!item.file">
          {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
        </v-icon>
        <v-icon v-else>
          mdi-file
        </v-icon>
      </template>
    </v-treeview>
  </div>
</template>

<script>
  export default {
    data: () => ({
      files: [],
      selected:[],
      open:[],
      active:[],
      items: [],
      isSelected: false,
      search: null,
    }),

    props:{
      loading: Boolean,
    },

    computed:{
      filter () {
        return this.caseSensitive
          ? (item, search, textKey) => item[textKey].indexOf(search) > -1
          : undefined
      },
      opened () {
        if (!this.active.length) return undefined
        const path = this.active[0]
        return path
      },
      selection(){
        // this.$router.push({ path: 'statistics', query: { files: this.selected }})
        if (!this.selected.length) return undefined
        const selected = this.selected
        return selected
      }
    },

    watch:{
      opened(){
        this.$emit('update-active', {active:this.active, path:this.active[0]});
      },
      async selection(){
        this.$emit('update:loading', true)
        await this.getData()
        this.$emit('update:loading', false)
        this.$emit('update-selected', this.selected);
      }
    },

    methods:{  
      getNodes(){
      const path = `http://${window.location.hostname}:5000/v1/nodes/`;
      fetch(path).then(response => response.json())
      .then(data => {
                    this.items = [data];
                                        })
      },

      addFile(){
        Array.from(this.files).forEach(async (file, f) => {
        let data = new FormData()
        data.append('file', file)
        try{
          let response =  await fetch(`http://${window.location.hostname}:5000/v1/nodes/`,
                                      {
                                      method: 'POST',
                                      body:data} )
          console.log(response.data)
          this.$emit('complete-loaded')
        }
        catch(e){
          console.error(e)
        }
          this.getNodes()
          console.log(this.items)
        })
      },

      async getData(){        
        try {
          let statData = {}
          if (localStorage.getItem("statData")){
              try{
                statData = JSON.parse(localStorage.getItem("statData"))
              }
              catch(e){
                localStorage.removeItem("data")
              }
          }
          for (let path of this.selected){
            if(path in statData){
            }
            else{
              let data = await fetch(`http://${window.location.hostname}:5000/v1/nodes/statistics?path=${path}`)
              //let data = await fetch(`/v1/nodes/statistics?path=${path}`)
              data = await data.json()
              statData[path]=data
              localStorage.setItem("statData", JSON.stringify(statData))
            }
          }
        } catch (e) {
          console.error(e)
        }
      },

    },

    created(){
      this.getNodes();
    }

  }
</script>
