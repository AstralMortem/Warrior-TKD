<template>
  <div class="flex flex-row gap-5 md:gap-8 px-4 py-4 md:px-16 lg:px-[209px] items-center justify-between hover:bg-yellow hover:text-black text-yellow cursor-pointer rounded-lg mx-2"
  @click="$router.push({path:`/participants/${props.id}`})">
    <div class="flex flex-row gap-4 lg:gap-8">
      <UIUserAvatar :src="props.photo"/>
      <div class="flex flex-col gap-4">
        <p class="text-base  font-title inline-flex flex-wrap">{{ props.full_name }}</p>
        <p class="text-base text-alabaster font-title" v-show="props.mobile">{{ props.mobile }}</p>
      </div>
    </div>
    <img :src="props.belt.photo" alt="belt" class="w-16 h-[24.87px] md:w-[100px] md:h-[38.85px] lg:w-[110px] lg:h-[42.74px]">
  </div>

</template>

<script lang="ts" setup>
import {type IUserSmall} from '~/types/db'
const props = defineProps<IUserSmall>()

</script>

<style>

</style>