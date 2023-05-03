// adds the name of a Swapi API character to the Div#character element
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data, status){
    $('div#character').text(data.name);
});
