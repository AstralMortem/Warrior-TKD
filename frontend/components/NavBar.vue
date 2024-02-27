<template>
<nav class="bg-transparent flex flex-row justify-between items-start md:items-center relative px-3 md:pl-2 lg:pl-[50px] p-2 md:pt-4">
    <div class="brand">
        <UILogo/>
    </div>
    
    <div class="flex flex-col items-end relative" >
        <button class="text-yellow -scale-x-100 font-semibold md:hidden" @click="showmenu = !showmenu" @blur="closeMenu">
            <Icon size="3rem" name="solar:list-bold"></Icon>
        </button>
        <Transition name="slide-fade">
            <ul class="flex flex-col md:flex-row md:bg-transparent bg-woodsmoke rounded-[5px] px-4 py-3 gap-2 md:gap-[37px] lg:gap-[42px] items-end md:items-center z-50 absolute top-11 md:relative md:top-0" 
        v-if="showmenu" >
            <li>
                <UINavLink path="/" hash="#news">Новини</UINavLink>
            </li>
            <hr class="md:hidden w-[141px]  bg-silver rounded-[1px]">
            <li>
                <UINavLink path="/" hash="#participants">Учасники</UINavLink>
            </li>
            <hr class="md:hidden w-[141px]  bg-silver rounded-[1px]">
            <li>
                <UINavLink path="/" hash="#map">Карта</UINavLink>
            </li>
            <hr class="md:hidden w-[141px]  bg-silver rounded-[1px]">
            <li>
                <UINavLink path="/events" >Події</UINavLink>
            </li>
            <hr class="md:hidden w-[141px]  bg-silver rounded-[1px]">
            <li>
                <UINavLink  @click="emit('showEncyclopedia')">Енциклопедія</UINavLink>
            </li>
            </ul>
        </Transition>
    </div>
</nav>
</template>

<script setup>

    let showmenu = ref(true)
    const emit = defineEmits(['showEncyclopedia'])

    const closeMenu = () =>{
       setTimeout(()=>{
        showmenu.value = false
       },200)
    }


    function checkSize(){
        if(window.innerWidth >= 768){
            showmenu.value = true
        }else{
            showmenu.value = false
        }
    }

    

onMounted(() => window.addEventListener('resize', checkSize))
onUnmounted(() => window.removeEventListener('resize', checkSize))
</script>



<style scoped>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>