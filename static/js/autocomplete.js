var req_url = 'http://api.glassdoor.com/api/api.htm?v=';

function getCompany(name){
  console.log({company: name})
  return $.ajax({
    url: '/acProxy',
    type: 'POST',
    data: name,
    dataType: 'json',
    contentType: 'string',
    success: function(data){
      console.log(data);
      console.log(typeof(data));
      var autocomplete_options = [];
      for (var key in data) {
        autocomplete_options.push(data[key]);
      }
      console.log(autocomplete_options);
      $("#companyinput").autocomplete({
        source: autocomplete_options
      });
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
