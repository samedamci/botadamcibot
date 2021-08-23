from telegram import Update
from telegram.ext import CallbackContext
from telegrask.ext import Moderation
from . import bot
from .config import FEDERATION
from .functions import do_action


@bot.command("mute", help="zmutuj użytkownika")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.mute)


@bot.command("unmute", help="odmutuj użytkownika")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.unmute)


@bot.command(["ban", "gban", "fban"], help="zbanuj użytkownika w federacji")
def ban(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.ban, in_federation=mod.chat_id in FEDERATION)


@bot.command("unban", help="odbanuj użytkownika w federacji")
def unban(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    do_action(mod, mod.unban, in_federation=mod.chat_id in FEDERATION)
