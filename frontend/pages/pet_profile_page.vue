<template>
    <b-container class="profile" v-if="item">
        <b-row>
            <b-col key='image' sm="4">
                <b-img :src='item.photo' fluid rounded/>
            </b-col>
            <b-col key='info'>
                <div>
                    Имя: {{item.name}}<br/>
                    Вид животного: {{item.species.name}}<br/>
                    Пол: {{item.gender.name}}<br/>
                    Порода: {{item.breed.name}}<br/>
                    Возраст: {{item.age + " " + make_word_end()}}<br/>
                    Регистрационный документ: {{item.doc.reg_num}}<br/>
                    Статус: {{!item.status ? 'Не приютили' : item.status.name}}
                </div>
                <b-button class="mt-3 btn" variant="primary" @click="shelter()">Приютить</b-button>
            </b-col>
        </b-row>
        <shelter-pet v-model="item"/>
    </b-container>
</template>

<script>
import rest from './../js/rest'
import functions from './js/functions'
import ShelterPet from './shelter_pet'

export default {
    name: 'ProfilePet',
    mixins: [
        functions,
    ],
    components: {
        ShelterPet,
    },
    data: function() {
        return {
            item: null,
        };
    },
    mounted: function() {
        this.loadData();
    },
    methods: {
        loadData() {
            rest.pet.get(this.$route.params['id']).then(res => {
                this.item = res.data;
            }).catch(err => {
                console.error(err);
                this.$router.go(-1);
            });
        },
    }
}
</script>