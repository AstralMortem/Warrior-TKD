<template>
  <div class="flex flex-col p-4 gap-4 bg-woodsmoke rounded-lg ">
      <div class="flex flex-col gap-2 ring-1 ring-yellow rounded-lg p-4">
          <div class="flex flex-col md:flex-row justify-evenly">
            <p class="text-base font-title lg:text-xl text-yellow">{{ props.title }}</p>
            <p class="text-sm md:text-base text-silver font-display ">{{ convertDate(props.created_at) }}</p>
          </div>

          <div class="flex flex-wrap">
            <p class="text-base lg:text-xl font-display text-alabaster line-clamp-5" v-html="props.text">
            </p>
          </div>
      </div>
      <div class="slider rounded-lg p-4 ring-1 ring-yellow h-max" v-if="props.news_images.length >0">
        <Swiper class="max-w-[360px]" 
        :modules="[Autoplay, Pagination, Navigation]"
                  :centeredSlides="true"
                  :navigation="false"
                  :slidesPerView="1"
                  :spaceBetween="10"
                  :loop="true"
                  :autoplay="{
                      delay: 2000,
                      disableOnInteraction: false,
                  }"
                  :pagination="{
                      clickable: true,
                  }"
                  :grabCursor="true">
          <SwiperSlide v-for="news_photo in props.news_images"  >
            <img :src="news_photo" class="rounded-lg w-fit "/>
          </SwiperSlide>
        </Swiper>
      </div>
      <UIButton @click="router.push({path:`/news/${props.id}`})">Читати</UIButton>
  </div>
</template>

<script setup lang="ts">
const router = useRouter()
import { Pagination,Autoplay,Navigation} from 'swiper/modules';
import { type INews } from '~/types/db';

const props = defineProps<INews>()

const convertDate = (date:string) =>{
  return new Date(date).toLocaleDateString()
}

</script>

