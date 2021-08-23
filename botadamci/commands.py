from telegram import Update
from telegram.ext import CallbackContext
from telegrask.ext import Moderation, UserURL
from . import bot
from .config import FEDERATION


@bot.command("mute", help="zmutuj użytkownika")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    user = update.message["reply_to_message"].from_user
    try:
        if mod.is_user_admin(update.message.from_user.id):
            mod.mute(user.id)
            update.message.reply_text(
                f"ℹ Użytkownik {UserURL(user)} został zmutowany.", parse_mode="markdown"
            )
        else:
            update.message.reply_text("❌ Błąd uprawnień.")
    except PermissionError:
        update.message.reply_text("❌ Błąd uprawnień.")


@bot.command("unmute", help="odmutuj użytkownika")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    user = update.message["reply_to_message"].from_user
    try:
        if mod.is_user_admin(update.message.from_user.id):
            mod.unmute(user.id)
            update.message.reply_text(
                f"ℹ Użytkownik {UserURL(user)} został odmutowany.",
                parse_mode="markdown",
            )
        else:
            update.message.reply_text("❌ Błąd uprawnień.")
    except PermissionError:
        update.message.reply_text("❌ Błąd uprawnień.")


@bot.command(["ban", "gban", "fban"], help="zbanuj użytkownika w federacji")
def ban(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    user = update.message["reply_to_message"].from_user
    try:
        if mod.is_user_admin(update.message.from_user.id):
            if mod.chat_id in FEDERATION:
                for chat_id in FEDERATION:
                    mod.chat_id = chat_id
                    mod.ban(user.id)
                    context.bot.send_message(
                        chat_id,
                        f"ℹ Użytkownik {UserURL(user)} został zbanowany.",
                        parse_mode="markdown",
                    )
        else:
            update.message.reply_text("❌ Błąd uprawnień.")
    except PermissionError:
        update.message.reply_text("❌ Błąd uprawnień.")


@bot.command("unban", help="odbanuj użytkownika w federacji")
def unban(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    user = update.message["reply_to_message"].from_user
    try:
        if mod.is_user_admin(update.message.from_user.id):
            if mod.chat_id in FEDERATION:
                for chat_id in FEDERATION:
                    mod.chat_id = chat_id
                    mod.unban(user.id)
                    context.bot.send_message(
                        chat_id,
                        f"ℹ Użytkownik {UserURL(user)} został odbanowany.",
                        parse_mode="markdown",
                    )
        else:
            update.message.reply_text("❌ Błąd uprawnień.")
    except PermissionError:
        update.message.reply_text("❌ Błąd uprawnień.")
