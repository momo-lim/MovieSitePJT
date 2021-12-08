import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
    
  ],
  state: {
    isLogin: false,
    loginUser: 'Anonymous',
    movieCards:[],
    genreCards:[],
    averageCards:[],
    openLogin: false
  },
  mutations: {
    LOGIN: function(state, username) {
      state.isLogin = true
      state.loginUser = username
      
    },
    LOGOUT: function(state) {
      state.isLogin = false,
      state.loginUser = 'Anonymous'
    },
    LOAD_MOVIE_CARDS:function(state,data){
      state.movieCards = data
    },
    LOAD_GENRE_CARDS:function(state,data){
      state.genreCards = state.movieCards.filter(card =>{
        for (const dd of data) {
          if (card.genres.includes(dd)){
            return true
          }
        }
        return false
      })
      

    },
    LOAD_VOTE_AVERAGE_CARDS:function(state) {
      state.averageCards = state.movieCards.sort(function(a,b) {
        return b.vote_average - a.vote_average
      })
    },
    OPENLOGIN: function(state) {
      state.openLogin = true
    }
  },
  actions: {

 

    login: function(context, username) {
      context.commit('LOGIN', username)
    },
    logout: function(context) {
      context.commit('LOGOUT')
    },
    LoadMovieCards:function({commit}) {
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/',
      })
        .then(res=>{
        
          commit('LOAD_MOVIE_CARDS',res.data)
          
        })
        .catch(err=>{
          console.log(err)
        })
    },
    LoadGenreCards:function({commit}) {
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/accounts/genres/${this.state.loginUser}/`,
        
      })
      .then(res=>{
        commit('LOAD_GENRE_CARDS',res.data.genres)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    LoadVoteAverageCards:function({commit}) {
      commit('LOAD_VOTE_AVERAGE_CARDS')
    },
    openlogin:function(context) {
      context.commit('OPENLOGIN')
    }
  },
  modules: {
  }
})
