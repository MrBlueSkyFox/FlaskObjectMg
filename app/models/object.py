import uuid

from app import db


class Object(db.Model):
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # uniq identification for object in db
    value = db.Column(db.Integer, nullable=False, unique=True)  # value of object
    is_busy = db.Column(db.Boolean, nullable=False, default=False)  # bool variable for managing state of objects

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "is_busy": self.is_busy,
        }
