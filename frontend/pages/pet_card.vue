<template>
    <div>
        {{JSON.stringify(value)}}
    </div>
</template>

<script>
export default {
    name: 'PetCard',
    props: {
        value: {
            default: null,
        },
    },

}
</script>