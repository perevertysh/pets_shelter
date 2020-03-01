<template>
    <div v-if="item" @click="select()" :style="{cursor: 'pointer'}">
        <b-icon v-if="!item.status" icon='circle' variant="primary" font-scale="2" :style='{position: "absolute"}'/>
        <b-icon v-else icon='check-circle' variant="success" font-scale="2" :style='{position: "absolute"}'/>
        <b-img :src='item.photo' fluid rounded/>
        <div 
            :title="item.name"
            :style="{
                'white-space': 'nowrap', 
                width: size + 'px', 
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
        readOnly: {
            type: Boolean,
            default: false,
        },
        size: {
            type: Number,
            default: 180,
        },
    },
    methods: {
        select() {
            // this.$bvModal.show('profile-modal');
            // this.$emit('input', this.item);
            if (!this.readOnly)
                this.$router.push({name: 'pet.edit',  params: { id: this.item.id }});
        },
    }
}
</script>