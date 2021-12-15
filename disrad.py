from HC_SR04 import HCSR04
from machine import Pin,I2C
from utime import sleep 
import math
from hmc5883l_main import hmcmain

import hmc5883l_main
from hmc5883l import HMC5883L
 
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)      #Init i2c
 
sensor = HCSR04(trigger_pin=17, echo_pin=16,echo_timeout_us=1000000)

try:
  for i in range(2):
    distance = sensor.distance_cm()
    #D=hmc5883l_main.hmcmain()
    a=int(distance)
    b=60
    if a>=1000:
          print("error")
    else:
      #hmは管理者から基準までの方位
      hm = hmcmain()
      print(f"基準点までの距離:{a}"+"cm")
      print(f"基準点の方位:{hm}"+"cm")
      #gはɤ(余弦定理計算サイトを参照)
      g=abs(hm-215)
      yogen=a**2+b**2-2*a*b*(math.cos(math.radians(g)))
      #自転車までの距離を計算する余弦定理
      c=math.sqrt(yogen)
      #自転車までの回転角度
      B=(a**2+c**2-b**2)/(2*c*a)
      #コサインの数値
      B=math.acos(B)
      #radiansから度数に変更
      B=math.degrees(B)
      print(f"自転車までの距離:{c}"+"cm")
      print(f"自転車までの回転角度:{B}"+"°")

      sleep(1)
      
except KeyboardInterrupt:
       pass    