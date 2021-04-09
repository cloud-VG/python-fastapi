from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

# Custom Imports
import schemas
import crud
from database import get_db


router = APIRouter(
    prefix='/audio',
    tags=['audio']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_audio(audio: schemas.Audio, db: Session = Depends(get_db)):
    return crud.create_audio(audio=audio, db=db)


@router.get('/{type_}', status_code=status.HTTP_200_OK)
def read_audios(type_: str, db: Session = Depends(get_db)):
    result = crud.read_audios(f_type=type_, db=db)
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Audio of Type: {type_} not available')
    return result


@router.get('/{type_}/{id_}', status_code=status.HTTP_200_OK)
def read_audio(type_: str, id_: int, db: Session = Depends(get_db)):
    result = crud.read_audio(f_type=type_, f_id=id_, db=db)
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Audio of Type: {type_} with Id: {id_} not available')
    return result


@router.put('/{type_}/{id_}', status_code=status.HTTP_202_ACCEPTED)
def update_audio(audio: schemas.Audio, type_: str, id_: int, db: Session = Depends(get_db)):
    result = crud.update_audio(audio=audio, f_type=type_, f_id=id_, db=db)
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Audio of Type: {type_} with Id: {id_} not available')
    return result


@router.delete('/{type_}/{id_}', status_code=status.HTTP_204_NO_CONTENT)
def delete_audio(type_: str, id_: int, db: Session = Depends(get_db)):
    result = crud.delete_audio(f_type=type_, f_id=id_, db=db)
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Audio of Type: {type_} with Id: {id_} not available')

