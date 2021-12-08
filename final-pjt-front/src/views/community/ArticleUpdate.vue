<template>
  <div>
    <v-card flat>
      <v-form
        ref="form"
        v-on:submit.prevent=""
      >
        <v-container fluid>
          <v-row>
            <v-col
              cols="12"
              sm="6"
            >
              <v-text-field
                v-model="title"
                color="purple darken-2"
                label="Title"
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-textarea
                v-model="content"
                color="teal"
              >
                <template v-slot:label>
                  <div>
                    Content
                  </div>
                </template>
              </v-textarea>
            </v-col>

          </v-row>
        </v-container>
        <v-card-actions>
          <v-btn
            text
            @click="cancelArticle"
          >
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="!formIsValid"
            text
            color="primary"
            type="submit"
            @click="updateArticle"
          >
            Register
          </v-btn>
        </v-card-actions>
      </v-form>
    
    
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleUpdate',
  data:function(){
    return{
      title:null,
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
    updateArticle:function(){
      const updateItem = {
        title:this.title,
        content:this.content
      }
     
      if (updateItem.title){
        axios({
          method:'put',
          url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}/`,
          data:updateItem,
          headers:this.setToken(),
        })
          .then(()=>{
            this.$router.push({name:'Article',params:{articleNum:this.$route.params.articleNum}})
          })
          .catch(err=>{
            console.log(err)
          })
      }
    },
    cancelArticle:function(){
      this.$router.push({ name: 'Community' })
    }
  },
  created:function(){
    this.title = this.$route.params.title
    this.content = this.$route.params.content
  },
  computed: {
    formIsValid () {
      return (
        this.title &&
        this.content
      )
    },
  },

}
</script>

<style>

</style>