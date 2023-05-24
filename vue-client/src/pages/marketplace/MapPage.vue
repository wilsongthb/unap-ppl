<!-- Author: Wilson Pilco Nunez -->
<!-- Email: wilsonaux1@gmail.com -->
<!-- Created at: 2023-01-13 22:11 -->
<!-- Description: -->
<template>
  <div>
    <MapEl ref="elMap"></MapEl>
    <PersonaLista></PersonaLista>
  </div>
</template>
<script>
/* Script part */
import MapEl from "./MapEl.vue";
import http from "src/utils/http.js";
import PersonaLista from "./PersonaLista.vue";
export default {
  name: "MapPage",
  components: {
    MapEl,
    PersonaLista
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

  async mounted() {
    var res = await http.get("api/marketplace/mapmark/?page_size=9999");
    res.data.results
      .map((x) => {
        x.lat = parseFloat(x.lat);
        x.lng = parseFloat(x.lng);
        return x;
      })
      .map((x) => {
        var map = this.$refs.elMap.getMap();
        new window.google.maps.Marker({
          position: {
            lat: x.lat,
            lng: x.lng
          },
          map,
          title: x.label,
          clickable: true,
          icon: x.iconSrc
        });
      });
  },

  methods: {
    //
    //
  }
};
</script>
<style scoped></style>
