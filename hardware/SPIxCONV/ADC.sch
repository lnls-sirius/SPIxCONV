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
Sheet 4 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L C C420
U 1 1 58D19D86
P 7325 1625
F 0 "C420" H 7375 1725 50  0000 L CNN
F 1 "10uF" H 7375 1525 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 7325 1625 60  0001 C CNN
F 3 "" H 7325 1625 60  0001 C CNN
	1    7325 1625
	1    0    0    -1  
$EndComp
$Comp
L C C418
U 1 1 58D19D87
P 7025 1625
F 0 "C418" H 7075 1725 50  0000 L CNN
F 1 "100nF" H 7075 1525 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 7025 1625 60  0001 C CNN
F 3 "" H 7025 1625 60  0001 C CNN
	1    7025 1625
	1    0    0    -1  
$EndComp
$Comp
L C C417
U 1 1 58D19D88
P 7025 1075
F 0 "C417" H 7075 1175 50  0000 L CNN
F 1 "10uF" H 7075 975 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 7025 1075 60  0001 C CNN
F 3 "" H 7025 1075 60  0001 C CNN
	1    7025 1075
	1    0    0    -1  
$EndComp
$Comp
L C C419
U 1 1 58D19D89
P 7325 1075
F 0 "C419" H 7375 1175 50  0000 L CNN
F 1 "100nF" H 7375 975 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 7325 1075 60  0001 C CNN
F 3 "" H 7325 1075 60  0001 C CNN
	1    7325 1075
	1    0    0    -1  
$EndComp
Text GLabel 8775 1925 1    60   UnSpc ~ 0
AD1-IN-
Text GLabel 8375 1925 1    60   UnSpc ~ 0
AD1-IN+
Text GLabel 9725 1925 2    60   UnSpc ~ 0
+5V-REG-AD1
$Comp
L C C424
U 1 1 58D19DA1
P 8725 5875
F 0 "C424" H 8775 5975 50  0000 L CNN
F 1 "100nF" H 8775 5775 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 8725 5875 60  0001 C CNN
F 3 "" H 8725 5875 60  0001 C CNN
	1    8725 5875
	1    0    0    -1  
$EndComp
$Comp
L C C423
U 1 1 58D19DA2
P 8475 5875
F 0 "C423" H 8525 5975 50  0000 L CNN
F 1 "10uF" H 8525 5775 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 8475 5875 60  0001 C CNN
F 3 "" H 8475 5875 60  0001 C CNN
	1    8475 5875
	1    0    0    -1  
$EndComp
$Comp
L C C422
U 1 1 58D19DA4
P 8275 5825
F 0 "C422" H 8325 5925 50  0000 L CNN
F 1 "100nF" H 8325 5725 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 8275 5825 60  0001 C CNN
F 3 "" H 8275 5825 60  0001 C CNN
	1    8275 5825
	1    0    0    -1  
$EndComp
$Comp
L C C421
U 1 1 58D19DA5
P 8075 5825
F 0 "C421" H 8125 5925 50  0000 L CNN
F 1 "10uF" H 8125 5725 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 8075 5825 60  0001 C CNN
F 3 "" H 8075 5825 60  0001 C CNN
	1    8075 5825
	1    0    0    -1  
$EndComp
$Comp
L C C416
U 1 1 58D19DA9
P 6400 3175
F 0 "C416" H 6450 3275 50  0000 L CNN
F 1 "100nF" H 6450 3075 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 6400 3175 60  0001 C CNN
F 3 "" H 6400 3175 60  0001 C CNN
	1    6400 3175
	1    0    0    -1  
$EndComp
$Comp
L C C415
U 1 1 58D19DAA
P 6075 3175
F 0 "C415" H 6125 3275 50  0000 L CNN
F 1 "10uF" H 6125 3075 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 6075 3175 60  0001 C CNN
F 3 "" H 6075 3175 60  0001 C CNN
	1    6075 3175
	1    0    0    -1  
$EndComp
$Comp
L AD7634 U406
U 1 1 58D19DAB
P 8425 3725
F 0 "U406" H 8425 3625 60  0000 C CNN
F 1 "AD7634" H 8425 3775 60  0000 C CNN
F 2 "Housings_QFP:LQFP-48_7x7mm_Pitch0.5mm" H 8425 3725 60  0001 C CNN
F 3 "" H 8425 3725 60  0001 C CNN
	1    8425 3725
	1    0    0    -1  
$EndComp
$Comp
L CP1 C425
U 1 1 58D19DCC
P 9125 1925
F 0 "C425" H 8875 2025 50  0000 L CNN
F 1 "47uF" H 8925 1825 50  0000 L CNN
F 2 "Capacitors_SMD:CP_Elec_6.3x5.3" H 9125 1925 60  0001 C CNN
F 3 "" H 9125 1925 60  0000 C CNN
	1    9125 1925
	0    1    1    0   
$EndComp
$Comp
L C C426
U 1 1 58D19DD3
P 10775 3425
F 0 "C426" H 10825 3525 50  0000 L CNN
F 1 "47pF" H 10825 3325 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 10550 3825 60  0001 C CNN
F 3 "~" H 10775 3425 60  0000 C CNN
	1    10775 3425
	1    0    0    -1  
$EndComp
Text HLabel 5025 5825 2    60   Input ~ 0
ADC_IN
Text Notes 700  4100 0    60   ~ 0
5v Positive ADC voltage reference
$Comp
L R R402
U 1 1 58D337A4
P 900 6900
F 0 "R402" V 980 6900 50  0000 C CNN
F 1 "820k" V 900 6900 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 830 6900 30  0001 C CNN
F 3 "" H 900 6900 30  0000 C CNN
	1    900  6900
	0    1    1    0   
$EndComp
$Comp
L R R401
U 1 1 58D337A5
P 900 7275
F 0 "R401" V 980 7275 50  0000 C CNN
F 1 "10k" V 900 7275 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 830 7275 30  0001 C CNN
F 3 "" H 900 7275 30  0000 C CNN
	1    900  7275
	0    -1   1    0   
$EndComp
$Comp
L GNDA #PWR047
U 1 1 58D337A6
P 700 7300
F 0 "#PWR047" H 700 7050 50  0001 C CNN
F 1 "GNDA" H 700 7150 50  0000 C CNN
F 2 "" H 700 7300 60  0000 C CNN
F 3 "" H 700 7300 60  0000 C CNN
	1    700  7300
	-1   0    0    -1  
$EndComp
Text Label 2200 5525 2    60   ~ 0
+15V
Text Label 800  6825 0    60   ~ 0
+15V
Text Label 2200 5625 2    60   ~ 0
-15V
$Comp
L C C407
U 1 1 58D337A7
P 1750 5350
F 0 "C407" H 1525 5450 50  0000 L CNN
F 1 "10uF" H 1500 5250 50  0000 L CNN
F 2 "Capacitors_SMD:CP_Elec_6.3x5.3" H 1788 5200 30  0001 C CNN
F 3 "" H 1750 5350 60  0000 C CNN
	1    1750 5350
	-1   0    0    1   
$EndComp
$Comp
L C C404
U 1 1 58D337A8
P 1475 5350
F 0 "C404" H 1275 5450 50  0000 L CNN
F 1 "100nF" H 1225 5250 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 1513 5200 30  0001 C CNN
F 3 "" H 1475 5350 60  0000 C CNN
	1    1475 5350
	-1   0    0    1   
$EndComp
$Comp
L C C409
U 1 1 58D337A9
P 1775 5825
F 0 "C409" H 1800 5925 50  0000 L CNN
F 1 "10uF" H 1775 5725 50  0000 L CNN
F 2 "Capacitors_SMD:CP_Elec_6.3x5.3" H 1813 5675 30  0001 C CNN
F 3 "" H 1775 5825 60  0000 C CNN
	1    1775 5825
	-1   0    0    -1  
$EndComp
$Comp
L C C405
U 1 1 58D337AA
P 1525 5825
F 0 "C405" H 1550 5925 50  0000 L CNN
F 1 "100nF" H 1550 5725 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 1563 5675 30  0001 C CNN
F 3 "" H 1525 5825 60  0000 C CNN
	1    1525 5825
	-1   0    0    -1  
$EndComp
Text Notes 650  7625 0    60   ~ 0
Positive and negative power supply
$Comp
L LT3015 U404
U 1 1 58D337AB
P 2725 6650
F 0 "U404" H 2525 7100 60  0000 C CNN
F 1 "LT3015" H 2825 6300 60  0000 C CNN
F 2 "Housings_SSOP:MSOP-12-1EP_3x4mm_Pitch0.65mm" H 2725 6650 60  0001 C CNN
F 3 "" H 2725 6650 60  0000 C CNN
	1    2725 6650
	1    0    0    -1  
$EndComp
Text Label 1975 6500 0    60   ~ 0
-15V
$Comp
L GNDA #PWR048
U 1 1 58D337AC
P 3075 6050
F 0 "#PWR048" H 3075 5800 50  0001 C CNN
F 1 "GNDA" H 3075 5900 50  0000 C CNN
F 2 "" H 3075 6050 60  0000 C CNN
F 3 "" H 3075 6050 60  0000 C CNN
	1    3075 6050
	1    0    0    -1  
$EndComp
$Comp
L R R405
U 1 1 58D337AE
P 3625 6700
F 0 "R405" V 3705 6700 50  0000 C CNN
F 1 "82k" V 3625 6700 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 3555 6700 30  0001 C CNN
F 3 "" H 3625 6700 30  0000 C CNN
	1    3625 6700
	0    1    1    0   
$EndComp
$Comp
L R R404
U 1 1 58D337AF
P 3525 6175
F 0 "R404" V 3605 6175 50  0000 C CNN
F 1 "9.1k" V 3525 6175 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 3455 6175 30  0001 C CNN
F 3 "" H 3525 6175 30  0000 C CNN
	1    3525 6175
	1    0    0    -1  
$EndComp
Text Notes 3975 6900 2    60   ~ 0
-13.04V
Text Notes 725  2575 0    60   ~ 0
+/- 10v input driver
Text Notes 5750 6375 0    60   ~ 0
ADC Circuit converter
Text HLabel 5025 6125 2    60   Input ~ 0
+5V_ADC
Text HLabel 5075 6725 2    60   Input ~ 0
GND
Text HLabel 5025 5975 2    60   Output ~ 0
ADC_AGND
Text HLabel 5075 6875 2    60   Input ~ 0
CS
Text HLabel 5075 7025 2    60   Input ~ 0
CLK
Text HLabel 5075 7175 2    60   Input ~ 0
MISO
Text HLabel 5075 7325 2    60   Input ~ 0
CNVST
Text HLabel 5075 7475 2    60   Input ~ 0
BUSY
Text Label 4675 5825 0    60   ~ 0
ADC_IN
Text Label 4725 6875 0    60   ~ 0
CS
Text Label 4725 7025 0    60   ~ 0
CLK
Text Label 4725 7175 0    60   ~ 0
MISO
Text Label 4725 7325 0    60   ~ 0
CNVST
Text Label 4725 7475 0    60   ~ 0
BUSY
$Comp
L GNDA #PWR049
U 1 1 58D337D3
P 1775 6075
F 0 "#PWR049" H 1775 5825 50  0001 C CNN
F 1 "GNDA" H 1775 5925 50  0000 C CNN
F 2 "" H 1775 6075 60  0000 C CNN
F 3 "" H 1775 6075 60  0000 C CNN
	1    1775 6075
	-1   0    0    -1  
$EndComp
$Comp
L DCP020515DU-RESCUE-PIAD-18bits U405
U 1 1 58D337F7
P 2850 4875
F 0 "U405" H 2850 5222 60  0000 C CNN
F 1 "DCP020515DU" H 2850 5116 60  0000 C CNN
F 2 "Controle:DCR01XXXXU" H 2850 4875 60  0001 C CNN
F 3 "" H 2850 4875 60  0000 C CNN
	1    2850 4875
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR050
U 1 1 58D337FE
P 3425 7425
F 0 "#PWR050" H 3425 7175 50  0001 C CNN
F 1 "GNDA" H 3425 7275 50  0000 C CNN
F 2 "" H 3425 7425 60  0000 C CNN
F 3 "" H 3425 7425 60  0000 C CNN
	1    3425 7425
	1    0    0    -1  
$EndComp
$Comp
L LT3080-RESCUE-PIAD-18bits U402
U 1 1 58D33800
P 1200 6425
AR Path="/58D33800" Ref="U402"  Part="1" 
AR Path="/58D18D68/58D33800" Ref="U402"  Part="1" 
F 0 "U402" V 950 6300 60  0000 L CNN
F 1 "LT3080" H 1025 6500 60  0000 L CNN
F 2 "Controle:SOT-223" H 1150 6425 60  0001 C CNN
F 3 "" H 1150 6425 60  0000 C CNN
	1    1200 6425
	1    0    0    -1  
$EndComp
Text HLabel 5025 6275 2    60   Input ~ 0
+3.3V
Text GLabel 3150 3425 2    60   UnSpc ~ 0
+5V-REG-AD1
$Comp
L C C410
U 1 1 58D4DF39
P 3050 3675
F 0 "C410" H 3100 3775 50  0000 L CNN
F 1 "4.7uF" H 3100 3575 50  0000 L CNN
F 2 "Capacitors_SMD:C_1210" H 3050 3675 60  0001 C CNN
F 3 "" H 3050 3675 60  0001 C CNN
	1    3050 3675
	1    0    0    -1  
$EndComp
$Comp
L C C401
U 1 1 58D4DF3A
P 1200 3375
F 0 "C401" H 1250 3475 50  0000 L CNN
F 1 "1uF" H 1250 3275 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 1200 3375 60  0001 C CNN
F 3 "" H 1200 3375 60  0001 C CNN
	1    1200 3375
	1    0    0    -1  
$EndComp
$Comp
L REF5050 U403
U 1 1 58D4DF3B
P 2200 3375
F 0 "U403" H 2200 3050 60  0000 C CNN
F 1 "REF5050" H 2200 3675 60  0000 C CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 2200 3375 60  0001 C CNN
F 3 "" H 2200 3375 60  0001 C CNN
	1    2200 3375
	1    0    0    -1  
$EndComp
Text Notes 4475 7625 0    60   ~ 0
Sheet connectors
Text GLabel 4825 1850 2    60   UnSpc ~ 0
AD1-IN-
Text GLabel 4825 1075 2    60   UnSpc ~ 0
AD1-IN+
$Comp
L R R407
U 1 1 58D8B215
P 4225 1075
F 0 "R407" V 4305 1075 50  0000 C CNN
F 1 "220" V 4225 1075 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" H 4225 1075 60  0001 C CNN
F 3 "" H 4225 1075 60  0001 C CNN
	1    4225 1075
	0    -1   -1   0   
$EndComp
$Comp
L C C413
U 1 1 58D8B21B
P 4475 1275
F 0 "C413" H 4525 1375 50  0000 L CNN
F 1 "330nF" H 4525 1175 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 4475 1275 60  0001 C CNN
F 3 "" H 4475 1275 60  0001 C CNN
	1    4475 1275
	1    0    0    -1  
$EndComp
$Comp
L R R408
U 1 1 58D8B227
P 4250 1850
F 0 "R408" V 4330 1850 50  0000 C CNN
F 1 "220" V 4250 1850 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" H 4250 1850 60  0001 C CNN
F 3 "" H 4250 1850 60  0001 C CNN
	1    4250 1850
	0    -1   -1   0   
$EndComp
$Comp
L C C414
U 1 1 58D8B22D
P 4475 1675
F 0 "C414" H 4525 1775 50  0000 L CNN
F 1 "330nF" H 4525 1575 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 4475 1675 60  0001 C CNN
F 3 "" H 4475 1675 60  0001 C CNN
	1    4475 1675
	1    0    0    -1  
$EndComp
$Comp
L R R403
U 1 1 58D8ECFB
P 2925 1450
F 0 "R403" V 3005 1450 50  0000 C CNN
F 1 "10k" V 2925 1450 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" H 2925 1450 60  0001 C CNN
F 3 "" H 2925 1450 60  0001 C CNN
	1    2925 1450
	0    -1   -1   0   
$EndComp
$Comp
L R R406
U 1 1 58D8EEC4
P 3550 1450
F 0 "R406" V 3630 1450 50  0000 C CNN
F 1 "10k" V 3550 1450 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" H 3550 1450 60  0001 C CNN
F 3 "" H 3550 1450 60  0001 C CNN
	1    3550 1450
	0    -1   -1   0   
$EndComp
$Comp
L OPA2277-RESCUE-PIAD-18bits U401
U 1 1 58D93A53
P 3550 1850
AR Path="/58D93A53" Ref="U401"  Part="1" 
AR Path="/58D18D68/58D93A53" Ref="U401"  Part="1" 
F 0 "U401" H 3775 2125 60  0000 C CNN
F 1 "OPA2277" H 3775 2025 60  0000 C CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 3550 1850 60  0001 C CNN
F 3 "" H 3550 1850 60  0000 C CNN
	1    3550 1850
	1    0    0    1   
$EndComp
$Comp
L OPA2277-RESCUE-PIAD-18bits U401
U 2 1 58D93B59
P 2275 1075
AR Path="/58D93B59" Ref="U401"  Part="2" 
AR Path="/58D18D68/58D93B59" Ref="U401"  Part="2" 
F 0 "U401" H 2275 1450 60  0000 C CNN
F 1 "OPA2277" H 2275 1350 60  0000 C CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 2275 1075 60  0001 C CNN
F 3 "" H 2275 1075 60  0000 C CNN
	2    2275 1075
	1    0    0    -1  
$EndComp
$Comp
L OPA2277-RESCUE-PIAD-18bits U401
U 3 1 58D93CA1
P 1000 1450
AR Path="/58D93CA1" Ref="U401"  Part="3" 
AR Path="/58D18D68/58D93CA1" Ref="U401"  Part="3" 
F 0 "U401" H 1228 1503 60  0000 L CNN
F 1 "OPA2277" H 1228 1397 60  0000 L CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 1000 1450 60  0001 C CNN
F 3 "" H 1000 1450 60  0000 C CNN
	3    1000 1450
	1    0    0    -1  
$EndComp
NoConn ~ 1600 3225
NoConn ~ 1600 3425
NoConn ~ 2800 3225
NoConn ~ 2800 3325
Text Label 1550 975  0    60   ~ 0
ADC_IN
Text Label 9175 5375 0    60   ~ 0
CLK
Text Label 10025 5475 0    60   ~ 0
MISO
Text Label 10675 3875 0    60   ~ 0
BUSY
NoConn ~ 9975 4175
NoConn ~ 9975 4075
NoConn ~ 9975 3975
NoConn ~ 8075 2175
NoConn ~ 8175 2175
NoConn ~ 6875 3875
NoConn ~ 6875 3975
NoConn ~ 6875 4075
NoConn ~ 6875 4175
NoConn ~ 6875 4275
NoConn ~ 8875 5275
NoConn ~ 8975 5275
Text Label 10175 3275 0    60   ~ 0
CNVST
Text Label 10175 3575 0    60   ~ 0
CS
NoConn ~ 2800 3525
Text Label 1750 6350 3    60   ~ 0
VDD_ADC
Text Label 925  3125 0    60   ~ 0
VDD_ADC
Text Label 4025 6350 3    60   ~ 0
VSS_ADC
Text Label 4525 6125 0    60   ~ 0
+5V_ADC
Text Label 4525 6275 0    60   ~ 0
+3.3V
Text Label 6075 3875 1    60   ~ 0
+5V
Text Label 6450 3575 0    60   ~ 0
+3.3V
Text Label 10450 4275 2    60   ~ 0
+3.3V
Text Label 7550 2025 0    60   ~ 0
+3.3V
Text Label 7575 6125 0    60   ~ 0
+3.3V
Text Label 1225 1100 2    60   ~ 0
VDD_ADC
Text Label 1225 1800 2    60   ~ 0
VSS_ADC
NoConn ~ 3350 4775
NoConn ~ 3350 4875
NoConn ~ 3350 4975
NoConn ~ 3350 5625
NoConn ~ 3350 5525
NoConn ~ 3350 5425
Text Label 1875 4775 0    60   ~ 0
+5V_ADC
Text Label 9150 5625 2    60   ~ 0
+5V
Text Label 8275 1725 3    60   ~ 0
+5V
Text Label 6525 825  0    60   ~ 0
VDD_ADC
Text Label 6525 1875 0    60   ~ 0
VSS_ADC
$Comp
L C C406
U 1 1 58D66CB4
P 1750 4950
F 0 "C406" H 1475 5050 50  0000 L CNN
F 1 "10uF" H 1475 4850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 1788 4800 30  0001 C CNN
F 3 "" H 1750 4950 60  0000 C CNN
	1    1750 4950
	-1   0    0    1   
$EndComp
$Comp
L C C403
U 1 1 58D66CBA
P 1475 4950
F 0 "C403" H 1275 5050 50  0000 L CNN
F 1 "100nF" H 1225 4850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 1513 4800 30  0001 C CNN
F 3 "" H 1475 4950 60  0000 C CNN
	1    1475 4950
	-1   0    0    1   
$EndComp
$Comp
L C C412
U 1 1 58D68B12
P 3675 7125
F 0 "C412" H 3325 7175 50  0000 L CNN
F 1 "10uF" H 3325 7100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 3713 6975 30  0001 C CNN
F 3 "" H 3675 7125 60  0000 C CNN
	1    3675 7125
	-1   0    0    1   
$EndComp
$Comp
L C C411
U 1 1 58D68B18
P 3425 7125
F 0 "C411" H 3225 7225 50  0000 L CNN
F 1 "100nF" H 3175 7025 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 3463 6975 30  0001 C CNN
F 3 "" H 3425 7125 60  0000 C CNN
	1    3425 7125
	-1   0    0    1   
$EndComp
$Comp
L C C402
U 1 1 58D77976
P 1475 7075
F 0 "C402" H 1500 7175 50  0000 L CNN
F 1 "10uF" H 1500 6975 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 1513 6925 30  0001 C CNN
F 3 "" H 1475 7075 60  0000 C CNN
	1    1475 7075
	1    0    0    -1  
$EndComp
$Comp
L C C408
U 1 1 58D7797C
P 1750 7075
F 0 "C408" H 1775 7175 50  0000 L CNN
F 1 "100nF" H 1775 6975 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 1788 6925 30  0001 C CNN
F 3 "" H 1750 7075 60  0000 C CNN
	1    1750 7075
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR051
U 1 1 58D7BAF6
P 1750 7325
F 0 "#PWR051" H 1750 7075 50  0001 C CNN
F 1 "GNDA" H 1750 7175 50  0000 C CNN
F 2 "" H 1750 7325 60  0000 C CNN
F 3 "" H 1750 7325 60  0000 C CNN
	1    1750 7325
	-1   0    0    -1  
$EndComp
$Comp
L CONN_01X02 P404
U 1 1 58D845FA
P 5125 5175
F 0 "P404" H 5203 5216 50  0000 L CNN
F 1 "Analog_in" H 4700 5025 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm" H 5125 5175 50  0001 C CNN
F 3 "" H 5125 5175 50  0000 C CNN
	1    5125 5175
	1    0    0    -1  
$EndComp
Text Label 4450 5125 0    60   ~ 0
ADC_IN
$Comp
L CONN_01X05 P405
U 1 1 58D8E10F
P 5175 4325
F 0 "P405" V 5375 4250 50  0000 L CNN
F 1 "ADC_pins" V 5275 4150 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 5175 4325 50  0001 C CNN
F 3 "" H 5175 4325 50  0000 C CNN
	1    5175 4325
	1    0    0    -1  
$EndComp
Text Label 4425 4125 0    60   ~ 0
MISO
Text Label 4425 4225 0    60   ~ 0
CLK
Text Label 4425 4325 0    60   ~ 0
BUSY
Text Label 4425 4425 0    60   ~ 0
CS
Text Label 4425 4525 0    60   ~ 0
CNVST
Text Notes 4425 4775 0    60   ~ 0
Test points (SPI)
$Comp
L GNDA #PWR052
U 1 1 58D5CA03
P 4725 1550
F 0 "#PWR052" H 4725 1300 50  0001 C CNN
F 1 "GNDA" H 4730 1377 50  0000 C CNN
F 2 "" H 4725 1550 50  0000 C CNN
F 3 "" H 4725 1550 50  0000 C CNN
	1    4725 1550
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR053
U 1 1 58D5CE87
P 3050 3925
F 0 "#PWR053" H 3050 3675 50  0001 C CNN
F 1 "GNDA" H 3055 3752 50  0000 C CNN
F 2 "" H 3050 3925 50  0000 C CNN
F 3 "" H 3050 3925 50  0000 C CNN
	1    3050 3925
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR054
U 1 1 58D5D5C8
P 1275 5275
F 0 "#PWR054" H 1275 5025 50  0001 C CNN
F 1 "GNDA" H 1280 5102 50  0000 C CNN
F 2 "" H 1275 5275 50  0000 C CNN
F 3 "" H 1275 5275 50  0000 C CNN
	1    1275 5275
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR055
U 1 1 58D5ECBC
P 4475 6775
F 0 "#PWR055" H 4475 6525 50  0001 C CNN
F 1 "GND" H 4480 6602 50  0000 C CNN
F 2 "" H 4475 6775 50  0000 C CNN
F 3 "" H 4475 6775 50  0000 C CNN
	1    4475 6775
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR056
U 1 1 58D5FA2D
P 2200 5025
F 0 "#PWR056" H 2200 4775 50  0001 C CNN
F 1 "GND" H 2350 4950 50  0000 C CNN
F 2 "" H 2200 5025 50  0000 C CNN
F 3 "" H 2200 5025 50  0000 C CNN
	1    2200 5025
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR057
U 1 1 58D62F48
P 10400 6175
F 0 "#PWR057" H 10400 5925 50  0001 C CNN
F 1 "GND" H 10405 6002 50  0000 C CNN
F 2 "" H 10400 6175 50  0000 C CNN
F 3 "" H 10400 6175 50  0000 C CNN
	1    10400 6175
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR058
U 1 1 58D62FE1
P 10800 6175
F 0 "#PWR058" H 10800 5925 50  0001 C CNN
F 1 "GNDA" H 10805 6002 50  0000 C CNN
F 2 "" H 10800 6175 50  0000 C CNN
F 3 "" H 10800 6175 50  0000 C CNN
	1    10800 6175
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR059
U 1 1 58D63A9E
P 9375 6125
F 0 "#PWR059" H 9375 5875 50  0001 C CNN
F 1 "GND" H 9380 5952 50  0000 C CNN
F 2 "" H 9375 6125 50  0000 C CNN
F 3 "" H 9375 6125 50  0000 C CNN
	1    9375 6125
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR060
U 1 1 58D644D7
P 7975 5625
F 0 "#PWR060" H 7975 5375 50  0001 C CNN
F 1 "GND" H 7980 5452 50  0000 C CNN
F 2 "" H 7975 5625 50  0000 C CNN
F 3 "" H 7975 5625 50  0000 C CNN
	1    7975 5625
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR061
U 1 1 58D64D84
P 6525 3825
F 0 "#PWR061" H 6525 3575 50  0001 C CNN
F 1 "GND" H 6530 3652 50  0000 C CNN
F 2 "" H 6525 3825 50  0000 C CNN
F 3 "" H 6525 3825 50  0000 C CNN
	1    6525 3825
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR062
U 1 1 58D65135
P 5825 3025
F 0 "#PWR062" H 5825 2775 50  0001 C CNN
F 1 "GNDA" H 5830 2852 50  0000 C CNN
F 2 "" H 5825 3025 50  0000 C CNN
F 3 "" H 5825 3025 50  0000 C CNN
	1    5825 3025
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR063
U 1 1 58D65DD6
P 6825 1425
F 0 "#PWR063" H 6825 1175 50  0001 C CNN
F 1 "GNDA" H 6830 1252 50  0000 C CNN
F 2 "" H 6825 1425 50  0000 C CNN
F 3 "" H 6825 1425 50  0000 C CNN
	1    6825 1425
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR064
U 1 1 58D6636B
P 8475 2150
F 0 "#PWR064" H 8475 1900 50  0001 C CNN
F 1 "GNDA" H 8480 1977 50  0000 C CNN
F 2 "" H 8475 2150 50  0000 C CNN
F 3 "" H 8475 2150 50  0000 C CNN
	1    8475 2150
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR065
U 1 1 58D670EA
P 10525 3725
F 0 "#PWR065" H 10525 3475 50  0001 C CNN
F 1 "GND" V 10425 3675 50  0000 C CNN
F 2 "" H 10525 3725 50  0000 C CNN
F 3 "" H 10525 3725 50  0000 C CNN
	1    10525 3725
	1    0    0    -1  
$EndComp
$Comp
L GNDA #PWR066
U 1 1 58D6E9A4
P 9025 1625
F 0 "#PWR066" H 9025 1375 50  0001 C CNN
F 1 "GNDA" H 9030 1452 50  0000 C CNN
F 2 "" H 9025 1625 50  0000 C CNN
F 3 "" H 9025 1625 50  0000 C CNN
	1    9025 1625
	-1   0    0    1   
$EndComp
$Comp
L R R409
U 1 1 58D6671D
P 10600 6000
F 0 "R409" V 10393 6000 50  0000 C CNN
F 1 "0" V 10484 6000 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 10530 6000 50  0001 C CNN
F 3 "" H 10600 6000 50  0000 C CNN
	1    10600 6000
	0    1    1    0   
$EndComp
$Comp
L GND #PWR067
U 1 1 58D733EE
P 1000 5275
F 0 "#PWR067" H 1000 5025 50  0001 C CNN
F 1 "GND" H 1005 5102 50  0000 C CNN
F 2 "" H 1000 5275 50  0000 C CNN
F 3 "" H 1000 5275 50  0000 C CNN
	1    1000 5275
	1    0    0    -1  
$EndComp
Connection ~ 8725 5625
Wire Wire Line
	900  1800 1225 1800
Wire Wire Line
	900  1100 1225 1100
Wire Wire Line
	8675 5275 8675 5475
Wire Wire Line
	8675 5475 10025 5475
Wire Wire Line
	6775 3775 6875 3775
Wire Wire Line
	6775 3375 6775 3775
Wire Wire Line
	8275 1725 8275 2175
Connection ~ 7325 1375
Wire Wire Line
	6825 1375 7325 1375
Connection ~ 7325 825 
Wire Wire Line
	8675 1325 8675 2175
Wire Wire Line
	7975 1325 8675 1325
Wire Wire Line
	7975 825  7975 1325
Wire Wire Line
	6525 825  7975 825 
Wire Wire Line
	7025 825  7025 925 
Connection ~ 7025 1875
Wire Wire Line
	7325 1875 7325 1775
Wire Wire Line
	7325 1225 7325 1475
Wire Wire Line
	8775 1925 8775 2175
Wire Wire Line
	8975 2175 8975 2125
Wire Wire Line
	8975 2125 9425 2125
Connection ~ 9425 1925
Wire Wire Line
	9425 2125 9425 1925
Wire Wire Line
	8875 1675 8875 2175
Wire Wire Line
	8875 1925 8975 1925
Wire Wire Line
	7875 2025 7875 2175
Connection ~ 10525 3475
Wire Wire Line
	9975 3375 10525 3375
Wire Wire Line
	10525 3375 10525 3725
Wire Wire Line
	9975 3675 10775 3675
Connection ~ 10075 4275
Wire Wire Line
	10075 3775 9975 3775
Connection ~ 9375 6075
Wire Wire Line
	8575 5275 8575 5525
Wire Wire Line
	8575 5525 9375 5525
Wire Wire Line
	9375 5525 9375 6125
Wire Wire Line
	8475 6075 9650 6075
Connection ~ 8475 5625
Wire Wire Line
	8725 5625 8725 5725
Wire Wire Line
	8475 5625 9150 5625
Connection ~ 8075 5575
Wire Wire Line
	8075 5275 8075 5675
Wire Wire Line
	7975 5275 7975 5625
Connection ~ 8275 6125
Wire Wire Line
	7575 6125 8375 6125
Wire Wire Line
	8375 6125 8375 5275
Connection ~ 7875 6125
Wire Wire Line
	8075 6125 8075 5975
Wire Wire Line
	8275 5275 8275 5675
Connection ~ 6775 3475
Wire Wire Line
	6775 3375 6875 3375
Connection ~ 6400 3425
Wire Wire Line
	6400 3425 6400 3325
Connection ~ 6075 2925
Wire Wire Line
	6075 2925 6075 3025
Wire Wire Line
	6675 3275 6875 3275
Wire Wire Line
	6675 3425 6675 3275
Wire Wire Line
	10400 6000 10400 6175
Wire Wire Line
	5825 3025 5825 2925
Wire Wire Line
	5825 2925 6675 2925
Wire Wire Line
	6675 2925 6675 3175
Wire Wire Line
	6675 3175 6875 3175
Wire Wire Line
	6400 2925 6400 3025
Connection ~ 6400 2925
Wire Wire Line
	6075 3325 6075 3875
Connection ~ 6075 3425
Wire Wire Line
	6775 3475 6875 3475
Wire Wire Line
	6525 3675 6875 3675
Connection ~ 8275 5575
Wire Wire Line
	8275 6125 8275 5975
Connection ~ 8075 6125
Wire Wire Line
	7875 5275 7875 6125
Wire Wire Line
	7975 5575 8275 5575
Connection ~ 7975 5575
Wire Wire Line
	8475 5275 8475 5725
Connection ~ 8725 6075
Wire Wire Line
	9975 4275 10450 4275
Wire Wire Line
	10075 3175 10075 4275
Wire Wire Line
	10075 3175 9975 3175
Connection ~ 10075 3775
Wire Wire Line
	10175 3575 9975 3575
Wire Wire Line
	10525 3475 9975 3475
Connection ~ 10525 3675
Wire Wire Line
	9975 3275 10175 3275
Wire Wire Line
	7550 2025 7975 2025
Wire Wire Line
	7975 2025 7975 2175
Connection ~ 7875 2025
Wire Wire Line
	9275 1925 9725 1925
Wire Wire Line
	8375 1925 8375 2175
Wire Wire Line
	7025 1225 7025 1475
Wire Wire Line
	7025 1775 7025 1875
Wire Wire Line
	6525 1875 8125 1875
Wire Wire Line
	8125 1875 8125 1425
Wire Wire Line
	8125 1425 8575 1425
Wire Wire Line
	8575 1425 8575 2175
Connection ~ 7325 1875
Wire Wire Line
	7325 825  7325 925 
Connection ~ 7025 825 
Wire Wire Line
	6825 1375 6825 1425
Connection ~ 7025 1375
Wire Wire Line
	8475 2150 8475 2175
Wire Wire Line
	9975 3875 10675 3875
Wire Wire Line
	9175 5375 8775 5375
Wire Wire Line
	8775 5375 8775 5275
Wire Wire Line
	9025 1625 9025 1675
Wire Wire Line
	9025 1675 8875 1675
Connection ~ 8875 1925
Wire Wire Line
	6525 3675 6525 3825
Wire Wire Line
	10800 6000 10800 6175
Wire Wire Line
	10775 3175 10775 3275
Wire Wire Line
	10775 3175 10125 3175
Wire Wire Line
	10125 3175 10125 3275
Connection ~ 10125 3275
Wire Wire Line
	10775 3675 10775 3575
Wire Wire Line
	6450 3575 6875 3575
Connection ~ 6775 3575
Wire Wire Line
	8175 5575 8175 5275
Connection ~ 8175 5575
Wire Wire Line
	4675 5825 5025 5825
Wire Notes Line
	4225 4150 650  4150
Wire Wire Line
	1475 4775 2350 4775
Wire Wire Line
	2200 4875 2200 5025
Wire Wire Line
	2200 4975 2350 4975
Wire Wire Line
	1475 6875 1475 6925
Wire Wire Line
	700  7300 700  7275
Wire Wire Line
	1100 7100 1100 7275
Wire Wire Line
	1150 6775 1150 6900
Wire Wire Line
	1750 6350 1750 6925
Wire Wire Line
	1250 6875 1250 6775
Wire Wire Line
	1475 5525 1475 5500
Wire Wire Line
	1750 5525 1750 5500
Wire Wire Line
	1475 5100 1475 5125
Wire Wire Line
	700  7275 750  7275
Wire Wire Line
	1975 6500 2275 6500
Wire Wire Line
	2225 6600 2275 6600
Wire Wire Line
	2225 6350 2225 6900
Connection ~ 2225 6500
Wire Wire Line
	2225 6900 2275 6900
Connection ~ 2225 6600
Wire Wire Line
	2225 6800 2275 6800
Connection ~ 2225 6800
Wire Wire Line
	2225 6700 2275 6700
Connection ~ 2225 6700
Wire Wire Line
	2275 6350 2225 6350
Wire Wire Line
	3075 6000 3075 6050
Wire Wire Line
	2825 6000 3525 6000
Wire Wire Line
	2825 6000 2825 6050
Connection ~ 2925 6000
Wire Wire Line
	4025 6900 4025 6350
Wire Wire Line
	3375 6900 4025 6900
Wire Wire Line
	3425 6800 3375 6800
Wire Wire Line
	3425 6600 3425 6975
Connection ~ 3425 6900
Wire Wire Line
	3375 6700 3475 6700
Connection ~ 3425 6800
Wire Wire Line
	3375 6600 3425 6600
Connection ~ 3425 6700
Wire Notes Line
	4150 7675 575  7675
Wire Notes Line
	575  7675 575  4425
Wire Notes Line
	575  4425 4150 4425
Wire Notes Line
	4150 4425 4150 7675
Wire Notes Line
	5700 6425 5700 600 
Wire Notes Line
	11125 6425 5700 6425
Wire Wire Line
	4375 5975 5025 5975
Wire Wire Line
	4525 6125 5025 6125
Wire Wire Line
	4475 6775 4475 6725
Wire Wire Line
	4475 6725 5075 6725
Wire Wire Line
	4725 6875 5075 6875
Wire Wire Line
	5075 7025 4725 7025
Wire Wire Line
	4725 7175 5075 7175
Wire Wire Line
	5075 7325 4725 7325
Wire Wire Line
	4725 7475 5075 7475
Wire Wire Line
	1525 6025 1775 6025
Wire Wire Line
	1775 5975 1775 6075
Wire Wire Line
	2925 6050 2925 6000
Wire Wire Line
	3525 6000 3525 6025
Connection ~ 3075 6000
Wire Wire Line
	2350 4875 2200 4875
Connection ~ 2200 4975
Wire Wire Line
	1775 5625 1775 5675
Wire Wire Line
	1525 5675 1525 5625
Connection ~ 1475 5125
Wire Wire Line
	1525 5975 1525 6025
Connection ~ 1775 6025
Wire Wire Line
	3425 7275 3425 7425
Wire Wire Line
	1050 6775 1050 6825
Wire Wire Line
	1050 6825 800  6825
Connection ~ 1475 6875
Wire Wire Line
	4525 6275 5025 6275
Connection ~ 1200 3125
Wire Wire Line
	3050 3225 3050 3525
Wire Wire Line
	1400 3325 1600 3325
Wire Wire Line
	1400 3125 1400 3325
Wire Wire Line
	925  3125 1400 3125
Wire Wire Line
	1200 3625 1400 3625
Wire Wire Line
	1400 3625 1400 3525
Wire Wire Line
	1400 3525 1600 3525
Wire Wire Line
	3050 3825 3050 3925
Wire Wire Line
	1200 3900 3050 3900
Wire Wire Line
	1200 3525 1200 3900
Connection ~ 1200 3625
Wire Wire Line
	2800 3425 3150 3425
Connection ~ 3050 3425
Connection ~ 3050 3900
Wire Wire Line
	1200 3125 1200 3225
Wire Notes Line
	650  2875 4225 2875
Wire Notes Line
	4225 2875 4225 4150
Wire Notes Line
	5700 600  11125 600 
Wire Notes Line
	11125 600  11125 6425
Wire Notes Line
	650  4150 650  2875
Wire Notes Line
	4250 5650 4250 7675
Wire Notes Line
	4250 7675 5575 7675
Wire Notes Line
	5575 7675 5575 5650
Wire Notes Line
	5575 5650 4250 5650
Connection ~ 4475 1075
Wire Wire Line
	4375 1075 4825 1075
Wire Wire Line
	2675 1075 4075 1075
Wire Wire Line
	4475 1075 4475 1125
Wire Wire Line
	4400 1850 4825 1850
Connection ~ 4475 1850
Wire Wire Line
	4475 1475 4725 1475
Wire Wire Line
	4475 1425 4475 1525
Connection ~ 4475 1475
Wire Wire Line
	4725 1475 4725 1550
Wire Wire Line
	2700 1075 2700 1450
Connection ~ 2700 1075
Wire Wire Line
	1875 1175 1875 1450
Wire Wire Line
	1875 1450 2775 1450
Connection ~ 2700 1450
Wire Wire Line
	3075 1450 3400 1450
Wire Wire Line
	3150 1450 3150 1750
Connection ~ 3150 1450
Wire Wire Line
	4025 1450 4025 1850
Wire Wire Line
	4025 1450 3700 1450
Wire Wire Line
	1875 975  1550 975 
Wire Wire Line
	4475 1825 4475 1850
Wire Wire Line
	3950 1850 4100 1850
Connection ~ 4025 1850
Wire Wire Line
	1600 1950 3150 1950
Wire Notes Line
	675  600  5375 600 
Wire Notes Line
	5375 600  5375 2625
Wire Notes Line
	5375 2625 675  2625
Wire Notes Line
	675  2625 675  600 
Wire Wire Line
	8475 6025 8475 6075
Wire Wire Line
	8725 6025 8725 6075
Wire Wire Line
	1475 4775 1475 4800
Wire Wire Line
	1750 4800 1750 4775
Connection ~ 1750 4775
Wire Wire Line
	3425 7350 3675 7350
Wire Wire Line
	3675 7350 3675 7275
Connection ~ 3425 7350
Wire Wire Line
	3675 6975 3675 6900
Connection ~ 3675 6900
Wire Wire Line
	1250 6875 1750 6875
Wire Wire Line
	1100 7275 1050 7275
Wire Wire Line
	1750 7225 1750 7325
Wire Wire Line
	1225 7300 1750 7300
Wire Wire Line
	1475 7225 1475 7300
Connection ~ 1750 7300
Connection ~ 1750 6875
Wire Wire Line
	4925 5125 4450 5125
Wire Wire Line
	4450 5225 4925 5225
Wire Notes Line
	4250 4975 4250 5525
Wire Notes Line
	4250 4975 5575 4975
Wire Notes Line
	5575 4975 5575 5525
Wire Notes Line
	5575 5525 4250 5525
Wire Wire Line
	4975 4125 4425 4125
Wire Wire Line
	4975 4225 4425 4225
Wire Wire Line
	4975 4325 4425 4325
Wire Wire Line
	4975 4425 4425 4425
Wire Wire Line
	4975 4525 4425 4525
Wire Notes Line
	4375 4000 5450 4000
Wire Notes Line
	5450 4000 5450 4850
Wire Notes Line
	5450 4850 4375 4850
Wire Notes Line
	4375 4850 4375 4000
Wire Wire Line
	10750 6000 10800 6000
Wire Wire Line
	10450 6000 10400 6000
Wire Wire Line
	1275 5200 2200 5200
Wire Wire Line
	1275 5275 1275 5200
Connection ~ 1475 5200
Wire Wire Line
	1000 5125 1000 5275
Wire Wire Line
	1000 5125 1750 5125
Wire Wire Line
	1750 5125 1750 5100
Connection ~ 1750 5200
Wire Wire Line
	6075 3425 6675 3425
Text HLabel 5025 6425 2    60   Input ~ 0
+5V
Wire Wire Line
	4525 6425 5025 6425
Text Label 4525 6425 0    60   ~ 0
+5V
$Comp
L CONN_01X02 P406
U 1 1 58F15A62
P 5275 3350
F 0 "P406" H 5225 3500 50  0000 L CNN
F 1 "CONN_01X02" H 4850 3200 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm" H 5275 3350 50  0001 C CNN
F 3 "" H 5275 3350 50  0000 C CNN
	1    5275 3350
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X02 P401
U 1 1 58F15B2A
P 1000 5925
F 0 "P401" H 950 6075 50  0000 L CNN
F 1 "CONN_01X02" H 575 5775 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm" H 1000 5925 50  0001 C CNN
F 3 "" H 1000 5925 50  0000 C CNN
	1    1000 5925
	0    1    1    0   
$EndComp
Wire Wire Line
	5075 3300 4525 3300
Text Label 4525 3300 0    60   ~ 0
VSS_ADC
Wire Wire Line
	5075 3400 4525 3400
Text Label 4525 3400 0    60   ~ 0
VDD_ADC
Wire Notes Line
	4375 3875 4375 3050
Wire Notes Line
	4375 3050 5550 3050
Wire Notes Line
	5550 3050 5550 3875
Wire Notes Line
	5550 3875 4375 3875
Text Notes 4450 3825 0    60   ~ 0
Test points (Power)
Wire Wire Line
	2200 5200 2200 5425
Wire Wire Line
	2200 5425 2350 5425
$Comp
L CONN_01X01 P402
U 1 1 58F2E577
P 3525 3225
F 0 "P402" H 3603 3266 50  0000 L CNN
F 1 "CONN_01X01" H 3603 3175 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x01_Pitch2.54mm" H 3525 3225 50  0001 C CNN
F 3 "" H 3525 3225 50  0000 C CNN
	1    3525 3225
	1    0    0    -1  
$EndComp
Wire Wire Line
	3325 3225 3050 3225
$Comp
L CONN_01X02 P403
U 1 1 58F6D20C
P 4725 2400
F 0 "P403" H 4803 2441 50  0000 L CNN
F 1 "CONN_01X02" H 4803 2350 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm" H 4725 2400 50  0001 C CNN
F 3 "" H 4725 2400 50  0000 C CNN
	1    4725 2400
	1    0    0    -1  
$EndComp
Text GLabel 4075 2350 0    60   UnSpc ~ 0
AD1-IN+
Wire Wire Line
	4525 2350 4075 2350
Text GLabel 4075 2450 0    60   UnSpc ~ 0
AD1-IN-
Wire Wire Line
	4525 2450 4075 2450
Wire Wire Line
	950  5525 2350 5525
Connection ~ 1750 5525
Wire Wire Line
	1050 5625 2350 5625
Connection ~ 1775 5625
Wire Wire Line
	1050 5625 1050 5725
Connection ~ 1525 5625
Wire Wire Line
	950  5725 950  5525
Connection ~ 1475 5525
$Comp
L R R410
U 1 1 58F7821A
P 900 7100
F 0 "R410" V 980 7100 50  0000 C CNN
F 1 "470k" V 900 7100 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 830 7100 30  0001 C CNN
F 3 "" H 900 7100 30  0000 C CNN
	1    900  7100
	0    1    1    0   
$EndComp
Wire Wire Line
	1050 6900 1225 6900
Wire Wire Line
	750  6900 700  6900
Wire Wire Line
	700  6900 700  7100
Wire Wire Line
	700  7100 750  7100
Wire Wire Line
	1050 7100 1100 7100
Wire Wire Line
	3525 6325 3525 6350
Wire Wire Line
	3375 6350 3825 6350
$Comp
L R R411
U 1 1 58F7ABD6
P 3825 6525
F 0 "R411" V 3905 6525 50  0000 C CNN
F 1 "6.2k" V 3825 6525 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 3755 6525 30  0001 C CNN
F 3 "" H 3825 6525 30  0000 C CNN
	1    3825 6525
	-1   0    0    1   
$EndComp
Wire Wire Line
	3825 6350 3825 6375
Connection ~ 3525 6350
Wire Wire Line
	3825 6675 3825 6700
Wire Wire Line
	3825 6700 3775 6700
Text Label 4450 5225 0    60   ~ 0
ADC_AGND
Text Label 1600 1950 0    60   ~ 0
ADC_AGND
Text Label 4375 5975 0    60   ~ 0
ADC_AGND
$Comp
L R R412
U 1 1 59158F35
P 9650 5700
F 0 "R412" H 9580 5654 50  0000 R CNN
F 1 "10k" H 9580 5745 50  0000 R CNN
F 2 "Resistors_SMD:R_0805" V 9580 5700 50  0001 C CNN
F 3 "" H 9650 5700 50  0000 C CNN
	1    9650 5700
	-1   0    0    1   
$EndComp
Wire Wire Line
	9650 5550 9650 5475
Connection ~ 9650 5475
Wire Wire Line
	9650 6075 9650 5850
Text Notes 2750 1275 0    60   ~ 0
R403, R406: tolerance 0.1%
Text Notes 1700 6875 2    60   ~ 0
+13.00V
Wire Wire Line
	1350 6775 1350 6875
Connection ~ 1350 6875
$Comp
L C C427
U 1 1 598E3CA4
P 1225 7125
F 0 "C427" H 1250 7275 50  0000 L CNN
F 1 "100nF" H 1225 7025 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805" H 1263 6975 50  0001 C CNN
F 3 "" H 1225 7125 50  0000 C CNN
	1    1225 7125
	1    0    0    -1  
$EndComp
Wire Wire Line
	1225 6900 1225 6975
Connection ~ 1150 6900
Wire Wire Line
	1225 7275 1225 7300
Connection ~ 1475 7300
$EndSCHEMATC