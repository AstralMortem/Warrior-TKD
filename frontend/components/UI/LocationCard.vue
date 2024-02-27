<template>
  <div class="flex flex-col gap-4 mb-4">
    <div class="flex flex-row">
      <Icon name="bx:map" size="2rem" class="text-yellow"/>
      <div class="flex flex-col gap-2">
        <p class="text-base font-title text-yellow">{{ props.title }}</p>
        <p class="text-base font-title text-alabaster" >Адреса: {{ props.address }}</p>
        <p class="text-base font-title text-alabaster" v-if="props.phone">Телефон: {{ props.phone }}</p>
        <p class="text-base font-title text-alabaster text-wrap w-[200px]" v-if="props.email">Email: {{ props.email }}</p>
      </div>
    </div>
    <div class="flex flex-row">
      <Icon name="mdi:clock-outline" size="2rem" class="text-yellow"/>
      <div class="flex flex-col gap-2">
        <p class="text-base font-title text-alabaster">Графік: {{ props.calendar }}</p>
        <p class="text-base font-title text-alabaster">Час: {{ props.time }}</p>
      </div>
    </div>
    <!-- <hr class="md:"/> -->
  </div>
</template>

<script lang="ts" setup>
import { type IGym } from '~/types/db';

const props = defineProps<IGym>()
  
</script>

<style>

</style>