import asyncio

from esfigram.core.client import TelegramClient
from esfigram.types import ReplyParameters
from esfigram.types.maybe_inaccessible_message import Message
from esfigram.enums.update_type import UpdateType


async def echo_message(bot: TelegramClient, message: Message):
    if message.text:
        await bot.send_message(chat_id=message.chat.id, text=message.text,
                               reply_parameters=ReplyParameters(message.message_id))
    else:
        await bot.send_message(chat_id=message.chat.id, text='just send text message!')


async def main():
    client = TelegramClient(token='BOT_TOKEN')
    client.handler_manager.add_handler(func=echo_message, update_type=UpdateType.MESSAGE)
    await client.run()


asyncio.run(main())
