export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event).public
  const data = await $fetch('/main-page/',{baseURL:config.BASE_URL})
  return data
})
