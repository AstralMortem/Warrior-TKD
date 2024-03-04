
$('#id_coach').on('change',function(e){
  let user_id = $(this).select2('data')[0]['id']
  if(user_id){
    $('#id_gym').select2({
      ajax:{
        url: '/api/gyms/get_gyms_by_coach/' + user_id,
        dataType: 'json',
        processResults: function(data){
          return {
            results: data.map(item=>{
              return {
                "id": item.id,
                "text": item.title
              }})
          }
        }
      }
    })
  }
})


$('#id_gym').on('change',function(e){
  let gym_id = $(this).select2('data')[0]['id']
  window.participants_arr = []
  if(gym_id){
    $('#id_group').select2({
      ajax:{
        url: '/api/gyms/get_groups_by_gym/' + gym_id,
        dataType: 'json',
        processResults: function(data){
          window.participants_arr = data.map(item=>item.participants)
          return {
            results: data.map(item=>{
              return {
                "id": item.id,
                "text": item.title,
              }})
          }
        },
      }
    })
  }
})


function preInitFormset(name,number){
  $ = django.jQuery
    for (let index = 0; index < number; index++) {
      const element = $(name).find("div.add-row").children()
      element.trigger("click");
    }
}

$("#id_group").on("change",function(e){
  $ = django.jQuery
  const index = $(this).index()
  const participants = window.participants_arr[index]
  preInitFormset("#participant_to_attendance-group",participants.length);

    for(let index = 0; index < participants.length; index++) {
      let select = $("select#id_participant_to_attendance-"+index+"-participant")
      select.val(participants[index]).trigger('change')
      const title = select.find(`option[value=${participants[index]}]`).text()
      select.parent().find('span.select2-selection__rendered').text(title)
    }
})


$("#id_coach").on('change',function(e){
  let user_id = $(this).select2('data')[0]['id']
  var $el = $("#id_participants_from")
  $.ajax({
    url: '/api/gyms/available/'+user_id,
    method: 'get',  
    dataType: 'json',
    success: function(data){
      console.log(data)
      $el.empty()
      for(let i =0;i<data.length;i++){
        $el.append($('<option></option>').attr("value",data[i].id).attr("title",data[i].full_name).text(data[i].full_name))
      }
    }
  })
})



$("#id_email").on('change',function(e){
  let el = $(this)
  if(el.val().split("@").length>1){
    const text = el.val()
    text += "warrior-tkd.pp.ua"
    el.val(text)
  }
})