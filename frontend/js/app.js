const _ = require('lodash');
import Vue from 'vue'
import Vuex from 'vuex'
import store from './store'
import {router} from './routes'
// plugins
import { BootstrapVue, IconsPlugin, NavbarPlugin, ModalPlugin } from 'bootstrap-vue'
// components
import { BPagination } from 'bootstrap-vue'


Vue.use(Vuex);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(NavbarPlugin);
Vue.use(ModalPlugin);

Vue.component('b-pagination', BPagination)

const app = new Vue({
    router,
    store,
    el: '#app',
    data: {
        drawer: true,
    },
});