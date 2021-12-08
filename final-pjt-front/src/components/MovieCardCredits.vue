<template>
  <div>
    <!-- 슬라이더 만들기 -->
        <v-sheet
          class="mx-auto" 
          max-width="800"
          outline
        >
          <v-slide-group
            class="pa-4"
            show-arrows
          >
            <v-slide-item
              v-for="actor in actors"
              :key="actor.id"
            >
              <v-card
                class="ma-4"
                height="220"
                width="100"
              >
                <p v-if="actor.profile_path === null"> 사진 없음 </p>
                <v-img v-else  :src="imgUrl + actor.profile_path"></v-img>
                <v-card-text>
                  {{ actor.name }}
                </v-card-text>
              </v-card>
            </v-slide-item>
          </v-slide-group>
        </v-sheet>
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
export default {
  name:'MovieCardCredits',
  data:function(){
    return {
      
      imgUrl:'https://image.tmdb.org/t/p/w92',
      actors:[],
      
    }
  },
  props:{
    movieCard:Object,
    API_KEY:String,
  },
  methods:{
    loadCredits:function(){
      const params = {
        api_key:API_KEY
      }
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/movie/${this.movieCard.id}/credits`,
        params
      })
        .then(res=>{
          this.actors = res.data.cast
        })
        .catch(err=>{
          console.log(err)
        })

    }
  },

  created: function(){
    this.loadCredits()

    
  }

}
</script>

<style>

</style>