from telegrask import Telegrask
from .config import TOKEN

bot = Telegrask(TOKEN)
bot.help.header = "Dostępne komendy"
bot.help.help_description = "wyświetl tą wiadomość"

from . import commands
