<!-- Author: Wilson Pilco Nunez -->
<!-- Email: wilsonaux1@gmail.com -->
<!-- Created at: 2023-05-24 13:43 -->
<!-- Description:  -->
<template>
  <table class="table">
    <thead>
      <tr>
        <th>ID</th>
        <th>RUC</th>
        <th>NOMBRE</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="l in list" :key="l.id">
        <td>{{ l.id }}</td>
        <td>{{ l.ruc }}</td>
        <td>{{ l.razon_social }}</td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import http from "src/utils/http.js";
// script content
export default {
  name: "PersonaLista",
  components: {
    //
  },

  // directives

  props: {
    //
  },

  data: () => ({
    list: []
  }),

  computed: {
    //
  },

  // watch: {},

  async mounted() {
    var res = await http.get("api/marketplace/persona/?page_size=999");
    this.list = res.data.results;
  },

  methods: {
    //
    //
    //
  }
};
</script>
<style scoped></style>
