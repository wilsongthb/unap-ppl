<!-- Author: Wilson Pilco Nunez -->
<!-- Email: wilsonaux1@gmail.com -->
<!-- Created at: 2023-01-15 16:06 -->
<!-- Description: -->
<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-sm-8">
        <Navbar></Navbar>
        <router-view />
        <Footer></Footer>
      </div>
    </div>
  </div>
</template>
<script>
import Navbar from "src/components/Navbar.vue";
import Footer from "src/components/Footer.vue";
/* Script part */
export default {
  name: "IndexPage",
  components: {
    Navbar,
    Footer
  },

  // directives
  // filters

  props: {
    //
  },

  data: () => ({
    //
  }),

  computed: {
    //
  },

  // watch: {},

  mounted() {
    //
  },

  methods: {
    //
    //
    //
  }
};
</script>
<style scoped></style>
