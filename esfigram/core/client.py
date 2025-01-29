import asyncio
import aiofiles
import json
import os
from typing import Dict, Union, Optional, List, Literal

import aiohttp

from esfigram.core.api import TelegramAPI
from esfigram.core.handlers import HandlerManager
from esfigram.core.utils import serialize_clean, replace_reserved_keys

from esfigram.types import MessageEntity, \
    LinkPreviewOptions, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, ReplyParameters, \
    InputFile, InputPaidMedia, InputPollOption, InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo, \
    ReactionType, ReactionTypeEmoji, ReactionTypeCustomEmoji, ReactionTypePaid, ChatPermissions, ChatInviteLink, \
    Message, UserProfilePhotos, File, InputMediaAnimation, InputMedia


class TelegramClient:
    def __init__(self, token: str):
        self.api = TelegramAPI(token)
        self.running = False
        self.handler_manager = HandlerManager(token)

    async def run(self):
        try:
            # Validate the bot token
            if not await self.api.validate_token():
                print("Invalid token. Exiting...")
                return

            print("Bot Started ...")
            self.running = True

            while self.running:
                try:
                    # Fetch updates
                    await self.get_updates()
                except aiohttp.ClientError as e:
                    print(f"Network error: {e}. Retrying in 5 seconds...")
                    await asyncio.sleep(5)
                except Exception as e:
                    print(f"Unexpected error: {e}. Retrying in 5 seconds...")
                    await asyncio.sleep(5)

        except Exception as global_error:
            print(f"Critical error: {global_error}. Shutting down...")

        finally:
            await self.stop()

    async def stop(self):
        self.running = False
        await self.api.close_session()
        print("Bot stopped and session closed.")

    async def get_updates(self):
        params = {
            'offset': self.api.offset,
            'limit': 10,
            'timeout': 30,
        }
        updates = await self.api.request("getUpdates", params)

        for update in updates.get("result", []):
            self.api.offset = update["update_id"] + 1
            update = replace_reserved_keys(update)
            if 'message' in update and update['message']['from_user']['id'] != int(self.api.token.split(':')[0]):
                await self.process_update(update)

    async def process_update(self, update: Dict):
        try:

            await self.handler_manager.handle_update(self, update)

        except KeyError as e:
            print(f"Process update error: Missing key {e}")
        except AttributeError as e:
            print(f"Process update error: {e}")
        except Exception as e:
            print(f"Process update error: {e}")

    async def send_message(
            self,
            chat_id: Union[int, str],
            text: str,
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            parse_mode: Optional[str] = None,
            entities: Optional[List[MessageEntity]] = None,
            link_preview_options: Optional[LinkPreviewOptions] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "text": text,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "parse_mode": parse_mode,
            "entities": entities,
            "link_preview_options": link_preview_options,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)

        if "entities" in params and params["entities"] is not None:
            params["entities"] = json.dumps(params["entities"])
        if "link_preview_options" in params and params["link_preview_options"] is not None:
            params["link_preview_options"] = json.dumps(params["link_preview_options"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        response = await self.api.request("sendMessage", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def forward_message(
            self,
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int,
            *,
            message_thread_id: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
        }

        params = serialize_clean(params)
        response = await self.api.request("forwardMessage", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def forward_messages(
            self,
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_ids: List[int],
            *,
            message_thread_id: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
    ) -> List[Dict]:
        params = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_ids": message_ids,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
        }

        params = serialize_clean(params)
        if "message_ids" in params and params["message_ids"] is not None:
            params["message_ids"] = json.dumps(params["message_ids"])
        response = await self.api.request("forwardMessages", params)
        response = response.get("result", response)
        response = replace_reserved_keys(response)
        return response

    async def copy_message(
            self,
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int,
            *,
            message_thread_id: Optional[int] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Dict:
        params = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "caption_entities" in params:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params:
            params["reply_markup"] = json.dumps(params["reply_markup"])
        response = await self.api.request("copyMessage", params)
        response = response.get("result", response)
        response = replace_reserved_keys(response)
        return response

    async def copy_messages(
            self,
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_ids: List[int],
            *,
            message_thread_id: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            remove_caption: Optional[bool] = None,
    ) -> List[Dict]:
        params = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_ids": message_ids,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "remove_caption": remove_caption,
        }
        params = serialize_clean(params)
        if "message_ids" in params:
            params["message_ids"] = json.dumps(params["message_ids"])
        response = await self.api.request("copyMessages", params)
        response = replace_reserved_keys(response)
        response = response.get("result", response)
        return response

    async def send_photo(
            self,
            chat_id: Union[int, str],
            photo: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            has_spoiler: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "photo": photo,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }

        params = serialize_clean(params)
        if "caption_entities" in params and params["caption_entities"] is not None:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(photo, InputFile):
            async with aiofiles.open(photo.file_path, 'rb') as file:
                params['photo'] = file
                response = await self.api.request("sendPhoto", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))
        else:
            response = await self.api.request("sendPhoto", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_audio(
            self,
            chat_id: Union[int, str],
            audio: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            duration: Optional[int] = None,
            performer: Optional[str] = None,
            title: Optional[str] = None,
            thumbnail: Optional[Union[str, InputFile]] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "audio": audio,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "performer": performer,
            "title": title,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "caption_entities" in params and params["caption_entities"] is not None:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(audio, InputFile):
            async with aiofiles.open(audio.file_path, 'rb') as file:
                params['audio'] = file
                response = await self.api.request("sendAudio", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))
        else:
            response = await self.api.request("sendAudio", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_document(
            self,
            chat_id: Union[int, str],
            document: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            thumbnail: Optional[Union[str, InputFile]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            disable_content_type_detection: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "document": document,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "thumbnail": thumbnail,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "disable_content_type_detection": disable_content_type_detection,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "caption_entities" in params and params["caption_entities"] is not None:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(document, InputFile):
            with open(document.file_path, 'rb') as file:
                params['document'] = file
                response = await self.api.request("sendDocument", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))
        else:
            response = await self.api.request("sendDocument", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_video(
            self,
            chat_id: Union[int, str],
            video: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            thumbnail: Optional[Union[str, InputFile]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            has_spoiler: Optional[bool] = None,
            supports_streaming: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "video": video,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "duration": duration,
            "width": width,
            "height": height,
            "thumbnail": thumbnail,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "supports_streaming": supports_streaming,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "caption_entities" in params and params["caption_entities"] is not None:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(video, InputFile):
            with open(video.file_path, 'rb') as file:
                params['video'] = file
                response = await self.api.request("sendVideo", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))

        else:
            response = await self.api.request("sendVideo", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_animation(
            self,
            chat_id: Union[int, str],
            animation: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            thumbnail: Optional[Union[str, InputFile]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            has_spoiler: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "animation": animation,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "duration": duration,
            "width": width,
            "height": height,
            "thumbnail": thumbnail,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "has_spoiler": has_spoiler,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "caption_entities" in params and params["caption_entities"] is not None:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(animation, InputFile):
            with open(animation.file_path, 'rb') as file:
                params['animation'] = file
                response = await self.api.request("sendAnimation", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))
        else:
            response = await self.api.request("sendAnimation", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_voice(
            self,
            chat_id: Union[int, str],
            voice: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            duration: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "voice": voice,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "caption_entities" in params and params["caption_entities"] is not None:
            params["caption_entities"] = json.dumps(params["caption_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(voice, InputFile):
            with open(voice.file_path, 'rb') as file:
                params['voice'] = file
                response = await self.api.request("sendVoice", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))
        else:
            response = await self.api.request("sendVoice", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_video_note(
            self,
            chat_id: Union[int, str],
            video_note: Union[str, InputFile],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            duration: Optional[int] = None,
            length: Optional[int] = None,
            thumbnail: Optional[Union[str, InputFile]] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "video_note": video_note,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "duration": duration,
            "length": length,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        if isinstance(video_note, InputFile):
            with open(video_note.file_path, 'rb') as file:
                params['video_note'] = file
                response = await self.api.request("sendVideoNote", params)
                response = replace_reserved_keys(response)
                return Message(**response.get("result", {}))

        else:
            response = await self.api.request("sendVideoNote", params)
            response = replace_reserved_keys(response)
            return Message(**response.get("result", {}))

    async def send_paid_media(
            self,
            chat_id: Union[int, str],
            star_count: int,
            media: List[InputPaidMedia],
            *,
            business_connection_id: Optional[str] = None,
            payload: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "star_count": star_count,
            "media": media,
            "business_connection_id": business_connection_id,
            "payload": payload,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "show_caption_above_media": show_caption_above_media,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "media" in params and params["media"] is not None:
            params["media"] = json.dumps(params["media"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])
        response = await self.api.request("sendPaidMedia", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def send_media_group(
            self,
            chat_id: Union[int, str],
            media: List[Union[
                InputMedia, InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo, InputMediaAnimation]],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
    ) -> List[Dict]:
        params = {
            "chat_id": chat_id,
            "media": media,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
        }
        params = serialize_clean(params)
        if "media" in params and params["media"] is not None:
            params["media"] = json.dumps(params["media"])
        response = await self.api.request("sendMediaGroup", params)
        response = response.get("result", response)
        return response

    async def send_location(
            self,
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            horizontal_accuracy: Optional[float] = None,
            live_period: Optional[int] = None,
            heading: Optional[int] = None,
            proximity_alert_radius: Optional[int] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "horizontal_accuracy": horizontal_accuracy,
            "live_period": live_period,
            "heading": heading,
            "proximity_alert_radius": proximity_alert_radius,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])
        response = await self.api.request("sendLocation", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def send_venue(
            self,
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            title: str,
            address: str,
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            foursquare_id: Optional[str] = None,
            foursquare_type: Optional[str] = None,
            google_place_id: Optional[str] = None,
            google_place_type: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "title": title,
            "address": address,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "foursquare_id": foursquare_id,
            "foursquare_type": foursquare_type,
            "google_place_id": google_place_id,
            "google_place_type": google_place_type,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])
        response = await self.api.request("sendVenue", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def send_contact(
            self,
            chat_id: Union[int, str],
            phone_number: str,
            first_name: str,
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            last_name: Optional[str] = None,
            vcard: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "phone_number": phone_number,
            "first_name": first_name,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "last_name": last_name,
            "vcard": vcard,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])
        response = await self.api.request("sendContact", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def send_poll(
            self,
            chat_id: Union[int, str],
            question: str,
            options: List[InputPollOption],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            question_parse_mode: Optional[str] = None,
            question_entities: Optional[List[MessageEntity]] = None,
            is_anonymous: Optional[bool] = True,
            type: Optional[Literal["regular", "quiz"]] = "regular",
            allows_multiple_answers: Optional[bool] = False,
            correct_option_id: Optional[int] = None,
            explanation: Optional[str] = None,
            explanation_parse_mode: Optional[str] = None,
            explanation_entities: Optional[List[MessageEntity]] = None,
            open_period: Optional[int] = None,
            close_date: Optional[int] = None,
            is_closed: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "question": question,
            "options": options,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "question_parse_mode": question_parse_mode,
            "question_entities": question_entities,
            "is_anonymous": is_anonymous,
            "type": type,
            "allows_multiple_answers": allows_multiple_answers,
            "correct_option_id": correct_option_id,
            "explanation": explanation,
            "explanation_parse_mode": explanation_parse_mode,
            "explanation_entities": explanation_entities,
            "open_period": open_period,
            "close_date": close_date,
            "is_closed": is_closed,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }

        params = serialize_clean(params)

        if "options" in params and params["options"] is not None:
            params["options"] = json.dumps(params["options"])
        if "question_entities" in params and params["question_entities"] is not None:
            params["question_entities"] = json.dumps(params["question_entities"])
        if "explanation_entities" in params and params["explanation_entities"] is not None:
            params["explanation_entities"] = json.dumps(params["explanation_entities"])
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])

        response = await self.api.request("sendPoll", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def send_dice(
            self,
            chat_id: Union[int, str],
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
            emoji: Optional[str] = "🎲",
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            allow_paid_broadcast: Optional[bool] = None,
            message_effect_id: Optional[str] = None,
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[
                    InlineKeyboardMarkup,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    ForceReply
                ]
            ] = None,
    ) -> Message:
        params = {
            "chat_id": chat_id,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "emoji": emoji,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        }
        params = serialize_clean(params)
        if "reply_markup" in params and params["reply_markup"] is not None:
            params["reply_markup"] = json.dumps(params["reply_markup"])
        response = await self.api.request("sendDice", params)
        response = replace_reserved_keys(response)
        return Message(**response.get("result", {}))

    async def send_chat_action(
            self,
            chat_id: Union[int, str],
            action: str,
            *,
            business_connection_id: Optional[str] = None,
            message_thread_id: Optional[int] = None,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "action": action,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
        }
        params = serialize_clean(params)
        response = await self.api.request("sendChatAction", params)
        return response.get("ok", False)

    async def set_message_reaction(
            self,
            chat_id: Union[int, str],
            message_id: int,
            *,
            reaction: Optional[List[Union[ReactionTypeEmoji, ReactionTypePaid, ReactionTypeCustomEmoji]]] = None,
            is_big: Optional[bool] = None,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction": reaction,
            "is_big": is_big,
        }
        params = serialize_clean(params)

        if "reaction" in params and params["reaction"] is not None:
            params["reaction"] = json.dumps([r.to_dict() if hasattr(r, "to_dict") else r for r in params["reaction"]])

        response = await self.api.request("setMessageReaction", params)
        return response.get("ok", False)

    async def get_user_profile_photos(
            self,
            user_id: int,
            offset: Optional[int] = None,
            limit: Optional[int] = 100,
    ) -> UserProfilePhotos:
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit,
        }
        params = serialize_clean(params)
        response = await self.api.request("getUserProfilePhotos", params)
        response = replace_reserved_keys(response)
        return UserProfilePhotos(**response.get("result", {}))

    async def set_user_emoji_status(
            self,
            user_id: int,
            emoji_status_custom_emoji_id: Optional[str] = None,
            emoji_status_expiration_date: Optional[int] = None,
    ) -> bool:
        params = {
            "user_id": user_id,
            "emoji_status_custom_emoji_id": emoji_status_custom_emoji_id or "",
            "emoji_status_expiration_date": emoji_status_expiration_date,
        }
        params = serialize_clean(params)
        response = await self.api.request("setUserEmojiStatus", params)
        return response.get("ok", False)

    async def get_file(self, file_id: str) -> File:
        params = {
            "file_id": file_id,
        }
        response = await self.api.request("getFile", params)
        response = replace_reserved_keys(response)
        return File(**response.get("result", {}))

    async def download_file(self, file_id: str, save_path: str) -> str:
        file_info = await self.get_file(file_id)
        file_path = file_info.file_path
        if not file_path:
            raise ValueError("File path not found in response")

        token = self.api.token
        download_url = f"https://api.telegram.org/file/bot{token}/{file_path}"

        async with aiohttp.ClientSession() as session:
            async with session.get(download_url) as response:
                if response.status == 200:
                    file_name = os.path.basename(file_path)
                    full_save_path = os.path.join(save_path, file_name)

                    with open(full_save_path, "wb") as file:
                        file.write(await response.read())

                    return full_save_path
                else:
                    raise Exception(f"Failed to download file. HTTP status code: {response.status}")

    async def ban_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            *,
            until_date: Optional[int] = None,
            revoke_messages: Optional[bool] = None
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "until_date": until_date,
            "revoke_messages": revoke_messages,
        }
        params = serialize_clean(params)
        response = await self.api.request("banChatMember", params)
        return response.get("result", False)

    async def unban_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            only_if_banned: Optional[bool] = None,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "only_if_banned": only_if_banned,
        }

        params = serialize_clean(params)

        response = await self.api.request("unbanChatMember", params)

        return response.get("result", False)

    async def restrict_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            permissions: ChatPermissions,
            *,
            use_independent_chat_permissions: Optional[bool] = None,
            until_date: Optional[int] = None,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "permissions": permissions,
            "use_independent_chat_permissions": use_independent_chat_permissions,
            "until_date": until_date,
        }
        params = serialize_clean(params)

        if "permissions" in params and params["permissions"] is not None:
            params["permissions"] = json.dumps(params["permissions"].to_dict())

        response = await self.api.request("restrictChatMember", params)
        return response.get("ok", False)

    async def promote_chat_member(
            self,
            chat_id: Union[int, str],
            user_id: int,
            *,
            is_anonymous: Optional[bool] = None,
            can_manage_chat: Optional[bool] = None,
            can_delete_messages: Optional[bool] = None,
            can_manage_video_chats: Optional[bool] = None,
            can_restrict_members: Optional[bool] = None,
            can_promote_members: Optional[bool] = None,
            can_change_info: Optional[bool] = None,
            can_invite_users: Optional[bool] = None,
            can_post_stories: Optional[bool] = None,
            can_edit_stories: Optional[bool] = None,
            can_delete_stories: Optional[bool] = None,
            can_post_messages: Optional[bool] = None,
            can_edit_messages: Optional[bool] = None,
            can_pin_messages: Optional[bool] = None,
            can_manage_topics: Optional[bool] = None,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "is_anonymous": is_anonymous,
            "can_manage_chat": can_manage_chat,
            "can_delete_messages": can_delete_messages,
            "can_manage_video_chats": can_manage_video_chats,
            "can_restrict_members": can_restrict_members,
            "can_promote_members": can_promote_members,
            "can_change_info": can_change_info,
            "can_invite_users": can_invite_users,
            "can_post_stories": can_post_stories,
            "can_edit_stories": can_edit_stories,
            "can_delete_stories": can_delete_stories,
            "can_post_messages": can_post_messages,
            "can_edit_messages": can_edit_messages,
            "can_pin_messages": can_pin_messages,
            "can_manage_topics": can_manage_topics,
        }
        params = serialize_clean(params)

        response = await self.api.request("promoteChatMember", params)
        return response.get("ok", False)

    async def set_chat_administrator_custom_title(
            self,
            chat_id: Union[int, str],
            user_id: int,
            custom_title: str,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "custom_title": custom_title,
        }
        params = serialize_clean(params)

        response = await self.api.request("setChatAdministratorCustomTitle", params)
        return response.get("ok", False)

    async def ban_chat_sender_chat(
            self,
            chat_id: Union[int, str],
            sender_chat_id: int,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id,
        }
        params = serialize_clean(params)

        response = await self.api.request("banChatSenderChat", params)
        return response.get("ok", False)

    async def unban_chat_sender_chat(
            self,
            chat_id: Union[int, str],
            sender_chat_id: int,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id,
        }
        params = serialize_clean(params)

        response = await self.api.request("unbanChatSenderChat", params)
        return response.get("ok", False)

    async def set_chat_permissions(
            self,
            chat_id: Union[int, str],
            permissions: ChatPermissions,
            *,
            use_independent_chat_permissions: Optional[bool] = None,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "permissions": permissions,
            "use_independent_chat_permissions": use_independent_chat_permissions,
        }
        params = serialize_clean(params)

        if "permissions" in params and params["permissions"] is not None:
            params["permissions"] = json.dumps(params["permissions"].to_dict())

        response = await self.api.request("setChatPermissions", params)
        return response.get("ok", False)

    async def export_chat_invite_link(
            self,
            chat_id: Union[int, str],
    ) -> str:
        params = {
            "chat_id": chat_id,
        }
        params = serialize_clean(params)

        response = await self.api.request("exportChatInviteLink", params)
        return response.get("result", "")

    async def create_chat_invite_link(
            self,
            chat_id: Union[int, str],
            *,
            name: Optional[str] = None,
            expire_date: Optional[int] = None,
            member_limit: Optional[int] = None,
            creates_join_request: Optional[bool] = None,
    ) -> ChatInviteLink:
        params = {
            "chat_id": chat_id,
            "name": name,
            "expire_date": expire_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }
        params = serialize_clean(params)

        response = await self.api.request("createChatInviteLink", params)
        return ChatInviteLink(**response.get("result", {}))

    async def edit_chat_invite_link(
            self,
            chat_id: Union[int, str],
            invite_link: str,
            *,
            name: Optional[str] = None,
            expire_date: Optional[int] = None,
            member_limit: Optional[int] = None,
            creates_join_request: Optional[bool] = None,
    ) -> ChatInviteLink:
        params = {
            "chat_id": chat_id,
            "invite_link": invite_link,
            "name": name,
            "expire_date": expire_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }
        params = serialize_clean(params)

        response = await self.api.request("editChatInviteLink", params)
        response = replace_reserved_keys(response)
        return ChatInviteLink(**response.get("result", {}))

    async def create_chat_subscription_invite_link(
            self,
            chat_id: Union[int, str],
            subscription_period: int,
            subscription_price: int,
            *,
            name: Optional[str] = None,
    ) -> ChatInviteLink:
        params = {
            "chat_id": chat_id,
            "name": name,
            "subscription_period": subscription_period,
            "subscription_price": subscription_price,
        }
        params = serialize_clean(params)

        response = await self.api.request("createChatSubscriptionInviteLink", params)
        response = replace_reserved_keys(response)
        return ChatInviteLink(**response.get("result", {}))

    async def edit_chat_subscription_invite_link(
            self,
            chat_id: Union[int, str],
            invite_link: str,
            *,
            name: Optional[str] = None,
    ) -> ChatInviteLink:
        params = {
            "chat_id": chat_id,
            "invite_link": invite_link,
            "name": name,
        }
        params = serialize_clean(params)

        response = await self.api.request("editChatSubscriptionInviteLink", params)
        response = replace_reserved_keys(response)
        return ChatInviteLink(**response.get("result", {}))

    async def revoke_chat_invite_link(
            self,
            chat_id: Union[int, str],
            invite_link: str,
    ) -> ChatInviteLink:
        params = {
            "chat_id": chat_id,
            "invite_link": invite_link,
        }
        params = serialize_clean(params)

        response = await self.api.request("revokeChatInviteLink", params)
        response = replace_reserved_keys(response)
        return ChatInviteLink(**response.get("result", {}))

    async def approve_chat_join_request(
            self,
            chat_id: Union[int, str],
            user_id: int,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
        }
        params = serialize_clean(params)

        response = await self.api.request("approveChatJoinRequest", params)
        return response.get("ok", False)

    async def decline_chat_join_request(
            self,
            chat_id: Union[int, str],
            user_id: int,
    ) -> bool:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
        }
        params = serialize_clean(params)

        response = await self.api.request("declineChatJoinRequest", params)
        return response.get("ok", False)

    async def set_chat_photo(self, chat_id: Union[int, str], photo: InputFile) -> bool:
        params = {"chat_id": chat_id}
        params = serialize_clean(params)
        with open(photo.file_path, 'rb') as file:
            params["photo"] = file
            response = await self.api.request("setChatPhoto", params)

        return response.get("ok", False)

    async def delete_chat_photo(self, chat_id: Union[int, str]) -> bool:
        params = {'chat_id': chat_id}
        params = serialize_clean(params)
        response = await self.api.request('deleteChatPhoto', params)
        return response.get('ok', False)
