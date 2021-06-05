<template>
    <v-col
        cols="12"
      >
        <div
          class="d-flex justify-space-around  mb-6"
        >
          <v-card class="py-5 "
            v-for="data of Object.entries(stat)"
            :key=data[0]
          >
            <v-col
              class="text-left ml-10- mb-2"
              tag="strong"
            >
              {{data[0]}}
            </v-col>
            <v-col class="d-inline">{{ Math.round(data[1])}}</v-col>
          </v-card> 
        </div>    
      </v-col>
</template>

<script>

export default({
    props:{
        statistics: Object,
        },
    data:()=>({

    }),

    computed:{
      stat(){
        if(!Object.keys(this.statistics).length) return undefined
        let filtered = Object.fromEntries(Object.entries(this.statistics).filter(([k,v]) => k!="isActive"));
        return filtered
      }
    }
})
</script>
