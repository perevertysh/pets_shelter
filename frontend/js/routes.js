import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

let routes = [];

import About from './../pages/about'
import Contact from './../pages/contact'
import Pets from './../pages/pets_main'
import PetProfile from './../pages/pet_profile_page'

routes.push({
  path: "/about",
  component: About,
  name: 'about'
});

routes.push({
  path: "/contact",
  component: Contact,
  name: 'contact'
});

routes.push({
  path: "/pets",
  component: Pets,
  name: 'pet.list'
});

routes.push({
  path: "/pets/:id",
  component: PetProfile,
  name: 'pet.edit'
});

const router = new VueRouter({
  mode: 'history',
  base: 'app/',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path == '/') {
    next('/pets');
  }
  else {
    next();
  }
})
  
export {router};