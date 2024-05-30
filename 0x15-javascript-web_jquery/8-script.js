$(document).ready(function(){
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
        var movies = data.results;
        movies.forEach(function(movie){
            $('<li>').text(movie.title).appendTo('#list_movies');
        });
    });
});
