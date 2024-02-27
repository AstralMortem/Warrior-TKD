<template>
  <div class="flex gap-2 flex-col lg:flex-row justify-between ring-1 rounded-lg p-4" :class="props.is_completed?'ring-silver bg-silver bg-opacity-20':'ring-yellow'">
    <div class="flex-col justify-start items-start gap-2.5 inline-flex">
      <div class="self-stretch text-yellow text-base font-normal lg:text-xl font-title">{{ props.title }}
      <span v-if="props.is_completed" class="text-base">(Завершено)</span>
      </div>
      <div class="flex-col justify-start items-start gap-1 flex">
        <div class="text-alabaster text-xs md:text-[15px] font-normal font-display">Час проведення: {{ convertBound(props.date)}} </div>
        <div class="text-center text-alabaster text-xs md:text-[15px] font-normal font-display">Місце проведення: {{ props.place }}</div>
      </div>
    </div>
    <div class="ring-1 ring-yellow rounded-lg p-4 flex flex-row gap-3 justify-center text-xl lg:text-4xl" v-if="props.is_completed">
      <div class="flex flex-row gap-1 justify-start items-center ">
        <p class="text-alabaster ">{{ props.total_medals.split(',')[0] }}</p>
        <Icon name="fluent-emoji-flat:1st-place-medal" />
      </div>
      <div class="flex flex-row gap-1 justify-start items-center">
        <p class="text-alabaster ">{{ props.total_medals.split(',')[1] }}</p>
        <Icon name="fluent-emoji-flat:2nd-place-medal" />
      </div>
      <div class="flex flex-row gap-1 justify-start items-center">
        <p class="text-alabaster ">{{ props.total_medals.split(',')[2] }}</p>
        <Icon name="fluent-emoji-flat:3rd-place-medal" />
      </div>
      
    </div>
  </div>
  
</template>

<script lang="ts" setup>
import type { IEventCompetition } from '~/types/db';
  const props = defineProps<IEventCompetition>()
  const convertBound = (bound:string) => {
    const date = JSON.parse(bound)
    return "З " + new Date(date.lower).toLocaleDateString() + ' по ' +new Date(date.upper).toLocaleDateString()
  }
</script>

<style>

</style>