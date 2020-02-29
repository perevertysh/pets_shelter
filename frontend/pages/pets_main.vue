<template>
    <b-container variant="info">
        <b-row v-for="indexRow in countRows" :key="indexRow">
            <b-col v-for="indexCol in countCol" :key="calcIndex(indexCol, indexRow)">
                <!-- <pet-card :value="calcIndex(indexCol, indexRow)"/> -->
                {{calcIndex(indexCol, indexRow)}}
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import rest from './../js/rest';
import PetCard from './pet_card';

export default {
    name: 'Pets',
    component: [
        PetCard,
    ],
    props:{
        model: {
            type: String,
            default: 'petslist',
        }
    },
    data: function() {
        return {
            items: [],
            countCol: 6,
        };
    },
    computed: {
        countRows() {
            return Math.ceil(this.items.length / this.countCol);
        },
    },
    mounted: function() {
        this.fetch();
    },
    methods: {
        fetch() {
            rest[this.model].get({status__code: 'unshelter'}).then(res => {
                if (res.data.results.length) {
                    this.items = res.data.results;
                }
                // test
                else {
                    this.items = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},];
                }
            }). catch(err => {
                console.error(err);
            });
        },
        calcIndex (col, row) {
            return col - 1 + (row - 1) * this.countCol;
        }
    }
}
</script>