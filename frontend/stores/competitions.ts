import { defineStore } from 'pinia'

export const useCompetitionsStore = defineStore({
  id: 'myCompetitionsStore',
  state: () => ({
    competitions: [],
    pending:false,
    next:null
   }),
   actions: {
    async initStore(){
      this.pending = true
      const {data} = await useApiRequest('/api/events/competitions/')
      this.next = data.value.next
      this.competitions = data.value.results
      this.pending = false
    },
    async fetchNext(){
      if(this.next){
        this.pending = true
        const  {data} = await useApiRequest(this.next)
        this.next = data.value.next
        this.competitions = [...this.competitions,data.value.results]
        this.pending = false
      }
    }
  }
})
