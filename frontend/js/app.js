import Vue from 'vue'
import Vuex from 'vuex'
import {router} from './routes'
import { BootstrapVue, IconsPlugin, NavbarPlugin, ModalPlugin } from 'bootstrap-vue'


Vue.use(Vuex);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(NavbarPlugin);
Vue.use(ModalPlugin);

import store from './store'

var _ = require('lodash');

const app = new Vue({
    router,
    store,
    el: '#app',
    data: {
        drawer: true,
    },
});