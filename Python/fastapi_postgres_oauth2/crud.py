from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: models.User, user: schemas.UserUpdate):
    db_user.email = user.email
    db_user.hashed_password = user.password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def get_pet_by_id(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

def update_pet(db: Session, db_pet: models.Pet, pet: schemas.PetUpdate):
    db_pet.name = pet.name
    db_pet.owner_id = pet.owner_id
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pet).offset(skip).limit(limit).all()