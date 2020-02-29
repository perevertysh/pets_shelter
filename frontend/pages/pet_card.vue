<template>
    <div v-if="item" @click="select()">
        <b-img :src='item.photo' fluid rounded/>
        <div 
            :title="item.name"
            :style="{
                'white-space': 'nowrap', 
                width: '180px', 
                display: 'inline-block'
            }"
        >
            {{item.name}}
        </div>
    </div>
</template>

<script>
export default {
    name: 'PetCard',
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
            this.$emit('input', this.item);
        },
    }
}
</script>