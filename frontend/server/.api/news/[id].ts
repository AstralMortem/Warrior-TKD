export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event).public
  const news_id = getRouterParam(event, 'id')
  const data = $fetch(`/news/${news_id}`,{baseURL:config.BASE_URL})
  return data
})
