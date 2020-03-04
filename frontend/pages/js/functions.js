export default {
    methods: {
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
        shelter() {
            this.$bvModal.show('shelter-modal');
        },
    },
}