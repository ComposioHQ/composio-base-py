# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RealtimeCredentialsResponse"]


class RealtimeCredentialsResponse(BaseModel):
    project_id: str
    """The project nanoId associated with the API Key provided.

    Used as part of the CLI channel name: private-cli-{project_id}
    """

    pusher_cluster: str
    """The Pusher cluster for subscribing to the trigger"""

    pusher_key: str
    """The Pusher client key for subscribing to the trigger"""
