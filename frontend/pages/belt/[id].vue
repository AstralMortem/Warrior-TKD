<template>
  <div class="flex flex-col">
    <UILoader v-if="pending"/>
    <div class="flex flex-col md:px-20 lg:px-28 py-4" v-else>
      <div class="relative px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex">
        <div class="absolute top-2 left-2">
          <Icon name="material-symbols:chevron-left" size="3rem" class="bg-yellow bg-opacity-50 hover:ring-2 ring-yellow-800 p-1 rounded-full hover:bg-opacity-100 text-black cursor-pointer"
        @click="$router.go(-1)"/>
        </div>
        <img :src="data.photo" class="w-[172px] h-[67px] md:w-56 md:h-[87px] lg:w-[300px] lg:h-[116px]" >
        <p class="text-yellow font-semibold text-[25px] lg:text-4xl text-center font-title">{{ data.title }} ({{ data.code }})</p>
      </div>
      <div class="flex flex-col space-y-5" v-if="data.description">
        <p class="text-center text-yellow text-base lg:text-base font-normal font-title mt-5">Атестаційні нормативи</p>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.tul">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Тулі</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.tul}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.sparings">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Спаринги</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.sparings}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.kicks">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Удари</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.kicks}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.self_defence">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Самозахист</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.self_defence}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.spec_tech">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Спецтехніка</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.spec_tech}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.power_breaking">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Силове розбивання</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.power_breaking}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.ofp">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">ОФП</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.ofp}}</p>
        </div>

        <div class="mx-10 px-2.5 py-5 md:px-5 md:py-[30px] lg:px-[50px] lg:py-[30px] lg:gap-[30px] bg-woodsmoke rounded-[10px] md:rounded-[15px] shadow flex-col justify-start items-center gap-2.5 md:gap-5 inline-flex"
        v-if="data.description.theory">
          <p class=" text-yellow text-base lg:text-base font-normal font-title">Теорія</p>
          <p class=" text-silver text-base font-normal font-display leading-[25px]">{{  data.description.theory}}</p>
        </div>

        
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const route = useRoute()

const {data,pending} = await useApiRequest(`/api/account/belts/${route.params.id}`)


useHead({
    title: data.value?.title +" | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: data }
    ]
})

useSeoMeta({
  title:data.value?.title +" | TKD клуб ВОЇН",
  description: data
})

</script>

<style>


</style>

