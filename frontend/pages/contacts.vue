<template>
    <div class="flex flex-col gap-4 justify-center p-6 ">
        <p class="font-title text-yellow text-4xl self-center">Контакти</p>
        <UILoader v-if="pending"/>
        <div class="flex flex-col md:flex-row flex-wrap gap-4" v-else>
        <div class="flex flex-col gap-2 p-4 ring-1 ring-yellow rounded-lg" v-for="user in coaches.results">
            <p class="text-alabaster font-display">{{user.full_name}}</p>
            <p class="text-alabaster font-display" v-if="user.coach_type">{{getEnumType(user.coach_type,COACH_TYPE)}}</p>
            <p class="text-alabaster font-display">Телефон: {{user.mobile}}</p>
            <p class="text-alabaster font-display">Пошта: {{user.email}}</p>
        </div>
        </div>
</div>

</template>

<script setup lang="ts">
import {COACH_TYPE} from '~/types/enums'

const {data:coaches,pending} = await useApiRequest('/api/account/users/',{query:{'is_staff':true}})

function getEnumType(key:string, dict:Object){
  return dict[key]
}

</script>