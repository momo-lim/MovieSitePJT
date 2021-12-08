<template>
  <div>
    <v-card class="pa-5">

      <div class="d-flex">
        <v-avatar
          color="teal"
          size="36"
        >
          <span class="white--text text-h5">{{avatar}}</span>
        </v-avatar>
        <p class="my-auto mx-2">{{ comment.user.username }}님의 댓글</p>
      </div>

      <div class="ma-5">
        <p>{{ comment.content }}</p>
      </div>
    
      <v-expand-transition>
        <v-btn
          class="mx-2"
          
          small
          color="warning"
          v-if="!this.edit && comment.user.username === loginUser"
          @click="editComment"
        >
        <v-icon left>
          mdi-pencil
        </v-icon>
        Edit
        </v-btn>
      </v-expand-transition>
      
      <v-btn
        
        small
        color="dark"
        dark
        v-if="comment.user.username === loginUser"
         @click="deleteBtn"
      >
      <v-icon left dark>
        mdi-cancel
      </v-icon>
      Delete
      </v-btn>
    </v-card>

      <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="deleteComment">OK</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
  
      <v-expand-transition>
        <v-form v-if="this.edit" v-on:submit.prevent="" class="pa-3">
          <v-text-field
            label="제목"
            outlined
            v-model="content"
          ></v-text-field>
            <v-btn
              :disabled="!formIsValid"
              
              small
              color="warning"
              @click="updateComment"
            >SAVE
            </v-btn>
        </v-form>
      </v-expand-transition>
      



    
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
export default {
  name:'ArticleCommentListItem',
  props:{
    comment:{
      type:Object
    },
    
  },
  data:function(){
    return {
      edit:false,
      content:null,
      expand:false,
      dialogDelete:false,
      avatar:null,
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

    deleteComment:function(){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/article/comment/${this.comment.id}/`,
        headers:this.setToken(),
      })
        .then(()=>{
          
          this.$emit('delete-comment')
        })
        .catch(err=>{
          console.log(err)
        })
    },
    editComment:function(){
      this.edit = true
      this.expand = true
      this.content = this.comment.content
    },
    updateComment:function(){
      const updateItem = {
        content:this.content
      }
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/article/comment/${this.comment.id}/`,
        data:updateItem,
        headers:this.setToken(),
      })
        .then(()=>{
          this.$emit('update-comment')
          this.edit = false
          this.expand = false
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
    }
  },
  created:function(){
    this.avatar = this.comment.user.username.slice(0, 1)
  },
  computed:{
    ...mapState(['loginUser']),
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