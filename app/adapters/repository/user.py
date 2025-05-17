from sqlalchemy import select, update, delete

from app.adapters.schemas.user import UserCreateSchema
from app.domain.ports.repository.user import IUsersRepository
from app.infra.database.sql import Session
from app.infra.models.user import UserModel


class UserRepository(IUsersRepository):
    def __init__(self):
        self.session = Session()

    def register(self, data: UserCreateSchema):

        already_exists = self.find(username=data.username)
        if already_exists:
            return already_exists

        model = UserModel(**data.dict())
        self.session.add(model)
        self.session.commit()
        model.id
        self.session.close()
        return model

    def find(self, **kwargs):

        response = self.session.execute(
            select(UserModel).filter_by(**kwargs)
        ).scalar()

        self.session.close()
        return response

    def findall(self, **kwargs):
        response = self.session.execute(
            select(UserModel)
        ).scalars().all()

        self.session.close()
        return response

    def update(self, uid: int, **kwargs):
        self.session.execute(
            update(UserModel).values(**kwargs).filter_by(id=uid)
        )
        self.session.commit()
        self.session.close()

    def delete(self, id: int):
        self.session.execute(
            delete(UserModel).filter_by(id=id)
        )
        self.session.commit()
        self.session.close()