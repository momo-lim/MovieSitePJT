<template>
  <div>
    <v-container class="grey lighten-5 mt-10">
      <!-- Stack the columns on mobile by making one full-width and the other half-width -->
      <v-row>
        <v-col cols="9">
          
            <h2 class="d-inline">{{ title }}</h2>
              <v-rating
              :value="this.rank"
              class="d-inline"
              color="amber"
              dense
              half-increments
              readonly
              size="20"
            ></v-rating>
            <v-btn
              class="ma-2 d-inline"
              color="primary"
              dark
            >
              Expert
              <v-icon
                dark
                right
              >
                mdi-checkbox-marked-circle
              </v-icon>
            </v-btn>
            <v-list-item class="d-inline" :to="{ name: 'Profile', params: { username: this.user }}">
                <v-list-item-title>{{ this.user }} | {{ created_at }}</v-list-item-title>
            </v-list-item>
             
        </v-col>
        <v-col v-if="user===loginUser" align-self="end" cols="3">
          <v-btn
          class="ma-2"
          color="orange darken-2"
          dark
          :to="{ name: 'ReviewUpdate', params: { reviewId: this.$route.params.reviewId } }"
          >
            EDIT
            <v-icon
            dark
            right
            >
            mdi-pencil
            </v-icon>
          </v-btn>
  
          <v-btn
          class="ma-2"
          dark
          @click.native="deleteReview"
          >
            DELETE
            <v-icon
            dark
            right
            >
            mdi-cancel
            </v-icon>
          </v-btn>
        </v-col>
        
      </v-row>
      <v-row align="start" justify="center">
        <v-col cols="12">
          <v-card class="pa-2">
            <v-card-title>
            {{ content }}
            </v-card-title>
            
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8">
          <!-- comment component -->
          <comment :reviewId="$route.params.reviewId"></comment>
        </v-col>
        <v-col cols="4">
          <v-card class="pa-2">
            <movie-card v-if="movieCard" :movieCard="movieCard"></movie-card>
          </v-card>
        </v-col>
        </v-row>
    </v-container>    
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/Comment'
import MovieCard from '@/components/MovieCard'

export default {
  components: {
    Comment,
    MovieCard
  },
  name: 'ReviewDetail',
  data: function () {
    return {
      content: null,
      created_at: null,
      movie: null,
      rank: null,
      title: null,
      user: null,
      movieCard: null,
      loginUser: this.$store.state.loginUser
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
    deleteReview: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/reviews/update/${this.$route.params.reviewId}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'ReviewIndex' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },  
  created: function () {
    // Review 정보 가져오기
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/reviews/detail/${this.$route.params.reviewId}`,
      headers: this.setToken()
    })
      .then(res => {
      console.log(res.data.user)
      this.content = res.data.content
      this.created_at = res.data.created_at
      this.movie = res.data.movie
      this.rank = res.data.rank
      this.title = res.data.title
      this.user = res.data.user
    })
      .then(() => {
        const moviecard = this.$store.state.movieCards.filter( obj => {
      return obj.title === this.movie
        
      })
      console.log(moviecard)
      this.movieCard = moviecard[0]
    })
    
     
    
  },
}
</script>

<style>
  #username {
    font-size: 1.3rem;
  }
</style>