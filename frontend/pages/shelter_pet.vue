<template>
    <b-modal 
        id="shelter-modal"
        title="Заявка"
        @ok="submit()"
        ok-only
        ok-title='Отправить'
    >
        <b-form>
            <b-form-group
                label='Животное:'
            >
                <b-form-input
                    v-model="animal.name"
                    type='text'
                    disabled
                />
            </b-form-group>
            <b-form-group
                label='Фамилия:'
            >
                <b-form-input
                    v-model="item.lastname"
                    type='text'
                    placeholder="Введите фамилию"
                />
            </b-form-group>
            <b-form-group
                label='Имя:'
            >
                <b-form-input
                    v-model="item.firstname"
                    type='text'
                    placeholder="Введите имя"
                />
            </b-form-group>
            <b-form-group
                label='Отчество:'
            >
                <b-form-input
                    v-model="item.middlename"
                    type='text'
                    placeholder="Введите отчество"
                />
            </b-form-group>
            <b-form-group
                label='Телефон:'
            >
                <b-form-input
                    v-model="item.phone_num"
                    type='tel'
                    placeholder="Введите номер телефона"
                />
            </b-form-group>
            <b-form-group
                label='E-mail:'
            >
                <b-form-input
                    v-model="item.email"
                    type='email'
                    placeholder="Введите номер телефона"
                />
            </b-form-group>
            <b-form-group
                label='Комментарий:'
            >
                <b-form-textarea
                    v-model="item.comment"
                    placeholder="Оставьте комментарий"
                    rows='3'
                />
            </b-form-group>
        </b-form>
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
                this.$set(this, 'item', {pet: this.value.id});
                this.$set(this, 'animal', this.value);
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