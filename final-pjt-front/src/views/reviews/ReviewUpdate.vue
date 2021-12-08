<template>
  <v-card flat>
    <v-snackbar
      v-model="snackbar"
      absolute
      top
      right
      color="success"
    >
      <span>Registration successful!</span>
      <v-icon dark>
        mdi-checkbox-marked-circle
      </v-icon>
    </v-snackbar>
    <v-form
      ref="form"
      @submit.prevent="submit"
    >
      <v-container fluid>
        <v-row>
          <v-col
            cols="12"
            sm="6"
          >
            <v-text-field
              v-model="form.title"
              color="purple darken-2"
              label="Title"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-textarea
              v-model="form.content"
              color="teal"
            >
              <template v-slot:label>
                <div>
                  Content
                </div>
              </template>
            </v-textarea>
          </v-col>
          <v-col
            cols="12"
            sm="6"
          >
            <v-select
              v-model="form.movie"
              :items="movies"
              item-text="title"
              item-value="id"
              color="pink"
              label="movie"
              required
            ></v-select>
          </v-col>
          <v-col
            cols="12"
            sm="6"
          >
            <v-slider
              v-model="form.rank"
              color="orange"
              label="rank"
              hint="Be honest"
              min="0"
              max="10"
              thumb-label
            ></v-slider>
          </v-col>
          <!-- <v-col cols="12">
            <v-checkbox
              v-model="form.terms"
              color="green"
            >
              <template v-slot:label>
                <div @click.stop="">
                  Do you accept the
                  <a
                    href="#"
                    @click.prevent="terms = true"
                  >terms</a>
                  and
                  <a
                    href="#"
                    @click.prevent="conditions = true"
                  >conditions?</a>
                </div>
              </template>
            </v-checkbox>
          </v-col> -->
        </v-row>
      </v-container>
      <v-card-actions>
        <v-btn
          text
          @click="resetForm"
        >
          Cancel
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!formIsValid"
          text
          color="primary"
          type="submit"
        >
          Register
        </v-btn>
      </v-card-actions>
    </v-form>
    <v-dialog
      v-model="terms"
      width="70%"
    >
      <v-card>
        <v-card-title class="text-h6">
          Terms
        </v-card-title>
        <v-card-text
          v-for="n in 5"
          :key="n"
        >
          {{ agreement }}
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            color="purple"
            @click="terms = false"
          >
            Ok
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="conditions"
      width="70%"
    >
      <v-card>
        <v-card-title class="text-h6">
          Conditions
        </v-card-title>
        <v-card-text
          v-for="n in 5"
          :key="n"
        >
          {{ agreement }}
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            color="purple"
            @click="conditions = false"
          >
            Ok
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    const defaultForm = Object.freeze({
      title: '',
      content: '',
      movie: '',
      rank: null,
    })

    return {
      form: Object.assign({}, defaultForm),
      rules: {
        required: [val => (val || '').length > 0 || 'This field is required'],
      },
      movies: this.$store.state.movieCards,
      conditions: false,
      agreement: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc.',
      snackbar: false,
      terms: false,
      defaultForm,
    }
  },
  computed: {
    formIsValid () {
      return (
        this.form.title &&
        this.form.content &&
        this.form.movie
      )
    },
  },
  methods: {
    // get jwt token
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateReview: function () {
      axios({
        method:'put',
        url: `http://127.0.0.1:8000/reviews/update/${this.$route.params.reviewId}/`,
        data: this.form,
        headers: this.setToken(),
      })
    },
    resetForm () {
      this.form = Object.assign({}, this.defaultForm)
      this.$refs.form.reset()
    },
    submit () {
      this.updateReview()
      this.snackbar = true
      this.resetForm()
    },
  },
  created: function () {
    this.$route.params.reviewId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/reviews/update/${this.$route.params.reviewId}/`,
      headers: this.setToken()
    })
      .then(res => {
        console.log(res.data)
        this.form.title = res.data.title
        this.form.content = res.data.content
        this.form.movie = res.data.movie
        this.form.rank = res.data.rank
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>