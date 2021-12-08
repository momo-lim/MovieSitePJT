<template>
  <v-row justify="center">
      <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="yellow darken-4"
            dark
            v-bind="attrs"
            v-on="on"
            width="150px"
          >
            L O G I N
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">LOGIN</span>
          </v-card-title>
          <v-card-text>
              <v-alert v-if="errormessage"
              shaped
              dense
              dark
              type="warning"
              >
              {{ errormessage }}
              </v-alert>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                >
                  <v-text-field
                    label="USERNAME"
                    required
                    v-model="credentials.username"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="PASSWORD"
                    type="password"
                    v-model="credentials.password"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue darken-1"
              text
              @click="close"
            >
              Close
            </v-btn>
            <v-btn
              color="blue darken-1"
              text
              @click="login"
            >
              lOGIN
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      dialog: false,
      errormessage: null,
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          // vuex에 로그인 상태 반영(isLogin)
          this.$store.dispatch('login', this.credentials.username)
          localStorage.setItem('jwt', res.data.token)
          this.$router.push({ name: 'Home' })
          this.errormessage = null
        })
        .catch(err => {
          console.log(err)
          this.errormessage = '아이디와 비밀번호를 다시 확인해보세요.'
        })
        
    },
    close: function () {
      this.credentials.username = null
      this.credentials.password = null
      this.dialog = false
      this.errormessage = null
    }
  }
}
</script>
