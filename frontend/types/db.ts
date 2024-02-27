export interface IBelt {
    code: string,
    photo: string,
    title: string
}

export interface INews {
    id: number,
    news_images: Array<string>,
    title: string,
    text: string,
    created_at: Date,
}

export interface IGym {
    title: string,
    phone?:string,
    email?:string,
    calendar:string,
    time:string,
    address: string,
    location: string,
}

export interface IUserSmall{
    id: string,
    full_name:string,
    photo?: string,
    mobile?:string,
    belt: IBelt
}

export interface IMainPage{
    coaches: Array<IUserSmall>,
    participants: Array<IUserSmall>,
    news: Array<INews>,
    gyms: Array<IGym>
}


export interface IEventCompetition {
    id:number
    title: string
    place: string
    date: string
    command_sparing: number
    command_tul:number
    total_medals:string
    is_completed:boolean
}