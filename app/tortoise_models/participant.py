from __future__ import annotations

from typing import TYPE_CHECKING

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel

if TYPE_CHECKING:
    from app.tortoise_models.meeting import MeetingModel
    from app.tortoise_models.participant_date import ParticipantDateModel


class ParticipantModel(BaseModel, Model):
    name = fields.CharField(max_length=255)
    meeting: fields.ForeignKeyRelation[MeetingModel] = fields.ForeignKeyField(
        "models.MeetingModel",
        related_name="participants",
        db_constraint=False,
        on_delete=fields.CASCADE,
        to_field="url_code",
        index=True,
    )
    meeting_id: str
    participant_dates: fields.ReverseRelation[ParticipantDateModel]

    class Meta:
        table = "participants"

    @classmethod
    async def create_participant(cls, name: str, meeting_url_code: str) -> ParticipantModel:
        return await cls.create(name=name, meeting_id=meeting_url_code)

    @classmethod
    async def delete_by_id(cls, participant_id: int) -> int:
        return await cls.filter(id=participant_id).delete()
