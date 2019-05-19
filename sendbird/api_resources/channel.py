from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.deletable_api_resource import DeletableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.updatable_api_resource import UpdatableAPIResource  # NOQA


class Channel(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource
):
    FIELD_PK = "channel_url"

    def instance_url(self):
        pk = self.get(self.FIELD_PK)

        base = self.class_url()
        return "{base}/{pk}".format(
            base=base,
            pk=pk
        )
