<template>
  <v-container fluid>
    <v-data-iterator
      :items="items"
      :items-per-page.sync="itemsPerPage"
      :page.sync="page"
      :search="search"
      :sort-by="sortBy"
      :sort-desc="sortDesc"
      hide-default-footer
    >
      <template v-slot:header>
        <v-toolbar
          light
          class="mb-1"
        >
          <v-text-field
            v-model="search"
            clearable
            flat
            hide-details
            color="deep-purple acent-3"
            prepend-inner-icon="mdi-magnify"
            label="Search"
          ></v-text-field>
          <template v-if="$vuetify.breakpoint.mdAndUp">
            <v-spacer></v-spacer>
            <v-select
              v-model="sortBy"
              flat 
              menu-props=auto
              hide-details
              :items="keys"
              color="deep-purple acent-3"
              label="Sort by"
            ></v-select>
            <v-spacer></v-spacer>
            <v-btn-toggle
              v-model="sortDesc"
              mandatory
            >
              <v-btn
                large
                outlined
                color="deep-purple accent-3"
                :value="false"
              >
                <v-icon color="deep-purple accent-3">mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn
                large
                outlined
                color="deep-purple accent-3"
                :value="true"
              >
                <v-icon color="deep-purple accent-3">mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>
          </template>
        </v-toolbar>
      </template>

      <template v-slot:default="props">
        <v-row>
          <v-col
            v-for="item, i in props.items"
            :key="i"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <v-card>
              <v-card-title class="subheading grey--text">
                {{ item.Name }}
              </v-card-title>

              <v-divider></v-divider>

              <v-list dense>
                <v-list-item
                  v-for="(key, index) in filteredKeys"
                  :key="index"
                >
                  <v-list-item-content :class="{ 'deep-purple--text':sortBy === key }">
                    {{ key }} (Cores):
                  </v-list-item-content>
                  <v-list-item-content
                    class="align-end"
                    :class="{ 'grey--text': sortBy === key }"
                  >
                    {{ Math.round(item[key]) }}
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </template>

      <template v-slot:footer>
        <v-row
          class="mt-2 mx-1"
          align="center"
          justify="center"
        >
          <span class="grey--text">Items per page</span>
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                dark
                text
                color="deep-purple acent3"
                class="ml-2"
                v-bind="attrs"
                v-on="on"
              >
                {{ itemsPerPage }}
                <v-icon>mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item
                v-for="(number, index) in itemsPerPageArray"
                :key="index"
                @click="updateItemsPerPage(number)"
              >
                <v-list-item-title>{{ number }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-spacer></v-spacer>

          <span
            class="mr-4
            grey--text"
          >
            Page {{ page }} of {{ numberOfPages }}
          </span>
          <span>
          <v-btn
            fab
            outlined
            color="deep-purple accent-3"
            class="mr-1"
            @click="formerPage"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn
            fab
            outlined
            color="deep-purple accent-3"
            class="ml-1"
            @click="nextPage"
          >
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
          </span>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>

export default ({
    props:{
        items: Array,
    },

    data:()=>({
        itemsPerPageArray: [4, 8, 12, 16,],
        search: '',
        filter: {},
        sortDesc: false,
        page: 1,
        itemsPerPage: 8,
        sortBy: 'Name',
        keys: [
          'Name',
          'Min',
          'Max',
          'Mean',
          'Amount',
        ],
    }),

    computed: {
      numberOfPages () {
        return Math.ceil(this.items.length / this.itemsPerPage)
      },
      filteredKeys() {
        return this.keys.filter(key => key !== 'Name')
      },
    },
    methods: {
      nextPage () {
        if (this.page + 1 <= this.numberOfPages) this.page += 1
      },
      formerPage () {
        if (this.page - 1 >= 1) this.page -= 1
      },
      updateItemsPerPage (number) {
        this.itemsPerPage = number
      },
    },
})
</script>

<style>
  .v-list .v-list-item--active { 
  background-color: rgba(101, 31, 255, 1)!important; 
  }

  .v-list .v-list-item--active .v-list-item__title {
    color: white !important;
  }
</style>