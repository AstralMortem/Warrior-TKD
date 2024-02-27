<template>
    <img :src="props.src" class="w-16 h-16 rounded-full md:w-[100px] md:h-[100px] lg:w-[110px] lg:h-[110px]" v-if="props.src">
    <img src="/img/no_photo.png" class="w-16 h-16 rounded-full md:w-[100px] md:h-[100px] lg:w-[110px] lg:h-[110px]" v-else/>
</template>

<script setup>
    const props = defineProps(['src'])
</script>