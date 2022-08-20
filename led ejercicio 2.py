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

def print_led(a,b,c,d,e,f,g,h,i,j):
  leda.value(a)
  ledb.value(b)
  ledc.value(c)
  ledd.value(d)
  lede.value(e)
  ledf.value(f)
  ledg.value(g)
  ledh.value(h)
  ledi.value(i)
  ledj.value(j)
  pausam(200)
while True:
  print_led(0,0,0,0,0,0,0,0,0,0)
  print_led(0,0,0,0,0,0,0,0,0,1)
  print_led(0,0,0,0,0,0,0,0,1,0)
  print_led(0,0,0,0,0,0,0,1,0,0)
  print_led(0,0,0,0,0,0,1,0,0,0)
  print_led(0,0,0,0,0,1,0,0,0,0)
  print_led(0,0,0,0,1,0,0,0,0,0)
  print_led(0,0,0,1,0,0,0,0,0,0)
  print_led(0,0,1,0,0,0,0,0,0,0)
  print_led(0,1,0,0,0,0,0,0,0,0)
  print_led(1,0,0,0,0,0,0,0,0,0)
  

