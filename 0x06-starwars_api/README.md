# Star Wars Movie Characters Printer

This project consists of a script written in Node.js that prints all characters of a specified Star Wars movie. It utilizes the Star Wars API to fetch the character data and displays it in the same order as the character list provided by the API.

## Installation

1. **Install Node.js 10:**
   ```bash
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
   ```

2. **Install semi-standard:**
   ```bash
   $ sudo npm install semistandard --global
   ```

3. **Install request module:**
   ```bash
   $ sudo npm install request --global
   ```

4. **Set NODE_PATH environment variable:**
   ```bash
   $ export NODE_PATH=/usr/lib/node_modules:
   ```

## Usage

Once you have installed Node.js, semi-standard, and the request module, you can run the script with the following command:

```bash
$ node script.js <Movie_ID>
```

Replace `<Movie_ID>` with the ID of the Star Wars movie you want to fetch characters from. For example, to fetch characters from "Return of the Jedi", you would use `3` as the Movie ID.

The script will then retrieve and print the characters from the specified movie, with each character's name displayed on a separate line, following the order provided by the Star Wars API.

## Dependencies

- **Node.js:** Version 10 or higher is required to run the script.
- **semistandard:** A coding style linter for JavaScript.
- **request:** A simplified HTTP client for making requests to the Star Wars API.

## Documentation

- **Star Wars API:** [https://swapi.dev/](https://swapi.dev/)
- **Node.js:** [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)
- **semi-standard:** [https://github.com/standard/semistandard](https://github.com/standard/semistandard)
- **request:** [https://www.npmjs.com/package/request](https://www.npmjs.com/package/request)

## License

This project is licensed under the MIT License. See the LICENSE file for details.