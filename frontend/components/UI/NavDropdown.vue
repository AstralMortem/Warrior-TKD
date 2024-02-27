<script setup lang="ts">
let showdrop = ref(false)

const router = useRouter()
defineProps({
  showUp:{
    default: false
  }
})


// const belts = ref(null)
// const pending = ref(true)

// onMounted(async ()=>{

//   pending.value = pending.value
//   belts.value = belts.value
// })

const {data:belts,pending} = await useApiRequest('/api/account/belts/')



</script>


<template>
  
    <div class="relative inline-block text-left">
      <div class="flex flex-row whitespace-nowrap font-title text-base lg:text-xl  hover:text-yellow transition-all ease-out duration-300" :class="[showdrop ? 'text-yellow' : '','text-alabaster-50']">
        <button type="button"  id="menu-button" aria-expanded="true" aria-haspopup="true" @click="showdrop = !showdrop">
          <slot/>
        </button>
        <Icon size="2rem" name="mdi:chevron-down" v-if="!showdrop"></Icon>
        <Icon size="2rem" name="mdi:chevron-up" v-else></Icon>
      </div>

  
  <div v-show="showdrop"  class="absolute w-min-100 bg-woodsmoke rounded-md min-w-max right-16  mt-5 py-5 px-5" :class="[showUp ? 'bottom-20  left-0' : '', '']"
  role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
    <p class="font-title text-xl pb-5 text-alabaster-50">Рейтингова система</p>
    <UILoader v-if="pending"/>
    <div class="grid grid-cols-4 gap-5" v-else>
      <img :src="belt.photo" class="w-[60px] h-[23.19px] lg:w-20 lg:h-[30.92px] opacity-60 hover:opacity-100 shadow cursor-pointer " v-for="belt in belts" :key="belt.code" @click="router.push({path:`/belt/${belt.code}`})"/>
    </div>
  </div>
  
  </div>
  

</template>