export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event).public
  const data = await $fetch('/news/',{baseURL:config.BASE_URL})
  return data
})
