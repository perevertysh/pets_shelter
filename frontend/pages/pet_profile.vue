<template>
    <b-modal 
        id="profile-modal"
        title="Анкета"
        ok-only
        @ok='shelder()'
        ok-title='Приютить'
    >
        <b-card
            :title="item.name"
            :img-src="item.photo"
            img-alt="Image"
            img-top
            tag="article"
            class="mb-2"
            border-variant="light"
        >
            <b-card-text>
                Вид животного: {{species}}<br/>
                Порода: {{breed}}<br/>
                Возраст: {{item.age}}<br/>
                Регистрационный документ: {{doc}}<br/>
                Статус: {{item.status ? 'Приютили' : 'Не приютили'}}
            </b-card-text>
        </b-card>
    </b-modal>
</template>

<script>
import rest from './../js/rest';

export default {
    name: 'ProfilePet',
    props: {
        value: {
            type: Object,
            default: null,
        },
    },
    data: function() {
        return {
            item: {},
            species: null,
            breed: null,
            doc: null,
        };
    },
    watch: {
        value: {
            handler(val) {
                if (!val) {
                    this.item = {};
                    this.clear();
                    return;
                }
                this.$set(this, 'item', val);
                this.loadDetailInfo();
            },
            deep: true,
        },
    },
    methods: {
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
        clear() {
            this.species = null;
            this.breed = null;
            this.doc = null;
        }
    }
}
</script>