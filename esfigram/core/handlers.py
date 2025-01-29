from __future__ import annotations
import asyncio
from typing import Callable, Optional, Union, Awaitable, Any, List

from esfigram.core.utils import replace_reserved_keys
from esfigram.types import Message, CallbackQuery, Poll, PollAnswer, ChatMemberUpdated, ChatJoinRequest
from esfigram.types.chosen_inline_result import ChosenInlineResult
from esfigram.types.inline_query import InlineQuery
from esfigram.types.pre_checkout_query import PreCheckoutQuery
from esfigram.types.shipping_query import ShippingQuery

from esfigram.enums.update_type import UpdateType


class HandlerManager:
    def __init__(self, token: str):
        self.handlers: List[dict] = []
        self.token = token

    def add_handler(
            self,
            func: Callable[..., Awaitable[Any]],
            update_type: Optional[Union[str, UpdateType]] = None,
            filter_funcs: Optional[List[Callable[..., Awaitable[bool]]]] = None,
    ):
        if not callable(func):
            raise ValueError("Handler must be a callable function.")

        if not update_type:
            raise ValueError("An 'update_type' must be provided.")

        if isinstance(update_type, UpdateType):
            update_type = update_type.value
        if update_type not in UpdateType.list_update_types():
            raise ValueError(f"Invalid update type: {update_type}")

        if filter_funcs:
            if not isinstance(filter_funcs, list):
                raise ValueError("Filters must be provided as a list.")
            for filter_func in filter_funcs:
                if not callable(filter_func):
                    raise ValueError("All filter functions must be callable.")

            filter_funcs = list(set(filter_funcs))

        if any(handler["func"] == func for handler in self.handlers):
            raise ValueError(f"The handler function '{func.__name__}' has already been added.")

        self.handlers.append({
            "func": func,
            "update_type": update_type,
            "filter_funcs": filter_funcs or [],
        })

    async def handle_update(self, bot: Optional[Any], update: dict):
        UPDATE_TYPE_CLASS_MAP = {
            "message": Message,
            "edited_message": Message,
            "channel_post": Message,
            "edited_channel_post": Message,
            "inline_query": InlineQuery,
            "chosen_inline_result": ChosenInlineResult,
            "callback_query": CallbackQuery,
            "shipping_query": ShippingQuery,
            "pre_checkout_query": PreCheckoutQuery,
            "poll": Poll,
            "poll_answer": PollAnswer,
            "my_chat_member": ChatMemberUpdated,
            "chat_member": ChatMemberUpdated,
            "chat_join_request": ChatJoinRequest,
        }
        try:
            update = replace_reserved_keys(update)
            for handler in self.handlers:
                func = handler.get('func')
                update_type = handler.get('update_type')
                filter_funcs = handler.get('filter_funcs', [])

                if not func or not update_type or update_type not in update:
                    continue

                update_class = UPDATE_TYPE_CLASS_MAP.get(update_type)
                if not update_class:
                    continue

                update_instance = update_class(**update[update_type])

                if filter_funcs:
                    results = await asyncio.gather(
                        *(f(update_instance) if asyncio.iscoroutinefunction(f) else f(update_instance)
                          for f in filter_funcs),
                        return_exceptions=True
                    )
                    if not all(isinstance(r, bool) and r for r in results):
                        continue

                try:
                    if bot:
                        await func(bot, update_instance)
                    else:
                        await func(update_instance)
                except Exception as e:
                    print(f"Handler execution error in '{func.__name__}': {type(e).__name__}: {e}")

        except Exception as global_error:
            print(f"Global handler error: {type(global_error).__name__}: {global_error}")
