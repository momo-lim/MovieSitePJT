<template>
  <v-container >
    <v-row>
      <v-col cols="6">
        <v-card
      :loading="loading"
      class="ml-auto my-12"
      max-width="600"
    >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>
  
      <v-img
        height="250"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>
  
      <v-card-title class="ml-2">{{ username }}'s Profile</v-card-title>
  
      <v-card-text>
        <v-row
          align="center"
          class="mx-0"
        >
          <v-btn
            v-if="is_expert"
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
        </v-row>
  
        <div class="ml-2 my-4 text-subtitle-1">
          <span v-for="(genre, index) in genres" :key="`genre-${index}`">#{{ genre }}</span>
        </div>
        <span class="ml-2">FOLLOWERS: {{ followers }}</span>
        <user-follow class="ml-2 d-inline" v-if="isNotMe" @refresh="refreshFollowCount"></user-follow>
        
        
      </v-card-text>
  
      <v-divider class="mx-4"></v-divider>
        </v-card>
      </v-col>
      
      
      
      
      <v-col class="mt-10 mx-auto" cols="3">
        <div>
      
      <ul>
        <div v-for="(review, index) in post_reviews" :key="`review-${index}`">
          <v-card
          class="mx-auto mt-3"
          max-width="344"
          outlined
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Review
                </div>
              <v-list-item-title class="text-h5 mb-1">
                {{ review.title }}
              </v-list-item-title>
              <v-list-item-subtitle>{{review.content}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-card-actions>
              <v-btn
                outlined
                rounded
                text
                :to="{ name: 'ReviewDetail', params: { reviewId: review.id }}"
              >
                보러가기
              </v-btn>
            </v-card-actions>
          </v-card>
        </div>
      </ul>
    </div>
      </v-col>
      <v-col class="mt-10" cols="3">
        <ul>
          <div v-for="(movie, index) in like_movies" :key="`movie-${index}`">
            <v-card
            class="mx-auto mt-3"
            max-width="344"
            >
      <v-img
        :src="imgUrl+movie.poster_path"
        height="200px"
      ></v-img>
  
              <v-card-title>
                {{ movie.title }}
              </v-card-title>
  
              <v-card-subtitle>
                {{ movie.overview }}
              </v-card-subtitle>
            </v-card>
          </div>
        </ul>
      </v-col>
    </v-row>  
  </v-container>
</template>

<script>
import axios from 'axios'
import UserFollow from '@/components/UserFollow'

export default {
  name: 'Profile',
  components: {
    UserFollow,
  },
  data: function() {
    return {
      isNotMe: null,
      username: null,
      genres: null,
      is_expert: false,
      post_articles: null,
      like_movies: null,
      followers: null,
      imgUrl : 'https://image.tmdb.org/t/p/w300',
    }
  },
  methods: {
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    refreshFollowCount: function(data) {
      this.followers = data
    }
  },
  created: function () {
    // user 정보 받아오기
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${this.$route.params.username}/`,
      headers: this.setToken()
    })
    .then(res => {
      console.log(res)
      this.username = res.data.username
      this.genres = res.data.genres
      this.is_expert = res.data.is_expert
      this.post_articles = res.data.post_articles
      this.like_movies = res.data.like_movies
      this.followers = res.data.followers.length
      this.post_reviews = res.data.post_reviews
    })
    const loggedUser = this.$store.state.loginUser
    const targetUser = this.$route.params.username

    if (loggedUser === targetUser){
      this.isNotMe = false
    } else {
      this.isNotMe = true
    }
  }
}
</script>

<style>

</style>