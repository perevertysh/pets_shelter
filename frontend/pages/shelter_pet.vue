<template>
    <b-modal 
        id="shelter-modal"
        size='lg'
        hide-footer
        hide-header
    >
        <b-container fluid class="request">
            <b-row class="header">
                <b-col :style="{'text-align': 'center'}">
                    <span>приютить питомца?!</span>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols='4' class="right">Имя</b-col>
                <b-col cols='8' class="left">
                    <b-form-input
                        v-model="item.firstname"
                        type='text'
                        placeholder="Введите имя"
                    />
                </b-col>
            </b-row>
            <b-row>
                <b-col cols='4' class="right">Фамилия</b-col>
                <b-col cols='8' class="left">
                    <b-form-input
                        v-model="item.lastname"
                        type='text'
                        placeholder="Введите фамилию"
                    />
                </b-col>
            </b-row>
            <b-row>
                <b-col cols='4' class="right">Отчество</b-col>
                <b-col cols='8' class="left">
                    <b-form-input
                        v-model="item.middlename"
                        type='text'
                        placeholder="Введите отчество"
                    />
                </b-col>
            </b-row>
            <b-row>
                <b-col cols='4' class="right">Телефон</b-col>
                <b-col cols='8' class="left">
                    <b-form-input
                        v-model="item.phone_num"
                        type='tel'
                        placeholder="Введите номер телефона"
                    />
                </b-col>
            </b-row>
            <b-row>
                <b-col cols='4' class="right">E-mail</b-col>
                <b-col cols='8' class="left">
                    <b-form-input
                        v-model="item.email"
                        placeholder="Введите электронный адрес"
                    />
                </b-col>
            </b-row>
            <b-row>
                <b-col >Комментарий</b-col>
            </b-row>
            <b-row>
                <b-col >
                    <b-form-textarea
                        v-model="item.comment"
                        placeholder="Оставьте комментарий"
                        rows='6'
                    />
                </b-col>
            </b-row>
            <b-row class="actions">
                <b-col class="left">
                    <b-button
                        class="btn cancel"
                        @click="$bvModal.hide('shelter-modal')"
                    >Нет</b-button>
                </b-col>
                <b-col class="right">
                    <b-button
                        class="btn success"
                        @click="submit()"
                    >Да!</b-button>
                </b-col>
            </b-row>
        </b-container>
    </b-modal>
</template>

<script>
import rest from './../js/rest'

export default {
    name: 'ShelterPet',
    props: {
        value: {
            type: Object,
            default: null,
        },
    },
    data: function () {
        return {
            item: {},
            animal: {},
        };
    },
    watch: {
        value: {
            handler(val) {
                console.log(val);
                this.$set(this, 'item', {pet: val ? val.id : val});
                this.$set(this, 'animal', val);
            },
            deep: true,
        }
    },
    mounted: function() {
        if (this.value) {
            this.$set(this, 'item', {pet: this.value.id});
            this.$set(this, 'animal', this.value);
        }
    },
    methods: {
        submit() {
            rest.pet_shelter_req.post(this.item).then(res =>{
            }).catch(err => {
                console.error(err);
            });
        },
    }
}
</script>