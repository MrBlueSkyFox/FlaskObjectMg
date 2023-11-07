from .object_mgr import ObjectMgr


def get_object(_, info):
    try:
        print("zzs")
        obj = ObjectMgr.get_object()
        print(obj)
        payload = obj.to_dict()
    except Exception as e:
        payload = None

    return payload
