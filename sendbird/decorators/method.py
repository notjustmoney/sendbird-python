def instancemethod(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            raise Exception({"message": "Instance method cannot call from class"})

    return inner


def delete_from_instance(func):
    def inner(*args, **kwargs):
        if not isinstance(args[0], type):
            raise Exception({"message": "static method cannot call from instance"})
        return func(*args, **kwargs)

    return inner
