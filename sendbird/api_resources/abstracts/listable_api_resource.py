from ...api_client import ApiClient
from ...constants import HttpMethods
from ...model import convert_to_sendbird_model, has_error
from ...exceptions import SendbirdException

from .api_resource import ApiResource


class ListableApiResource(ApiResource):
    @classmethod
    def list(cls, api_token=None):
        client = ApiClient(api_token)
        url = cls.class_url()
        response = client.request(HttpMethods.GET, url)
        instance, _ = convert_to_sendbird_model(response, cls)

        if has_error(instance):
            raise SendbirdException(instance)
        return instance
