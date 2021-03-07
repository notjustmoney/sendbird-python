from ...constants import HttpMethods
from ...model import convert_to_sendbird_model, has_error
from ...exceptions import SendbirdException

from ...api_client import ApiClient

from .api_resource import ApiResource


class CreatableApiResource(ApiResource):
    @classmethod
    def create(cls, api_token=None, **params):
        client = ApiClient(api_token)
        url = cls.class_url()
        response = client.request(HttpMethods.POST, url, params)
        instance, _ = convert_to_sendbird_model(response, cls)
        if has_error(instance):
            raise SendbirdException(instance)
        return instance
