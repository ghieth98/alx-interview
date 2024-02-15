#!/usr/bin/node
// A script that prints all characters of a Star war movie

const request = require('request');

function getCharacters(movieId) {
    return new Promise((resolve, reject) => {
        const url = `https://swapi.dev/api/films/${movieId}/`;
        request(url, (error, response, body) => {
            if (error || response.statusCode !== 200) {
                reject(error || `Failed to fetch data`);
            } else {
                const filmData = JSON.parse(body);
                const characters = filmData.characters;
                resolve(characters)
            }
        });
    });
}

function getCharacterDetails(characterUrl) {
    return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
            if (error || response.statusCode !== 200) {
                reject(error || 'Failed to Fetch Data');
            } else {
                const characterData = JSON.parse(body);
                resolve(characterData.name)
            }
        });
    })
}

// Print characters of a movie
async function printMovieCharacters(movieId) {
    try {
        const characterUrls = await getMovieCharacters(movieId);
        for (const characterUrl of characterUrls) {
            const characterName = await getCharacterDetails(characterUrl);
            console.log(characterName);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

// Extract Movie ID from command line argument
const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
    console.error("Please provide a valid movie ID as the first argument.");
} else {
    printMovieCharacters(movieId);
}