<template>
  <div>
    <div class="flex flex-row justify-center md:justify-start items-center gap-4 px-4">
      <Icon name="material-symbols:chevron-left" size="3rem" class="bg-yellow bg-opacity-50 hover:ring-2 ring-yellow-800 p-1 rounded-full hover:bg-opacity-100 text-black cursor-pointer"
      @click="$router.go(-1)"/>
        <div class="inline-flex flex-row rounded-full border-2 border-alabaster cursor-pointer" @click="toggler = !toggler">
        <div class="font-title text-base rounded-full p-1 lg:text-xl" :class="toggler? 'bg-yellow text-black':'bg-transparent text-alabaster'">Тренери</div>
        <div class="font-title text-base rounded-full p-1 lg:text-xl" :class="!toggler? 'bg-yellow text-black':'bg-transparent text-alabaster'">Учасники</div>
      </div>
    </div>
    <div>
      <section id="couches" v-if="toggler" class="flex flex-col gap-5">
        <UIUserListItem v-for="user in coaches" :key="user.id"
        :id="user.id"
        :mobile="user.mobile"
        :full_name="user.full_name"
        :belt="user.belt"
        :photo="user.photo"
        />
        <UILoader v-if="pending"/>
        <UIButton class="self-center" v-else @click="userStore.fetchNextCoaches()">Завантажити ще</UIButton>
      </section>
      <section id="participants" v-else class="flex flex-col gap-5">
        <UIUserListItem v-for="user in participants" :key="user.id"
        :id="user.id"
        :mobile="user.mobile"
        :full_name="user.full_name"
        :belt="user.belt"
        :photo="user.photo"
        />
        <UILoader v-if="pending" />
        <UIButton class="self-center" v-else @click="userStore.fetchNextParticipants()">Завантажити ще</UIButton>
      </section>
    </div>
  </div>
</template>

<script lang="ts" setup>
let toggler = ref(true)

const userStore = useUsersStore()
const {pending, coaches,participants} = storeToRefs(userStore) 

onMounted(()=>{
  userStore.initStore()
})

useHead({
    title: "Учасники | TKD клуб ВОЇН",
    meta: [
        {name: 'description', content: "Учасники спортивного клубу taekwondo ВОЇН" }
    ]
})

useSeoMeta({
  title: "Учасники | TKD клуб ВОЇН",
  description:participants
})

</script>

<style>

</style>