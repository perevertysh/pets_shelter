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
                    Порода: {{breed}}<br/>
                    Возраст: {{item.age + " " + make_word_end()}}<br/>
                    Регистрационный документ: {{doc}}<br/>
                    Статус: {{item.status ? 'Приютили' : 'Не приютили'}}
                </div>
                <b-button class="mt-3" variant="primary" @click="shelder()">Приютить</b-button>
            </b-col>
        </b-row>
        <shelter-pet v-model="item"/>
    </b-container>
</template>

<script>
import rest from './../js/rest'
import ShelterPet from './shelter_pet'
import PetCard from './pet_card'

export default {
    name: 'ProfilePet',
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
            rest.pet.get(this.$route.params['id']).then(res => {
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
        shelder() {
            this.$bvModal.show('shelter-modal');
        },
        make_word_end() {
            let word = "лет";
            let n = this.item.age;
            if (n > 99)
                n = n % 100;
            if (4 < n && n < 21)
                word = "лет";
            else if (n % 10 == 1)
                word = "год";
            else if (1 < n % 10 &&  n % 10 < 5)
                word = "года";
            return word;
        },
        clear() {
            this.species = null;
            this.breed = null;
            this.doc = null;
        },
    }
}
</script>