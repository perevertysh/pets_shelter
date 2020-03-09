const _ = require('lodash');
import Vue from 'vue'
import Vuex from 'vuex'
import store from './store'
import {router} from './routes'
// plugins
import { BootstrapVue, NavbarPlugin, ModalPlugin } from 'bootstrap-vue'
// components
import { BPagination } from 'bootstrap-vue'
import mainPage from './../pages/main.vue'

Vue.use(Vuex);
Vue.use(BootstrapVue);
Vue.use(NavbarPlugin);
Vue.use(ModalPlugin);

Vue.component('b-pagination', BPagination);
Vue.component('main-page', mainPage);

const app = new Vue({
    router,
    store,
    el: '#app',
    data: {
        drawer: true,
    },
});