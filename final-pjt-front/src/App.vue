<template>
  <v-app>
    <!-- <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer> -->

    <v-app-bar
        app
        clipped-left
        color="yellow darken-4"
        dark
      >
        <!-- <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
  
        <v-toolbar-title>ROTTEN APPLE</v-toolbar-title>
            <v-icon
            dark
            right
            >
            mdi-apple
            </v-icon>
  
        <v-spacer></v-spacer>
        
        <v-btn :to="{ name: 'Home' }" text>Home</v-btn>
        <v-btn :to="{ name: 'ReviewIndex' }" text>Reviews</v-btn>
        <v-btn :to="{ name: 'Community' }" text>Community</v-btn>
        
        <v-spacer></v-spacer>
  
        <v-menu offset-y
          left
          bottom
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              text
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-account</v-icon>{{ loginUser }}
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
  
          <v-list>
            <span v-if="isLogin">
              <v-list-item :to="{ name: 'Profile', params: { username: loginUser }}">
                <v-list-item-title>Profile</v-list-item-title>
              </v-list-item>
              <v-list-item @click.native="logout" to="#">
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item>
            </span>
            <span v-else>
              <!-- <v-list-item :to="{ name: 'Login' }">
                <v-list-item-title>Login</v-list-item-title>
              </v-list-item> -->
              <v-list-item>
                <login></login>
              </v-list-item>
              <v-list-item>
                <sign-up></sign-up>
              </v-list-item >
            </span>
            
            
          </v-list>
        </v-menu>
      </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
      
    <v-footer app>
      <span>2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'
import Login from '@/components/Login'
import SignUp from '@/components/SignUp'

  export default {
    components: { 
      Login,
      SignUp
    },
    props: {
      source: String
    },
    data: function () {
      return {
        username: null,
        drawer: null,
        items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard' },
          { title: 'Photos', icon: 'mdi-image' },
          { title: 'About', icon: 'mdi-help-box' },
        ]
      } 
    },
    methods: {
      logout: function () {
        localStorage.removeItem('jwt')
        this.$store.dispatch('logout')
        this.$router.push({ name: 'Login' })
      }
    },
    computed: {
      ...mapState([
        'isLogin',
        'loginUser'
      ])
    },
    created:function(){
      this.$router.push({ name:'Home'})
    }
  }
</script>