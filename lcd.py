
## This module requires the serial module###

import serial

header = chr(254)          #Converts the decimal 254 to hex
dimset = chr(89)            #Sets the dim variable
on = chr(66)                  #LCD on
neveroff = chr(0)            #stay on until I say otherwise
blockoff = chr(84)           #turn off block cursor
home = chr(72)              #move cursor home
cls = chr(88)                  #Converts decimal 88 to hex to clear


ser = serial.Serial(0, 19200, timeout = 1)

class Lcd : 
	def serial(self, port, speed, option) :
		ser = serial.Serial(port,speed,option)
		
	def text(self,text,column, row) :
	    ser.write(header); ser.write(chr(71)) 
	    ser.write(chr(column)); ser.write(chr(row))
	    ser.write(text)                
	
	def clear(self) :
	    ser.write(chr(254)); ser.write(chr(88))
	            
	def move(self,column, row) :
	    ser.write(header); ser.write(chr(71)) 
	    ser.write(chr(column)); ser.write(chr(row))
	
	def brightness(self, level) :
	    ser.write(header); ser.write(dimset); ser.write(chr(level))
	
	def setup(self) :
	    ser.write(header); ser.write(on); ser.write(neveroff)        #Turn on LCD and leave it on   
	    ser.write(header); ser.write(blockoff)                             #Turns off block cursor
	    ser.write(header); ser.write(cls)                                    #Clears the LCD
	    ser.write(header); ser.write(dimset); ser.write(chr(3))     #Dim as possible
	    
	def scroll(self, state) :
		if state == 1 :
			ser.write(header); ser.write(chr(81))
			
		if state == 0 :
			ser.write(header); ser.write(chr(82))
			
	def wrap(self,state) :
		if state == 1 :
			ser.write(header); ser.write(chr(67))    		
		if state == 0 :
			ser.write(header); ser.write(chr(68))
	
	def readkey(self) :
		key = ser.read()
		return key
	
	def gpo(self,number, state) :
		if state == 1 :
			ser.write(header); ser.write(chr(87)); ser.write(chr(number))   
		if state == 0 :
			ser.write(header); ser.write(chr(86)); ser.write(chr(number))