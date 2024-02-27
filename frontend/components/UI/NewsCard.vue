<template>
  <div class="flex flex-col space-y-3">
  <div class="flex flex-col-reverse md:flex-row space-x-4">
    <div class="slider rounded-lg p-4 ring-1 ring-yellow" v-if="props.news_images.length>0">
        <Swiper class="max-w-[360px] "
                  :modules="[Autoplay, Pagination, Navigation]"
                  :centeredSlides="true"
                  :navigation="true"
                  :slidesPerView="1"
                  :spaceBetween="10"
                  :loop="true"
                  :autoplay="{
                      delay: 5000,
                      disableOnInteraction: false,
                  }"
                  :pagination="{
                      clickable: true,
                  }"
                  :grabCursor="true">
                    <SwiperSlide v-for="news_photo in props.news_images"  >
                      <img :src="news_photo" class="rounded-lg w-fit h-fit"/>
                    </SwiperSlide>
                  </Swiper>
    </div>
    <div class="flex flex-col">
          <p class="text-base text-yellow font-title lg:text-xl">{{ props.title }}</p>
          <div class="flex flex-wrap">
              <p class="text-base lg:text-xl font-display text-alabaster line-clamp-5" v-html="props.text"></p>
          </div>
          <p class="text-sm md:text-base text-silver font-display">{{ convertDate(props.created_at) }}</p>
          <UIButton class="mt-4 self-center" @click="router.push({path:`/news/${props.id}`})">Більше...</UIButton>
    </div>
  </div>
  <hr/>
  </div>
</template>

<script setup lang="ts">
const router = useRouter()
import { Pagination,Autoplay, Navigation} from 'swiper/modules';
import {type INews} from '~/types/db'

const props = defineProps<INews>()

function convertDate(date_string:string){
    const d = new Date(date_string)
    return d.toLocaleDateString()
  }
</script>

