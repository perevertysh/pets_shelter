<template>
    <div>
        <b-container fluid variant="info" v-if="items && items.length">
            <b-row v-for="indexRow in countRows" :key="indexRow">
                <b-col v-for="indexCol in countCol" :key="calcIndex(indexCol, indexRow)">
                    <pet-card
                        v-if="items[calcIndex(indexCol, indexRow)]"
                        :item="items[calcIndex(indexCol, indexRow)]"
                        v-model='selectItem'
                    />
                </b-col>
            </b-row>
        </b-container>
        <div v-else>
            Приют пуст
        </div>
        <b-pagination
            align="center"
            class="mx-2 mt-2"
            v-model="curPage"
            :total-rows="totalRows"
            :per-page="perPage"
            first-number
            last-number
        ></b-pagination>
        <shelter-pet v-model="selectItem"/>
    </div>
</template>

<script>
import rest from './../js/rest'
import PetCard from './pet_card'
import ShelterPet from './shelter_pet'

export default {
    name: 'Pets',
    components: {
        PetCard,
        ShelterPet,
    },
    props:{
        model: {
            type: String,
            default: 'pet',
        }
    },
    data: function() {
        return {
            items: null,
            selectItem: null,
            countCol: 3,
            curPage: 1,
            perPage: 6,
            totalRows: 0,
        };
    },
    computed: {
        countRows() {
            return Math.ceil(this.items.length / this.countCol);
        },
    },
    watch: {
        curPage () {
            this.fetch();    
        },
    },
    mounted: function() {
        this.fetch();
    },
    methods: {
        fetch() {
            rest[this.model].get({page: this.curPage, page_size: this.perPage}).then(res => {
                if (res.data.results.length) {
                    this.items = res.data.results;
                    // this.items = this.items.concat(this.items.concat(this.items).concat(this.items).concat(this.items).concat(this.items).concat(this.items).concat(this.items).concat(this.items));
                    this.totalRows = res.data.count;
                }
                // test
                // else {
                //     this.items = [
                //         {id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},
                //         {id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},
                //         {id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},
                //         {id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},{id:'1'},
                //         {id:'1'},{id:'1'},{id:'1'},{id:'1'},
                //     ];
                //     this.totalRows = this.items.length;
                // }
            }). catch(err => {
                console.error(err);
            });
        },
        calcIndex (col, row) {
            return col - 1 + (row - 1) * this.countCol;
        },
    }
}
</script>