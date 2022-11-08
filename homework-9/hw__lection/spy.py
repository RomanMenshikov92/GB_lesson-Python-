from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os.path


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    directory = '../Семинары/homework-9/hw__lection'
    filename = 'db.csv'
    file_0 = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_0, 'a', encoding='utf-8')
    file.write(
        f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()
