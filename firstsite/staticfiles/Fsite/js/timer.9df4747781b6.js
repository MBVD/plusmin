moment.locale('ru');
function declOfNum(n, text_forms) {  
  n = Math.abs(n) % 100; 
  var n1 = n % 10;
  if (n > 10 && n < 20) { return text_forms[2]; }
  if (n1 > 1 && n1 < 5) { return text_forms[1]; }
  if (n1 == 1) { return text_forms[0]; }
  return text_forms[2];
}
class Timer {
  constructor (options) {
    this.start_datetime = new Date(options.start_datetime)
    this.end_datetime = new Date(options.end_datetime)
    this.pk = options.pk
  }

  set change_start_datetime(date){
    delete this.start_datetime;
    this.start_datetime = date;
  }

  valid() {
    if (new Date() <= this.start_datetime){
      // console.log('контест ожидается, приятного решения')
      // console.log(this.pk)
      // delete_response = new Request ('/change_publish')
      // request добавляем статус активный
      
      ;
    }
    if (new Date() >= this.end_datetime){
      // console.log('контест не активен')
      // console.log(this.pk)
      // delete_response = new Request ('')
      //request // убираем статус активный
    }
    return true
  }

  countdown() {
    var timer_element = document.getElementById("timer" + this.pk)
    // console.log(timer_element)
    var date = this.start_datetime
    var current_moment = new Date()
    if (date - current_moment > 0){
      var difference = date - current_moment
    }
    else{
      var difference = "Уже началось"
    }
    
    if (typeof(difference) == "string"){
      timer_element.innerHTML = difference ;
      return;
    }
    else{
      var diff = moment(date).fromNow()
      timer_element.innerHTML = diff;
    }
  }
}
function checking(contests)
{
  for (var key in contests){
    timer = new Timer({start_datetime: contests[key]['started_at'], end_datetime: contests[key]['completed_at'], pk: key})
    // console.log(timer.end_datetime) Проверка
    // console.log(timer.start_datetime) Проверка
    timer.valid()
    timer.countdown()
  }
}

