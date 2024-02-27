export default defineEventHandler(async (event) => {
    const code = getRouterParam(event, 'code')
    const config = useRuntimeConfig().public
    const data = await $fetch(`/account/belts/${code}/`,{baseURL:config.BASE_URL})
    return data
  })
  