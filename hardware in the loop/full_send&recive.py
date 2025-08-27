import serial
import time
import re

ser = serial.Serial('COM6',115200,timeout=1)
time.sleep(2)
ser.reset_input_buffer()
print('Serial OK')
counter = 0.5
error = 0
start_time = time.time()
try:
    while True:    
        # time.sleep(0.00000001)
        to_send = f"hello from python {counter}\n"
        ser.write(to_send.encode('utf-8'))
        print(f"sent: {to_send.strip('\n')}")
        while ser.in_waiting <= 0:
            1# time.sleep(0.000000001)
        response = ser.readline().decode('utf-8').strip("\n")
        float_list = [float(x) for x in re.findall(r'[-+]?\d*\.\d+', response)]
        if float_list[0] != counter-0.5:
            error +=1
        print(float_list,error)
        counter+=1


except KeyboardInterrupt:
    end_time=time.time()-start_time
    print(f"took {end_time}")
    print(f"expected time{counter*0.01}")
    print(f"frequancy: {(counter-0.5)/end_time} ,  dt:{end_time/(counter-0.5)}")

    ser.close()
    print("Closed Serial Communication")
ser.close()
#findings : sending maxes out at 160 HZ with no errors in comutnication
#           at sending 1 float and reciveing 2 floats in strings

