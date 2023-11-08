from .object_mgr import ObjectMgr


def get_object(_, info):
    try:
        obj = ObjectMgr.get_object()
        payload = obj.to_dict()
    except Exception as e:
        payload = None

    return payload
