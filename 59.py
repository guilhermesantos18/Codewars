from time import strftime
from time import gmtime
def make_readable(seconds):
    x = strftime("%H:%M:%S", gmtime(seconds))
    minutos = x[3:5]
    segundos = x[6:]
    horas = seconds * 99 / 359999
    print(horas)
    return str(horas).zfill(2) + ':' + minutos.zfill(2) + ':' + segundos.zfill(2)


print(make_readable(86399))
