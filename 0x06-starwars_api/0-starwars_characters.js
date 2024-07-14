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

// Function to fetch character name
const fetchCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

// Make a request to the Star Wars API
request(url, async (error, response, body) => {
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

  // Fetch all character names
  try {
    const characterNames = await Promise.all(characters.map(fetchCharacterName));
    // Print each character name in the correct order
    characterNames.forEach(name => console.log(name));
  } catch (fetchError) {
    console.error('Error:', fetchError);
  }
});
