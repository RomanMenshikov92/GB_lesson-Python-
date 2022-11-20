# 2. (* ) Прикрутить бота к задачам с предыдущего семинара:
# 2.1. (* *) Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

# import os
# os.system('cls||clear')

# print('2. (* ) Прикрутить бота к задачам с предыдущего семинара:\n')
# print('2.1. (* *) Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования\n')

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botCommands import *

app = ApplicationBuilder().token(
    "5848426541:AAGkst4S1LdmRMX24Q5DxucvRs7q2KrkD2c").build()

app.add_handler(CommandHandler("hello", hi_commands))
app.add_handler(CommandHandler("help", help_commands))
app.add_handler(CommandHandler("time", time_commands))
app.add_handler(CommandHandler("sum", sum_commands))
app.add_handler(CommandHandler("diff", diff_commands))
app.add_handler(CommandHandler("multi", multi_commands))
app.add_handler(CommandHandler("div", div_commands))
print('server start')
app.run_polling()


