#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

// Define the URL for the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body as JSON
  const film = JSON.parse(body);

  // Check if film is found
  if (!film.title) {
    console.error('Movie not found');
    return;
  }

  // Get the list of character URLs
  const characters = film.characters;

  // For each character URL, make a request to get the character name
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      // Parse the character response body as JSON
      const character = JSON.parse(charBody);

      // Print the character name
      console.log(character.name);
    });
  });
});
