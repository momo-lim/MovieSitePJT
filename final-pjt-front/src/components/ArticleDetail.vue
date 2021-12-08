<template>
  <div>
    <v-row>
      <v-col cols="8">
        <h2>{{title}}</h2>
        <span class="font-weight-medium">{{ user }} | {{ created_at }}</span>
        <v-btn
          class="mx-2"
          fab
          dark
          small
          color="pink"
          @click="getlike"
        >
          <v-icon dark>
            mdi-heart
          </v-icon>{{ like_users }}
        </v-btn>

        <v-btn
          class="mx-2"
          
          small
          color="warning"
          v-if="user === loginUser"
          @click="moveUpdate"
        >
        <v-icon left>
          mdi-pencil
        </v-icon>
        Edit
        </v-btn>

        <v-btn
          
          small
          color="dark"
          dark
          v-if="user === loginUser"
          
          @click="deleteBtn"
        >
        <v-icon left dark>
          mdi-cancel
        </v-icon>
          Delete
        </v-btn>

        <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="deleteData(id)">OK</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
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

  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
export default {
  name:'ArticleDetail',
  data:function(){
    return{    
      category:null,
      id:null,
      content:null,
      created_at:null,
      like_users:null,
      rate:null,
      title:null,
      user:null,
      dialogDelete:false,
    }
  },
  methods:{
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    moveUpdate:function(){
      this.$router.push({name:'ArticleUpdate',params:{articleNum:this.id,title:this.title,content:this.content}})
    },
    deleteData:function(id){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/articles/${id}/`,
        headers:this.setToken()
      })
        .then(()=>{
          this.$router.push({name:'Community'})
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getlike:function(){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}/likes/`,
        headers:this.setToken()
      })
        .then(()=>{
          this.getData()
        })
        .catch(err=>{
          console.log(err)
          
        })
    },
    getData:function() {
      // console.log(this.$route.params.articleNum)
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}`,

    })
      .then(res=>{
        this.category = res.data.category
        this.content = res.data.content
        this.title = res.data.title
        this.id = res.data.id
        this.like_users = res.data.like_users.length
        this.created_at = res.data.created_at
        this.user = res.data.user
        this.rate = res.data.rate
      })
      .catch(err=>{
        console.log(err)
      })
    },
    closeDelete:function(){
      this.dialogDelete = false
    },
    deleteBtn:function(){
      this.dialogDelete = true
    },
  },

  computed:{
    ...mapState(['loginUser'])
  },

  created:function(){
    this.getData()
  }
}
</script>

<style>

</style>
