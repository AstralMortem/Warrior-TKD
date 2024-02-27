<template>
  <div class="flex flex-col gap-y-2">
    <section id="home">
            <div class="flex flex-col-reverse md:flex-row justify-center md:justify-evenly items-center">
                <div class="inline-flex flex-col items-center md:items-end px-4 text-center md:text-right">
                    <p class="font-title lg:text-4xl text-[25px] text-yellow font-semibold pb-5">Спортивний клуб "Воїн"</p>
                    <p class="font-title lg:text-xl text-base text-alabaster-50 font-normal pb-5" >Виховання духу</p>
                    <p class="font-title lg:text-xl text-base text-alabaster-50 font-normal pb-5">Дисципліна</p>
                    <p class="font-title lg:text-xl text-base text-alabaster-50 font-normal pb-5">Формування характеру</p>
                </div>
                <div class=" w-[328px] h-[340px] md:w-[809px] md:h-[798px]">
                    <img src="/img/background.jpg" class="filter backdrop-blur-md object-cover rounded-lg md:rounded-full">
                </div>
            </div>
    </section>
    <section id="news">
            <div class="flex flex-col justify-center items-center gap-6 mt-2">
                <p class="text-[25px] lg:text-4xl font-title text-yellow font-semibold ">Останні новини</p>
                <UILoader v-if="pending"/>
                <Swiper v-else 
                
                :modules="[SwiperEffectCreative, Autoplay, Pagination, Navigation]"
                :centeredSlides="true"
                :slidesPerView="2"
                :spaceBetween="50"
                :loop="true"
                :autoplay="{
                    delay: 4000,
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
                    <SwiperSlide v-for="news in data?.news" :key="news.id" >
                        <UISmallNewsCard 
                        :id="news.id"
                        :news_images="news.news_images"
                        :title="news.title"
                        :text="news.text"
                        :created_at="news.created_at"
                        />
                    </SwiperSlide>
                </Swiper>
                
                <UIButton href="/news">Всі новини</UIButton>
            </div>
    </section>
    <section id="participants" >
            <div class="flex py-3 lg:py-5 flex-col justify-center items-center gap-5  ">
                <p class="lg:text-4xl text-[25px] text-yellow font-title">Наші тренери</p>
                <div class="grid grid-cols-2 md:grid-cols-2 gap-4 md:gap-6 lg:gap-[106px] items-center">
                    <UILoader v-if="pending"/>
                    <UIUserCard v-for="coach in data?.coaches"
                    :full_name="coach.full_name"
                    :belt="coach.belt"
                    :id="coach.id"
                    :mobile="coach.mobile"
                    :photo="coach.photo"
                    v-else/>
                    
                </div>
                <p class="lg:text-4xl text-[25px] text-yellow font-title">Наші учасники</p>
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 md:gap-6 lg:gap-[106px] items-center">
                    <UILoader v-if="pending"/>
                    <UIUserCard v-for="user in data?.participants" 
                    :full_name="user.full_name"
                    :belt="user.belt"
                    :id="user.id"
                    :photo="user.photo"
                    v-else/>
                </div>
                <UIButton href="/participants">Всі учасники</UIButton>
            </div>
    </section>
    <section id="map" >
            <div class="flex flex-col items-center py-2.5 gap-2.5 md:gap-10 md:px-6 md:pt-5 lg:pt-10 lg:pb-[120px] lg:gap-[50px]">
                <p class="text-yellow text-[25px] font-semibold font-title lg:text-4xl">Наші зали</p>
                <div class="inline-flex flex-col-reverse md:flex-row md:gap-[100px] lg:gap-[100px] items-center lg:items-start">
                    <div class="flex flex-col lg:flex-row mt-4 md:mt-0 gap-5" >
                        <UILoader v-if="pending"/>
                        <UILocationCard v-for="gym in data?.gyms" 
                        :address="gym.address"
                        :calendar="gym.calendar"
                        :email="gym.email"
                        :phone="gym.phone"
                        :time="gym.time"
                        :title="gym.title"
                        v-else/>
                    </div>
                    <div class=" w-[300px] h-[300px] md:h-[500px] md:w-[500px] rounded-[20px] bg-yellow overflow-clip">
                        <LMap ref="map" :zoom="zoom" :center="[50.3405,31.2599]" class="rounded-lg">
                            <LTileLayer class="rounded-lg"
                                url="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
                                attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors"
                                layer-type="base"
                                name="OpenStreetMap"
                            />
                            <LMarker :latLng="gym.location.split(',')" v-for="gym in data?.gyms"/>
                        </LMap>
                    </div>
                </div>
            </div>
    </section>

  </div>
</template>

<script lang="ts" setup>
import {Autoplay, Pagination, Navigation} from 'swiper/modules'

const {data,pending} = await useAsyncData('main-page', async ()=>{
    const [{data:news_value},{data:coaches_value},{data:participants_value},{data:gyms_value}] = await Promise.all([
        useBaseFetch('/api/news/',{query:{
            "limit": "5"
        }}),
        useBaseFetch('/api/account/users/',{query:{
            "is_staff": true,
            "limit": "3"
        }}),
        useBaseFetch('/api/account/users/',{query:{
            "is_staff": false,
            "limit": "5"
        }}),
        useBaseFetch('/api/gyms/',{query:{
            "limit": "2"
        }})
    ])
    
    const news = news_value.value.results;
    const coaches = coaches_value.value.results;
    const participants = participants_value.value.results;
    const gyms = gyms_value.value.results;

    return {
        news,
        coaches,
        participants,
        gyms
    }
})



const zoom = ref(10)

useHead({
    title: "Головна | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: "Спортивний клуб Taekwon-do ВОЇН, Виховання духу, Дисципліна, Формування характеру" }
    ]
})

useSeoMeta({
  title:"Головна | TKD клуб ВОЇН",
  description: data
})

</script>

<style scoped>
.swiper-pagination-bullet{
    margin-top: 25px !important;
}
</style>