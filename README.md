<img src="./assets/logo.webp" style="width:100%; object-fit:cover;"/>
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![Discord](https://img.shields.io/discord/829038891611717753?label=Tesseract%20Coding)](http://bit.ly/TCDiscordInvite)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fwww.tesseractcoding.tech%2F)](https://www.tesseractcoding.tech/)
[![GitHub issues](https://img.shields.io/github/issues/TesseractCoding/Ric-Bot)](https://github.com/TesseractCoding/Ric-Bot/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/TesseractCoding/Ric-bot)](https://github.com/TesseractCoding/Ric-Bot/pulls)
[![Deploy to Heroku](https://img.shields.io/badge/-Deploy%20to%20Heroku-brightgreen)](https://heroku.com/deploy)

A Discord bot completely written to be taken from the source and built
according to your own custom needs.

This bot supports some core features and is built to be pluggable with other
features when and where required.

The core features which will be available for you to use when you setup this bot with the secrets are

1. Fetching latest Memes from Reddit
2. [Development] Deleting promotional messages from your server and keeping control where
   links are allowed.
3. [Development] Random and motivating quotes on demand and on certain times.
4. [Development] Saving random messages for particular users in your guild.

While source code of this bot is OpenSource you will need to build and host
this bot somewhere to have it running on your guild and steps for that can be
found [here](#)

## Building and running the bot locally

For running the bot there are two ways.

1. Building a [docker](https://www.docker.com/products/docker-desktop) image and then running that image.
2. Running the bot on local virtual environment using [pipenv](https://pipenv.pypa.io/en/latest/).

Steps for running with docker are -

1. Build a docker image for the repository. Make sure you have you have docker
   desktop installed before you do this step.

```
docker build -t ric-bot-image .
```

This command will take the Dockerfile in the current directory `.` and build
image for the same.

2. Run the image by providing necessary `.env` variables to it.

   In this repository there is a `.env.example` file which you will have to
   rename to `.env` and fill the variable values with correct values yourself.

   DISCORD_TOKEN is bot token provided to you by discord.

   REDDIT_CLIENT_ID is client id of your reddit account.

   REDDIT_CLIENT_SECRET is client secret of your reddit app.

   After doing so run the following command.

```
docker run --env-file .env -it --rm --name ric-bot-running ric-bot-image
```

The above command

1. Checks if there is a image running with the name
   `ric-bot-running` and removes it if present.
2. Provides the `.env` file to the
   process.
3. Runs the image with the provided variables.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://www.iamprins.com"><img src="https://avatars.githubusercontent.com/u/54654484?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ricardo Prins</b></sub></a><br /><a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=ricardoprins" title="Code">💻</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/kamaldgrt/"><img src="https://avatars.githubusercontent.com/u/43444282?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kamal Sharma</b></sub></a><br /><a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=KamalDGRT" title="Code">💻</a> <a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=KamalDGRT" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/adnan007d"><img src="https://avatars.githubusercontent.com/u/53809439?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adnan Mansuri</b></sub></a><br /><a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=adnan007d" title="Code">💻</a></td>
    <td align="center"><a href="https://anushkrishnav.rocks/"><img src="https://avatars.githubusercontent.com/u/54374648?v=4?s=100" width="100px;" alt=""/><br /><sub><b>A N U S H</b></sub></a><br /><a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=anushkrishnav" title="Code">💻</a></td>
    <td align="center"><a href="http://gats.dev"><img src="https://avatars.githubusercontent.com/u/22629774?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ganesh Tiwari</b></sub></a><br /><a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=gat786" title="Code">💻</a> <a href="https://github.com/TesseractCoding/Ric-Bot/commits?author=gat786" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!