import { createRouter, createWebHashHistory } from "vue-router";
// import HomeView from "../views/HomeView.vue";
import PublicContainer from "src/pages/PublicContainer.vue";
import PublicIndex from "src/pages/PublicIndex.vue";

const routes = [
  {
    path: "/",
    component: PublicContainer,
    children: [
      { path: "", component: PublicIndex },
      {
        path: "about",
        name: "about",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "about" */ "../views/AboutView.vue")
      }
    ]
  },

  { path: "/store", component: () => import("../pages/StorePage.vue") },
  { path: "/login", component: () => import("../pages/LoginPage.vue") },
  { path: "/profile", component: () => import("../pages/ProfilePage.vue") },
  {
    path: "/marker-view/:id",
    name: "marker-view",
    component: () => import("../pages/MarkerViewPage.vue"),
    props: true
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
