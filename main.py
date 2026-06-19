import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# গিটহাব সিক্রেট থেকে টোকেন এবং এপিআই কি নেওয়া হবে
BOT_TOKEN = os.getenv("8860054505:AAHOt9UYAN-l_Oj5JTOEaHBKHY5ZMV6ZlTI")
API_KEY = os.getenv("") 
# HeroSMS এর এপিআই লিঙ্ক
API_URL = "https://hero-sms.com/stubs/handler_api.php"

# স্টার্ট কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("✅ Verify Now", callback_data="verify")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("স্বাগতম! বট ব্যবহার করতে প্রথমে ভেরিফাই করুন।", reply_markup=reply_markup)

# মূল মেনু
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 Get Number", callback_data="get_num"), InlineKeyboardButton("🔑 2Fa", callback_data="2fa")],
        [InlineKeyboardButton("🤖 Api Number", callback_data="api_num"), InlineKeyboardButton("🚦 Live Traffic", callback_data="traffic")],
        [InlineKeyboardButton("💸 Withdraw", callback_data="withdraw"), InlineKeyboardButton("💰 Balance", callback_data="balance")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("মেনু সিলেক্ট করুন:", reply_markup=reply_markup)

# API থেকে নাম্বার আনার ফাংশন (HeroSMS প্রোটোকল অনুযায়ী)
async def get_api_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # API প্যারামিটার সেট করা
    params = {
        'api_key': API_KEY,
        'action': 'getNumber',
        'service': 'ot' # এখানে 'ot' বা আপনার প্রয়োজনীয় সার্ভিস কোড দিন
    }
    try:
        response = requests.get(API_URL, params=params)
        await update.callback_query.message.reply_text(f"API রেসপন্স: {response.text}")
    except Exception as e:
        await update.callback_query.message.reply_text("এপিআই কানেকশনে সমস্যা হয়েছে।")

# API Number প্যানেল
async def api_number_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 Get API Number", callback_data="get_api_num")],
        [InlineKeyboardButton("⬅️ Back", callback_data="verify")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("API প্যানেল:", reply_markup=reply_markup)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(main_menu, pattern="verify"))
    application.add_handler(CallbackQueryHandler(api_number_menu, pattern="api_num"))
    application.add_handler(CallbackQueryHandler(get_api_number, pattern="get_api_num"))
    
    application.run_polling()

if __name__ == "__main__":
    main()
                         
