<template>
  <div class="container">
    <!-- <nav class="mb-2"> -->
    <!--   <router-link to="/">Home</router-link> | -->
    <!--   <router-link to="/about">About</router-link> | -->
    <!--   <router-link to="/store">Store</router-link> -->
    <!-- </nav> -->
    <div class="row">
      <div class="col-12 col-sm-8">
        <TopNavbar class="mb-2"></TopNavbar>
        <router-view />
      </div>
    </div>
  </div>
</template>
<script>
import TopNavbar from "./components/TopNavbar.vue";
export default {
  components: {
    TopNavbar
  }
};
</script>
<style></style>
