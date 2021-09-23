def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# x, y = 7, 0
# result = careful_divide(x, y)
# if result is None:
#     print('Invalid inputs')

x, y = 5, 0
# result = careful_divide(x, y)
# if not result:
#     print('Invalid inputs')


# def careful_divide(a, b):
#     try:
#         return True, a / b
#     except ZeroDivisionError:
#         return False, None
#
#
# success, result = careful_divide(x, y)
# if not success:
#     print('Invalid inputs')


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    Raises:
    ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


print(careful_divide(5, 0))
