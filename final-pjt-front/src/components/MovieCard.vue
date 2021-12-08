<template>
  <div>
    <v-row justify="center">
      <v-col cols="auto">
        <v-dialog
          transition="dialog-bottom-transition"
          width="800"       
          v-model="dialog"
        >
          <template v-slot:activator="{ on, attrs }">
          <v-card max-width="300" class="ma-4"
          v-bind="attrs"
          v-on="on"
          @click="openCard"         
          >   
          <v-img height="480px" width="300px" :src="imgUrl"></v-img>

          </v-card>
          </template>

          <template v-if="dialog">
            <v-card>
              <v-toolbar
                color="warning"
                dark
              >
                <v-card-actions class="justify-end">
                  <v-btn
                    text
                    @click="dialog = false"
                  ><v-icon>mdi-close</v-icon></v-btn>
                </v-card-actions>
              Movie Detail
              </v-toolbar>
              <v-card class="d-flex justify-center" >
                <iframe allow="autoplay; encrypted-media" id="ytplayer" type="text/html" width="800" height="360"
                  :src="videoUrl"
                  frameborder="0"></iframe>
              </v-card>
              
              <v-container> 
              <v-row >
                <v-col cols="4">
                <v-img height="200px" contain :src="imgUrl"></v-img>
                </v-col>

                <v-col cols="8">  
                  <div class="text-h2 pa-12">{{ movieCard.title }}</div>       
                </v-col>
              </v-row>
              </v-container>
              
              <v-card-text>
                <v-chip-group
                  v-model="selection"
                  active-class="deep-purple accent-4 white--text"
                  column
                >
                  <v-chip>출연진</v-chip>
          
                  <v-chip>줄거리</v-chip>
          
                  <v-chip>리뷰</v-chip>
          
                  <v-chip>보러가기</v-chip>
                </v-chip-group>
              </v-card-text>

              <!-- 여기에 내용 출력하기 -->

              <movie-card-credits 
                v-show="selection === 0"
                :movieCard="movieCard"  
              >
              </movie-card-credits>

              <movie-card-over-view
                v-show="selection === 1"
                :movieCard="movieCard"
              >
              </movie-card-over-view>

              <movie-card-review
                v-show="selection === 2"
                :movieId="movieCard.id"
              >
              </movie-card-review>

              <movie-card-providers
                v-show="selection === 3"
                :movieId="movieCard.id"
              >
              </movie-card-providers>
              
            </v-card>
              
          </template>
        </v-dialog>
      </v-col>
  
     
    </v-row>

  </div>
</template>

<script>
import axios from 'axios'
import MovieCardCredits from '@/components/MovieCardCredits'
import MovieCardOverView from '@/components/MovieCardOverView'
import MovieCardProviders from '@/components/MovieCardProviders'
import MovieCardReview from '@/components/MovieCardReview'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name:'MovieCard',
  components:{
    MovieCardCredits,
    MovieCardOverView,
    MovieCardProviders,
    MovieCardReview,
    
  },
  props:{
    movieCard:Object
  },
  data:function(){
    return {
      imgUrl : `https://image.tmdb.org/t/p/w300${this.movieCard.poster_path}`,
      selection: 0,
      dialog:false,
      videoUrl:null,
    }
  },
  methods:{
    openCard:function(){
      this.dialog = true
      this.youtube()
    },


    youtube:function(){
      const params = {
        key:API_KEY,
        part:'snippet',
        q:this.movieCard.title + 'Trailer',
        type:'video'
      }
      axios({
        method:'get',
        url:API_URL,
        params,
      })
        .then(res=>{
          const videoId = res.data.items[0].id.videoId
          this.videoUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1`
        })
        .catch(err => {
          console.log(err)
        })

    },
  }
}
</script>

<style>

</style>