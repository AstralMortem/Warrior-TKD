<template>
    <div>
        <Transition>
            <UIModalBelt v-model="show_enc"/>
        </Transition>
        
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

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>