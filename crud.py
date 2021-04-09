import models
import schemas

from sqlalchemy.orm import Session
from datetime import datetime

types = {
    'song': models.Song,
    'podcast': models.Podcast,
    'audiobook': models.AudioBook
}


def read_audio(f_type: str, f_id: int, db: Session):
    if f_type in types:
        return db.query(types[f_type]).filter(types[f_type].id == f_id).first()


def read_audios(f_type: str, db: Session):
    if f_type in types:
        return db.query(types[f_type]).all()


def create_audio(audio: schemas.Audio, db: Session):
    new_audio = None
    if audio.type == 'song':
        new_audio = models.Song(id=audio.id,
                                name=audio.name,
                                duration=audio.duration,
                                time=datetime.now())

    elif audio.type == 'podcast':
        if audio.host and audio.participants:
            participants = ','.join(audio.participants)
            new_audio = models.Podcast(id=audio.id,
                                       name=audio.name,
                                       duration=audio.duration,
                                       time=datetime.now(),
                                       host=audio.host,
                                       participants=participants)

    elif audio.type == 'audiobook':
        if audio.author and audio.narrator:
            new_audio = models.AudioBook(id=audio.id,
                                         name=audio.name,
                                         duration=audio.duration,
                                         time=datetime.now(),
                                         author=audio.author,
                                         narrator=audio.narrator)
    if new_audio:
        db.add(new_audio)
        db.commit()
        return new_audio


def delete_audio(f_type: str, f_id: int, db: Session):
    if f_type in types:
        data = db.query(types[f_type]).filter(types[f_type].id == f_id).first()
        if data:
            db.query(types[f_type]).filter(types[f_type].id == f_id).delete()
            return data


def update_audio(audio: schemas.Audio, f_type: str, f_id: int, db: Session):
    if f_type in types:
        data = db.query(types[f_type]).filter(types[f_type].id == f_id).first()
        flag = 0
        if data:
            if audio.type == 'song':
                db.query(types[f_type]).filter(types[f_type].id == f_id).update({
                    'name': audio.name,
                    'duration': audio.duration,
                    'time': datetime.now()
                })

                db.commit()
                flag = 1

            elif audio.type == 'podcast':
                if audio.host and audio.participants:
                    participants = ','.join(audio.participants)

                    db.query(types[f_type]).filter(types[f_type].id == f_id).update({
                        'name': audio.name,
                        'duration': audio.duration,
                        'time': datetime.now(),
                        'host': audio.host,
                        'participants': participants
                    })
                    db.commit()
                    flag = 1

            elif audio.type == 'audiobook':
                if audio.author and audio.narrator:
                    db.query(types[f_type]).filter(types[f_type].id == f_id).update({
                        'name': audio.name,
                        'duration': audio.duration,
                        'time': datetime.now(),
                        'author': audio.author,
                        'narrator': audio.narrator
                    })
                    db.commit()
                    flag = 1
        if flag:
            return db.query(types[f_type]).filter(types[f_type].id == f_id).first()
