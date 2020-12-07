try:
    # print(10 / 0)
    namen = ['Tanja', 'Maria']

    print(namen[3])

    print('Wird nicht ausgeführ')
except ZeroDivisionError as e:
    print('Fehler aufgetreten')
except IndexError:
    print('Fehler im Array aufgetreten')

print('Wird jetzt ausgeführt')


def is_sinn(zahl):
    if zahl == 42:
        return True

    if zahl == 666:
        # Selber Exceptions werfen
        raise Exception('?!?!')

    return False


def set_ps(ps):
    if ps >= 2000:
        # ps = 1999
        raise ValueError('Glaub ich nicht')

