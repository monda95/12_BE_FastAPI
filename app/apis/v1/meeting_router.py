import uuid
from datetime import datetime
from typing import Dict

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.dtos.get_meeting_response import GetMeetingResponse
from app.dtos.update_meeting_request import UpdateMeetingDateRangeRequest
from app.service.meeting_service_mysql import service_get_meeting_mysql
from app.tortoise_models.meeting import MeetingModel

# 실전에서는 db url 적지않을것. 강의에서만 사용하는것

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)


@mysql_router.post("")
async def create_meeting_mysql() -> Dict[str, str]:
    url_code = str(uuid.uuid4())[:8]

    await MeetingModel.create_meeting(url_code=url_code)

    return {"url_code": url_code}


@mysql_router.get(
    "/{meeting_url_code}",  # path variable
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    meeting = await service_get_meeting_mysql(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return GetMeetingResponse(
        url_code=meeting.url_code,
        start_date=datetime.now().date(),
        end_date=datetime.now().date(),
        title="test",
        location="test",
    )


@mysql_router.patch("/{meeting_url_code}/date_range", description="meeting 의 날짜 range 를 설정합니다.")
async def api_update_meeting_date_range_mysql(
    meeting_url_code: str, update_meeting_date_range_request: UpdateMeetingDateRangeRequest
) -> GetMeetingResponse:
    return GetMeetingResponse(
        url_code="abc",
        start_date=datetime.now().date(),
        end_date=datetime.now().date(),
        title="test",
        location="test",
    )
