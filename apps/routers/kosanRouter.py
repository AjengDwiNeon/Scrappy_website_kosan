import json
from fastapi import APIRouter, Body, Response
#from apps.controllers.LoanController import ControllerLoan as loan
from apps.controllers.KosanController import ControllerKosan as kosan

router = APIRouter()
@router.get("/how_to_scrap")
async def how_to_scrap(response: Response):
    result = kosan.how_to_scrap()
    response.status_code = result.status
    return result

@router.get("/getdetail")
async def getdetail(response: Response):
    result = kosan.getdetail()
    #response.status_code = result.status
    return result

@router.post("/simpan_data")
async def simpan_data(response: Response):
    result = kosan.simpan_data()
    #response.status_code = result.status
    return result
