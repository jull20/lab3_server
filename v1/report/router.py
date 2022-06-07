from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix='/report', tags=['report'])


@router.get(
    path='/',
    summary="Получить отчеты по продажам в виде файла",
    response_model=None,
)
async def get_csv_file_with_orders_report(
    # TODO: db and userSession here
):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not implemented")