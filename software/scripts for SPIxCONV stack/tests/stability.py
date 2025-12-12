#!/usr/bin/python3

from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
import dac
import adc
import sys
import math
import time

#=======================================================
#	stability test
#=======================================================

dac.config()
adc.read()

from time import gmtime, strftime
timestr = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
filename = "ADC stability/" + timestr + "_"

#from epics import caput
#from epics import caget
#import Agilent34420A

#voltage = [-9, -5, 0, 5, 9]
voltage = [9]
#total time of the test (in seconds)
total_measures = 10000
# defining variables for MAX, MIN and MEAN (ADC measure)
min_adc = [0] * 5
max_adc = [0] * 5
mean_adc = [0] * 5
std_var = [0] * 5
i = 0
j = 0
############################################################
for x in voltage:
	measure = []
	if (x > 0):
		log = open(filename + "+" + str(x) + "V.csv", "a+")
	else:
		log = open(filename + str(x) + "V.csv", "a+")
	#set tabs of .csv file
	log.write('Indice')
	log.write(';Valor lido no multimetro (V)')
	log.write(';Valor lido no multimetro (LSB)')
	log.write(';ADC - Leitura do valor integrado (V)')
	log.write(';ADC - Leitura do valor integrado (LSB)')
	log.write(';MBTemp1:Channel5 (graus C)')
	log.write('\n')
	#Update the file
	log.close()
	print("  ============================================================================")
#	sys.stdout.write("  |                         ESTABILIDADE: ")
	sys.stdout.write("  |                           STABILITY: ")
	if(x < 0):
		sys.stdout.write(str(x) + "V" + "                                 |\n")
	elif(x > 0):
		sys.stdout.write("+" + str(x) + "V" + "                                 |\n")
	else:
		sys.stdout.write(str(x) + "V" + "                                  |\n")
	print("  ============================================================================")
	print("  | INDEX\tMULT.\t\tMULT.[LSB]\tADC\tADC(V)\t\tTEMP.|")
	print("  |--------------------------------------------------------------------------|")

	# select DAC and write correspondent value
	base = int(((x+10)/(20/float(262144))))
	dac.write(base)
	time.sleep(60)

	measure = []
	for i in range (total_measures):
		if (x > 0):
			log = open(filename + "+" + str(x) + "V.csv", "a+")
		else:
			log = open(filename + str(x) + "V.csv", "a+")
		#---------------------------------------------------

#		for k in range(100):
#			measure.append(adc.read())
#		#	#print numpy.mean(measure)
#		adc_value = sum(measure) / len(measure)

		adc_value = adc.read()
		measure.append(adc_value)
		# check if it is the first measure
		if(i == 0):
			min_adc[j] = measure[0]
			max_adc[j] = measure[0]
			mean_adc[j] = measure[0]*1.0
		# if not, calculate max, min and mean
		else:
			if(measure[i] < min_adc[j]):
				min_adc[j] = measure[i]
			if(measure[i] > max_adc[j]):
				max_adc[j] = measure[i]
			mean_adc[j] = (mean_adc[j]*i + measure[i])/(i + 1)
		i += 1
		#adc = "{:1}".format(adc)
		#adc = numpy.mean(measure)
		adc_volt = float(adc_value)/262143*20-10
		adc_volt_str = str(adc_volt)
		adc_volt_str = adc_volt_str[0:adc_volt_str.find(".")+8]
		#---------------------------------------------------
		#Get temperature
		#temp = caget("MBTemp_RAFAEL_1:Channel5")
		#temp_str = ("%.2f" %temp)
		#temp_str = str(temp_str)
		#temp_str = temp_str[0:temp_str.find(".")+3]
		#---------------------------------------------------
		#Write all data
		#log.write(str(base+i)+ ';' + multimeter_int_str + ';' + str(multimeter_lsb) + ';' + str(adc) + ';' + str(adc_volt) + ';' + str(temp) + '\n')
		#log.write(str(base+i)+ ';' + multimeter_int_str + ';' + str(multimeter_lsb) + ';' + str(adc) + ';' + str(adc_volt) + ';' + '\n')
		#log.write(str(base+i)+ ';' + multimeter_int_str + ';' + str(multimeter_lsb) + ';' + str(adc) + ';' + str(adc_volt) + ';;')
		log.write(str(base+i)+ ';;;' + str(adc_value) + ';' + str(adc_volt) + ';;')

#		for k in range(100):
#			log.write(str(measure[k]) + ';')
		log.write('\n')

		#Update the file
		log.close()
		#print data on terminal
		sys.stdout.write("  | " + str(base) + "\t" + "------" + "\t\t" + "------\t" + "\t")
		#---------------------------------------------------------
		sys.stdout.write(str(adc_value) + "\t")
		#---------------------------------------------------------
		if(adc_volt < 0):
			sys.stdout.write(str(adc_volt_str) + "\t")
		else:
			sys.stdout.write("+" + str(adc_volt_str) + "\t")
		#---------------------------------------------------------
		#sys.stdout.write(temp_str + "|" + "\n")
		sys.stdout.write('---\t' + "|" + "\n")
	print("  |                                                                          |")

	#calculate standard deviation
	diff = measure
	diff[:] = [x - mean_adc[j] for x in measure]
	diff_square = [x**2 for x in diff]
	std_var[j] = sum(diff_square)/(len(measure)*1.0)
	std_var[j] = math.sqrt(std_var[j])
	std_var[j] = "{0:.2f}".format(std_var[j])

	print("  ============================================================================")
	#---------------------------------------------------
	# print standard variation
	sys.stdout.write("  |    std_dev  = %s" %str(std_var[j]))
	for i in range (0, (6 - len(str(std_var[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#-------------------------------------------------------
	# print minimum value acquired
	sys.stdout.write("  |    ADC_min  = %s" %min_adc[j])
	for i in range (0, (6 - len(str(min_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	# print maximum value acquired
	sys.stdout.write("  |    ADC_max  = %s" %max_adc[j])
	for i in range (0, (6 - len(str(max_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	# print mean
	sys.stdout.write("  |    ADC_mean = %s" %mean_adc[j])
	for i in range (0, (6 - len(str(mean_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	# print difference between max and min (histogram thickness)
	sys.stdout.write("  |        diff = %s" %(max_adc[j] - min_adc[j]))
	for i in range (0, (6 - len(str(max_adc[j] - min_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	print("  =============================")
	j += 1

# Print it all again after all the data were acquired
j = 0
for x in voltage:
	sys.stdout.write("  |     ESTABILIDADE: ")
	if(x > 0):
		sys.stdout.write("+")
	if(x == 0):
		sys.stdout.write(" ")
	sys.stdout.write(str(x) + "V     |\n")
	print("  =============================")
	#---------------------------------------------------
	# print standard variation
	sys.stdout.write("  |    std_dev  = %s" %str(std_var[j]))
	for i in range (0, (6 - len(str(std_var[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#-------------------------------------------------------
	# print minimum value acquired
	sys.stdout.write("  |    ADC_min  = %s" %min_adc[j])
	for i in range (0, (6 - len(str(min_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	# print maximum value acquired
	sys.stdout.write("  |    ADC_max  = %s" %max_adc[j])
	for i in range (0, (6 - len(str(max_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	# print mean
	sys.stdout.write("  |    ADC_mean = %s" %mean_adc[j])
	for i in range (0, (6 - len(str(mean_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	# print difference between max and min (histogram thickness)
	sys.stdout.write("  |        diff = %s" %(max_adc[j] - min_adc[j]))
	for i in range (0, (6 - len(str(max_adc[j] - min_adc[j])))):
		sys.stdout.write(' ')
	sys.stdout.write('      |\n')
	#---------------------------------------------------
	print("  =============================")
	j += 1
