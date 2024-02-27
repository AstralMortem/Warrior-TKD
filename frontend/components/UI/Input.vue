<script setup>
defineProps({
  modelValue:{},
  placeholder:{
    default: 'Пошук'
  }
})
defineEmits(['update:modelValue'])
</script>

<template>
  <input :placeholder="placeholder"
  class="font-display text-lg font-normal text-silver hover:text-alabaster-50 hover:border-yellow mx-[2px] focus:text-alabaster px-10 py-4 bg-[#2B2A28] rounded-full "
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>