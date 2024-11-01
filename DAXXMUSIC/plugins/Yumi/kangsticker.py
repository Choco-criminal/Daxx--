import imghdr
import os
from asyncio import gather
from traceback import format_exc
import sys
import traceback

from pyrogram import filters
from pyrogram.errors import (
    PeerIdInvalid,
    ShortnameOccupyFailed,
    StickerEmojiInvalid,
    StickerPngDimensions,
    StickerPngNopng,
    UserIsBlocked,
    StickersetInvalid  # <-- Added the missing import
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err

from DAXXMUSIC.utils.files import (
    get_document_from_file_id,
    resize_file_to_sticker_size,
    upload_document,
)

from DAXXMUSIC.utils.stickerset import (
    add_sticker_to_set,
    create_sticker,
    create_sticker_set,
    get_sticker_set_by_name,
)

# -----------

MAX_STICKERS = 120  # would be better if we could fetch this limit directly from Telegram
SUPPORTED_TYPES = ["jpeg", "png", "webp"]

# ------------------------------------------

@app.on_message(filters.command("get_sticker"))
@capture_err
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("Reply to a sticker.")

    if not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending...")
    f = await r.download(f"{r.sticker.file_unique_id}.png")

    await gather(
        *[
            message.reply_photo(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)


#----------------
@app.on_message(filters.command("kang"))
@capture_err
async def kang(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a sticker/image to kang it.")
    if not message.from_user:
        return await message.reply_text(
            "You are anon admin, kang stickers in my pm."
        )
    msg = await message.reply_text("Kanging Sticker...")

    # Find the proper emoji
    args = message.text.split()
    if len(args) > 1:
        sticker_emoji = str(args[1])
    elif (
        message.reply_to_message.sticker
        and message.reply_to_message.sticker.emoji
    ):
        sticker_emoji = message.reply_to_message.sticker.emoji
    else:
        sticker_emoji = "🤔"

    # Get the corresponding fileid, resize the file if necessary
    doc = message.reply_to_message.photo or message.reply_to_message.document
    try:
        if message.reply_to_message.sticker:
            sticker = await create_sticker(
                await get_document_from_file_id(
                    message.reply_to_message.sticker.file_id
                ),
                sticker_emoji,
            )
        elif doc:
            if doc.file_size > 10000000:
                return await msg.edit("File size too large.")

            temp_file_path = await app.download_media(doc)
            image_type = imghdr.what(temp_file_path)
            if image_type not in SUPPORTED_TYPES:
                return await msg.edit(
                    "Format not supported! ({})".format(image_type)
                )
            try:
                temp_file_path = await resize_file_to_sticker_size(
                    temp_file_path
                )
            except OSError as e:
                await msg.edit_text("Something wrong happened.")
                raise Exception(
                    f"Something went wrong while resizing the sticker (at {temp_file_path}); {e}"
                )
            sticker = await create_sticker(
                await upload_document(client, temp_file_path, message.chat.id),
                sticker_emoji,
            )
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)
        else:
            return await msg.edit("Nope, can't kang that.")
    except ShortnameOccupyFailed:
        await message.reply_text("Change Your Name Or Username")
        return

    except Exception as e:
        await message.reply_text(str(e))
        e = format_exc()
        return print(e)

    # Sticker set handling
    packnum = 0
    packname = f"f{message.from_user.id}_by_{BOT_USERNAME}"
    packtitle = f"{message.from_user.first_name[:32]}'s kang pack"
    limit = 0

    while True:
        try:
            stickerset = await get_sticker_set_by_name(client, packname)
            if stickerset.set.count >= MAX_STICKERS:
                packnum += 1
                packname = f"f{packnum}_{message.from_user.id}_by_{BOT_USERNAME}"
                limit += 1
                if limit >= 50:
                    return await msg.edit("Too many packs, can't kang.")
                continue
            else:
                await add_sticker_to_set(client, stickerset, sticker)
            break
        except StickerPngNopng:
            await message.reply_text(
                "Stickers must be png files but the provided image was not a png"
            )
            return
        except StickerPngDimensions:
            await message.reply_text("The sticker png dimensions are invalid.")
            return
        except StickerEmojiInvalid:
            await msg.edit("[ERROR]: INVALID_EMOJI_IN_ARGUMENT")
            return
        except PeerIdInvalid:
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Start", url=f"t.me/{BOT_USERNAME}")]]
            )
            await msg.edit(
                "You Need To Start A Private Chat With Me.",
                reply_markup=keyboard,
            )
            return
        except UserIsBlocked:
            await msg.edit("It looks like you've blocked me. Unblock me first!")
            return
        except StickersetInvalid:
            # Create a new sticker set
            await create_sticker_set(
                client,
                message.from_user.id,
                packtitle,
                packname,
                [sticker],
            )
            break
        except Exception as e:
            errors = traceback.format_exception(*sys.exc_info())  # Removed 'etype'
            print(errors)
            await msg.edit_text(f"Error: {str(e)}")
            return

    await msg.edit(
        f"Sticker Kanged To [Pack](t.me/addstickers/{packname})\nEmoji: {sticker_emoji}"
    )
