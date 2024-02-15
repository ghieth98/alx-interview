#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie:
*/
const util = require('util');
const request = util.promisify(require('request'));
const id = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getUsers(urls, ids) {
    request(urls[ids], (err, res, body) => {
        if (!err) {
            console.log(JSON.parse(body).name);
            if (ids < urls.length - 1) {
                getUsers(urls, ids + 1);
            }
        }
    });
}

// Parallel Exectution Version
function fetchUsers(urls) {
    const fetchPromises = urls.map((url) => request({url}));

    Promise.all(fetchPromises)
        .then((responses) => {
            responses.forEach((resp) => console.log(JSON.parse(resp.body).name));
        })
        .catch((err) => {
            console.error(err);
        });
}

request(apiURL, (err, res, body) => {
    if (!err) {
        const allCharacters = JSON.parse(body).characters;
        fetchUsers(allCharacters);
        if (allCharacters.length < 0) {
            getUsers(allCharacters, 0);
        }
    }
});