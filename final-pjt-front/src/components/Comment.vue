<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="comments"
      class="elevation-1"
      @click:row="rowClick"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Comments</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="yellow darken-4"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                CREATE
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
  
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.content"
                        label="content"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.user"
                        label="user"
                        disabled
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <div>
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
          v-if="item.user===loginUser"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
          v-if="item.user===loginUser"
        >
          mdi-delete
        </v-icon>

        </div>

      </template>
      <!-- <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template> -->
    </v-data-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    loginUser: null,
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: 'user',
        align: 'start',
        value: 'user',
      },
      { text: 'content', value: 'content' },
      { text: 'actions', value: 'actions', sortable: false },
    ],
    comments: [],
    editedIndex: -1,
    editedItem: {
      user: '',
      content: '',
    },
    defaultItem: {
      user: '',
      content: '',
    },
  }),
  props:{
    reviewId:{
      type: Number
    }
  },
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    },
  },
  created () {
    this.loginUser = this.$store.state.loginUser
    this.editedItem.user = this.loginUser
    this.defaultItem.user = this.loginUser
    this.getComments()
  },
  methods: {
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    rowClick: function(value) {
      console.log(value.user)
    },
    getComments: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/reviews/detail/${this.reviewId}/comments/`,
        headers:this.setToken()
      })
      .then(res => {
        this.comments = res.data
        console.log(res.data)
      })
    },
    
    editItem (item) {
      // comments 배열에서 수정할 것(item)의 인덱스를 정한다
      this.editedIndex = this.comments.indexOf(item)
      // {}에 item을 담는다. 이제 editedItem에 담겻다.
      this.editedItem = Object.assign({}, item)
      // dialog를 연다
      this.dialog = true

    },

    deleteItem (item) {
      this.editedIndex = this.comments.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      this.comments.splice(this.editedIndex, 1)
      this.saveComment()
      this.closeDelete()
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
      

    },

    createComment: function () {
      const newComment = {
        content: this.editedItem.content
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/reviews/detail/${this.reviewId}/createcomment/`,
        data: newComment,
        headers: this.setToken()
      })
    },

    saveComment: function () {
      
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/reviews/detail/${this.reviewId}/updatecomment/`,
        data: this.comments,
        headers: this.setToken()
      })
    },

    save () {
      // editedIndex가 -1인 경우는 새로 댓글을 생성하는 경우
      // editedIndex가 0이상인 경우는 댓글을 수정하는 경우이다.
      if (this.editedIndex > -1) {
        // 수정
        Object.assign(this.comments[this.editedIndex], this.editedItem)
        // this.saveComment()
        this.saveComment()

      } else {
        // 생성
        this.comments.push(this.editedItem)
        this.saveComment()
      }
      this.close()
    },
  },
}
</script>

<style>

</style>