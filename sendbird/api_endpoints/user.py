# All endpoint constants for the User resource
ADD_DEVICE_TOKEN = "/push/{token_type}"
BAN_FROM_CHANNELS_WITH_CUSTOM_TYPES = "/banned_channel_custom_types"
BLOCK = "/block"
CHOOSE_PUSH_MESSAGE_TEMPLATE = "/push/template"
LIST_BANNED_CHANNELS = "/ban"
LIST_BLOCKED_USERS = "/block"
LIST_DEVICE_TOKENS = "/push/{token_type}"
LIST_MUTED_CHANNELS = "/mute"
MARK_AS_READ_ALL = "/mark_as_read_all"
MUTE_FROM_CHANNELS_WITH_CUSTOM_TYPES = "/muted_channel_custom_types"
MY_GROUP_CHANNELS = "/my_group_channels"
REGISTER_OPERATOR_CHANNELS_CUSTOM_TYPES = "/operating_channel_custom_types"
REMOVE_ALL_DEVICE_TOKENS = "/push"
REMOVE_DEVICE_TOKEN = "/push/{token_type}/{token}"
REMOVE_DEVICE_TOKEN_FROM_OWNER = "/push/device_tokens/{token_type}/{token}"
RESET_PUSH_PREFERENCE = "/push_preference"
UNBLOCK = "/block/{target_id}"
UNREAD_CHANNEL_COUNT = "/unread_channel_count"
UNREAD_ITEM_COUNT = "/unread_item_count"
UNREAD_MESSAGE_COUNT = "/unread_message_count"
UPDATE_CHANNEL_INVITE_PREFERENCE = "/channel_invitation_preference"
UPDATE_COUNT_PREFERENCE_OF_CHANNEL = "/count_preference/{channel_url}"
UPDATE_PUSH_PREFERENCE = "/push_preference"
UPDATE_PUSH_PREFERENCE_FOR_CHANNEL = "/push_preference/{channel_url}"
VIEW_CHANNEL_INVITE_PREFERENCE = "/channel_invitation_preference"
COUNT_PREFERENCE_OF_CHANNEL = "/count_preference/{channel_url}"
VIEW_DEVICE_TOKEN_OWNER = "/push/device_tokens/{token_type}/{token}"
VIEW_GROUP_CHANNEL_COUNT_BY_JOIN_STATUS = "/group_channel_count"
VIEW_PUSH_PREFERENCE = "/push_preference"
VIEW_PUSH_PREFERENCE_FOR_CHANNEL = "/push_preference/{channel_url}"

CREATE_METADATA = "/metadata"
DELETE_METADATA = "/metadata"
UPDATE_METADATA = "/metadata"
VIEW_METADATA = "/metadata"
