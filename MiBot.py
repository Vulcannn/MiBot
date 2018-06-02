import discord
import logging
import json

from discord.ext import commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('MiBot')

try:
    with open('config.json', 'r') as data:
        config = json.load(data)
        logger.info('Config Loaded')
except Exception as e:
    logger.error('Config Load Error: {}'.format(e))

bot = commands.Bot(command_prefix=config['prefix'], description=config['description'], pm_help=False)

@bot.event
async def on_ready():
    logger.info("Bot has started up!")

    try:
        bot.load_extension('plugins.commands')
    except Exception as e:
        logger.error('Plugins Load Error: {}'.format(e))

bot.run(config['token'])



