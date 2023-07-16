from environs import Env
from django.core.management.base import BaseCommand
from telegram import ForceReply, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    InvalidCallbackData,
    MessageHandler,
    PicklePersistence,
    filters
)


class Command(BaseCommand):
    help = "Telegram bot for finances management"

    def handle(self, *args, **options):
        pass


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user = update.effective_user
#     await update.message.reply_html(
#         rf"Hi {user.mention_html()}!",
#         reply_markup=ForceReply(selective=True),
#     )
#
#
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     await update.message.reply_text(update.message.text)
#
#
# def main() -> None:
#     env = Env()
#     env.read_env()
#
#     telegram_token = env.str('TG_TOKEN')
#     application = Application.builder().token(telegram_token).build()
#
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#
#     application.run_polling(allowed_updates=Update.ALL_TYPES)
#
#
# if __name__ == "__main__":
#     main()
