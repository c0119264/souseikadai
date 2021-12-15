from hmc5883l import HMC5883L
from machine import I2C,Pin
import time

def hmcmain():
    sensor = HMC5883L(scl=4, sda=5)

    for i in range(5):
        x, y, z = sensor.read()
        #print(sensor.format_result(x,y+400,z))
        #f=open("hmc.csv","a")
        #data=sensor.format_result(x,y+400,z) +"\n"
        #f.write(data)
        #f.close()

        data = sensor.format_result(x,y+400,z)
        #print('X: {:.4f}, Y: {:.4f}, Z: {:.4f}, Heading: {}° {}′ '.format(data[0], data[1], data[2], data[3], data[4]))
        #print('方位 : {}°'.format(data[3]))

        #print("debag1")
        time.sleep(0.2)
    return data[3]

hmcmain()

    