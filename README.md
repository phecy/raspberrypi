# raspberrypi

![image](https://mcuoneclipse.files.wordpress.com/2015/12/rp2_pinout.png)

## Sensor Info

### MOTOR and l298N

BOARD

Left_wheel  GPIO: 13, 15 ENA:  7, 11
			 
right_wheel GPIO: 16, 18 ENB:  22, 29


### Hc-sr04

top right

> trig_pin = 06(BCM) (BOARD)  pin 31
> 
> echo_pin = 13(BCM) (BOARD)  pin 33

bottom right

> trig_pin = 19(BCM) (BOARD)  pin 35
> 
> echo_pin = 26(BCM) (BOARD)  pin 37


top left

> trig_pin = 12(BCM) (BOARD)  pin 32
> 
> echo_pin = 16(BCM) (BOARD)  pin 36


bottom left 

> trig_pin = 20(BCM) (BOARD)  pin 38
> 
> echo_pin = 21(BCM) (BOARD)  pin 40

[https://github.com/alaudet/hcsr04sensor
](https://github.com/alaudet/hcsr04sensor)

> sudo pip install hcsr04sensor
> 
> python /usr/local/bin/hcsr04.py -t 6 -e 13 -sp 0.001


### DHT11 (温度湿度)

DHT11 19(BCM)   35 (BOARD)


