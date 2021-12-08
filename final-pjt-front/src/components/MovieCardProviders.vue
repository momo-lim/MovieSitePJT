<template>
  <div>

    <div v-if="movieProviderFlatrate">
      <h1>스트리밍</h1>
      <div class="d-flex pb-1">
        <v-card 
          v-for="(movieFlatrate,index) in movieProviderFlatrate"
          :key="index"
          height="45"  class="d-flex mx-3"
        >
        <v-img contain :src="imgUrl + movieFlatrate.logo_path"></v-img>
        <p class="my-auto mx-2">
          {{ movieFlatrate.provider_name }}
        </p>
        </v-card>
      </div>
    </div>

    <div v-if="movieProviderRent">
      <h1>대여</h1>
      <div class="d-flex pb-1">

      <v-card 
        v-for="(movieRent,index) in movieProviderRent"
        :key="index"
        height="45" class="d-flex mx-3"
      >
      <v-img contain :src="imgUrl + movieRent.logo_path"></v-img>
      <p class="my-auto mx-2">
        {{ movieRent.provider_name }}  
      </p>
      </v-card>
      </div>
    </div>


    <div v-if="movieProviderBuy">
      <h1>구매</h1>
      <div class="d-flex pb-1">
        <v-card 
          v-for="(movieBuy,index) in movieProviderBuy"
          :key="index"
          height="45" class="d-flex mx-3"
        >
        <v-img contain :src="imgUrl + movieBuy.logo_path"></v-img>
        <p class="my-auto mx-2">
          {{ movieBuy.provider_name }}
        </p>
        </v-card>
      </div>
    </div>
    <div v-if="!movieProviderBuy && !movieProviderRent && !movieProviderFlatrate">
      <h1 class="text-center pa-10"> 한국에서 서비스 하지 않습니다.</h1>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name:'MovieCardProviders',
  props:{
    movieId:Number
  },
  data:function(){
    return {
      imgUrl:"https://image.tmdb.org/t/p/w45",
      movieProviderRent:null,
      movieProviderBuy:null,
      movieProviderFlatrate:null,
    }
  },
  methods:{
    loadData:function(){
      
      const params = {
        api_key:API_KEY
      }
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/movie/${this.movieId}/watch/providers`,
        params,
      })
        .then(res=>{
          
          if (res.data.results.KR.buy) {
            this.movieProviderBuy = res.data.results.KR.buy
            
          }
          if (res.data.results.KR.rent) {
            this.movieProviderRent = res.data.results.KR.rent
            
          }
          if (res.data.results.KR.flatrate) {
            this.movieProviderFlatrate = res.data.results.KR.flatrate
            
          }
          
          
          
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
  created:function(){
    this.loadData()
  }
}
</script>

<style>

</style>