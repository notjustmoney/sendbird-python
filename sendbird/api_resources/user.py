from .. import api_endpoints

from ..constants import HttpMethods
from ..decorators.method import instancemethod

from .constants import unread_count_preferences
from .abstracts import (
    RetrievableApiResource,
    CreatableApiResource,
    DeletableApiResource,
    ListableApiResource,
    UpdatableApiResource,
)


class User(
    RetrievableApiResource,
    CreatableApiResource,
    DeletableApiResource,
    ListableApiResource,
    UpdatableApiResource,
):
    RESOURCE_NAME = "user"

    FIELD_PK_NAME = "user_id"
    FIELD_PROFILE_URL = "profile_url"
    DEFAULT_PROFILE_URL = ""

    @classmethod
    def create(
        cls,
        email: str,
        nickname: str,
        api_token=None,
        **params,
    ):
        profile_url = params.get(cls.FIELD_PROFILE_URL, cls.DEFAULT_PROFILE_URL)
        params[cls.FIELD_PROFILE_URL] = profile_url
        return super(User, cls).create(
            user_id=email,
            nickname=nickname,
            api_token=api_token,
            issue_access_token="true",
            **params,
        )

    @classmethod
    def view_device_token_owner(cls, **params):
        formatted_endpoint = api_endpoints.USER.VIEW_DEVICE_TOKEN_OWNER.format(
            token_type=params.get("token_type"), token=params.get("token")
        )

        resp = User.static_request(HttpMethods.GET, formatted_endpoint)
        if hasattr(resp, "error"):
            return resp
        return resp[0].user_id

    @classmethod
    def remove_device_token_from_owner(cls, **params):
        formatted_endpoint = api_endpoints.USER.REMOVE_DEVICE_TOKEN_FROM_OWNER.format(
            token_type=params.get("token_type"), token=params.get("token")
        )

        resp = User.static_request(HttpMethods.DELETE, formatted_endpoint)
        if hasattr(resp, "error"):
            return resp
        return resp[0].user_id

    @classmethod
    def view_access_token(cls, email):
        user = cls.retrieve(email)
        return user["access_token"]

    @classmethod
    def retrieve_or_create(cls, email, nickname):
        try:
            user = cls.retrieve(email)
        except Exception:
            user = cls.create(email, nickname)
        return user

    @instancemethod
    def instantiate_url(self):
        pk = self.get(User.FIELD_PK_NAME)
        base = self.class_url()
        return f"{base}/{pk}"

    @instancemethod
    def list_group_channels(self):
        url = self.instantiate_url() + api_endpoints.USER.MY_GROUP_CHANNELS
        return self.request(HttpMethods.GET, url)

    def unread_message_count(self):
        url = self.instantiate_url() + api_endpoints.USER.UNREAD_MESSAGE_COUNT
        return self.request(HttpMethods.GET, url).get("unread_count")

    def unread_item_count(self, params=None):
        url = self.instantiate_url() + api_endpoints.USER.UNREAD_ITEM_COUNT
        return self.request(HttpMethods.GET, url, params=params)

    def mark_all_messages_as_read(self, params=None):
        url = self.instantiate_url() + api_endpoints.USER.MARK_AS_READ_ALL
        self.request(HttpMethods.PUT, url, params=params)

    def block(self, **params):
        url = self.instantiate_url() + api_endpoints.USER.BLOCK
        return self.request(HttpMethods.POST, url, params=params)

    def list_blocked_users(self, **params):
        url = self.instantiate_url() + api_endpoints.USER.LIST_BLOCKED_USERS
        return self.request(HttpMethods.GET, url, params=params)

    def unblock(self, target_id=None):
        formatted_endpoint = api_endpoints.USER.UNBLOCK.format(target_id=target_id)
        url = self.instantiate_url() + formatted_endpoint
        self.request(HttpMethods.DELETE, url)

    def add_device_token(self, **params):
        formatted_endpoint = api_endpoints.USER.ADD_DEVICE_TOKEN.format(
            token_type=params.get("token_type")
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.POST, url, params=params)

    def list_device_tokens(self, token_type=None):
        formatted_endpoint = api_endpoints.USER.LIST_DEVICE_TOKENS.format(
            token_type=token_type
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url)

    def remove_device_token(self, **params):
        formatted_endpoint = api_endpoints.USER.REMOVE_DEVICE_TOKEN.format(
            token_type=params.get("token_type"), token=params.get("token")
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.DELETE, url)

    def remove_all_device_tokens(self):
        url = self.instantiate_url() + api_endpoints.USER.REMOVE_ALL_DEVICE_TOKENS
        return self.request(HttpMethods.DELETE, url)

    def view_push_preference(self):
        url = self.instantiate_url() + api_endpoints.USER.VIEW_PUSH_PREFERENCE
        return self.request(HttpMethods.GET, url)

    def update_push_preference(self, **params):
        url = self.instantiate_url() + api_endpoints.USER.UPDATE_PUSH_PREFERENCE
        return self.request(HttpMethods.PUT, url, params=params)

    def reset_push_preference(self):
        url = self.instantiate_url() + api_endpoints.USER.RESET_PUSH_PREFERENCE
        self.request(HttpMethods.DELETE, url)

    def view_push_preference_for_channel(self, **params):
        formatted_endpoint = api_endpoints.USER.VIEW_PUSH_PREFERENCE_FOR_CHANNEL.format(
            channel_url=params.get("channel_url")
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url)

    def update_push_preference_for_channel(self, **params):
        formatted_endpoint = (
            api_endpoints.USER.UPDATE_PUSH_PREFERENCE_FOR_CHANNEL.format(
                channel_url=params.get("channel_url")
            )
        )

        enable = params.get("enable", True)
        params["enable"] = enable

        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.PUT, url, params)

    def list_muted_channels(self):
        url = self.instantiate_url() + api_endpoints.USER.LIST_MUTED_CHANNELS
        return self.request(HttpMethods.GET, url)

    def list_banned_channels(self):
        url = self.instantiate_url() + api_endpoints.USER.LIST_BANNED_CHANNELS
        return self.request(HttpMethods.GET, url)

    def view_channel_invite_preference(self):
        url = self.instantiate_url() + api_endpoints.USER.VIEW_CHANNEL_INVITE_PREFERENCE
        return self.request(HttpMethods.GET, url)

    def update_channel_invite_preference(self, auto_accept=True):
        url = (
            self.instantiate_url() + api_endpoints.USER.UPDATE_CHANNEL_INVITE_PREFERENCE
        )
        params = {
            "auto_accept": auto_accept,
        }
        return self.request(HttpMethods.PUT, url, params=params)

    def choose_push_message_template(self, **params):
        url = self.instantiate_url() + api_endpoints.USER.CHOOSE_PUSH_MESSAGE_TEMPLATE
        return self.request(HttpMethods.PUT, url, params=params)

    def view_unread_channel_count(self, **params) -> int:
        url = self.instantiate_url() + api_endpoints.USER.UNREAD_CHANNEL_COUNT
        return self.request(HttpMethods.GET, url, params=params)["unread_count"]

    def view_group_channel_count_by_join_status(self, **params) -> int:
        url = (
            self.instantiate_url()
            + api_endpoints.USER.VIEW_GROUP_CHANNEL_COUNT_BY_JOIN_STATUS
        )
        return self.request(HttpMethods.GET, url, params=params)["group_channel_count"]

    def view_count_preference_of_channel(self, channel_url=None):
        formatted_endpoint = api_endpoints.USER.COUNT_PREFERENCE_OF_CHANNEL.format(
            channel_url=channel_url
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url)["count_preference"]

    def update_count_preference_of_channel(self, **params):
        formatted_endpoint = (
            api_endpoints.USER.UPDATE_COUNT_PREFERENCE_OF_CHANNEL.format(
                channel_url=params.get("channel_url")
            )
        )

        count_preference = params.get("count_preference", unread_count_preferences.ALL)
        params["count_preference"] = count_preference

        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.PUT, url, params=params)["count_preference"]

    def ban_from_channel_with_custom_types(self, channel_custom_types=[]):
        url = (
            self.instantiate_url()
            + api_endpoints.USER.BAN_FROM_CHANNELS_WITH_CUSTOM_TYPES
        )
        params = {
            "channel_custom_types": channel_custom_types,
        }
        self.request(HttpMethods.POST, url, params=params)

    def mute_from_channel_with_custom_types(self, channel_custom_types=[]):
        url = (
            self.instantiate_url()
            + api_endpoints.USER.MUTE_FROM_CHANNELS_WITH_CUSTOM_TYPES
        )
        params = {
            "channel_custom_types": channel_custom_types,
        }
        self.request(HttpMethods.POST, url, params=params)

    def register_operator_channels_custom_types(self, channel_custom_types=[]):
        url = (
            self.instantiate_url()
            + api_endpoints.USER.REGISTER_OPERATOR_CHANNELS_CUSTOM_TYPES
        )
        params = {
            "channel_custom_types": channel_custom_types,
        }
        self.request(HttpMethods.POST, url, params=params)

    def view_metadata(self):
        url = self.instantiate_url() + api_endpoints.USER.VIEW_METADATA
        return self.request(HttpMethods.GET, url)

    def create_metadata(self, metadata):
        url = self.instantiate_url() + api_endpoints.USER.CREATE_METADATA
        params = {
            "metadata": metadata,
        }
        return self.request(HttpMethods.POST, url, params=params)

    def update_metadata(self, metadata):
        url = self.instantiate_url() + api_endpoints.USER.UPDATE_METADATA
        params = {"metadata": metadata}
        return self.request(HttpMethods.PUT, url, params=params)

    def delete_metadata(self, key=None):
        url = self.instantiate_url() + api_endpoints.USER.DELETE_METADATA
        if key:
            url += "/{key}".format(key=key)
        self.request(HttpMethods.DELETE, url)

    def create_or_update_metadata(self, metadata):
        input_metadata = metadata
        retrieved_metadata = self.view_metadata()

        new_items = set(input_metadata) - set(retrieved_metadata)
        old_items = set(input_metadata) - set(new_items)

        new_metadata = {k: v for k, v in input_metadata.items() if k in new_items}
        old_metadata = {k: v for k, v in input_metadata.items() if k in old_items}

        self.create_metadata(new_metadata)
        self.update_metadata(old_metadata)
