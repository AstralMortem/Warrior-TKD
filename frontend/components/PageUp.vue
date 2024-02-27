<template>
  <div class="fixed z-50 bottom-4 right-4">
    <Icon name="gg:chevron-up-o" size="3rem" class="text-yellow text-opacity-50 hover:text-opacity-100 cursor-pointer" v-show="showButton"
    @click="topFunction"></Icon>
  </div>
</template>

<script lang="ts" setup>
  let showButton = ref(false)

function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    showButton.value = true
  } else {
    showButton.value = false
  }
}


function topFunction() {
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0; 
}
onMounted(()=>{
  window.addEventListener('scroll', scrollFunction);
})

onUnmounted(()=>{
  window.removeEventListener('scroll', scrollFunction);
})

</script>

<style>

</style>