<template>
  <div>
    <v-container class="grey lighten-5 mt-10">
       
      <article-detail></article-detail>
        

      <v-row>
        <v-col cols="12">
          <article-comment-list
          class="pt-2"
          :articleNum="$route.params.articleNum"
          ></article-comment-list>
        </v-col>
      </v-row>

    </v-container>
  </div>
</template>

<script>
import ArticleDetail from '@/components/ArticleDetail'
import ArticleCommentList from '@/components/ArticleCommentList'


export default {
  name:'Article',
  components:{
    ArticleDetail,
    ArticleCommentList,
    
  },
}
</script>

<style>
    

</style>