EESchema Schematic File Version 2
LIBS:PIAD-18bits-rescue
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:PIAD-18bits-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 3750 2900 0    60   Input ~ 0
+3.3V
Text HLabel 3750 3050 0    60   Input ~ 0
GND
Text HLabel 5375 2825 0    60   Input ~ 0
AI7
Text HLabel 5375 2725 0    60   Input ~ 0
AI6
Text HLabel 5375 2625 0    60   Input ~ 0
AI5
Text HLabel 5375 2525 0    60   Input ~ 0
AI4
Text HLabel 5375 2425 0    60   Input ~ 0
AI3
Text HLabel 5375 2325 0    60   Input ~ 0
AI2
Text HLabel 5375 2225 0    60   Input ~ 0
AI1
Text HLabel 5375 2125 0    60   Input ~ 0
AI0
Text HLabel 5375 3025 0    60   Input ~ 0
DIR_A
Text HLabel 5375 3125 0    60   Input ~ 0
A_OE
Text HLabel 7075 2825 2    60   Input ~ 0
AO7
Text HLabel 7075 2625 2    60   Input ~ 0
AO5
Text HLabel 7075 2725 2    60   Input ~ 0
AO6
Text HLabel 7075 2525 2    60   Input ~ 0
AO4
Text HLabel 7075 2425 2    60   Input ~ 0
AO3
Text HLabel 7075 2325 2    60   Input ~ 0
AO2
Text HLabel 7075 2225 2    60   Input ~ 0
AO1
Text HLabel 7075 2125 2    60   Input ~ 0
AO0
Text HLabel 5400 4175 0    60   Input ~ 0
BI0
Text HLabel 5400 4275 0    60   Input ~ 0
BI1
Text HLabel 5400 4375 0    60   Input ~ 0
BI2
Text HLabel 5400 4475 0    60   Input ~ 0
BI3
Text HLabel 5400 4575 0    60   Input ~ 0
BI4
Text HLabel 5400 4675 0    60   Input ~ 0
BI5
Text HLabel 5400 4775 0    60   Input ~ 0
BI6
Text HLabel 5400 4875 0    60   Input ~ 0
BI7
Text HLabel 5400 5075 0    60   Input ~ 0
DIR_B
Text HLabel 7050 4175 2    60   Input ~ 0
BO0
Text HLabel 7050 4275 2    60   Input ~ 0
BO1
Text HLabel 7050 4375 2    60   Input ~ 0
BO2
Text HLabel 7050 4475 2    60   Input ~ 0
BO3
Text HLabel 7050 4575 2    60   Input ~ 0
BO4
Text HLabel 7050 4675 2    60   Input ~ 0
BO5
Text HLabel 7050 4775 2    60   Input ~ 0
BO6
Text HLabel 7050 4875 2    60   Input ~ 0
BO7
Text HLabel 5400 5175 0    60   Input ~ 0
B_OE
$Comp
L C C501
U 1 1 58D195F9
P 3400 4500
F 0 "C501" H 3425 4600 50  0000 L CNN
F 1 "10uF" H 3425 4400 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 3438 4350 50  0001 C CNN
F 3 "" H 3400 4500 50  0000 C CNN
	1    3400 4500
	1    0    0    -1  
$EndComp
$Comp
L C C502
U 1 1 58D195FA
P 3650 4500
F 0 "C502" H 3675 4600 50  0000 L CNN
F 1 "100nF" H 3675 4400 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 3688 4350 50  0001 C CNN
F 3 "" H 3650 4500 50  0000 C CNN
	1    3650 4500
	1    0    0    -1  
$EndComp
$Comp
L C C503
U 1 1 58D195FB
P 3950 4500
F 0 "C503" H 3975 4600 50  0000 L CNN
F 1 "10uF" H 3975 4400 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 3988 4350 50  0001 C CNN
F 3 "" H 3950 4500 50  0000 C CNN
	1    3950 4500
	1    0    0    -1  
$EndComp
$Comp
L C C504
U 1 1 58D195FC
P 4200 4500
F 0 "C504" H 4225 4600 50  0000 L CNN
F 1 "100nF" H 4225 4400 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 4238 4350 50  0001 C CNN
F 3 "" H 4200 4500 50  0000 C CNN
	1    4200 4500
	1    0    0    -1  
$EndComp
Connection ~ 3950 4300
Wire Wire Line
	3950 4350 3950 4300
Connection ~ 3950 4700
Wire Wire Line
	3950 4650 3950 4700
Connection ~ 3650 4700
Wire Wire Line
	4200 4700 4200 4650
Connection ~ 3650 4300
Wire Wire Line
	4200 4300 4200 4350
Connection ~ 3400 4700
Wire Wire Line
	3400 4650 3400 4700
Wire Wire Line
	3650 4700 3650 4650
Wire Wire Line
	3050 4700 4200 4700
Connection ~ 3400 4300
Wire Wire Line
	3400 4350 3400 4300
Wire Wire Line
	3650 4300 3650 4350
Wire Wire Line
	3050 4300 4200 4300
Wire Wire Line
	3750 2900 4250 2900
Wire Wire Line
	3750 3050 4250 3050
Wire Wire Line
	5400 5175 5550 5175
Wire Wire Line
	5400 5075 5550 5075
Wire Wire Line
	5550 4875 5400 4875
Wire Wire Line
	5400 4775 5550 4775
Wire Wire Line
	5550 4675 5400 4675
Wire Wire Line
	5400 4575 5550 4575
Wire Wire Line
	5400 4475 5550 4475
Wire Wire Line
	5400 4375 5550 4375
Wire Wire Line
	5400 4275 5550 4275
Wire Wire Line
	5400 4175 5550 4175
Wire Wire Line
	6950 4175 7050 4175
Wire Wire Line
	7050 4275 6950 4275
Wire Wire Line
	6950 4375 7050 4375
Wire Wire Line
	7050 4475 6950 4475
Wire Wire Line
	6950 4575 7050 4575
Wire Wire Line
	7050 4675 6950 4675
Wire Wire Line
	6950 4775 7050 4775
Wire Wire Line
	7050 4875 6950 4875
Wire Wire Line
	7075 2825 6950 2825
Wire Wire Line
	6950 2725 7075 2725
Wire Wire Line
	6950 2625 7075 2625
Wire Wire Line
	6950 2525 7075 2525
Wire Wire Line
	7075 2425 6950 2425
Wire Wire Line
	6950 2325 7075 2325
Wire Wire Line
	7075 2225 6950 2225
Wire Wire Line
	6950 2125 7075 2125
Wire Wire Line
	5375 3125 5550 3125
Wire Wire Line
	5375 2125 5550 2125
Wire Wire Line
	5375 2225 5550 2225
Wire Wire Line
	5550 2325 5375 2325
Wire Wire Line
	5375 2425 5550 2425
Wire Wire Line
	5375 2525 5550 2525
Wire Wire Line
	5375 2625 5550 2625
Wire Wire Line
	5550 2725 5375 2725
Wire Wire Line
	5375 2825 5550 2825
Wire Wire Line
	5375 3025 5550 3025
Text Label 4250 2900 2    60   ~ 0
+3.3V
Text Label 3050 4300 0    60   ~ 0
+3.3V
$Comp
L 74LCX245 U501
U 1 1 58D2A55C
P 6250 2625
F 0 "U501" H 6250 3350 50  0000 C CNN
F 1 "74LCX245" H 6250 3259 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-20W_7.5x12.8mm_Pitch1.27mm" H 6250 2625 50  0001 C CNN
F 3 "" H 6250 2625 50  0000 C CNN
	1    6250 2625
	1    0    0    -1  
$EndComp
$Comp
L 74LCX245 U502
U 1 1 58D2A5F4
P 6250 4675
F 0 "U502" H 6250 5400 50  0000 C CNN
F 1 "74LCX245" H 6250 5309 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-20W_7.5x12.8mm_Pitch1.27mm" H 6250 4675 50  0001 C CNN
F 3 "" H 6250 4675 50  0000 C CNN
	1    6250 4675
	1    0    0    -1  
$EndComp
Wire Wire Line
	6775 5075 7200 5075
Text Label 7200 5075 2    60   ~ 0
+3.3V
Text Label 4250 3050 2    60   ~ 0
GND
Text Label 3050 4700 0    60   ~ 0
GND
Wire Wire Line
	6775 3125 7200 3125
Wire Wire Line
	6775 5175 7200 5175
Text Label 7200 5175 2    60   ~ 0
GND
Text Label 7200 3125 2    60   ~ 0
GND
Wire Wire Line
	6775 3025 7200 3025
Text Label 7200 3025 2    60   ~ 0
+3.3V
$EndSCHEMATC
