from telegrask import Telegrask
from .config import TOKEN

bot = Telegrask(TOKEN)
bot.help.header = "Dostępne komendy"

from . import commands
