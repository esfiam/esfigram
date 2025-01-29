from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.message_entity import MessageEntity
    from esfigram.types.link_preview_options import LinkPreviewOptions
    from esfigram.types.labeled_price import LabeledPrice


class InputMessageContent(BaseObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class InputTextMessageContent(InputMessageContent):
    def __init__(
            self,
            message_text: str,
            parse_mode: Optional[str] = None,
            entities: Optional[List[MessageEntity]] = None,
            link_preview_options: Optional[LinkPreviewOptions] = None,
    ) -> None:
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options
        super().__init__(
            message_text=message_text,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
        )


class InputLocationMessageContent(InputMessageContent):
    def __init__(
            self,
            latitude: float,
            longitude: float,
            horizontal_accuracy: Optional[float] = None,
            live_period: Optional[int] = None,
            heading: Optional[int] = None,
            proximity_alert_radius: Optional[int] = None,
    ) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        super().__init__(
            latitude=latitude,
            longitude=longitude,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
        )


class InputVenueMessageContent(InputMessageContent):
    def __init__(
            self,
            latitude: float,
            longitude: float,
            title: str,
            address: str,
            foursquare_id: Optional[str] = None,
            foursquare_type: Optional[str] = None,
            google_place_id: Optional[str] = None,
            google_place_type: Optional[str] = None,
    ) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        super().__init__(
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
        )


class InputContactMessageContent(InputMessageContent):
    def __init__(
            self,
            phone_number: str,
            first_name: str,
            last_name: Optional[str] = None,
            vcard: Optional[str] = None,
    ) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        super().__init__(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            vcard=vcard,
        )


class InputInvoiceMessageContent(InputMessageContent):
    def __init__(
            self,
            title: str,
            description: str,
            payload: str,
            provider_token: str,
            currency: str,
            prices: List[LabeledPrice],
            max_tip_amount: Optional[int] = 0,
            suggested_tip_amounts: Optional[List[int]] = None,
            provider_data: Optional[str] = None,
            photo_url: Optional[str] = None,
            photo_size: Optional[int] = None,
            photo_width: Optional[int] = None,
            photo_height: Optional[int] = None,
            need_name: Optional[bool] = False,
            need_phone_number: Optional[bool] = False,
            need_email: Optional[bool] = False,
            need_shipping_address: Optional[bool] = False,
            send_phone_number_to_provider: Optional[bool] = False,
            send_email_to_provider: Optional[bool] = False,
            is_flexible: Optional[bool] = False,
    ) -> None:
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible
        super().__init__(
            title=title,
            description=description,
            payload=payload,
            provider_token=provider_token,
            currency=currency,
            prices=prices,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
        )