$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const result = data.results;
  for (const movie of result) {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  }
});
