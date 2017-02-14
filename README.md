# raspberrypi

![image](http://bbs.elecfans.com/data/attachment/forum/201604/08/102423paxwx43zgg5pay7g.png)

## Sensor Info

### MOTOR and l298N

BOARD

Left_wheel  GPIO: 13, 15 ENA:  7, 11
			 
right_wheel GPIO: 16, 18 ENB:  22, 29


### Hc-sr04

trig_pin = 06(BCM) (BOARD)  pin 31

echo_pin = 13(BCM) (BOARD)  pin 33

[https://github.com/alaudet/hcsr04sensor
](https://github.com/alaudet/hcsr04sensor)

> sudo pip install hcsr04sensor
> 
> python /usr/local/bin/hcsr04.py -t 6 -e 13 -sp 0.001


### DHT11 (温度湿度)

DHT11 19(BCM)   35 (BOARD)


