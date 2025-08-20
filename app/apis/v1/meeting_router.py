from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse

# 실전에서는 db url 적지않을것. 강의에서만 사용하는것
edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)


@edgedb_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.get(
    "/{meeting_url_code}",  # path variable
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    return GetMeetingResponse(url_code="abc")
