<template>
  <div>
    <UILoader v-if="pending"/>
    <div class="flex flex-col px-4 md:px-[74px] lg:px-[200px] gap-3" v-else>

      <div class="bg-woodsmoke rounded-[10px] md:rounded-[30px] p-3 md:p-5 lg:px-[30px] lg:py-[50px] relative">
        <div class="absolute top-2 left-2">
          <Icon name="material-symbols:chevron-left" size="3rem"
            class="bg-yellow bg-opacity-50 hover:ring-2 ring-yellow-800 p-1 rounded-full hover:bg-opacity-100 text-black cursor-pointer"
            @click="$router.go(-1)" />
        </div>
        <div class="flex flex-col md:flex-row-reverse items-center md:justify-between mt-2">

          <img :src="user.photo" class="w-[230px] h-[230px] rounded-full lg:w-[350px] lg:h-[350px] shadow" v-if="user.photo"/>
          <img src="/img/no_photo.png" class="w-[230px] h-[230px] rounded-full lg:w-[350px] lg:h-[350px] shadow" v-else/>

          <div class="flex-col inline-flex  gap-4">
            <div class="flex flex-col gap-[9px] md:gap-[15px] ">
              <p class="text-yellow text-[25px] lg:text-4xl font-semibold font-title text-center md:text-left">{{
                user.full_name }}</p>
              <div class="flex flex-col justify-center gap-2 items-center">
                <img :src="user.belt.photo" class="w-fit h-10"/>
                <p class="text-base font-normal font-title text-silver text-center md:text-left">{{ user.belt.title }}</p>
              </div>

              <p class="text-base font-normal font-title text-silver text-center md:text-left" v-if="user.coach_type">{{
                getEnumType(user.coach_type, COACH_TYPE) }}</p>
              <p class="text-base font-normal font-title text-silver text-center md:text-left" v-if="user.judge_type">{{
                getEnumType(user.judge_type, JUDGE_TYPE) }}</p>
              
              
            </div>
            <div class="flex flex-col gap-[9px] md:gap-[15px]">
              <p class="text-base font-normal font-title text-silver text-center md:text-left">Дата народження: {{
                user.birthday }}</p>
              <p class="text-base font-normal font-title text-silver text-center md:text-left" v-if="user.itf_code">Карта
                учасника:
                <NuxtLink :to="`/participants/${user.itf_link}`" class=" underline">
                  {{ user.itf_code }}
                </NuxtLink>
              </p>
              <p class="text-base font-normal font-title text-silver text-center md:text-left" v-if="user.coach">Тренер:
                <NuxtLink :to="`/participants/${user.coach.id}`" class=" underline">
                  {{ user.coach.full_name }}
                </NuxtLink>
              </p>
            </div>

          </div>

        </div>

        <div class="flex flex-col lg:flex-row gap-4 mt-2 justify-evenly">
          <div class="flex flex-col space-y-3 p-4 rounded-lg ring-1 ring-yellow shadow-md shadow-yellow" v-if="user.mobile">
            <p class="text-base lg:text-xl text-yellow font-title">Телефон</p>
            <p class="text-base lg:text-xl text-alabaster font-title">{{user.mobile}}</p>
          </div>
          <div class="flex flex-col space-y-3 p-4 rounded-lg ring-1 ring-yellow shadow-md shadow-yellow" v-if="user.email">
            <p class="text-base lg:text-xl text-yellow font-title">Пошта</p>
            <p class="text-base lg:text-xl text-alabaster font-title">{{user.email}}</p>
          </div>
          <div class="flex flex-col space-y-3 p-4 rounded-lg ring-1 ring-yellow shadow-md shadow-yellow" v-if="user.links.length>0">
            <p class="text-base lg:text-xl text-yellow font-title">Соцмережі</p>
            <div class="flex flex-row gap-1">
              <NuxtLink v-for="link in user.links" :to="link">
                <img :src="fetchIcon(link)" class="w-10 h-10">
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
      <div class="flex flex-col gap-3 justify-evenly">
        <UICollapse :results="user.competitions" v-if="user.competitions.length>0">Спортивний досвід</UICollapse>
        <UICollapse :results="user.judgments" v-if="user.judgments.length>0">Судійський досвід</UICollapse>
        <UICollapse :results="user.attestations" v-if="user.attestations.length>0">Aтестації</UICollapse>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

import {COACH_TYPE,JUDGE_TYPE} from '~/types/enums'

function convertDate(data_string: string) {
  const d = new Date(data_string)
  return d.toLocaleDateString()
}
const route = useRoute()

const { data: user, pending } = await useApiRequest('/api/account/users/' + route.params.id)

function getEnumType(key:string, dict:Object){
  return dict[key]
}

const fetchIcon = (url:string) =>{
  const base ="https://s2.googleusercontent.com/s2/favicons?domain="
  const uri = new URL(url).hostname
  return base + uri
} 
useHead({
    title: user.value.full_name +" | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: user }
    ]
})

useSeoMeta({
  title: user.value?.full_name +" | TKD клуб ВОЇН" ,
  description:user
})



</script>