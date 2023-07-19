from django.conf import settings
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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    print(update.message)
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True)
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


class Command(BaseCommand):
    help = "Telegram bot for finances management"

    def handle(self, *args, **options):
        telegram_token = settings.TG_TOKEN
        application = Application.builder().token(telegram_token).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        application.run_polling(allowed_updates=Update.ALL_TYPES)



#
#

#
#
# def main() -> None:
#
#
#
#
#
# if __name__ == "__main__":
#     main()
