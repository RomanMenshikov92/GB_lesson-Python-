from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botCommands import *

app = ApplicationBuilder().token(
    "5741655823:AAHyFoUe6GA5Ca7GuDOPInzHqZdUUvk9CpY").build()

app.add_handler(CommandHandler("hi", hi_commands))
app.add_handler(CommandHandler("time", time_commands))
app.add_handler(CommandHandler("help", help_commands))
app.add_handler(CommandHandler("sum", sum_commands))
print('server start')
app.run_polling()
