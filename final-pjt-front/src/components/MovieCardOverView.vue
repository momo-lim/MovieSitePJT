<template>
  <div>
    <!-- 평점 -->
    <div class="d-flex">
      <v-rating
        v-model="rating"
        background-color="orange lighten-3"
        color="orange"
        readonly
      ></v-rating>
      <span class="my-auto">({{ rating }})</span>
    </div>
    <p class="pb-3">{{ movieCard.overview }}</p>
  </div>
</template>

<script>
export default {
  name:'MovieCardOverView',
  props:{
    movieCard:Object,
  },
  data:function(){
    return {
      rating:null,
    }
  },

  created: function(){
    this.rating = this.movieCard.vote_average / 2
  }
}
</script>

<style>

</style>