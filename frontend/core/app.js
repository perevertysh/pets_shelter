import Vue from 'vue'
import Vuex from 'vuex'
import store from './store'
import {router} from './routes'

Vue.use(Vuex);

const app = new Vue({
    router,
    store,
    el: '#app',
    data: {
        drawer: true,
    },
});