from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("hello", hello_com))
app.add_handler(CommandHandler("date", date_com))
app.add_handler(CommandHandler("time", time_com))
app.add_handler(CommandHandler("help", help_com))

app.run_polling()