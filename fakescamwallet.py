from telegram.ext import Application, CommandHandler

TOKEN = "8895928497:AAEHmebwhrKqQJ5uR51n6R3Ewbe0yVo7b0o"


async def start(update, context):

    text = """
⚠️ WARNING

🚫 This bot is NOT a real crypto wallet.

Fake Wallet — это demo Mini App,
созданный только для обучения,
дизайна и тестов Telegram Mini Apps.

❌ Не отправляйте:
• TON
• BTC
• ETH
• USDT
• или другие криптовалюты

❌ Не вводите:
• seed phrase
• private key
• passwords

Все балансы, монеты и транзакции —
полностью фейковые.

🎨 Project features:
• Fake crypto wallet UI
• Demo balance
• Fake transactions
• Telegram Mini App interface
• Educational purpose only

👇 Нажми кнопку слева возле строки сообщения,
чтобы открыть Mini App 🚀
"""

    await update.message.reply_text(text)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Fake Wallet Bot Started!")

app.run_polling()