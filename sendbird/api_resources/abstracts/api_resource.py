import abc

import sendbird
from ...api_client import ApiClient
from ...model import SendbirdModel, convert_to_sendbird_model, has_error
from ...exceptions import SendbirdException
from ...constants import HttpMethods


class ApiResource(SendbirdModel):
    def refresh(self, client: ApiClient = None):
        if client is None:
            client = ApiClient(self.api_token)
        response = client.request(HttpMethods.GET, self.instantiate_url())
        instance, is_converted = convert_to_sendbird_model(response, self.__class__)
        if has_error(instance):
            raise SendbirdException(instance)
        if is_converted:
            self.set_items_from_dict(instance)
            return self
        return instance

    @classmethod
    def class_url(cls):
        if cls == ApiResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform actions on its subclasses (e.g. Message)"
            )

        return f"{cls.RESOURCE_NAME}s"

    @abc.abstractmethod
    def instantiate_url(self):
        raise NotImplementedError(
            "APIResource is an abstract class. You should perform actions on its subclasses (e.g. Message)"
        )

    @classmethod
    def static_request(cls, method, url, api_token=None, params=None):
        client = ApiClient(api_token or sendbird.api_token)
        response = client.request(method, url, params)
        instance, _ = convert_to_sendbird_model(response, cls)

        if has_error(instance):
            raise SendbirdException(instance)
        return instance

    def request(self, method, url, params=None):
        client = ApiClient(self.api_token)
        response = client.request(method, url, params)
        instance, _ = convert_to_sendbird_model(response, self.__class__)

        if has_error(instance):
            raise SendbirdException(instance)
        return instance
