import { createRouter, createWebHashHistory } from "vue-router";
// import HomeView from "../views/HomeView.vue";
import authGuard from "@/auth-module/index.js";
import PublicContainer from "src/pages/PublicContainer.vue";
import PublicIndex from "src/pages/PublicIndex.vue";
import store from "@/store";
const routes = [
  {
    path: "/",
    component: PublicContainer,
    meta: {
      requiresAuth: true
    },
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
      },
      {
        path: "/marketplace",
        component: () => import("../pages/marketplace/Index.vue")
      },
      {
        path: "/marketplace/map",
        component: () => import("../pages/marketplace/MapPage.vue")
      }
    ]
  },

  { path: "/store", component: () => import("../pages/StorePage.vue") },
  {
    path: "/login",
    component: () => import("../pages/LoginPage.vue"),
    meta: { requiresAuth: false },
    beforeEnter: (to, from, next) => {
      console.log(store.state.logged);
      if (store.state.logged) {
        next({ path: "/" });
      } else {
        next();
      }
    }
  },
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

router.beforeEach(authGuard);

export default router;
