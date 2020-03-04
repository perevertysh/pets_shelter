<template>
    <b-container>
        <b-row>
            <b-col key='image' sm="4">
                <pet-card 
                    :item="item"
                    :size='360'
                    read-only
                />
            </b-col>
            <b-col key='info'>
                <div>
                    Вид животного: {{species}}<br/>
                    Пол: {{item.sex}}<br/>
                    Порода: {{breed}}<br/>
                    Возраст: {{item.age + " " + make_word_end()}}<br/>
                    Регистрационный документ: {{doc}}<br/>
                    Статус: {{item.status ? 'Приютили' : 'Не приютили'}}
                </div>
                <b-button class="mt-3" variant="primary" @click="shelter()">Приютить</b-button>
            </b-col>
        </b-row>
        <shelter-pet v-model="item"/>
    </b-container>
</template>

<script>
import rest from './../js/rest'
import functions from './js/functions'
import ShelterPet from './shelter_pet'
import PetCard from './pet_card'

export default {
    name: 'ProfilePet',
    mixins: [
        functions,
    ],
    components: {
        ShelterPet,
        PetCard,
    },
    data: function() {
        return {
            item: {},
            species: null,
            breed: null,
            doc: null,
        };
    },
    mounted: function() {
        this.loadData();
    },
    methods: {
        loadData() {
            rest.petslist.get(this.$route.params['id']).then(res => {
                this.item = res.data;
                this.loadDetailInfo();
            }).catch(err => {
                console.error(err);
                this.$router.go(-1);
            });
        },
        loadDetailInfo() {
            this.clear();
            rest.breed.get(this.item.breed).then(res => {
                this.breed = res.data.name;
            }).catch(err => console.error(err));
            rest.species.get(this.item.species).then(res => {
                this.species = res.data.name;
            }).catch(err => console.error(err));
            rest.doc.get(this.  item.doc).then(res => {
                this.doc = res.data.reg_num;
            }).catch(err => console.error(err));
        },
        clear() {
            this.species = null;
            this.breed = null;
            this.doc = null;
        },
    }
}
</script>