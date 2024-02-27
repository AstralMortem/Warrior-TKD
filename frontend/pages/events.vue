<template>
  <div class="flex flex-col gap-4">
    <div class="flex flex-row justify-center md:justify-start items-center gap-4 px-4">
      <Icon name="material-symbols:chevron-left" size="3rem" class="bg-yellow bg-opacity-50 hover:ring-2 ring-yellow-800 p-1 rounded-full hover:bg-opacity-100 text-black cursor-pointer"
        @click="$router.go(-1)"/>
      <p class="text-yellow font-semibold font-title text-[25px] lg:text-4xl">Найближчі заходи</p>
    </div>
    <div class="flex flex-col px-4 md:px-20 lg:px-28 space-y-3">
      <UIEventCard v-for="event in competitions" :key="event.id" 
        :id="event.id"
        :title="event.title"
        :place="event.place"
        :date="event.date"
        :total_medals="event.total_medals"
        :is_completed="event.is_completed"
      />
    </div>
    <div class="flex justify-center items-center">
      <UILoader v-if="pending"/>
      <UIButton  @click="competitionStore.fetchNext()" v-else>Завантажити ще...</UIButton>
    </div>
  </div>
</template>

<script lang="ts" setup>
const competitionStore = useCompetitionsStore()
const {competitions,pending} = storeToRefs(competitionStore)

onMounted(()=>{
  competitionStore.initStore()
})

useHead({
    title: "Змагання | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: competitions }
    ]
})


</script>

<style>

</style>