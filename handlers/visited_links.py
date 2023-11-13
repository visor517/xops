from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
def read_visited_links():
    return "Ok"
