from ...api_client import ApiClient
from ...constants import HttpMethods
from ...model import convert_to_sendbird_model, has_error
from ...exceptions import SendbirdException

from .api_resource import ApiResource


class UpdatableApiResource(ApiResource):
    def update(self, api_token=None, **params):
        client = ApiClient(api_token)
        url = self.instantiate_url()
        response = client.request(HttpMethods.PUT, url, params)
        instance, _ = convert_to_sendbird_model(response, self.__class__)

        if has_error(instance):
            raise SendbirdException(instance)
        return instance
