<template>
    <div class='main'>
        <b-container fluid :style='{margin: 0}'>
            <b-row align-h="start">
                <b-col cols='2'>
                    <b-button
                        class="btn"
                        :class="{
                            select: select.status__code == 'out_home',
                        }"
                        @click="changeStatus('out_home')"
                    >Питомцы без дома</b-button>
                </b-col>
                <b-col cols='2'>
                    <b-button
                        class="btn"
                        :class="{
                            select: select.status__code == 'at_home',
                        }"
                        @click="changeStatus('at_home')"
                    >Счастливчики</b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col sm='8'>
                    <div class="filter-1">
                        <b-form inline  @reset="onReset">
                            <b-form inline v-for="(key, index) in filter_key" :key='index'>
                                <label 
                                    :for="'inline-form-input-' + key"
                                    :style="{
                                        'padding-right': '15px',
                                    }"
                                >{{filter[key].name}}</label>
                                <b-form-select
                                    :id="'inline-form-input-' + key"
                                    class="mb-2 mr-sm-2 mb-sm-0"
                                    v-model='select[key]'
                                    :value-field='filter[key].value_field'
                                    text-field='name'
                                    :options='filter[key].items'
                                ></b-form-select>
                            </b-form>
                            <b-form inline>
                                <label 
                                    for='inline-form-input-age'
                                    :style="{
                                        'padding-right': '15px',
                                    }"
                                >Возвраст</label>
                                <b-form-input
                                    id="inline-form-input-age"
                                    class="mb-2 mr-sm-2 mb-sm-0"
                                    v-model='select.age'
                                    type='number'
                                    :style="{
                                        width: '100px'
                                    }"
                                ></b-form-input>
                            </b-form>
                            <b-button type="reset" @click="onReset()">Сбросить</b-button>
                        </b-form>
                    </div>
                </b-col>
                <b-col sm='4'>
                    <div class="filter-1">
                        <b-form inline :style="{'justify-content': 'end'}">
                            <label
                                for="inline-form-input-sort"
                                :style="{
                                    'padding-right': '15px',
                                }"
                            >Сортировать по</label>
                            <b-form-select
                                id="inline-form-input-sort"
                                class="mb-2 mr-sm-4 mb-sm-0"
                                v-model='sortBy'
                                :options='optionsSort'
                            ></b-form-select>
                        </b-form>
                    </div>
                </b-col>
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
        <div v-else class="empty">
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
            sortBy: null,
            optionsSort: [
                {
                    value: 'species', text: 'Вид животного',
                },{
                    value: '-species', text: 'Вид животного (назад)',
                },{
                    value: 'age', text: 'Возраст',
                },{
                    value: '-age', text: 'Возраст (назад)',
                },{
                    value: 'name', text: 'Кличка',
                },{
                    value: '-name', text: 'Кличка (назад)',
                },{
                    value: 'gender', text: 'Пол',
                },{
                    value: '-gender', text: 'Пол (назад)',
                },{
                    value: 'breed', text: 'Порода',
                },{
                    value: '-breed', text: 'Порода (назад)',
                },{
                    value: 'doc', text: 'Регистрационный номер',
                },{
                    value: '-doc', text: 'Регистрационный номер (назад)',
                },{
                    value: 'status', text: 'Статус',
                },{
                    value: '-status', text: 'Статус (назад)',
                }
            ],
            filter_key: ['species', 'breed', 'gender'],
            filter: {
                species: {
                    name: 'Вид животного',
                    items: [],
                    value_field: 'name'
                },
                breed: {
                    name: 'Порода',
                    items: [],
                    value_field: 'code'
                },
                gender: {
                    name: 'Пол',
                    items: [],
                    value_field: 'code'
                },
            },
            select: {
                specie: null,
                gender: null,
                breed: null,
                age: null,
                status__code: null,
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
        sortBy (val, oldval) {
            this.fetch();
        },
        select: {
            handler() {
                this.fetch();
            },
            deep: true,
        }
    },
    mounted: function() {
        this.fetch();
        this.loadFilters();
    },
    methods: {
        fetch() {
            // name=
            // age=
            // species__name=
            // breed__code=
            // gender_code=
            // status__code=
            // ordering=
            let query = {page: this.curPage, page_size: this.perPage, ordering: this.sortBy};
            for (let key in this.filter) {
                let item = this.filter[key];
                query[key + '__' + item.value_field] = this.select[key];
            }
            query.age = this.select.age;
            query.status__code = this.select.status__code;
            rest[this.model].get(query).then(res => {
                if (res.data) {
                    this.items = res.data.results;
                    this.totalRows = res.data.count;
                }
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
        onReset() {
            for (let key in this.filter) {
                this.select[key] = null;
            }
            this.select.age = null;
        },
        changeStatus(status) {
            if (this.select.status__code == status) {
                this.select.status__code = null;
                return;
            }
            this.select.status__code = status;
        },
        calcIndex (col, row) {
            return col - 1 + (row - 1) * this.countCol;
        },
    }
}
</script>