# Previewer example for WuCCD
# By Cetec(NightFuryAstro)
import ADS1263
import RPi.GPIO as GPIO
import time, numpy,cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT) #S0
GPIO.setup(16, GPIO.OUT) #S1
GPIO.setup(20, GPIO.OUT) #S2
GPIO.setup(21, GPIO.OUT) #S3

def col0():
	GPIO.output((12,16,20,21), (0,0,0,0))

def col1():
	GPIO.output((12,16,20,21), (1,0,0,0))

def col2():
	GPIO.output((12,16,20,21), (0,1,0,0))

def col3():
	GPIO.output((12,16,20,21), (1,1,0,0))

def col4():
	GPIO.output((12,16,20,21), (0,0,1,0))

def col5():
	GPIO.output((12,16,20,21), (1,0,1,0))

def col6():
	GPIO.output((12,16,20,21), (0,1,1,0))

def col7():
	GPIO.output((12,16,20,21), (1,1,1,0))

def acquire():
	img = numpy.zeros((8,10))
	col0()
	img[0] = ADC.ADS1263_GetAll_ADC2()
	col1()
	img[1] = ADC.ADS1263_GetAll_ADC2()
	col2()
	img[2] = ADC.ADS1263_GetAll_ADC2()
	col3()
	img[3] = ADC.ADS1263_GetAll_ADC2()
	col4()
	img[4] = ADC.ADS1263_GetAll_ADC2()
	col5()
	img[5] = ADC.ADS1263_GetAll_ADC2()
	col6()
	img[6] = ADC.ADS1263_GetAll_ADC2()
	col7()
	img[7] = ADC.ADS1263_GetAll_ADC2()
	return img

#Init
ADC = ADS1263.ADS1263()
ADC.ADS1263_SetMode(0)
ADC.ADS1263_init_ADC2()

# Acquire Bias
print('Cover the sensor to get bias')
bias = acquire()
bias = bias + acquire()
bias = bias + acquire()
bias = bias + acquire()
bias = bias/4  - 600000
plt.ion()
print('Ready')
while True:
	tmpimg = acquire() - bias
	tmpimg = tmpimg / 25600
	tmpimg = tmpimg.astype('uint8')
	print(tmpimg)
	plt.imshow(tmpimg)
	plt.show()
	plt.pause(0.1)
	
