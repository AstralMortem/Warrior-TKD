<template>
  <div class="pt-[5px] md:pt-2.5 md:rounded-[15px] lg:px-[50px] lg:pt-[15px] lg:pb-[5px] lg:rounded-[20px] bg-woodsmoke rounded-[10px] shadow flex-col justify-center items-start inline-flex  hover:bg-opacity-90 cursor-pointer"
  @click="expanded = !expanded">
    <div class="text-yellow text-[15px] lg:text-xl font-normal font-title self-center"><slot/></div>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4" v-show="expanded">
      <div class="text-silver font-display  text-left border-b-2 border-l-2 border-yellow rounded-md p-1" v-for="result in results">
        <p class="text-lg text-yellow">{{ result.total.split('|')[0] }}</p>
        <p class="text-base">{{ result.total.split('|')[1] }}</p>
      </div>
    </div>
    <div class="w-8 h-8 relative self-center">
      <Icon name="tabler:chevron-up" size="2rem" class="text-yellow" v-if="expanded"/>
      <Icon name="tabler:chevron-down" size="2rem" class="text-yellow" v-else/>
    </div>
</div>
</template>

<script lang="ts" setup>

const expanded = ref(false)
defineProps(['title','results'])


</script>

<style>

</style>