<template>
  <div>
    <h1 class="text-center pt-5">전체 영화리스트</h1>
    <v-container fluid>
      <v-sheet 
          class="mt-5 mx-auto"
          max-width="100%"
          outline     
      >
        <v-slide-group  show-arrows center-active>
          <movie-card v-for="movieCard in movieCards" :key="movieCard.id" :movieCard="movieCard">
          </movie-card>
        </v-slide-group>
      </v-sheet>
    </v-container>



    <h1 class="text-center">평점이 높은 영화</h1>
    <v-container fluid>
      <v-sheet 
          class="mt-5 mx-auto"
          max-width="100%"
          outline    
      >
        <v-slide-group  show-arrows center-active>
          <movie-card v-for="averageCard in averageCards" :key="averageCard.id" :movieCard="averageCard">  
          </movie-card>
        </v-slide-group>
      </v-sheet>
    </v-container>

    <h1 class="text-center">{{ loginUser }}님이 좋아할 만한 영화</h1>
    <v-container fluid>
      <v-sheet 
          class="mt-5 mx-auto"
          max-width="100%"
          outline
      >
        <v-slide-group  show-arrows center-active>
          <movie-card v-for="genreCard in genreCards" :key="genreCard.id" :movieCard="genreCard">          
          </movie-card>
        </v-slide-group>
      </v-sheet>
    </v-container>   
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieCard from '@/components/MovieCard'
export default {
  name:'Home',
  components: {
    MovieCard  
  },

  computed:{
    ...mapState(['movieCards','is','genreCards','loginUser','averageCards'])
  },
  created: function () {
    
    this.$store.dispatch('LoadMovieCards')
    this.$store.dispatch('LoadGenreCards')
    this.$store.dispatch('LoadVoteAverageCards')
  },
  Mount:function(){
    
  }
}
</script>

<style>

</style>