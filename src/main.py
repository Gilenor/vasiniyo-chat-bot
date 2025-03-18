import logging
import random

from commands.dispatcher import COMMANDS
from commands.help import handle_unknown
from commands.stickers import handle_stickers
from commands.text import handle_text
from commands.top import handle_top
from config import bot, templates

logger = logging.getLogger(__name__)


@bot.message_handler(commands=list(COMMANDS.keys()))
def handle_command(message):
    command_text = message.text.lstrip("/")
    command_name = command_text.split()[0].split("@")[0]

    command_func, _ = COMMANDS.get(command_name, (None, None))
    if command_func:
        command_func(message)
    else:
        handle_unknown(message)


bot.message_handler(func=lambda m: True)(handle_text)
bot.message_handler(content_types=["sticker"])(handle_stickers)

if __name__ == "__main__":
    logger.info("Bot started")
    bot.polling()
