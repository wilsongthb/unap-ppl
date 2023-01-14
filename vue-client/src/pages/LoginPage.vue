<!-- Author: Wilson Pilco Nunez -->
<!-- Email: wilsonaux1@gmail.com -->
<!-- Created at: 2023-01-12 21:24 -->
<!-- Description: -->
<template>
  <div>
    <form @submit.prevent="login()" action="">
      <div class="mb-3">
        <label for="">Email</label>
        <input class="form-control" type="text" v-model="username" />
      </div>
      <div class="mb-3">
        <label for="">Password</label>
        <input class="form-control" type="password" v-model="password" />
      </div>
      <button class="btn btn-primary" type="submit">Submit</button>
      <div class="alert mt-3 alert-warning" v-show="message">
        {{ message }}
      </div>
    </form>
  </div>
</template>
<script>
import AuthService from "@/utils/AuthService.js";
/* Script part */
export default {
  name: "LoginPage",
  components: {
    //
  },

  // directives
  // filters

  props: {
    //
  },

  data: () => ({
    username: "",
    password: "",
    loading: false,
    message: ""
  }),

  computed: {
    //
  },

  // watch: {},

  mounted() {
    //
  },

  methods: {
    async login() {
      var result = await AuthService.login(this.username, this.password);
      if (result.success) {
        //
      } else {
        this.message = result.message;
      }
    }
    //
    //
  }
};
</script>
<style scoped></style>
