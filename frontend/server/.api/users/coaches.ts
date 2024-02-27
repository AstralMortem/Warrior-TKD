export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event).public
  const data = await $fetch('/account/users/?is_staff=true',{baseURL:config.BASE_URL})
  return data
})
