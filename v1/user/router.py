from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from v1.user.schema import ResponseIsAdmin
from core.settings.database import get_db


router = APIRouter(prefix='/user', tags=['user'])
