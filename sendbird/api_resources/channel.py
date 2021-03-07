from .. import api_endpoints

from ..constants import HttpMethods

from .abstracts import (
    RetrievableApiResource,
    CreatableApiResource,
    DeletableApiResource,
    ListableApiResource,
    UpdatableApiResource,
)


class Channel(
    RetrievableApiResource,
    CreatableApiResource,
    DeletableApiResource,
    ListableApiResource,
    UpdatableApiResource,
):
    FIELD_PK_NAME = "channel_url"

    def instantiate_url(self):
        pk = self.get(Channel.FIELD_PK_NAME)
        base = self.class_url()
        return f"{base}/{pk}"

    def freeze(self, freeze=False):
        url = self.instantiate_url() + api_endpoints.CHANNEL.FREEZE
        params = {
            "freeze": freeze,
        }
        return self.request(HttpMethods.PUT, url, params=params)

    def ban_user(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.BAN_USER
        return self.request(HttpMethods.POST, url, params=params)

    def unban_user(self, **params):
        banned_user_id = params.get("banned_user_id")
        formatted_endpoint = api_endpoints.CHANNEL.UNBAN_USER.format(
            banned_user_id=banned_user_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.DELETE, url, params=params)

    def update_ban(self, **params):
        banned_user_id = params.get("banned_user_id")
        formatted_endpoint = api_endpoints.CHANNEL.UPDATE_BAN.format(
            banned_user_id=banned_user_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.PUT, url, params=params)

    def list_banned_users(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.LIST_BANNED_USERS
        return self.request(HttpMethods.GET, url, params=params)

    def view_ban(self, **params):
        banned_user_id = params.get("banned_user_id")
        formatted_endpoint = api_endpoints.CHANNEL.VIEW_BAN.format(
            banned_user_id=banned_user_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url, params=params)

    def mute_user(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.MUTE_USER
        return self.request(HttpMethods.POST, url, params=params)

    def unmute_user(self, **params):
        muted_user_id = params.get("muted_user_id")
        formatted_endpoint = api_endpoints.CHANNEL.UNMUTE_USER.format(
            muted_user_id=muted_user_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.DELETE, url, params=params)

    def list_muted_users(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.LIST_MUTED_USERS
        return self.request(HttpMethods.GET, url, params=params)

    def view_mute(self, **params):
        muted_user_id = params.get("muted_user_id")
        formatted_endpoint = api_endpoints.CHANNEL.VIEW_MUTE.format(
            muted_user_id=muted_user_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url, params=params)

    # TODO: Convert usage to channel.messages.list()
    def list_messages(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.LIST_MESSAGES
        return self.request(HttpMethods.GET, url, params=params)

    # TODO: Convert usage to channel.messages.send()
    def send_text_message(self, **params):
        params["message_type"] = "MESG"

        url = self.instantiate_url() + api_endpoints.CHANNEL.SEND_MESSAGE
        return self.request(HttpMethods.POST, url, params=params)

    # TODO: Convert usage to channel.messages.retrieve()
    def view_message(self, **params):
        message_id = params.get("message_id")
        formatted_endpoint = api_endpoints.CHANNEL.VIEW_MESSAGE.format(
            message_id=message_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url, params=params)

    # TODO: Convert usage to message.update()
    def update_text_message(self, **params):
        message_id = params.get("message_id")
        formatted_endpoint = api_endpoints.CHANNEL.UPDATE_MESSAGE.format(
            message_id=message_id
        )

        params["message_type"] = "MESG"

        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.PUT, url, params=params)

    # TODO: Convert usage to message.delete()
    def delete_message(self, **params):
        message_id = params.get("message_id")
        formatted_endpoint = api_endpoints.CHANNEL.DELETE_MESSAGE.format(
            message_id=message_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.DELETE, url, params=params)

    # TODO: Convert usage to channel.messages.count()
    def view_message_count(self):
        url = self.instantiate_url() + api_endpoints.CHANNEL.VIEW_MESSAGE_COUNT
        return self.request(HttpMethods.GET, url).total

    def view_unread_messages_count(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.VIEW_MEMBER_UNNREAD_COUNT

        user_ids = params.get("user_ids")
        if user_ids:
            url += "?user_ids={user_ids}".format(user_ids=user_ids)

        return self.request(HttpMethods.GET, url).unread

    def mark_as_read(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.MARK_AS_READ
        return self.request(HttpMethods.PUT, url, params=params)

    def view_metadata(self):
        url = self.instantiate_url() + api_endpoints.CHANNEL.VIEW_METADATA
        return self.request(HttpMethods.GET, url)

    def create_metadata(self, metadata=None):
        url = self.instantiate_url() + api_endpoints.CHANNEL.CREATE_METADATA
        params = {
            "metadata": metadata,
        }
        return self.request(HttpMethods.POST, url, params=params)

    def update_metadata(self, metadata):
        url = self.instantiate_url() + api_endpoints.CHANNEL.UPDATE_METADATA
        params = {"metadata": metadata}
        return self.request(HttpMethods.PUT, url, params=params)

    def delete_metadata(self, key=None) -> None:
        url = self.instantiate_url() + api_endpoints.CHANNEL.DELETE_METADATA
        if key:
            url += "/{key}".format(key=key)
        self.request(HttpMethods.DELETE, url)

    def view_metacounter(self):
        url = self.instantiate_url() + api_endpoints.CHANNEL.VIEW_METACOUNTER
        return self.request(HttpMethods.GET, url)

    def create_metacounter(self, metacounter=None):
        url = self.instantiate_url() + api_endpoints.CHANNEL.CREATE_METACOUNTER
        params = {
            "metacounter": metacounter,
        }
        return self.request(HttpMethods.POST, url, params)

    def update_metacounter(self, **params):
        url = self.instantiate_url() + api_endpoints.CHANNEL.UPDATE_METACOUNTER
        return self.request(HttpMethods.PUT, url, params=params)

    def delete_metacounter(self, key=None):
        url = self.instantiate_url() + api_endpoints.CHANNEL.DELETE_METACOUNTER
        if key:
            url += "/{key}".format(key=key)
        return self.request(HttpMethods.DELETE, url)

    def create_or_update_metadata(self, metadata):
        input_metadata = metadata
        retrieved_metadata = self.view_metadata()

        new_items = set(input_metadata) - set(retrieved_metadata)
        old_items = set(input_metadata) - set(new_items)

        new_metadata = {k: v for k, v in input_metadata.items() if k in new_items}
        old_metadata = {k: v for k, v in input_metadata.items() if k in old_items}

        self.create_metadata(new_metadata)
        self.update_metadata(old_metadata)
