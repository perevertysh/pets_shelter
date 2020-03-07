<template>
    <b-container class="tail" v-if="item">
        <b-row>
            <b-col key='image' id='image' sm="7" @click="select()">
                <b-img :src='item.photo' fluid rounded/>
            </b-col>
            <b-col key='info' id='info' sm="5">
                <div>
                    {{item.name}}<br/>
                    {{item.gender.name}}<br/>
                    {{item.age + " " + make_word_end()}}
                </div>
                <b-button
                    class="btn"
                    :class="{
                        wait: out_home,
                        lucky: !out_home,
                    }"
                    @click="out_home && shelterReq()"
                >
                    {{!item.status ? 'без дома' : item.status.name}}
                </b-button>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import functions from './js/functions'

export default {
    name: 'PetCard',
    mixins: [
        functions,
    ],
    props: {
        item: {
            default: null,
        },
        value: {
            type: Object,
            default: null,
        },
    },
    computed: {
        out_home() {
            return !this.item.status || this.item.status.code == 'out_home';
        }
    },
    methods: {
        select() {
            this.$router.push({name: 'pet.edit',  params: { id: this.item.id }});
        },
        shelterReq() {
            this.$emit('input', this.item);
            this.shelter();
        }
    }
}
</script>