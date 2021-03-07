from .abstracts import (
    RetrievableApiResource,
    CreatableApiResource,
    ListableApiResource,
    DeletableApiResource,
    UpdatableApiResource,
)


class Message(
    RetrievableApiResource,
    CreatableApiResource,
    ListableApiResource,
    DeletableApiResource,
    UpdatableApiResource,
):
    RESOURCE_NAME = "message"
    FIELD_PK_NAME = "message_id"

    def instantiate(self):
        pass
