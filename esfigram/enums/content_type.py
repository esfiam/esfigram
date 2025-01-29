from enum import Enum


class ContentType(str, Enum):
    """
    Represents a type of content in a message.

    Attributes:
        UNKNOWN: Unknown content type.
        ANY: Any content type.
        TEXT: Text message.
        ANIMATION: Animation (GIF or video).
        AUDIO: Audio message.
        DOCUMENT: Document message.
        PAID_MEDIA: Paid media message.
        PHOTO: Photo message.
        STICKER: Sticker message.
        STORY: Story message.
        VIDEO: Video message.
        VIDEO_NOTE: Video note message.
        VOICE: Voice message.
        CONTACT: Contact information.
        DICE: Dice roll.
        GAME: Game message.
        POLL: Poll message.
        VENUE: Venue location.
        LOCATION: Geographic location.
        NEW_CHAT_MEMBERS: New members added to chat.
        LEFT_CHAT_MEMBER: A member left the chat.
        NEW_CHAT_TITLE: Chat title changed.
        NEW_CHAT_PHOTO: Chat photo changed.
        DELETE_CHAT_PHOTO: Chat photo deleted.
        GROUP_CHAT_CREATED: Group chat created.
        SUPERGROUP_CHAT_CREATED: Supergroup chat created.
        CHANNEL_CHAT_CREATED: Channel chat created.
        MESSAGE_AUTO_DELETE_TIMER_CHANGED: Auto-delete timer changed.
        MIGRATE_TO_CHAT_ID: Migrated to another chat ID.
        MIGRATE_FROM_CHAT_ID: Migrated from another chat ID.
        PINNED_MESSAGE: Message pinned.
        INVOICE: Invoice message.
        SUCCESSFUL_PAYMENT: Successful payment message.
        REFUNDED_PAYMENT: Refunded payment message.
        USERS_SHARED: Shared users.
        CHAT_SHARED: Shared chats.
        CONNECTED_WEBSITE: Website connected.
        WRITE_ACCESS_ALLOWED: Write access allowed.
        PASSPORT_DATA: Passport data shared.
        PROXIMITY_ALERT_TRIGGERED: Proximity alert triggered.
        BOOST_ADDED: Chat boost added.
        CHAT_BACKGROUND_SET: Chat background set.
        FORUM_TOPIC_CREATED: Forum topic created.
        FORUM_TOPIC_EDITED: Forum topic edited.
        FORUM_TOPIC_CLOSED: Forum topic closed.
        FORUM_TOPIC_REOPENED: Forum topic reopened.
        GENERAL_FORUM_TOPIC_HIDDEN: General forum topic hidden.
        GENERAL_FORUM_TOPIC_UNHIDDEN: General forum topic unhidden.
        GIVEAWAY_CREATED: Giveaway created.
        GIVEAWAY: Giveaway message.
        GIVEAWAY_WINNERS: Giveaway winners announced.
        GIVEAWAY_COMPLETED: Giveaway completed.
        VIDEO_CHAT_SCHEDULED: Video chat scheduled.
        VIDEO_CHAT_STARTED: Video chat started.
        VIDEO_CHAT_ENDED: Video chat ended.
        VIDEO_CHAT_PARTICIPANTS_INVITED: Participants invited to video chat.
        WEB_APP_DATA: Data from a web app.
        USER_SHARED: User shared.
    """
    UNKNOWN = "unknown"
    ANY = "any"
    TEXT = "text"
    ANIMATION = "animation"
    AUDIO = "audio"
    DOCUMENT = "document"
    PAID_MEDIA = "paid_media"
    PHOTO = "photo"
    STICKER = "sticker"
    STORY = "story"
    VIDEO = "video"
    VIDEO_NOTE = "video_note"
    VOICE = "voice"
    CONTACT = "contact"
    DICE = "dice"
    GAME = "game"
    POLL = "poll"
    VENUE = "venue"
    LOCATION = "location"
    NEW_CHAT_MEMBERS = "new_chat_members"
    LEFT_CHAT_MEMBER = "left_chat_member"
    NEW_CHAT_TITLE = "new_chat_title"
    NEW_CHAT_PHOTO = "new_chat_photo"
    DELETE_CHAT_PHOTO = "delete_chat_photo"
    GROUP_CHAT_CREATED = "group_chat_created"
    SUPERGROUP_CHAT_CREATED = "supergroup_chat_created"
    CHANNEL_CHAT_CREATED = "channel_chat_created"
    MESSAGE_AUTO_DELETE_TIMER_CHANGED = "message_auto_delete_timer_changed"
    MIGRATE_TO_CHAT_ID = "migrate_to_chat_id"
    MIGRATE_FROM_CHAT_ID = "migrate_from_chat_id"
    PINNED_MESSAGE = "pinned_message"
    INVOICE = "invoice"
    SUCCESSFUL_PAYMENT = "successful_payment"
    REFUNDED_PAYMENT = "refunded_payment"
    USERS_SHARED = "users_shared"
    CHAT_SHARED = "chat_shared"
    CONNECTED_WEBSITE = "connected_website"
    WRITE_ACCESS_ALLOWED = "write_access_allowed"
    PASSPORT_DATA = "passport_data"
    PROXIMITY_ALERT_TRIGGERED = "proximity_alert_triggered"
    BOOST_ADDED = "boost_added"
    CHAT_BACKGROUND_SET = "chat_background_set"
    FORUM_TOPIC_CREATED = "forum_topic_created"
    FORUM_TOPIC_EDITED = "forum_topic_edited"
    FORUM_TOPIC_CLOSED = "forum_topic_closed"
    FORUM_TOPIC_REOPENED = "forum_topic_reopened"
    GENERAL_FORUM_TOPIC_HIDDEN = "general_forum_topic_hidden"
    GENERAL_FORUM_TOPIC_UNHIDDEN = "general_forum_topic_unhidden"
    GIVEAWAY_CREATED = "giveaway_created"
    GIVEAWAY = "giveaway"
    GIVEAWAY_WINNERS = "giveaway_winners"
    GIVEAWAY_COMPLETED = "giveaway_completed"
    VIDEO_CHAT_SCHEDULED = "video_chat_scheduled"
    VIDEO_CHAT_STARTED = "video_chat_started"
    VIDEO_CHAT_ENDED = "video_chat_ended"
    VIDEO_CHAT_PARTICIPANTS_INVITED = "video_chat_participants_invited"
    WEB_APP_DATA = "web_app_data"
    USER_SHARED = "user_shared"

    @classmethod
    def list_content_types(cls):
        """
        Returns a list of all available content types.

        Returns:
            list[str]: A list of all content type names.
        """
        return [content_type.value for content_type in cls]

