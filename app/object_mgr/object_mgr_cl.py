import random

from sqlalchemy import select

from app import db as db
from app.exceptions import WrongObject, NotFoundObject
from app.models.object import Object


class ObjectMgr:
    """This class provides methods to manage a pool of objects."""
    @staticmethod
    def init_object_pool(objects_in_pool):
        """Initialize objects pool"""
        objects = [Object(value=i) for i in range(1, objects_in_pool + 1)]
        db.session.add_all(objects)
        db.session.commit()

    @staticmethod
    def get_object() -> Object:
        """Returns any object available in the pool.

        Raises:
            Exception: If the pool is empty.
        """
        stmt = select(Object).where(Object.is_busy == False)
        free_objects = db.session.scalars(stmt).all()
        obj = random.choice(free_objects)
        obj.is_busy = True
        db.session.commit()
        return obj

    @staticmethod
    def free_object(obj_val: int):
        """Returns the object back to the pool.

        Args:
            obj_val: The object id to free.

        Raises:
            WrongObject: If the object is not in use.
            NotFoundObject: If the objects is not found
        """
        stmt = select(Object).where(Object.value == obj_val)
        obj = db.session.scalars(stmt).first()
        if obj is None:
            raise NotFoundObject("Wrong id ,can't find")
        if not obj.is_busy:
            raise WrongObject("Object not in use")
        obj.is_busy = False
        db.session.commit()
