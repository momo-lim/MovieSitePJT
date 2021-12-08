<template>
  <div>
    <v-carousel hide-delimiters height="200">
    <v-carousel-item
      v-for="reviewData in reviewDatas"
      :key="reviewData.id">
          <!--  -->
        <v-card
          class="mx-auto"
          color="warning"
          dark
          max-width="500"
          
        >
          <v-card-title>
            <v-icon
              large
              left
            >
              mdi-twitter
            </v-icon>
            <span class="text-h6 font-weight-light">Review</span>
          </v-card-title>

          <v-card-text class="text-h5 font-weight-bold">
            "{{ reviewData.title }}""
          </v-card-text>

          <v-card-actions>
            <v-list-item class="grow">
              <!-- <v-list-item-avatar color="grey darken-3">
                <v-img
                  class="elevation-6"
                  alt=""
                  src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-img>
              </v-list-item-avatar> -->
              <v-list-item-avatar color="grey darken-3"
                
                
              >
                <span class="white--text text-h5">{{reviewData.user.slice(0,1)}}</span>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>{{ reviewData.user }}</v-list-item-title>
              </v-list-item-content>

              <v-row
                align="center"
                justify="end"
              >
                <v-icon class="mr-1">
                  mdi-star
                </v-icon>
                <span class="subheading mr-2">{{ reviewData.rank }}</span>
                
              </v-row>
            </v-list-item>
          </v-card-actions>
        </v-card>
          <!--  -->
      </v-carousel-item>
  </v-carousel>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'MovieCardReview',
  data:function(){
    return {
      reviewDatas:[],
    }
  },
  props:{
    movieId:Number,
  },
  methods:{
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    
  },
  created:function(){
    
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/movies/${this.movieId}/`,
      headers:this.setToken()
    })
      .then(res=>{
        this.reviewDatas = res.data.review_set
      })
      .catch(err=>{
        console.log(err)
      })
  },
}
</script>

<style>

</style>
  created:function(){
    this.avatar = this.comment.user.username.slice(0, 1)
  },