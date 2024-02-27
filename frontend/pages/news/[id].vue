<template>
  <div>
    <UiLoader v-if="pending"/>
    <div class="flex flex-col gap-4 mb-4" v-else>
    <div class="flex flex-row justify-center md:justify-start items-center gap-4 px-4">
      <Icon name="material-symbols:chevron-left" size="3rem" class="bg-yellow bg-opacity-50 hover:ring-2 ring-yellow-800 p-1 rounded-full hover:bg-opacity-100 text-black cursor-pointer"
        @click="$router.go(-1)"/>
      <p class="text-yellow font-semibold font-title text-[25px] lg:text-4xl">{{ data.title }}</p>
    </div>
    <div class="flex flex-col gap-3 md:gap-5 px-2 md:px-16 lg:px-60">
      <p class="text-base lg:text-xl font-display text-alabaster" v-html="data.text"/>
      <p class="text-sm md:text-base text-silver font-display text-left">{{ convertDate(data.created_at) }}</p>
      <Swiper  class="ring-2 ring-yellow p-4 rounded-lg" v-if="data.news_images"
                :modules="[SwiperEffectCreative, Autoplay, Pagination, Navigation]"
                :centeredSlides="true"
                :slidesPerView="2"
                :spaceBetween="50"
                :loop="true"
                :autoplay="{
                    delay: 5000,
                    disableOnInteraction: false,
                }"
                :pagination="{
                    clickable: true,
                }"
                :navigation="true"
                :grabCursor="true"
                :effect="'creative'"
                :breakpoints="{
                '@0.00': {
                    slidesPerView: 1,
                    spaceBetween: 10,
                },
                '@0.75': {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                '@1.00': {
                    slidesPerView: 2,
                    spaceBetween: 50,
                },
                }"
                :creativeEffect="{
                prev: {
                    shadow: true,
                    translate: ['-120%', 0, -500],
                    opacity: 0.10,
                },
                next: {
                    shadow: true,
                    translate: ['120%', 0, -500],
                    opacity: 0.10,
                },}">
                    <SwiperSlide v-for="(news_photo,index) in data.news_images" :key="index"  >
                      <img :src="news_photo" class="rounded-lg w-75 h-75 "/>
                    </SwiperSlide>
                </Swiper>
    </div>
    </div>
  </div>
  
</template>

<script lang="ts" setup>

import {Autoplay, Pagination, Navigation} from 'swiper/modules';

const route = useRoute()

const {data,pending} = await useApiRequest(`/api/news/${route.params.id}`)


function convertDate(date_string:string){
    const d = new Date(date_string)
    return d.toLocaleDateString() 
  }

  useHead({
    title: "Новини | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: data }
    ]
})

useSeoMeta({
  title: data.value?.full_name +" | TKD клуб ВОЇН",
  description: data
})
  

</script>

<style scoped>
.swiper-pagination-bullet{
    margin-top: 25px !important;
}
</style>