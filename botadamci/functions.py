from telegram import Update
from telegram.ext import CallbackContext
from telegrask.ext import Moderation, UserURL
from typing import Callable
from .config import FEDERATION


def do_action(mod: Moderation, method: Callable, in_federation: bool = False):
    update, context = mod.update, mod.context
    user = update.message["reply_to_message"].from_user
    user_url = UserURL(user)

    activities = {
        "mute": "zmutowany",
        "unmute": "odmutowany",
        "ban": "zbanowany",
        "unban": "odbanowany",
    }

    msg = f"ℹ Użytkownik {user_url} został {activities[method.__name__]}\."

    try:
        if mod.is_user_admin(update.message.from_user.id):
            if in_federation:
                for chat_id in FEDERATION:
                    mod.chat_id = chat_id
                    method(user.id)
                    context.bot.send_message(mod.chat_id, msg, parse_mode="MarkdownV2")
            else:
                method(user.id)
                context.bot.send_message(mod.chat.id, msg, parse_mode="MarkdownV2")
        else:
            update.message.reply_text("❌ Nie masz wystarczających uprawnień.")
    except PermissionError:
        update.message.reply_text("❌ Błąd uprawnień.")
