<template>
    <div>
        <b-container v-if="items && items.length">
            <b-row>
                <b-col sm='1'>
                    <b-button>

                    </b-button>
                </b-col>
                <b-col sm='1'>
                    <b-button>
                        
                    </b-button>
                </b-col>
            </b-row>
                <b-col sm='8'>
                    <b-form inline>
                        <div v-for="(key, index) in filter" :key='index'>
                            <label :for="'inline-form-input-' + key">{{filter[key].name}}</label>
                            <b-form-select
                                :id="'inline-form-input-' + key"
                                class="mb-2 mr-sm-2 mb-sm-0"
                                v-model='select[key]'
                                value-field='id'
                                text-field='name'
                                :options='filter[key].items'
                            ></b-form-select>
                        </div>
                        <label for='inline-form-input-age'>Возвраст</label>
                        <b-form-input
                            id="inline-form-input-age"
                            class="mb-2 mr-sm-2 mb-sm-0"
                            v-model='select.age'
                            type='number'
                        ></b-form-input>
                    </b-form>
                </b-col>
                <b-col sm='4'>
                    
                </b-col>
            <b-row>

            </b-row>
        </b-container>
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
            filter: {
                species: {
                    name: 'Вид животного',
                    items: [],
                },
                breed: {
                    name: 'Порода',
                    items: [],
                },
                gender: {
                    nam: 'Пол',
                    items: [],
                },
            },
            select: {
                specie: null,
                gender: null,
                breed: null,
                age:null,
            },
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
                this.loadFilters();
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
        loadFilters() {
            for (let key in this.filter) {
                rest[key].get().then(res => {
                    this.filter[key].items = res.data.results;
                }).catch(err => {
                    console.error(err);
                });
            }
        },
        calcIndex (col, row) {
            return col - 1 + (row - 1) * this.countCol;
        },
    }
}
</script>