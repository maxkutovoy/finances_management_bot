from asgiref.sync import sync_to_async
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

from accounting.models import Customer, Wallet, Transaction

@sync_to_async
def check_customer(user_id):
    user, created = Customer.objects.get_or_create(id=user_id)
    if created:
        user.wallets.create()
    return user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tg_user = update.effective_user
    customer = await check_customer(tg_user.id)

    await update.message.reply_html(
        rf"Hi {tg_user.mention_html()}",
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
