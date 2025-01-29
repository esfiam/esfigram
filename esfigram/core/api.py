import aiohttp
from typing import Dict, Optional

from esfigram.core.exceptions import TelegramAPIError, UnknownError, ERROR_MAP, InternalServerError, \
    TooManyRequestsError, NotFoundError, ForbiddenError, UnauthorizedError, BadRequestError


class TelegramAPI:
    def __init__(self, token: str):
        self.token = token
        self.session: Optional[aiohttp.ClientSession] = None
        self.authentication = False
        self.offset = 0

        if not self.token:
            raise ValueError("Bot token is required.")

        self.base_url = f'https://api.telegram.org/bot{self.token}/'

    async def create_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

    async def close_session(self):
        if self.session and not self.session.closed:
            await self.session.close()

    async def validate_token(self) -> bool:
        if not self.authentication:
            try:
                response = await self.request(method="getMe", params={})
                if not response.get("ok"):
                    raise ValueError(
                        "Invalid token: The provided bot token is invalid. Please check your token and try again.")
                self.authentication = True
            except Exception as e:
                raise ValueError(f"Failed to validate token: {e}")
        return self.authentication

    import aiohttp
    from typing import Dict, Any

    async def request(self, method: str, params: Dict[str, Any]) -> Dict:

        await self.create_session()
        url = f'{self.base_url}{method}'

        is_multipart = any(hasattr(value, 'read') for value in params.values())

        try:
            if is_multipart:
                form_data = aiohttp.FormData()
                for key, value in params.items():
                    if hasattr(value, 'read'):
                        form_data.add_field(key, value, filename=getattr(value, 'name', key))
                    else:
                        form_data.add_field(key, str(value))
                data_to_send = {"data": form_data}

            else:
                data_to_send = {"json": params}

            async with self.session.post(url, **data_to_send) as response:
                data = await response.json()

                if data.get('ok'):
                    return data

                elif response.status == 400:
                    raise BadRequestError(
                        message=data.get('description'),
                        method=method,
                        params=params,
                        status_code=response.status
                    )
                elif response.status == 401:
                    raise UnauthorizedError(
                        message=data.get('Unauthorized access'),
                        method=method,
                        params=params,
                        status_code=response.status
                    )
                elif response.status == 403:
                    raise ForbiddenError(
                        message=data.get('description'),
                        method=method,
                        params=params,
                        status_code=response.status
                    )
                elif response.status == 404:
                    raise NotFoundError(
                        message=data.get('description'),
                        method=method,
                        params=params,
                        status_code=response.status
                    )
                elif response.status == 429:
                    retry_after = data.get('parameters', {}).get('retry_after')
                    raise TooManyRequestsError(
                        message=data.get('description'),
                        method=method,
                        params=params,
                        status_code=response.status,
                        retry_after=retry_after
                    )
                elif response.status == 500:
                    raise InternalServerError(
                        message=data.get('description'),
                        method=method,
                        params=params,
                        status_code=response.status
                    )

                else:
                    raise TelegramAPIError(
                        message=data.get('description'),
                        method=method,
                        params=params,
                        status_code=response.status
                    )

        except aiohttp.ClientError as e:
            raise aiohttp.ClientError(
                f"Network error during {method}: {str(e)} (Method: {method}, Params: {params})"
            )

        except Exception as e:
            raise TelegramAPIError(
                message=f"Unexpected error during {method}: {e}",
                method=method,
                params=params
            )


