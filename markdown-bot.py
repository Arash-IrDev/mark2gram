from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegramify_markdown import markdownify
from telegramify_markdown.customize import get_runtime_config

# Custom visual separator symbol
CUSTOM_SEPARATOR = "➖➖➖➖➖"

# FAKE_RTL_CHAR is a directional character to force right-to-left rendering without affecting visual output
FAKE_RTL_CHAR = "\u061C"

# Telegram API has a strict message length limit
MAX_TELEGRAM_LENGTH = 4096

# Customize the default emoji symbols for headings, links, images, tasks, etc.
symbols = get_runtime_config().markdown_symbol
symbols.head_level_1 = "📌"
symbols.head_level_2 = "🔶"
symbols.head_level_3 = "🔹"
symbols.head_level_4 = "◽️"
symbols.image = "🖼"
symbols.link = "🔗"
symbols.task_completed = "✅"
symbols.task_uncompleted = "◻️"

# Replace default separator symbols with a RTL-aware separator (wrapped in FAKE_RTL_CHAR)
def process_separators(text: str) -> str:
    return text.replace("————————", f"{FAKE_RTL_CHAR}{CUSTOM_SEPARATOR}{FAKE_RTL_CHAR}")

# Analyze each paragraph separately and wrap it in FAKE_RTL_CHAR if it contains mostly RTL characters
def process_paragraphs_with_direction(text: str) -> str:
    paragraphs = text.split("\n")
    processed = []

    for p in paragraphs:
        rtl_count = sum(1 for c in p if '\u0600' <= c <= '\u06FF')
        total_count = sum(1 for c in p if c.strip())
        rtl_ratio = rtl_count / max(1, total_count)

        # Logging for debugging direction detection
        print(f"[PARA DETECT] RTL chars: {rtl_count}, total: {total_count}, ratio: {rtl_ratio:.2f}")

        if rtl_ratio > 0.5:
            processed.append(f"{FAKE_RTL_CHAR}{p}{FAKE_RTL_CHAR}")
        else:
            processed.append(p)

    return "\n".join(processed)

# Break long text into chunks that are below Telegram's 4096 character limit
# Uses paragraph blocks to preserve readability
def split_text(text: str, max_length: int) -> list[str]:
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_length:
            current += para + "\n\n"
        else:
            chunks.append(current.strip())
            current = para + "\n\n"

    if current.strip():
        chunks.append(current.strip())

    return chunks

# Telegram Bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Main message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Receive user message
    text = update.message.text

    # Convert standard Markdown to Telegram MarkdownV2 format
    converted = markdownify(text)

    # Replace visual separators with custom ones
    converted = process_separators(converted)

    # Detect RTL/LTR for each paragraph
    converted = process_paragraphs_with_direction(converted)

    # Split final message into safe Telegram-size chunks
    parts = split_text(converted, MAX_TELEGRAM_LENGTH)

    # Send each chunk individually
    for part in parts:
        await update.message.reply_text(part, parse_mode='MarkdownV2')

# Initialize the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Register message handler for plain text (excluding commands)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Start the polling loop to receive messages
app.run_polling()
