# doot-bot

This is a Discord bot written in Python that joins a voice channel and loops the doot music forever.

![](https://github.com/1nderr/doot-bot/blob/main/assets/doot.png?raw=true)

The `song.mp3` in this repo is based on [this YouTube playlist](https://www.youtube.com/watch?v=WzFXaEYPE10&list=PLelh_z0pMOn-J5ZReYaR_UVOyoDJUT3HR).

## Features

### Play

`?play` joins the voice channel named `Doot Land` and starts playing `song.mp3` through ffmpeg. When the song ends it starts it over again, so it never stops on its own. If there is no channel with that name, the bot says so and tells you to make one.

### Leave

`?leave` disconnects the bot from the voice channel. This command is admin only.

## Setup

This bot requires a file named `.env` in the root folder with the following content:

```bash
TOKEN="PASTE_YOUR_BOT_TOKEN_HERE"
```

## Build

`docker build -t dootbot .`

## Run

`docker run --rm -d dootbot`
