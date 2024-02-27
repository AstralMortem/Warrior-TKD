<template>
    <div>
        <UIModalBelt v-model="show_enc"/>
        <NavBar v-on:showEncyclopedia="show_enc=true"/>
        <PageUp/>
            <Wrapper>
                <slot/>
            </Wrapper>
        <Footer class="mt-4" v-on:showEncyclopedia="show_enc=true"/>
    </div>
</template>

<script setup>

const show_enc = ref(false)

</script>