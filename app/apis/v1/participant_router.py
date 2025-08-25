from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from app.dtos.create_participant_request import CreateParticipantRequest
from app.dtos.create_participant_response import (
    CreateParticipantMysqlResponse,
    ParticipantDateMysql,
)
from app.service.meeting_service_mysql import service_get_meeting_mysql
from app.service.participant_service_mysql import (
    service_create_participant,
    service_delete_participant_mysql,
)

edgedb_router = APIRouter(prefix="/v1/edgedb/participants", tags=["Participant"])
mysql_router = APIRouter(prefix="/v1/mysql/participants", tags=["Participant"])


@mysql_router.post("", description="participant 를 생성합니다.")
async def api_create_participant_mysql(
    create_participant_request: CreateParticipantRequest,
) -> CreateParticipantMysqlResponse:
    meeting = await service_get_meeting_mysql(create_participant_request.meeting_url_code)

    if not meeting:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"meeting with url_code: {create_participant_request.meeting_url_code} not found",
        )

    if not (meeting.start_date and meeting.end_date):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="start and end should be set.",
        )

    participant, participant_dates = await service_create_participant(
        create_participant_request,
        meeting.start_date,
        meeting.end_date,
    )

    return CreateParticipantMysqlResponse(
        participant_id=participant.id,
        participant_dates=[ParticipantDateMysql(id=pd.id, date=pd.date) for pd in participant_dates],
    )


@mysql_router.delete(
    "/{participant_id}", description="participant 를 삭제합니다.", status_code=status.HTTP_204_NO_CONTENT
)
async def api_delete_participant_mysql(
    participant_id: int,
) -> None:
    deleted_participant_count = await service_delete_participant_mysql(participant_id)
    if not deleted_participant_count:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"participant with id: {participant_id} not found",
        )
