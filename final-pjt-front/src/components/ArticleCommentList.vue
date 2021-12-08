<template>
  <div>

    <v-container>
      <v-card>
        <article-comment-list-item
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
        @delete-comment="deleteComment"
        @update-comment="updateComment"
        ></article-comment-list-item>
      </v-card>

      <v-card class="mt-5">
        <article-comment-create
        :articleId="articleNum"
        @create-comment="updateList"
        ></article-comment-create>
      </v-card>
      </v-container>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleCommentListItem from './ArticleCommentListItem.vue'
import ArticleCommentCreate from './ArticleCommentCreate.vue'
export default {
  components: { ArticleCommentListItem, ArticleCommentCreate },
  name:'ArticleCommentList',
  data:function(){
    return{
      comments:null,
    }
  },
  props:{
    articleNum:{
      type:[Number,String]
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
    getDate:function(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/articles/${this.articleNum}`,
        headers:this.setToken()
      })
        .then(res=>{
          if (res.data.communitycomment_set){
            this.comments = res.data.communitycomment_set
          } 
        })
        .catch(err=>{
          console.log(err)
        })
    },
    updateList:function(){
      this.getDate()
    },
    deleteComment:function(){
      this.getDate()
    },
    updateComment:function(){
      this.getDate()
    },
  },
  created:function(){
    this.getDate()
  },

}
</script>

<style>

</style>