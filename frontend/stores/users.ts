import { defineStore } from 'pinia'

export const useUsersStore = defineStore({
  id: 'myUsersStore',
  state: () => ({
    coaches: [],
    participants: [],
    pending: false,
    nextParticipants: null,
    nextCoaches: null
   }),
   actions: {
    async initStore(){
      this.pending = true
      const {data:coachesData} = await useApiRequest('/api/account/users/', {params:{"is_staff":true}})
      const {data:participantsData} = await useApiRequest('/api/account/users/',{params:{"is_staff":false}})
      this.nextCoaches = coachesData.value.next
      this.coaches = coachesData.value.results
      this.nextParticipants = participantsData.value.next
      this.participants = participantsData.value.results
      this.pending = false
    },
    async fetchNextCoaches(){
      if(this.nextCoaches){
        this.pending = true
        const {data} = await useApiRequest(this.nextCoaches)
        this.nextCoaches = data.value.next
        this.coaches = [...this.coaches,data.value.results]
        this.pending = false
      }
    },
    async fetchNextParticipants(){
      if(this.nextParticipants){
        this.pending = true
        const {data} = await useApiRequest(this.nextParticipants)
        this.nextParticipants = data.value.next
        this.coaches = [...this.participants,data.value.results]
        this.pending = false
      }
    }
  }
})
