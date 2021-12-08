<template>
  <div>
    <v-btn :class="{followed: isFollowed}" @click="follow" >follow</v-btn>
    
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserFollow',
  data: function () {
    return {
      targetUser: this.$route.params.username,
      isFollowed: null,
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
    follow: function () {
      axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/follow/${this.targetUser}/`,
      headers: this.setToken()
    })
      .then(res => {
        console.log(res)
        this.$emit('refresh', res.data.followers_count)
        this.isFollowed = res.data.isFollowed
      })
    },
  },

}
</script>

<style>

  .followed {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
  }

</style>