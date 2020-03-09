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
            <b-row v-for="field in fields" :key="field.key">
                <b-col cols='4' class="right">field.name</b-col>
                <b-col cols='8' class="left">
                    <b-form-input
                        :id='"input-" + field.field'
                        v-model="item[field.field]"
                        :state="errorHas(field.field)"
                        :aria-describedby='"input-" + field.field + "-feedback"'
                        type='text'
                        :placeholder="field.placeholder"
                    />
                    <b-form-invalid-feedback :id='"input-" + field.field + "-feedback"' v-if="error[field.field]">
                        {{error[field.field][0]}}
                    </b-form-invalid-feedback>
                </b-col>
            </b-row>
            <b-row>
                <b-col >Комментарий</b-col>
            </b-row>
            <b-row>
                <b-col >
                    <b-form-textarea
                        id="input-comment"
                        v-model="item.comment"
                        :state="errorHas('comment')"
                        aria-describedby="input-comment-feedback"
                        placeholder="Оставьте комментарий"
                        rows='6'
                    />
                    <b-form-invalid-feedback id="input-comment-feedback" v-if="error.comment">
                        {{error.comment[0]}}
                    </b-form-invalid-feedback>
                </b-col>
            </b-row>
            <b-row class="actions">
                <b-col class="left">
                    <b-button
                        class="btn cancel"
                        @click="onReset()"
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
            error: {},
            fields: [
                { field: 'firstname', key: 'fn', name: 'Имя', placeholder: 'Введите имя' },
                { field: 'lastname', key: 'ln', name: 'Фамилия', placeholder: 'Введите фамилию' },
                { field: 'middlename', key: 'mn', name: 'Отчество', placeholder: 'Введите отчество' },
                { field: 'phone_num', key: 'pn', name: 'Телефон', placeholder: '+7 ваш номер' },
                { field: 'email', key: 'em', name: 'E-mail', placeholder: 'your@email.com' },
            ],
        };
    },
    watch: {
        value: {
            handler(val) {
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
                if (err.response.data) {
                    this.$set(this, 'error', err.response.data);
                }
                console.error(err);
            });
        },
        onReset() {
            this.error = {};
            this.$bvModal.hide('shelter-modal');
        },
        errorHas(field) {
            if (JSON.stringify(this.error) === JSON.stringify({})) {
                return null;
            }
            console.log(this.error[field] ? false : true);
            return this.error[field] ? false : true;
        },
    }
}
</script>