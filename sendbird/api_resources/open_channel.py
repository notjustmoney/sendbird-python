from .. import api_endpoints

from ..constants import HttpMethods

from . import Channel


class OpenChannel(Channel):
    RESOURCE_NAME = "open_channel"

    def list_participants(self):
        url = self.instantiate_url() + api_endpoints.OPEN_CHANNEL_LIST_PARTICIPANTS
        return self.request(HttpMethods.GET, url)
