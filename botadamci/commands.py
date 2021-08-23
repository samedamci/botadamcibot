from telegram import Update
from telegram.ext import CallbackContext
from telegrask.ext import Moderation, UserURL
from . import bot
from .config import FEDERATION


@bot.command("mute", help="mute chat user")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    user = update.message["reply_to_message"].from_user
    try:
        if mod.is_user_admin(update.message.from_user.id):
            mod.mute(user.id)
            update.message.reply_text(
                f"ℹ User {UserURL(user)} has been muted.", parse_mode="markdown"
            )
        else:
            update.message.reply_text("❌ Permission error.")
    except PermissionError:
        update.message.reply_text("❌ Permission error.")


@bot.command("unmute", help="unmute chat user")
def mute(update: Update, context: CallbackContext):
    mod = Moderation(update, context)
    user = update.message["reply_to_message"].from_user
    try:
        if mod.is_user_admin(update.message.from_user.id):
            mod.unmute(user.id)
            update.message.reply_text(
                f"ℹ User {UserURL(user)} has been unmuted.", parse_mode="markdown"
            )
        else:
            update.message.reply_text("❌ Permission error.")
    except PermissionError:
        update.message.reply_text("❌ Permission error.")


@bot.command(["ban", "gban", "fban"], help="ban user in federation")
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
                        f"ℹ User {UserURL(user)} has been banned in federation.",
                        parse_mode="markdown",
                    )
        else:
            update.message.reply_text("❌ Permission error.")
    except PermissionError:
        update.message.reply_text("❌ Permission error.")


@bot.command("unban", help="unban user in federation")
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
                        f"ℹ User {UserURL(user)} has been unbanned in federation.",
                        parse_mode="markdown",
                    )
        else:
            update.message.reply_text("❌ Permission error.")
    except PermissionError:
        update.message.reply_text("❌ Permission error.")
