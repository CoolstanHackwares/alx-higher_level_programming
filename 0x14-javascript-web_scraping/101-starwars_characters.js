#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character details:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
