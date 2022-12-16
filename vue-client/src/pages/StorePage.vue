<!-- Author: Wilson Pilco Nunez -->
<!-- Email: wilsonaux1@gmail.com -->
<!-- Created at: 2022-12-15 19:48 -->
<!-- Description: -->
<template>
  <div class="row">
    <StoreMap ref="elMap"></StoreMap>
    <div class="col"><i class="fa-solid fa-store"></i> Store Page</div>
  </div>
</template>
<script>
import StoreMap from "../components/StoreMap.vue";
export default {
  name: "StorePage",
  components: {
    StoreMap
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
