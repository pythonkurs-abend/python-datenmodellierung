def is_sinn(zahl):
    if zahl == 42 or zahl == '42':
        return True

    return False


print(is_sinn(42))
print(is_sinn(33))
