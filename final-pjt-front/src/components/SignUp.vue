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
            S I G N U P
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">SIGN UP</span>
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
                    label="username"
                    required
                    v-model="credentials.username"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Password"
                    type="password"
                    v-model="credentials.password"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Password Confirmation"
                    v-model="credentials.passwordConfirmation"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="6"
                >
                  <v-select
                    v-model="credentials.genres"
                    :items="options"
                    item-text="name"
                    item-value="id"
                    label="Select"
                    return-id
                    single-line
                    multiple
                  ></v-select>
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
              Close
            </v-btn>
            <v-btn
              color="blue darken-1"
              text
              @click="signup"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
</template>

<script>
import axios from 'axios'
// import Multiselect from 'vue-multiselect'

export default {
  components: {
    // Multiselect,
  },
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        genres: []
      },
      dialog: false,
      errormessage: null,
      options: [
        { id: 12, name: '모험',  },
        { id: 14, name: '판타지',  },
        { id: 16, name: '애니메이션',  },
        { id: 18, name: '드라마',  },
        { id: 27, name: '공포',  },
        { id: 28, name: '액션',  },
        { id: 35, name: '코미디'},
        { id: 36, name: '역사'},
        { id: 37, name: '서부'},
        { id: 53, name: '스릴러'},
        { id: 80, name: '범죄'},
        { id: 99, name: '다큐멘터리'},
        { id: 878, name: 'SF'},
        { id: 9648, name: '미스터리'},
        { id: 10402, name: '음악'},
        { id: 10749, name: '로맨스'},
        { id: 10751, name: '가족'},
        { id: 10752, name: '전쟁'},
        { id: 10770, name: 'TV영화'},
      ],
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(() => {
          this.dialog = false
          this.$store.dispatch('openlogin')

          this.credentials = {
            username: null,
            password: null,
            passwordConfirmation: null,
            genres: []
          }
          this.errormessage = null,
          
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err.response.data.error)
          this.errormessage = err.response.data.error
        })
    },
    close: function () {
      this.dialog = false
      this.errormessage = null
      this.credentials =  {
        username: null,
        password: null,
        passwordConfirmation: null,
        genres: []
      }
    }
  }
}
</script>
