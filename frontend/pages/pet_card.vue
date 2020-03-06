<template>
    <b-container class="tail" v-if="item">
        <b-row>
            <b-col key='image' id='image' sm="7">
                <b-img :src='item.photo' fluid rounded @click="select()"/>
            </b-col>
            <b-col key='info' id='info' sm="5">
                <div>
                    {{item.name}}<br/>
                    {{item.sex}}<br/>
                    {{item.age + " " + make_word_end()}}
                </div>
                <b-button 
                    class="btn" 
                    :class="{
                        wait: !item.status,
                        lucky: item.status,
                    }"
                    @click="!item.status && shelterReq()"
                >
                    {{item.status ? 'ждет хозяина' : 'без дома'}}
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