from .. import api_endpoints

from ..utils import get_random_hash
from ..constants import HttpMethods

from .channel import Channel


class GroupChannel(Channel):
    RESOURCE_NAME = "group_channel"

    @classmethod
    def create_couple(
        cls,
        user_ids: list,
        channel_url=None,
        conversation_id=None,
        api_token=None,
        **params,
    ):
        name = f"{user_ids[0]} {user_ids[1]} 매칭방"
        if channel_url is None:
            channel_url = f"MATCH_{get_random_hash()}"

        channel = super().create(
            name=name,
            user_ids=user_ids,
            channel_url=channel_url,
            api_token=api_token,
            **params,
        )

        payload = {}
        if conversation_id:
            # 일반 채팅방인 경우
            payload["isActive"] = "False"
            payload["conversation_id"] = str(conversation_id)
        else:
            # 랜덤 채팅방인 경우 isActive=True
            payload["isActive"] = "True"
            payload["isRandom"] = "True"

        channel.create_metadata(payload)
        return channel

    def list_members(self):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.LIST_MEMBERS
        return self.request(HttpMethods.GET, url)

    def check_if_member(self, **params):
        user_id = params.get("user_id")
        formatted_endpoint = api_endpoints.GROUP_CHANNEL.CHECK_IF_MEMBER.format(
            user_id=user_id
        )
        url = self.instantiate_url() + formatted_endpoint
        return self.request(HttpMethods.GET, url, params=params)["is_member"]

    def accept_invitation(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.ACCEPT_INVITATION
        return self.request(HttpMethods.PUT, url, params=params)

    def reject_invitation(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.REJECT_INVITATION
        return self.request(HttpMethods.PUT, url, params=params)

    def join(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.JOIN
        return self.request(HttpMethods.PUT, url, params=params)

    def leave(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.LEAVE
        self.request(HttpMethods.PUT, url, params=params)

    def hide(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.HIDE
        self.request(HttpMethods.PUT, url, params=params)

    def unhide(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.UNHIDE
        self.request(HttpMethods.DELETE, url, params=params)

    def reset_chat_history(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.RESET_CHAT_HISTORY
        self.request(HttpMethods.PUT, url, params=params)

    def invite_users(self, **params):
        url = self.instantiate_url() + api_endpoints.GROUP_CHANNEL.INVITE_USERS
        return self.request(HttpMethods.POST, url, params=params)
