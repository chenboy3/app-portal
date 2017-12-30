$.getScript('./js/config.js');
var req_url = 'http://api.glassdoor.com/api/api.htm?v=';

function getCompany(name){
  var url = buildURL('1', 'json', getId(), getKey(), 'employers',
  '75.104.65.154', window.navigator.userAgent, name);
  return $.post({
    url: url,
    success: function(data){
      console.log(data);
    }
  });
}


function buildURL(v, format, tp, tk, action, userip, useragent, searchterm){
    return (req_url + v + "&format=" + format + "&t.p=" + tp + "&t.k=" + tk +
         "&action=" + action + "&q=" + searchterm + "&userip=" + userip +
         "&useragent=" + useragent);
}

$("#companyinput").on('input', function(){
  var str = $(this)[0].value;
  getCompany(str);
});
