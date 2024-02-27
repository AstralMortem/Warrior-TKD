<template>
  <div class="flex flex-col gap-4">
    <div class="flex flex-row justify-center md:justify-start items-center gap-4 px-4">
    <Icon name="material-symbols:chevron-left" size="3rem" class="bg-yellow bg-opacity-50 hover:ring-2 ring-yellow-800 p-1 rounded-full hover:bg-opacity-100 text-black cursor-pointer"
      @click="$router.go(-1)"/>
    <p class="text-yellow font-semibold font-title text-[25px] lg:text-4xl">Всі новини</p>
    </div>
    <div class="flex flex-col gap-3 md:gap-5 px-2 md:px-16 lg:px-60">
      <UINewsCard v-for="item in news" 
        :id="item.id"
        :text="item.text"
        :title="item.title"
        :news_images="item.news_images"
        :created_at="item.created_at"
      />
    </div>
    <div class="flex justify-center items-center">
      <UILoader v-if="pending"/>
      <UIButton @click="newsStore.fetchNext()" v-else >Завантажити ще</UIButton>
    </div>
    
  </div>
  
  
</template>

<script lang="ts" setup>

const newsStore = useNewsStore()
const {news,pending} = storeToRefs(newsStore) 

onMounted(()=>{
  newsStore.initStore()
})


useHead({
    title: "Новини | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: "Новини спортивного клубу Taekwon-do ВОЇН" }
    ]
})

useSeoMeta({
  title:"Новини | TKD клуб ВОЇН",
  description: news
})



</script>

<style>

</style>