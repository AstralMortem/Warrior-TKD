


<template>
<NuxtLink class="cursor-pointer font-title text-base lg:text-xl group text-alabaster transition-all duration-300 ease-in-out" :to="{path: path, hash: hash}">
  <span class="font-title cursor-pointer text-base lg:text-xl bg-left-bottom bg-gradient-to-r from-alabaster to-alabaster bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-in-out">
    <slot/>
  </span>
</NuxtLink>
</template>

<script setup>


defineProps({
    'path':{
        default: '/'
    },
    'hash': {
        default: null
    }
});

</script>