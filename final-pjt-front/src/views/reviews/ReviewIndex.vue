<template>
  <v-container>
    <v-card>
      <v-card-title>
        리뷰 목록
        <v-spacer></v-spacer>
        
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        <v-btn color="yellow darken-4 white--text" class="ml-5" :to="{ name: 'ReviewCreate' }">CREATE</v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="reviews"
        :search="search"
        @click:row="rowClick"
      ></v-data-table>
      
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'ReviewIndex',
    data: function () {
      return {
        search: '',
        headers: [
          { text: '영화', value: 'movie', align: 'start'},
          { text: '제목', value: 'title'},
          { text: '작성자', value: 'user' },
          { text: '작성일', value: 'created_at' },
          
        ],
        reviews: [],
        title: null,
      }
    },
    methods: {
      setToken:function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
      return config
      },
      rowClick: function (value) {
        this.$router.push({name:'ReviewDetail',params:{reviewId:value.id}})
      }
    },
    created: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/reviews/list/',
        headers: this.setToken()
      })
      .then(res => {
          console.log(res.data)
          this.reviews = res.data
      })
    }
  }
</script>

<style>

</style>