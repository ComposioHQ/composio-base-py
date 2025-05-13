from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `composio.client.generated.resources` module.

    This is used so that we can lazily import `composio.client.generated.resources` only when
    needed *and* so that users can just import `composio.client.generated` and reference `composio.client.generated.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("composio.client.generated.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
