<template>
  <div class="flex flex-col gap-3 justify-center p-3 md:p-5 bg-woodsmoke">
    <div class="flex flex-row justify-between px-6">
      <UILogo/>
      <div class="flex flex-row gap-2 items-center">
        <Icon name="mdi:instagram" color="white" size="2rem"></Icon>
        <Icon name="ic:baseline-facebook" color="white" size="2rem"/>
      </div>
    </div>
    <hr class="min-w-[300px] sm:w-[300px] md:w-[760px] lg:w-[1280px]  h-0.5 bg-black rounded-[1px] flex self-center"/>
    <ul class="inline-flex flex-col sm:flex-row justify-center items-center sm:justify-evenly">
            <li>
                <UINavLink path="/" hash="#news">Новини</UINavLink>
            </li>
            
            <li>
                <UINavLink path="/" hash="#participants">Учасники</UINavLink>
            </li>
            
            <li>
                <UINavLink path="/" hash="#map">Карта</UINavLink>
            </li>
            
            <li>
                <UINavLink path="/events" >Події</UINavLink>
            </li>
            
            <li>
              <UINavLink  @click="emit('showEncyclopedia')">Енциклопедія</UINavLink>
            </li>
    </ul>
    <div class="flex flex-row justify-between px-0 md:px-52 lg:px-[500px]">
      <NuxtLink to="/contacts">
        <div class="flex flex-col justify-center items-center gap-3 hover:bg-yellow-300 hover:ring-3 hover:ring-yellow-900 rounded-lg p-4 hover:text-black text-yellow">
          <Icon name="material-symbols:mail" class="text-inherit " size="3rem"></Icon>
          <p class="text-[25px] font-semibold font-title text-center text-inherit">Mail</p>
        </div>
      </NuxtLink>

      <NuxtLink to="/contacts">
        <div class="flex flex-col justify-center items-center gap-3 hover:bg-yellow-300 hover:ring-3 hover:ring-yellow-900 rounded-lg p-4 hover:text-black text-yellow">
          <Icon name="material-symbols:call" class="text-inherit " size="3rem"></Icon>
          <p class="text-[25px] font-semibold font-title text-center text-inherit">Call</p>
        </div>
      </NuxtLink>

      <NuxtLink to="/contacts">
        <div class="flex flex-col justify-center items-center gap-3 hover:bg-yellow-300 hover:ring-3 hover:ring-yellow-900 rounded-lg p-4 hover:text-black text-yellow">
          <Icon name="bxs:map" class="text-inherit " size="3rem"></Icon>
          <p class="text-[25px] font-semibold font-title text-center text-inherit">Find us</p>
        </div>
      </NuxtLink>
    </div>
    <hr class="min-w-[300px] sm:w-[300px] md:w-[760px] lg:w-[1280px]  h-0.5 bg-black rounded-[1px] flex self-center"/>
    <div class="flex flex-col-reverse sm:flex-row justify-center items-center sm:justify-evenly">
      <p class="font-display font-normal text-[15px] text-silver hover:underline cursor-pointer">Copyright © 2023 Warrior. All rights reserved.</p>
      <NuxtLink to="/terms-of-use">
        <p class="font-display font-normal text-[15px] text-silver hover:underline cursor-pointer">Правила користування</p>
      </NuxtLink>
      <NuxtLink to="/privacy-policy">
        <p class="font-display font-normal text-[15px] text-silver hover:underline cursor-pointer">Політика конфіденційності</p>
      </NuxtLink>
      <NuxtLink :to="config.public.BASE_URL + '/admin/'">
        <p class="font-display font-normal text-[15px] text-silver hover:underline cursor-pointer">Адмін</p>
      </NuxtLink>
    </div>
  </div>
</template>

<script lang="ts" setup>
const config = useRuntimeConfig()
const emit = defineEmits(['showEncyclopedia'])
</script>

<style>

</style>