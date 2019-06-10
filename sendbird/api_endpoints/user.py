# All endpoint constants for the User resource
USER_ADD_DEVICE_TOKEN = "/push/{token_type}"
USER_BLOCK = "/block"
USER_LIST_BANNED_CHANNELS = "/ban"
USER_LIST_BLOCKED_USERS = "/block"
USER_LIST_DEVICE_TOKENS = "/push/{token_type}"
USER_LIST_MUTED_CHANNELS = "/mute"
USER_MARK_AS_READ_ALL = "/mark_as_read_all"
USER_MY_GROUP_CHANNELS = "/my_group_channels"
USER_REMOVE_ALL_DEVICE_TOKENS = "/push"
USER_REMOVE_DEVICE_TOKEN = "/push/{token_type}/{token}"
USER_REMOVE_DEVICE_TOKEN_FROM_OWNER = "/push/device_tokens/{token_type}/{token}"
USER_RESET_PUSH_PREFERENCE = "/push_preference"
USER_UNBLOCK = "/block/{target_id}"
USER_UNREAD_ITEM_COUNT = "/unread_item_count"
USER_UNREAD_MESSAGE_COUNT = "/unread_message_count"
USER_UPDATE_CHANNEL_INVITE_PREFERENCE = "/channel_invitation_preference"
USER_UPDATE_PUSH_PREFERENCE = "/push_preference"
USER_VIEW_CHANNEL_INVITE_PREFERENCE = "/channel_invitation_preference"
USER_VIEW_DEVICE_TOKEN_OWNER = "/push/device_tokens/{token_type}/{token}"
USER_VIEW_PUSH_PREFERENCE = "/push_preference"
