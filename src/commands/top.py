from config import bot
from likes import fetch_top


def handle_top(message):

    def get_user_name(chat_id, user_id):
        user = bot.get_chat_member(chat_id, user_id).user
        return f"{user.first_name} (@{user.username})"

    top_message = "\n".join(
        f"{position + 1}. {get_user_name(message.chat.id, user_id)} — {count}"
        for position, (user_id, count) in enumerate(fetch_top(message.chat.id, 10))
    )
    bot.reply_to(message, f"🏆test Топ по лайкам:\n{top_message}")
