import telebot
from telebot import types
import os

# Token uthane ke liye
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Jab user /start dabaye
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('💰 Zakat Calculator')
    btn2 = types.KeyboardButton('📈 Halal Profit Check')
    btn3 = types.KeyboardButton('📊 Business Hisaab')
    btn4 = types.KeyboardButton('ℹ️ Help & Info')
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.reply_to(message, "✨ Mizan Bot mein aapka swagat hai! ✨\n\nNiche diye gaye buttons par click karke aap calculation shuru kar sakte hain.", reply_markup=markup)

# Button clicks ko handle karne ke liye
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == '💰 Zakat Calculator':
        msg = bot.reply_to(message, "💵 Apni kul jama-poonji (Total Wealth) ka amount sirf numbers mein likh kar bhejein:\n*(Jaise: 100000)*")
        bot.register_next_step_handler(msg, process_zakat)
    elif message.text == '📈 Halal Profit Check':
        bot.reply_to(message, "📊 Yeh feature jald hi chalu hoga! Stay tuned.")
    elif message.text == '📊 Business Hisaab':
        bot.reply_to(message, "📝 Yeh feature jald hi chalu hoga! Stay tuned.")
    elif message.text == 'ℹ️ Help & Info':
        bot.reply_to(message, "ℹ️ Yeh bot aapki financial calculations ko aasan banane ke liye hai.\n\nZakat kul wealth ka 2.5% calculate hoti hai.")

def process_zakat(message):
    try:
        wealth = float(message.text)
        zakat = wealth * 0.025
        bot.reply_to(message, f"✅ **Zakat Calculation Result:**\n\n💰 Aapki Total Wealth: ₹{wealth:,.2f}\n✨ Wajib Zakat Amount (2.5%): **₹{zakat:,.2f}**\n\n_Allah aapke maal mein barkat ata farmaye!_")
    except ValueError:
        bot.reply_to(message, "❌ Galti! Kripya sirf numbers type karein (Commas ya letters mat lagana). Fir se try karne ke liye button dabaayein.")

print("Bot chalu ho gaya hai...")
bot.infinity_polling()

