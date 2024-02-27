<template>
  <div class="relative">
    
    <div class="rounded-full w-[300px] h-[300px] bg-yellow blur-[200px] fixed overflow-hidden hidden sm:block -z-10"  v-for="index in 2" 
    :class="index%2==0?`top-[${calculateTopOffset(index)}] -left-[150px]`:`top-[${calculateTopOffset(index)}] -right-[150px]`"/>
    <slot class="relative"/>
    
  </div>
</template>

<script lang="ts" setup>

function calculateTopOffset(index:number):string{
  return 300*index + 'px'
}
</script>

<style>

</style>