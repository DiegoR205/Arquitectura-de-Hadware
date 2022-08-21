from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam
leda=pin(5,pin.OUT)
ledb=pin(18,pin.OUT)
ledc=pin(19,pin.OUT)
ledd=pin(21,pin.OUT)
lede=pin(22,pin.OUT)
ledf=pin(23,pin.OUT)
ledg=pin(26,pin.OUT)
ledh=pin(25,pin.OUT)
ledi=pin(33,pin.OUT)
ledj=pin(32,pin.OUT)
ledt=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]
def derecha():
    for i in ledt:
        for j in range (2):
            i.value(not i.value())
            pausam(50)
def izquierda():
    for i in reversed(ledt):
        for j in range (2):
            i.value(not i.value())
            pausam(250)
while True:
    derecha()
    izquierda()