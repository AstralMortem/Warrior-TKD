<template>
<div class="relative z-[9999]" aria-labelledby="modal-title" role="dialog" aria-modal="true" v-show="show">

  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" ></div>

  <div class="fixed inset-0 z-10 w-screen">
    <div class="flex min-h-full items-center justify-center p-4 text-center sm:items-center sm:p-0" @click="show=false">
      <div class="bg-woodsmoke rounded-md min-w-max mt-5 py-5 px-5">
      <p class="font-title text-xl pb-5 text-alabaster-50">Рейтингова система</p>
      <UILoader v-if="pending"/>
      <div class="grid grid-cols-4 gap-5" v-else>
        <NuxtLink :to="`/belt/${belt.code}`" v-for="belt in belts" :key="belt.code">
          <img :src="belt.photo" class="w-[60px] h-[23.19px] lg:w-20 lg:h-[30.92px] opacity-60 hover:opacity-100 shadow cursor-pointer "/>
        </NuxtLink>
      </div>
    </div>
    </div>  
  </div>
</div>
</template>

<script setup lang="ts">

const show = defineModel({default:false})


const {data:belts,pending} = await useApiRequest('/api/account/belts/')

</script>