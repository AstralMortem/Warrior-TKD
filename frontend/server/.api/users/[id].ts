export default defineEventHandler(async (event) => {
  const code = getRouterParam(event, 'id')
  const config = useRuntimeConfig().public
  const data = await $fetch(`/account/users/${code}/`,{baseURL:config.BASE_URL})
  return data
})
