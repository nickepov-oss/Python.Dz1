import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Рекомендую видалити токен з публічного доступу після тестування!
TOKEN = "8561382965:AAHtsVE1PHq80g252Cca3tYLve3yCXY0zNg"

# Налаштування логування, щоб бачити помилки в консолі
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

questions = [
    {"q": "Скільки буде 5*5?", "a": "25"},
    {"q": "Яка столиця України?", "a": "Київ"},
    {"q": "Скільки континентів на Землі?", "a": "7"},
    {"q": "Який птах не вміє літати?", "a": "Пінгвін"},
    {"q": "Скільки кольорів у весельці?", "a": "7"},
    {"q": "Що важче 1 кг заліза чи пір'я?", "a": "Однаково"},
    {"q": "Що йде але стоїть на місці?", "a": "Годинник"},
    {"q": "Скільки місяців мають 28 днів (відповідь цифрою)?", "a": "12"}
]

user_data = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data[user_id] = {
        "index": 0,
        "score": 0
    }
    await update.message.reply_text(f"Привіт, {update.effective_user.first_name}! Це гра квіз-вікторина.")
    await send_question(update, user_id)


async def send_question(update: Update, user_id):
    index = user_data[user_id]["index"]

    if index < len(questions):
        q = questions[index]["q"]
        await update.message.reply_text(f"Запитання №{index + 1}: {q}")
    else:
        score = user_data[user_id]["score"]
        total = len(questions)
        await update.message.reply_text(f"Гра закінчена! Твій рахунок: {score} з {total}.")
        # Очищуємо дані користувача після гри
        del user_data[user_id]


async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Перевірка, чи розпочав користувач гру командою /start
    if user_id not in user_data:
        await update.message.reply_text("Напиши /start, щоб почати гру.")
        return

    text = update.message.text
    index = user_data[user_id]["index"]
    correct_answer = questions[index]["a"]

    if text.lower().strip() == correct_answer.lower():
        user_data[user_id]["score"] += 1
        await update.message.reply_text("✅ Правильно!")
    else:
        await update.message.reply_text(f"❌ Неправильно! Правильна відповідь: {correct_answer}")

    # Переходимо до наступного питання
    user_data[user_id]["index"] += 1
    await send_question(update, user_id)


if name == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Додаємо обробник команди /start
    app.add_handler(CommandHandler("start", start))

    # Додаємо обробник для текстових повідомлень (відповідей)
    # filters.TEXT & (~filters.COMMAND) означає "будь-який текст, який не є командою"
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), check_answer))

    print("Бот запущений...")
    app.run_polling()