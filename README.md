# zelda-bot

This program launches a Discord bot. Users can talk to the bot on Discord,
sending it commands to return information about creatures, items, etc.
in the video game "Zelda, Breath of the Wild." For example, if you message
"?creatures" to the bot, it will reply with a list of all the creatures in
Breath of the Wild. If you message "?creature lord of the mountain" it will
reply with detailed information on the "Lord of the Mountain" creature in
Breath of the Wild (e.g. a description of the creature, where it can be found
on the map, any items it drops, etc.)

The commands this bot supports are:

| command           | description                            |
| ----------------- | -------------------------------------- |
| ?creatures        | for a list of all creature names       |
| ?equipments       | " " " " " equipment "                  |
| ?materials        | " " " " " material "                   |
| ?monsters         | " " " " " monster "                    |
| ?treasures        | " " " " " treasure "                   |
| ?creature <name>  | for information on a specific creature |
| ?equipment <name> | " " " " " piece of equipment           |
| ?material <name>  | " " " " " material                     |
| ?monster <name>   | " " " " " monster                      |
| ?treasure <name>  | " " " " " treasure                     |

Inspired by:
https://www.reddit.com/r/Python/comments/kphbuk/api_for_the_legend_of_zelda_breath_of_the_wilds/

## Usage instructions

First, you must have created a Discord Application and Bot in the Discord Developer Console.
Instructions for doing that can be found [here](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)

Then you're ready to use this code...

Create a virtual environment

```
python3 -m venv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install depedencies

```
pip install -r requirements.txt
```

Add your Discord Bot token to a `.env` file

```
cat "DISCORD_BOT_TOKEN=<your discord bot token>" > .env
```

Run the bot!

```
python main.py
```
