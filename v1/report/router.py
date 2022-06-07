from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/report', tags=['report'])

@router.get(
    path='/'
)
async def get_csv_file_with_orders_report():
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")