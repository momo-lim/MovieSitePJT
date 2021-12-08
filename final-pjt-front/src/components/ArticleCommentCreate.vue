<template>
  <div>
    <v-form v-on:submit.prevent="" class="pa-3">
      <v-text-field
        label="댓글 달기"
        outlined
        v-model="content"
      ></v-text-field>
      <v-btn
        :disabled="!formIsValid"
        tile
        small
        color="primary"
        @click="createComment"
      >SAVE
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleCommentCreate',
  props:{
    articleId:{
      type:[Number,String]
    }
  },
  data:function(){
    return{
      content:null,
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
    createComment:function(){
      const createItem = {
        content:this.content
      }
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/articles/${this.articleId}/comments/`,
        data:createItem,
        headers:this.setToken(),
      })
        .then(()=>{
          this.$emit('create-comment')
          this.content=null
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
  computed: {
    formIsValid () {
      return (
        this.content
        
      )
    },
  },
}
</script>

<style>

</style>