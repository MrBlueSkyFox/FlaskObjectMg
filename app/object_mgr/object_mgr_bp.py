from flask import (
    Blueprint, request, jsonify
)

from app.exceptions import NotFoundObject, WrongObject
from .object_mgr_cl import ObjectMgr

bp = Blueprint("object_mgr", __name__, url_prefix="/object_mgr")


@bp.route("/set_object_pool", methods=["POST"])
def set_object_pool():
    data = request.json
    objects_number = data['objects_number']
    ObjectMgr.init_object_pool(objects_number)
    return jsonify({"message": "Success"}), 200


@bp.route("/get_object", methods=["GET"])
def get_object():
    obj = ObjectMgr.get_object()
    return jsonify(obj.to_dict())


@bp.route("/free_object/<obj_val>", methods=["POST"])
def free_object(obj_val: int):
    ObjectMgr.free_object(obj_val)
    return jsonify({"message": "Success"}), 200


@bp.errorhandler(WrongObject)
def exception_handler_wrong_object(e):
    return jsonify({"message": str(e)}), 400


@bp.errorhandler(NotFoundObject)
def exception_handler_not_found_object(e):
    return jsonify({"message": str(e)}), 400
