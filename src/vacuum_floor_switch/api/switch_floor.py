from enum import Enum
from typing import Annotated

from fastapi import APIRouter, Depends
from miio import DreameVacuum
from pydantic import BaseModel
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK

from ..settings import Settings, get_settings


class FloorEnum(str, Enum):
    lower = "lower"
    upper = "upper"

class Floor(BaseModel):
    floor: FloorEnum

router = APIRouter()

@router.put("/floor")
async def switch_floor(floor: Floor, settings: Annotated[Settings, Depends(get_settings)]) -> str:
    device = DreameVacuum(
        ip=settings.ip,
        token=settings.token
    )

    if floor.floor == FloorEnum.lower:
        map_id = settings.lower_floor_id
    else:
        map_id = settings.upper_floor_id

    value = f'{{"sm": {{}}, "mapid":{map_id}}}'

    try:
        response = str(device.raw_command(
            "action",
            {"did": settings.device_id, "siid":6, "aiid":2, "in":[{"piid":4, "value": value}]}
        ))
    except Exception as e:
        response = str(e)

    return response