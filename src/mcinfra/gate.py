class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if body.get("cloud") not in {"gcp", "aws", "azure"}: failed.append("cloud")\n    if body.get("action") != "plan": failed.append("action")
    return {"passed": not failed, "failed": failed, "applied": False}
