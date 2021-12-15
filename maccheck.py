import machine
import ubinascii
print(ubinascii.hexlify(machine.unique_id()).decode("utf-8"))