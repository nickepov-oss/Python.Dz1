from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8938207085:AAEVEaTmUY6XZDT5YFwBIcvonJxNQ-pmHSg"


# ---------------- START ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("▶ Начать", callback_data="start_game")],
        [InlineKeyboardButton("❓ Как играть", callback_data="help")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет!\n\n"
        "Это история «Последний сигнал».\n\n"
        "Твои выборы влияют на сюжет.\n"
        "Готов начать?",
        reply_markup=reply_markup
    )


# ---------------- КНОПКИ ----------------

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # -------- HELP --------

    if query.data == "help":

        keyboard = [
            [InlineKeyboardButton("▶ Начать", callback_data="start_game")]
        ]

        await query.message.reply_text(
            "• Нажимай кнопки\n"
            "• Выборы влияют на сюжет\n"
            "• Иногда решения меняют концовку",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # -------- START GAME --------

    elif query.data == "start_game":

        keyboard = [
            [InlineKeyboardButton("Кто это?", callback_data="who")],
            [InlineKeyboardButton("Ты ошибся номером", callback_data="wrong")],
            [InlineKeyboardButton("Не отвечать", callback_data="ignore")]
        ]

        await query.message.reply_text(
            "23:47\n\n"
            "На улице дождь.\n\n"
            "Тебе приходит странное сообщение.\n\n"
            "Неизвестный:\n"
            "привет...\n"
            "кто-нибудь меня видит?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # -------- ПЕРВЫЙ ВЫБОР --------

    elif query.data == "who":

        keyboard = [
            [InlineKeyboardButton("Что слышал?", callback_data="sound")],
            [InlineKeyboardButton("Ты меня пугаешь", callback_data="fear")]
        ]

        await query.message.reply_text(
            "...\n\n"
            "слава богу\n"
            "кто-то ответил\n\n"
            "я в какой-то школе\n"
            "тут очень темно\n\n"
            "ты тоже это слышал?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "wrong":

        await query.message.reply_text(
            "нет\n\n"
            "пожалуйста не выходи..."
        )

    elif query.data == "ignore":

        await query.message.reply_text(
            "Пожалуйста ответь.\n\n"
            "Мне страшно."
        )

    # -------- ВТОРОЙ ВЫБОР --------

    elif query.data == "sound":

        keyboard = [
            [InlineKeyboardButton("🚪 Закрыться", callback_data="hide")],
            [InlineKeyboardButton("🔦 Посмотреть в коридор", callback_data="corridor")]
        ]

        await query.message.reply_text(
            "будто кто-то идет по коридору...\n\n"
            "я нашел кабинет 214\n\n"
            "что мне делать?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "fear":

        await query.message.reply_text(
            "я сам напуган..."
        )

    # -------- КОРИДОР --------

    elif query.data == "corridor":

        keyboard = [
            [InlineKeyboardButton("Беги!", callback_data="run")],
            [InlineKeyboardButton("Посвети фонариком", callback_data="flash")]
        ]

        await query.message.reply_text(
            "...\n\n"
            "в конце коридора кто-то стоит\n\n"
            "он не двигается",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "hide":

        await query.message.reply_text(
            "я закрыл дверь...\n\n"
            "но теперь кто-то скребется снаружи"
        )

    # -------- МОНСТР --------

    elif query.data == "flash":

        await query.message.reply_text(
            "ЧЕРТ\n\n"
            "ЭТО НЕ ЧЕЛОВЕК"
        )

        await query.message.reply_text(
            "оно идет сюда..."
        )

        await query.message.reply_text(
            "ОНО ИДЕТ—"
        )

        await query.message.reply_text(
            "...\n\n"
            "кажется я убежал"
        )

        await query.message.reply_text(
            "Контакт UNKNOWN:\n\n"
            "НЕ ПУСКАЙ ЕГО ВНИЗ"
        )

        await query.message.reply_text(
            "ГЛАВА 1 ЗАВЕРШЕНА"
        )

    elif query.data == "run":

        await query.message.reply_text(
            "я побежал...\n\n"
            "оно слишком быстрое..."
        )

    # ---------------- ЗАПУСК ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot started")

if __name__ == "__main__":
    app.run_polling()