function autocomplete(company){
  return $.ajax({
    url: '/acProxy',
    type: 'POST',
    data: company,
    dataType: 'json',
    contentType: 'string',
    success: function(data){
      var autocomplete_options = [];
      for (var key in data) {
        autocomplete_options.push(data[key]);
      }
      #console.log(autocomplete_options);
      $("#companyinput").autocomplete({
        source: autocomplete_options
      });
    }
  });
}

$("#companyinput").on('input', function(){
  var company = $(this)[0].value;
  autocomplete(company);
});
