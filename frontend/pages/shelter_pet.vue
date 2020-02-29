<template>
    <b-modal 
        id="shelter-modal"
        title="Заявка"
        @hidden='reset()'
        @ok="submit()"
    >
        <b-form>
            <b-form-group
                label='Животное:'
            >
                <b-form-input
                    v-model="animal.name"
                    disabled
                />
            </b-form-group>
            <b-form-group
                label='Фамилия:'
            >
                <b-form-input
                    v-model="item.lastname"
                    placeholder="Введите фамилию"
                />
            </b-form-group>
            <b-form-group
                label='Имя:'
            >
                <b-form-input
                    v-model="item.firstname"
                    placeholder="Введите имя"
                />
            </b-form-group>
            <b-form-group
                label='Отчество:'
            >
                <b-form-input
                    v-model="item.middlename"
                    placeholder="Введите отчество"
                />
            </b-form-group>
            <b-form-group
                label='Телефон:'
            >
                <b-form-input
                    v-model="item.phone_num"
                    placeholder="Введите номер телефона"
                />
            </b-form-group>
            <b-form-group
                label='Комментарий:'
            >
                <b-form-input
                    v-model="item.comment"
                    placeholder="Оставьте комментарий"
                />
            </b-form-group>
        </b-form>
    </b-modal>
</template>

<script>
import rest from './../js/rest';

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
            modalShelter: false,
        };
    },
    watch: {
        value: {
            handler(val) {
                if (!val) {
                    this.item = {};
                    this.animal = {};
                    return;
                }
                this.$bvModal.show('shelter-modal');
                this.$set(this, 'item', {pet: val.id});
                this.$set(this, 'animal', val);
            },
            deep: true,
        },
    },
    methods: {
        submit() {
            rest.pet_shelter_req.post(this.item).then(res => {

            }).catch(err => {
                console.error(err);
            });
        },
        reset() {
            this.$emit('input', null);
        }
    }
}
</script>