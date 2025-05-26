# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SessionInfoResponse", "APIKey", "OrgMember", "Project", "ProjectOrg", "ProjectOrgOrgMember"]


class APIKey(BaseModel):
    id: str
    """UUID identifier for the API key"""

    auto_id: float
    """Internal auto-incrementing ID for the API key"""

    created_at: str
    """Date and time when the API key was created"""

    deleted: bool
    """Flag indicating if the API key has been deleted"""

    deleted_at: Optional[str] = None
    """Date and time when the API key was deleted (if applicable)"""

    key: str
    """The actual API key value (usually only shown once during creation)"""

    name: str
    """User-defined name for the API key"""

    org_member_id: str
    """UUID identifier for the organization member who owns this API key"""

    project_id: str
    """Short, URL-friendly unique identifier for the associated project"""

    updated_at: str
    """Date and time when the API key was last modified"""


class OrgMember(BaseModel):
    id: str
    """UUID identifier for the organization member"""

    email: str
    """Email address of the authenticated user"""

    name: str
    """Display name of the authenticated user"""

    role: str
    """Access role of the authenticated user within the organization"""


class ProjectOrgOrgMember(BaseModel):
    id: str
    """UUID identifier for the organization member"""

    auto_id: float
    """Internal auto-incrementing ID for the organization member"""

    created_at: str
    """Date and time when the member was added to the organization"""

    deleted_at: Optional[str] = None
    """Date and time when the member was removed from the organization (if applicable)"""

    email: str
    """Email address of the organization member"""

    name: str
    """User-defined name for the organization member"""

    org_id: str
    """Organization UUID that this member belongs to"""

    role: str
    """Access role of the member within the organization"""

    updated_at: str
    """Date and time when the member was last modified"""

    metadata: Optional[object] = None
    """Optional custom metadata for the organization member"""


class ProjectOrg(BaseModel):
    id: str
    """Short, URL-friendly unique identifier for the organization"""

    name: str
    """User-defined name for the organization"""

    org_members: List[ProjectOrgOrgMember]
    """Array of members belonging to this organization"""

    plan: str
    """Current subscription plan level"""


class Project(BaseModel):
    id: str
    """UUID identifier for the project"""

    auto_id: float
    """Internal auto-incrementing ID for the project"""

    created_at: str
    """Date and time when the project was created"""

    deleted: bool
    """Flag indicating if the project has been deleted"""

    email: str
    """Email address used for project notifications"""

    event_webhook_url: Optional[str] = None
    """Endpoint URL for event webhook notifications"""

    is_new_webhook: bool
    """Flag indicating if the project uses the new webhook format"""

    last_subscribed_at: Optional[str] = None
    """Date and time when the project last subscribed to updates"""

    name: str
    """User-defined name for the project"""

    nano_id: str
    """Short, URL-friendly unique identifier for the project"""

    org: ProjectOrg
    """Organization details including members"""

    org_id: str
    """Organization UUID that this project belongs to"""

    triggers_enabled: bool
    """Flag indicating if triggers are enabled for this project"""

    updated_at: str
    """Date and time when the project was last modified"""

    webhook_secret: Optional[str] = None
    """Secret used to verify webhook signatures"""

    webhook_url: Optional[str] = None
    """Endpoint URL for trigger webhook notifications"""


class SessionInfoResponse(BaseModel):
    api_key: Optional[APIKey] = None
    """Details of the API key used for authentication (null if using session auth)"""

    org_member: OrgMember
    """Information about the authenticated user"""

    project: Optional[Project] = None
    """
    Details of the current active project (null if accessing with org-level
    credentials)
    """
