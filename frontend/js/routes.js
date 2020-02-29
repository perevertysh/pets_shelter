import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

let routes = [];

import Pets from './../pages/pets_main'

routes.push({
  path: "",
  component: Pets,
  name: 'pet.list'
});

const router = new VueRouter({
    mode: 'history',
    base: '',
    routes
  })
  
export {router};