# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionGetInfoResponse", "APIKey", "OrgMember", "Project", "ProjectOrg", "ProjectOrgOrgMember"]


class APIKey(BaseModel):
    id: str

    auto_id: float = FieldInfo(alias="autoId")

    created_at: str = FieldInfo(alias="createdAt")

    deleted: bool

    deleted_at: Optional[str] = FieldInfo(alias="deletedAt", default=None)

    key: str

    name: str

    org_member_id: str = FieldInfo(alias="orgMemberId")

    project_id: str = FieldInfo(alias="projectId")

    updated_at: str = FieldInfo(alias="updatedAt")


class OrgMember(BaseModel):
    id: str

    email: str

    name: str

    role: str


class ProjectOrgOrgMember(BaseModel):
    id: str

    auto_id: float = FieldInfo(alias="autoId")

    created_at: str = FieldInfo(alias="createdAt")

    deleted_at: Optional[str] = FieldInfo(alias="deletedAt", default=None)

    email: str

    name: str

    org_id: str = FieldInfo(alias="orgId")

    role: str

    updated_at: str = FieldInfo(alias="updatedAt")

    metadata: Optional[object] = None


class ProjectOrg(BaseModel):
    id: str

    name: str

    org_members: List[ProjectOrgOrgMember] = FieldInfo(alias="orgMembers")

    plan: str


class Project(BaseModel):
    id: str

    auto_id: float = FieldInfo(alias="autoId")

    created_at: str = FieldInfo(alias="createdAt")

    deleted: bool

    email: str

    event_webhook_url: Optional[str] = FieldInfo(alias="eventWebhookURL", default=None)

    is_new_webhook: bool = FieldInfo(alias="isNewWebhook")

    last_subscribed_at: Optional[str] = FieldInfo(alias="lastSubscribedAt", default=None)

    name: str

    nano_id: str = FieldInfo(alias="nanoId")

    org: ProjectOrg

    org_id: str = FieldInfo(alias="orgId")

    triggers_enabled: bool = FieldInfo(alias="triggersEnabled")

    updated_at: str = FieldInfo(alias="updatedAt")

    webhook_secret: Optional[str] = FieldInfo(alias="webhookSecret", default=None)

    webhook_url: Optional[str] = FieldInfo(alias="webhookURL", default=None)


class SessionGetInfoResponse(BaseModel):
    api_key: Optional[APIKey] = FieldInfo(alias="apiKey", default=None)

    org_member: OrgMember

    project: Optional[Project] = None
