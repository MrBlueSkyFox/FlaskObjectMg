from app.object_mgr import ObjectMgr


def set_object_pool(_, info, n: int) -> bool:
    try:
        ObjectMgr.init_object_pool(n)
        payload = True
    except Exception as e:
        payload = False
    return payload


def free_object(_, info, object_value: int) -> bool:
    try:
        ObjectMgr.free_object(object_value)
        payload = True
    except Exception as e:
        payload = False
    return payload
