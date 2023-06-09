from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def choose_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="Putar Music",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="Putar Video",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Tutup",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def livestream_markup(quality, videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎥 Start Live",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="Tutup",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def stream_quality_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📽 360𝐩",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 720𝐩",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 480𝐩",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Tutup",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
