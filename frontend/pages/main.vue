<template>
    <div>
        <b-navbar>
            <b-navbar-nav>
                <b-nav-form>
                    <b-button class="mx-2 header-btn" href='/app/about'>О нас</b-button>
                    <b-button class="mx-2 header-btn" href='/app/pets'>Питомцы</b-button>
                    <b-button class="mx-2 header-btn" href='/app/contact'>Контакты</b-button>
                </b-nav-form>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto mr-auto">
                <b-nav-text class="header-title">дом питомца</b-nav-text>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                    <b-form-input
                        v-model='search_str'
                        size="sm" 
                        class="mr-sm-2" 
                        type='search' 
                        placeholder="Найти питомца..."
                    />
                </b-nav-form>
            </b-navbar-nav>
        </b-navbar>
        <main class="main-content mt-2 mx-2">
            <router-view :search_str='search_str'/>
        </main>
    </div>    
</template>

<script>
export default {
    name: 'mainPage',
    data: function() {
        return {
            search_str: null,
        };
    },
}
</script>