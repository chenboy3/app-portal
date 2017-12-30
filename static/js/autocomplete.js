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
      $('#companyAutofill').empty();
      for (var i = 0; i < autocomplete_options.length; i++) {
        $('#companyAutofill').append(
          '<a class="inputText acCompany" href="#">'+
          autocomplete_options[i] + '</a><br><br>');
      }

      $('.acCompany').click(function(){
        $('#companyAutofill').empty();
        $('#companyinput')[0].value = $(this)[0].innerHTML;
      });
    }
  });
}

$('#companyinput').on('input', function(){
  var company = $(this)[0].value;
  autocomplete(company);
});
