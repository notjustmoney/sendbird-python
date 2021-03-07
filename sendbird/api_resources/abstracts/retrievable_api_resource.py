from ...api_client import ApiClient

from .api_resource import ApiResource


class RetrievableApiResource(ApiResource):
    @classmethod
    def retrieve(cls, pk=None, api_token=None, **params):
        client = ApiClient(api_token)
        instance = cls(pk, api_token, **params)
        instance.refresh(client)
        return instance
