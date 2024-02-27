<template>
  <button @click="routerGo" class="px-[25px] py-2 cursor-pointer bg-yellow bg-opacity-50 hover:bg-opacity-100 rounded-[25px] shadow justify-center items-center inline-flex">
    <p class="text-center text-stone-950 text-base lg:text-xl font-normal font-title"><slot/></p>
  </button>
</template>

<script lang="ts" setup>

let props = defineProps({
  href:{
    default: '/'
  },
  hash: {
    default: null
  },
})

function routerGo(){
  if(props.href != '/'){
    router.push({path:props.href})
  }
}

const router = useRouter();
</script>

