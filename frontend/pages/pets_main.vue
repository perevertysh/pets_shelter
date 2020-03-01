<template>
    <div>
        <b-container variant="info" v-if="items && items.length">
            <b-row v-for="indexRow in countRows" :key="indexRow" class="my-4">
                <b-col v-for="indexCol in countCol" :key="calcIndex(indexCol, indexRow)">
                    <pet-card :item="items[calcIndex(indexCol, indexRow)]"/>
                </b-col>
            </b-row>
        </b-container>
        <div v-else>
            Приют пуст
        </div>
        <b-pagination
            align="right"
            class="mx-2 mt-2"
            v-model="curPage"
            :total-rows="totalRows"
            :per-page="perPage"
        ></b-pagination>
    </div>
</template>

<script>
import rest from './../js/rest'
import PetCard from './pet_card'

export default {
    name: 'Pets',
    components: {
        PetCard,
    },
    props:{
        model: {
            type: String,
            default: 'petslist',
        }
    },
    data: function() {
        return {
            items: null,
            countCol: 5,
            curPage: 1,
            perPage: 10,
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
            rest[this.model].get({page: this.curPage, }).then(res => {
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