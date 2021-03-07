from __future__ import annotations

from typing import Any, List, Tuple, Union

from .response import SendbirdResponse


class SendbirdModel(dict):
    FIELD_PK_NAME = None

    def __init__(self, pk, api_token=None, **params):
        super().__init__()
        object.__setattr__(self, "api_token", api_token)

        if pk is None:
            raise Exception("SendbirdModel must be set pk")

        pk_field = self.get_pk_field()
        self[pk_field] = pk

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value

    def __getattr__(self, name: str):
        return self[name]

    @classmethod
    def get_pk_field(cls):
        return cls.FIELD_PK_NAME

    @classmethod
    def construct_from(
        cls: SendbirdModel, response: dict
    ) -> Tuple("SendbirdModel", bool):
        pk = response.get(cls.get_pk_field())
        if pk:
            instance = cls(pk)
            return instance.set_items_from_dict(response), True
        return response, False

    def set_items_from_dict(self, data):
        for k, v in data.items():
            super().__setitem__(k, v)
        return self


def convert_to_sendbird_model(
    response: Union(SendbirdResponse, List[SendbirdResponse], dict), cls: SendbirdModel
) -> Union(
    Tuple(SendbirdModel, True), Tuple(List[SendbirdModel], True), Tuple(Any, False)
):
    if isinstance(response, SendbirdResponse) and isinstance(response.data, dict):
        return cls.construct_from(response.data)
    if isinstance(response, SendbirdResponse) and not isinstance(response.data, dict):
        return response.data, False
    if isinstance(response, dict) and not isinstance(response, SendbirdResponse):
        return cls.construct_from(response)
    if isinstance(response, list):
        converted_list = [convert_to_sendbird_model(res, cls) for res in response]
        return [item[0] for item in converted_list], False
    raise Exception("Invalid parameter: cannot convert to SendbirdModel")


def has_error(instance):
    if isinstance(instance, dict) and instance.get("error", False):
        return True
    return False
