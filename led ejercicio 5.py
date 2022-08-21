from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam,sleep_us as pausa
puerto=[32,33,25,26,23,22,21,19,18,5]
toditicos=[]
for i in puerto:
    toditicos.append (pin(i, pin.OUT) )
print (toditicos)
def derecha () :
    for i in toditicos:
        for j in range (2):
             i.value(not i.value ())
             pausam(150)
def izquierda () :
    for i in reversed (toditicos):
        for j in range (2):
            i.value (not i.value ())
            pausam(150)
while True:
    derecha()
    izquierda ()