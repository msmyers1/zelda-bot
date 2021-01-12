# Mathis Souef

# This program launches a Discord bot. Users can talk to the bot on Discord,
# sending it commands to return information about creatures, items, etc.
# in the video game "Zelda, Breath of the Wild." For example, if you message
# "?creatures" to the bot, it will reply with a list of all the creatures in
# Breath of the Wild. If you message "?creature lord of the mountain" it will
# reply with detailed information on the "Lord of the Mountain" creature in
# Breath of the Wild (e.g. a description of the creature, where it can be found
# on the map, any items it drops, etc.)
#
# The commands this bot supports are:
#
# * ?creatures        - for a list of all creature names
# * ?equipments       -  "  "   "   "  "  equipment  "
# * ?materials        -  "  "   "   "  "  material   "
# * ?monsters         -  "  "   "   "  "  monster    "
# * ?treasures        -  "  "   "   "  "  treasure   "
#
# * ?creature <name>  - for information on a specific creature
# * ?equipment <name> -  "       "       " "     "    piece of equipment
# * ?material <name>  -  "       "       " "     "    material
# * ?monster <name>   -  "       "       " "     "    monster
# * ?treasure <name>  -  "       "       " "     "    treasure
#
# Inspired by:
# https://www.reddit.com/r/Python/comments/kphbuk/api_for_the_legend_of_zelda_breath_of_the_wilds/

import json
import os
from pathlib import Path
import pprint
from typing import Any, Dict

from discord.ext import commands
from dotenv import load_dotenv

BOT = commands.Bot(command_prefix="?", description="A really cool Discord bot")


def read_json(path: Path) -> Dict[str, Any]:
    """
    Function that reads a json file located at the provided path and returns
    a dictionary that maps the names of items to information about those items
    """
    f = open(path, "r")
    s = f.read()
    f.close()
    items = json.loads(s)
    output = {}
    for item in items:
        name = item.get("name")
        if name is None:
            continue
        output[name] = item
    return output


CREATURES = read_json(Path("./data/creatures.json"))
EQUIPMENT = read_json(Path("./data/equipment.json"))
MATERIALS = read_json(Path("./data/materials.json"))
MONSTERS = read_json(Path("./data/monsters.json"))
TREASURES = read_json(Path("./data/treasure.json"))


def describe_item(data: Dict[str, Any], name: str) -> str:
    """
    Function that takes in a data set (e.g. CREATURES, EQUIPMENT, etc.) and
    the name of an item in that data set and returns detailed information about
    that item in the form of a string that is ready to be sent to Discord
    """
    item = data.get(name)
    if item is None:
        return "I'm sorry. I don't know about that thing"
    s = pprint.pformat(item, indent=2, sort_dicts=True)
    return s


def describe_items(data: Dict[str, Any]) -> str:
    """
    Function that takes in a data set (e.g. CREATURES, EQUIPMENT, etc.) and
    returns the names of all the items in the data set as a string that is
    ready to be sent to Discord
    """
    names = []
    for name in data.keys():
        names.append(name)
    names.sort()
    s = "\n".join(names)
    return s


@BOT.event
async def on_ready():
    """Function that runs when the Discord bot becomes ready"""
    print("Logged in as")
    print(BOT.user.name)
    print(BOT.user.id)
    print("------")


@BOT.command(description="Get info on a creature")
async def creature(ctx, *name: str):
    """Function that runs when the creature command is called by a user"""
    s = describe_item(CREATURES, " ".join(name))
    await ctx.send(s)


@BOT.command(description="List all the creatures in the database")
async def creatures(ctx):
    """Function that runs when the creatures command is called by a user"""
    s = describe_items(CREATURES)
    await ctx.send(s)


@BOT.command(description="Get info on a piece of equipment")
async def equipment(ctx, *name: str):
    """Function that runs when the equipment command is called by a user"""
    s = describe_item(EQUIPMENT, " ".join(name))
    await ctx.send(s)


@BOT.command(description="List all the pieces of equipment in the database")
async def equipments(ctx):
    """Function that runs when the equipments command is called by a user"""
    s = describe_items(EQUIPMENT)
    await ctx.send(s)


@BOT.command(description="Get info on a piece of material")
async def material(ctx, *name: str):
    """Function that runs when the material command is called by a user"""
    s = describe_item(MATERIALS, " ".join(name))
    await ctx.send(s)


@BOT.command(description="List all the pieces of material in the database")
async def materials(ctx):
    """Function that runs when the materials command is called by a user"""
    s = describe_items(MATERIALS)
    await ctx.send(s)


@BOT.command(description="Get info on a monster")
async def monster(ctx, *name: str):
    """Function that runs when the monster command is called by a user"""
    s = describe_item(MONSTERS, " ".join(name))
    await ctx.send(s)


@BOT.command(description="List all the monsters in the database")
async def monsters(ctx):
    """Function that runs when the monsters command is called by a user"""
    s = describe_items(MONSTERS)
    await ctx.send(s)


@BOT.command(description="Get info on a piece of treasure")
async def treasure(ctx, *name: str):
    """Function that runs when the treasure command is called by a user"""
    s = describe_item(TREASURES, " ".join(name))
    await ctx.send(s)


@BOT.command(description="List all the pieces of treasures in the database")
async def treasures(ctx):
    """Function that runs when the treasures command is called by a user"""
    s = describe_items(TREASURES)
    await ctx.send(s)


def test_describe_item():
    """
    Function that tests that the describe_item function is working correctly
    """
    actual = describe_item(MONSTERS, "chuchu")
    expected = """
{ 'common_locations': ['Hyrule Field', 'West Necluda'],
  'description': 'This low-level, gel-based monster can be found all over '
                 'Hyrule. It tends to spring its attacks on unsuspecting prey '
                 'from the ground or from trees. Its strength varies by size, '
                 'and the type of jelly it drops varies depending on whether '
                 'the Chuchu was heated up, cooled down, or shocked.',
  'drops': ['chuchu jelly'],
  'id': 84,
  'name': 'chuchu'}
"""
    if actual != expected.strip():
        raise Exception("Failed test_describe_item")
    actual = describe_item(MONSTERS, "i do not exist")
    expected = "I'm sorry. I don't know about that thing"
    if actual != expected.strip():
        raise Exception("Failed test_describe_item")


def test_describe_items():
    """
    Function that tests that the describe_items function is working correctly
    """
    actual = describe_items(MONSTERS)
    expected = """
black bokoblin
black hinox
black lizalfos
black moblin
blizzrobe
blue bokoblin
blue hinox
blue lizalfos
blue moblin
blue-maned lynel
bokoblin
calamity ganon
chuchu
cursed bokoblin
cursed lizalfos
cursed moblin
dark beast ganon
decayed guardian
dinraal
electric chuchu
electric keese
electric lizalfos
electric wizzrobe
farosh
fire chuchu
fire keese
fire wizzrobe
fire-breath lizalfos
fireblight ganon
forest octorok
frost pebblit
frost talus
guardian scout i
guardian scout ii
guardian scout iii
guardian scout iv
guardian skywatcher
guardian stalker
guardian turret
hinox
ice chuchu
ice keese
ice wizzrobe
ice-breath lizalfos
igneo pebblit
igneo talus
igneo talus titan
keese
lizalfos
lynel
master kohga
meteo wizzrobe
moblin
molduga
molduking
monk maz koshia
naydra
rock octorok
sentry
silver bokoblin
silver lizalfos
silver lynel
silver moblin
snow octorok
stalizalfos
stalkoblin
stalmoblin
stalnox
stone pebblit
stone talus
stone talus (luminous)
stone talus (rare)
thunder wizzrobe
thunderblight ganon
treasure octorok
water octorok
waterblight ganon
white-maned lynel
windblight ganon
yiga blademaster
yiga footsoldier
"""
    if actual != expected.strip():
        raise Exception("Failed test_describe_items")


def main():
    load_dotenv()
    test_describe_item()
    test_describe_items()
    BOT.run(os.environ["DISCORD_BOT_TOKEN"])


if __name__ == "__main__":
    main()
