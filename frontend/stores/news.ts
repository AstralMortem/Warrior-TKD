import { defineStore } from 'pinia'

export const useNewsStore = defineStore({
  id: 'myNewsStore',
  state: () => ({ 
    news: [],
    pending: false,
    next: null,
  }),
  actions: {
    async initStore(){
      this.pending = true
      const {data} = await useApiRequest('/api/news/')
      this.next = data.value.next
      this.news = data.value.results
      this.pending = false
    },
    async fetchNext(){
      if(this.next){
        this.pending = true
        const {data} = await useApiRequest(this.next)
        this.next = data.value.next
        this.news = [...this.news,data.value.results]
        this.pending = false
      }
    }
  }
})
