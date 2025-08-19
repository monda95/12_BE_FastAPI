from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.apis.v1.meeting_router import edgedb_router as meeting_router
from app.apis.v1.meeting_router import mysql_router as mysql_router
from app.configs.tortoise_cconfig import initialize_tortoise

app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(meeting_router)
app.include_router(mysql_router)

initialize_tortoise(app)
