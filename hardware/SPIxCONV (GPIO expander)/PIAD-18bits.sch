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
Sheet 1 1
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
L CONN_02X13 P1
U 1 1 58D18D60
P 8775 5225
F 0 "P1" H 8775 5925 50  0000 C CNN
F 1 "CONN_02X13" V 8775 5225 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x13" H 8775 4075 60  0001 C CNN
F 3 "" H 8775 4075 60  0000 C CNN
	1    8775 5225
	1    0    0    -1  
$EndComp
Text Label 8175 4625 0    60   ~ 0
AO
Text Label 8175 4725 0    60   ~ 0
AO_GND
Text Label 9350 4725 2    60   ~ 0
AI_GND
NoConn ~ 8525 4825
NoConn ~ 9025 4825
$Comp
L GND #PWR01
U 1 1 58D18D6D
P 8150 4975
F 0 "#PWR01" H 8150 4725 50  0001 C CNN
F 1 "GND" H 8150 4825 50  0000 C CNN
F 2 "" H 8150 4975 50  0000 C CNN
F 3 "" H 8150 4975 50  0000 C CNN
	1    8150 4975
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 58D18D6E
P 9425 4975
F 0 "#PWR02" H 9425 4725 50  0001 C CNN
F 1 "GND" H 9425 4825 50  0000 C CNN
F 2 "" H 9425 4975 50  0000 C CNN
F 3 "" H 9425 4975 50  0000 C CNN
	1    9425 4975
	1    0    0    -1  
$EndComp
Text Label 7600 5775 2    60   ~ 0
PA0
Text Label 7600 5675 2    60   ~ 0
PA1
Text Label 7600 5575 2    60   ~ 0
PA2
Text Label 7600 5475 2    60   ~ 0
PA3
Text Label 7600 5375 2    60   ~ 0
PA4
Text Label 7600 5275 2    60   ~ 0
PA5
Text Label 7600 5175 2    60   ~ 0
PA6
Text Label 7600 5075 2    60   ~ 0
PA7
NoConn ~ 8525 5825
NoConn ~ 9025 5825
Text Label 9275 5025 2    60   ~ 0
PB0
Text Label 9275 5125 2    60   ~ 0
PB1
Text Label 9275 5225 2    60   ~ 0
PB2
Text Label 9275 5325 2    60   ~ 0
PB3
Text Label 9275 5425 2    60   ~ 0
PB4
Text Label 9275 5525 2    60   ~ 0
PB5
Text Label 9275 5625 2    60   ~ 0
PB6
Text Label 9275 5725 2    60   ~ 0
PB7
Text Label 9350 4625 2    60   ~ 0
AI
$Comp
L CONN_01X03 P4
U 1 1 5A677AC8
P 2825 2200
F 0 "P4" H 2825 2400 50  0000 C CNN
F 1 "CONN_01X03" V 2925 2200 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x03" H 2825 2200 50  0001 C CNN
F 3 "" H 2825 2200 50  0000 C CNN
	1    2825 2200
	-1   0    0    -1  
$EndComp
$Comp
L CONN_02X13 P3
U 1 1 5A67E7F3
P 4625 3875
F 0 "P3" H 4625 4575 50  0000 C CNN
F 1 "CONN_02X13" V 4625 3875 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x13" H 4625 2725 60  0001 C CNN
F 3 "" H 4625 2725 60  0000 C CNN
	1    4625 3875
	1    0    0    -1  
$EndComp
Text Label 4025 3275 0    60   ~ 0
AO
Text Label 4025 3375 0    60   ~ 0
AO_GND
Text Label 5200 3375 2    60   ~ 0
AI_GND
NoConn ~ 4375 3475
NoConn ~ 4875 3475
$Comp
L GND #PWR03
U 1 1 5A67E7FE
P 3850 3625
F 0 "#PWR03" H 3850 3375 50  0001 C CNN
F 1 "GND" H 3850 3475 50  0000 C CNN
F 2 "" H 3850 3625 50  0000 C CNN
F 3 "" H 3850 3625 50  0000 C CNN
	1    3850 3625
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 5A67E804
P 5400 3625
F 0 "#PWR04" H 5400 3375 50  0001 C CNN
F 1 "GND" H 5400 3475 50  0000 C CNN
F 2 "" H 5400 3625 50  0000 C CNN
F 3 "" H 5400 3625 50  0000 C CNN
	1    5400 3625
	1    0    0    -1  
$EndComp
NoConn ~ 4375 4475
NoConn ~ 4875 4475
Text Label 5200 3275 2    60   ~ 0
AI
$Comp
L XRA1405 U1
U 1 1 5A67E8AC
P 6875 5050
F 0 "U1" H 7075 4200 60  0000 C CNN
F 1 "XRA1405" H 6700 4200 60  0000 C CNN
F 2 "Housings_SSOP:TSSOP-24_4.4x7.8mm_Pitch0.65mm" H 6825 4750 60  0001 C CNN
F 3 "" H 6825 4750 60  0000 C CNN
	1    6875 5050
	1    0    0    -1  
$EndComp
$Comp
L CONN_02X10 P2
U 1 1 5A67F20B
P 8775 2700
F 0 "P2" H 8775 3250 50  0000 C CNN
F 1 "CONN_02X10" V 8775 2700 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x10" H 8775 1500 50  0001 C CNN
F 3 "" H 8775 1500 50  0000 C CNN
	1    8775 2700
	1    0    0    -1  
$EndComp
Text Label 7650 4975 2    60   ~ 0
PB0
Text Label 7650 4875 2    60   ~ 0
PB1
Text Label 7650 4775 2    60   ~ 0
PB2
Text Label 7650 4675 2    60   ~ 0
PB3
Text Label 7650 4575 2    60   ~ 0
PB4
Text Label 7650 4475 2    60   ~ 0
PB5
Text Label 7650 4375 2    60   ~ 0
PB6
Text Label 7650 4275 2    60   ~ 0
PB7
Text Label 8325 5025 0    60   ~ 0
PA0
Text Label 8325 5125 0    60   ~ 0
PA1
Text Label 8325 5225 0    60   ~ 0
PA2
Text Label 8325 5325 0    60   ~ 0
PA3
Text Label 8325 5425 0    60   ~ 0
PA4
Text Label 8325 5525 0    60   ~ 0
PA5
Text Label 8325 5625 0    60   ~ 0
PA6
Text Label 8325 5725 0    60   ~ 0
PA7
Text Label 3375 2100 2    60   ~ 0
+5V
Text Label 3375 2200 2    60   ~ 0
+1.8V
Text Label 3375 2300 2    60   ~ 0
+3.3V
Text Label 6000 5775 0    60   ~ 0
GND
Text Label 5925 5175 0    60   ~ 0
CLK
Text Label 5925 5075 0    60   ~ 0
MISO_1
Text Label 5925 4375 0    60   ~ 0
MOSI
Text Label 5925 5275 0    60   ~ 0
CS_1
Text Label 5925 4275 0    60   ~ 0
+3.3V
Wire Wire Line
	9025 5725 9275 5725
Wire Wire Line
	9275 5625 9025 5625
Wire Wire Line
	9025 5525 9275 5525
Wire Wire Line
	9275 5425 9025 5425
Wire Wire Line
	9025 5325 9275 5325
Wire Wire Line
	9275 5225 9025 5225
Wire Wire Line
	9025 5125 9275 5125
Wire Wire Line
	9275 5025 9025 5025
Wire Wire Line
	7400 5075 7600 5075
Wire Wire Line
	7600 5175 7400 5175
Wire Wire Line
	7400 5275 7600 5275
Wire Wire Line
	7600 5375 7400 5375
Wire Wire Line
	7400 5475 7600 5475
Wire Wire Line
	7600 5575 7400 5575
Wire Wire Line
	7400 5675 7600 5675
Wire Wire Line
	7600 5775 7400 5775
Wire Wire Line
	9425 4925 9025 4925
Wire Wire Line
	9425 4975 9425 4925
Wire Wire Line
	8150 4925 8525 4925
Wire Wire Line
	8150 4975 8150 4925
Wire Wire Line
	9350 4725 9025 4725
Wire Wire Line
	8175 4725 8525 4725
Wire Wire Line
	8525 4625 8175 4625
Wire Wire Line
	9025 4625 9350 4625
Wire Wire Line
	5400 3575 4875 3575
Wire Wire Line
	5400 3625 5400 3575
Wire Wire Line
	3850 3575 4375 3575
Wire Wire Line
	3850 3625 3850 3575
Wire Wire Line
	5200 3375 4875 3375
Wire Wire Line
	4025 3375 4375 3375
Wire Wire Line
	4375 3275 4025 3275
Wire Wire Line
	4875 3275 5200 3275
Wire Wire Line
	7400 4275 7650 4275
Wire Wire Line
	7650 4375 7400 4375
Wire Wire Line
	7400 4475 7650 4475
Wire Wire Line
	7650 4575 7400 4575
Wire Wire Line
	7400 4675 7650 4675
Wire Wire Line
	7650 4775 7400 4775
Wire Wire Line
	7400 4875 7650 4875
Wire Wire Line
	7650 4975 7400 4975
Wire Wire Line
	8525 5725 8325 5725
Wire Wire Line
	8325 5625 8525 5625
Wire Wire Line
	8525 5525 8325 5525
Wire Wire Line
	8325 5425 8525 5425
Wire Wire Line
	8525 5325 8325 5325
Wire Wire Line
	8325 5225 8525 5225
Wire Wire Line
	8525 5125 8325 5125
Wire Wire Line
	8325 5025 8525 5025
Wire Wire Line
	3025 2100 3375 2100
Wire Wire Line
	3375 2200 3025 2200
Wire Wire Line
	3025 2300 3375 2300
Wire Wire Line
	6300 5775 6000 5775
Wire Wire Line
	6300 5175 5925 5175
Wire Wire Line
	6300 5075 5925 5075
Wire Wire Line
	6300 4975 5925 4975
Wire Wire Line
	6300 5275 5925 5275
Wire Wire Line
	5925 4275 6300 4275
Wire Wire Line
	5925 4375 6300 4375
$Comp
L CONN_01X01 P5
U 1 1 5A68882F
P 2825 2775
F 0 "P5" H 2825 2875 50  0000 C CNN
F 1 "CONN_01X01" V 2925 2775 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x01" H 2825 2775 50  0001 C CNN
F 3 "" H 2825 2775 50  0000 C CNN
	1    2825 2775
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X01 P6
U 1 1 5A688968
P 2825 3350
F 0 "P6" H 2825 3450 50  0000 C CNN
F 1 "CONN_01X01" V 2925 3350 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x01" H 2825 3350 50  0001 C CNN
F 3 "" H 2825 3350 50  0000 C CNN
	1    2825 3350
	-1   0    0    1   
$EndComp
Wire Wire Line
	3025 2775 3375 2775
Wire Wire Line
	3025 3350 3375 3350
Text Label 3375 2775 2    60   ~ 0
GND
Text Label 3375 3350 2    60   ~ 0
GND
Wire Wire Line
	6300 4650 5925 4650
Text Label 5925 4650 0    60   ~ 0
IRQ_1
Text Label 7600 3450 2    60   ~ 0
PC0
Text Label 7600 3350 2    60   ~ 0
PC1
Text Label 7600 3250 2    60   ~ 0
PC2
Text Label 7600 3150 2    60   ~ 0
PC3
Text Label 7600 3050 2    60   ~ 0
PC4
Text Label 7600 2950 2    60   ~ 0
PC5
Text Label 7600 2850 2    60   ~ 0
PC6
Text Label 7600 2750 2    60   ~ 0
PC7
$Comp
L XRA1405 U2
U 1 1 5A68AF56
P 6875 2725
F 0 "U2" H 7075 1875 60  0000 C CNN
F 1 "XRA1405" H 6700 1875 60  0000 C CNN
F 2 "Housings_SSOP:TSSOP-24_4.4x7.8mm_Pitch0.65mm" H 6825 2425 60  0001 C CNN
F 3 "" H 6825 2425 60  0000 C CNN
	1    6875 2725
	1    0    0    -1  
$EndComp
Text Label 7650 2650 2    60   ~ 0
PD0
Text Label 7650 2550 2    60   ~ 0
PD1
Text Label 7650 2450 2    60   ~ 0
PD2
Text Label 7650 2350 2    60   ~ 0
PD3
Text Label 7650 2250 2    60   ~ 0
PD4
Text Label 7650 2150 2    60   ~ 0
PD5
Text Label 7650 2050 2    60   ~ 0
PD6
Text Label 7650 1950 2    60   ~ 0
PD7
Text Label 6000 3450 0    60   ~ 0
GND
Text Label 5925 2850 0    60   ~ 0
CLK
Text Label 5925 2750 0    60   ~ 0
MISO_2
Text Label 5925 2050 0    60   ~ 0
MOSI
Text Label 5925 2950 0    60   ~ 0
CS_2
Text Label 5925 1950 0    60   ~ 0
+3.3V
Wire Wire Line
	7400 2750 7600 2750
Wire Wire Line
	7600 2850 7400 2850
Wire Wire Line
	7400 2950 7600 2950
Wire Wire Line
	7600 3050 7400 3050
Wire Wire Line
	7400 3150 7600 3150
Wire Wire Line
	7600 3250 7400 3250
Wire Wire Line
	7400 3350 7600 3350
Wire Wire Line
	7600 3450 7400 3450
Wire Wire Line
	7400 1950 7650 1950
Wire Wire Line
	7650 2050 7400 2050
Wire Wire Line
	7400 2150 7650 2150
Wire Wire Line
	7650 2250 7400 2250
Wire Wire Line
	7400 2350 7650 2350
Wire Wire Line
	7650 2450 7400 2450
Wire Wire Line
	7400 2550 7650 2550
Wire Wire Line
	7650 2650 7400 2650
Wire Wire Line
	6300 3450 6000 3450
Wire Wire Line
	6300 2850 5925 2850
Wire Wire Line
	6300 2750 5925 2750
Wire Wire Line
	6300 2650 5925 2650
Wire Wire Line
	6300 2950 5925 2950
Wire Wire Line
	6300 2325 5925 2325
Text Label 5925 2325 0    60   ~ 0
IRQ_2
Text Label 9225 2350 2    60   ~ 0
PC0
Text Label 9225 2450 2    60   ~ 0
PC1
Text Label 9225 2550 2    60   ~ 0
PC2
Text Label 9225 2650 2    60   ~ 0
PC3
Text Label 9225 2750 2    60   ~ 0
PC4
Text Label 9225 2850 2    60   ~ 0
PC5
Text Label 9225 2950 2    60   ~ 0
PC6
Text Label 9225 3050 2    60   ~ 0
PC7
Wire Wire Line
	9025 3050 9225 3050
Wire Wire Line
	9225 2950 9025 2950
Wire Wire Line
	9025 2850 9225 2850
Wire Wire Line
	9225 2750 9025 2750
Wire Wire Line
	9025 2650 9225 2650
Wire Wire Line
	9225 2550 9025 2550
Wire Wire Line
	9025 2450 9225 2450
Wire Wire Line
	9225 2350 9025 2350
Text Label 8275 2350 0    60   ~ 0
PD0
Text Label 8275 2450 0    60   ~ 0
PD1
Text Label 8275 2550 0    60   ~ 0
PD2
Text Label 8275 2650 0    60   ~ 0
PD3
Text Label 8275 2750 0    60   ~ 0
PD4
Text Label 8275 2850 0    60   ~ 0
PD5
Text Label 8275 2950 0    60   ~ 0
PD6
Text Label 8275 3050 0    60   ~ 0
PD7
Wire Wire Line
	8525 3050 8275 3050
Wire Wire Line
	8275 2950 8525 2950
Wire Wire Line
	8525 2850 8275 2850
Wire Wire Line
	8275 2750 8525 2750
Wire Wire Line
	8525 2650 8275 2650
Wire Wire Line
	8275 2550 8525 2550
Wire Wire Line
	8525 2450 8275 2450
Wire Wire Line
	8275 2350 8525 2350
Text Label 8225 2250 0    60   ~ 0
GND
Wire Wire Line
	8525 2250 8225 2250
Text Label 8225 3150 0    60   ~ 0
GND
Wire Wire Line
	8525 3150 8225 3150
Text Label 9325 2250 2    60   ~ 0
GND
Wire Wire Line
	9025 2250 9325 2250
Text Label 9325 3150 2    60   ~ 0
GND
Wire Wire Line
	9025 3150 9325 3150
$Comp
L CONN_01X01 P7
U 1 1 5A693AAD
P 2825 5850
F 0 "P7" H 2825 5950 50  0000 C CNN
F 1 "LOGO" V 2925 5850 50  0000 C CNN
F 2 "Controle:LNLS_LOGO_Silk" H 2825 5850 50  0001 C CNN
F 3 "" H 2825 5850 50  0000 C CNN
	1    2825 5850
	-1   0    0    1   
$EndComp
NoConn ~ 3025 5850
Text Label 4000 4375 0    60   ~ 0
MISO_2
Wire Wire Line
	4375 4375 4000 4375
Wire Wire Line
	4375 3675 4000 3675
Text Label 4000 3675 0    60   ~ 0
IRQ_1
Wire Wire Line
	4375 4175 4000 4175
Text Label 4000 4175 0    60   ~ 0
IRQ_2
Text Label 5300 4075 2    60   ~ 0
CLK
Text Label 5300 3775 2    60   ~ 0
MOSI
Text Label 5300 4175 2    60   ~ 0
CS_1
Wire Wire Line
	4875 4075 5300 4075
Wire Wire Line
	4875 3775 5300 3775
Wire Wire Line
	4875 4175 5300 4175
Text Label 5300 3975 2    60   ~ 0
CS_2
Wire Wire Line
	4875 3975 5300 3975
NoConn ~ 4375 3875
NoConn ~ 4375 3975
NoConn ~ 4375 4075
NoConn ~ 4875 4375
NoConn ~ 3375 2200
NoConn ~ 3375 2100
$Comp
L CONN_01X01 P8
U 1 1 5A69D3A4
P 2825 4025
F 0 "P8" H 2825 4125 50  0000 C CNN
F 1 "MH1" V 2925 4025 50  0000 C CNN
F 2 "Controle:M3_Hole" H 2825 4025 50  0001 C CNN
F 3 "" H 2825 4025 50  0000 C CNN
	1    2825 4025
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X01 P9
U 1 1 5A69D698
P 2825 4225
F 0 "P9" H 2825 4325 50  0000 C CNN
F 1 "MH3" V 2925 4225 50  0000 C CNN
F 2 "Controle:M3_Hole" H 2825 4225 50  0001 C CNN
F 3 "" H 2825 4225 50  0000 C CNN
	1    2825 4225
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X01 P10
U 1 1 5A69D755
P 2825 4425
F 0 "P10" H 2825 4525 50  0000 C CNN
F 1 "MH4" V 2925 4425 50  0000 C CNN
F 2 "Controle:M3_Hole" H 2825 4425 50  0001 C CNN
F 3 "" H 2825 4425 50  0000 C CNN
	1    2825 4425
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X01 P11
U 1 1 5A69D875
P 2825 4775
F 0 "P11" H 2825 4875 50  0000 C CNN
F 1 "MP1" V 2925 4775 50  0000 C CNN
F 2 "Controle:M3_Hole" H 2825 4775 50  0001 C CNN
F 3 "" H 2825 4775 50  0000 C CNN
	1    2825 4775
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X01 P12
U 1 1 5A69D87B
P 2825 4975
F 0 "P12" H 2825 5075 50  0000 C CNN
F 1 "MP2" V 2925 4975 50  0000 C CNN
F 2 "Controle:M3_Hole" H 2825 4975 50  0001 C CNN
F 3 "" H 2825 4975 50  0000 C CNN
	1    2825 4975
	-1   0    0    1   
$EndComp
NoConn ~ 3025 4025
NoConn ~ 3025 4225
NoConn ~ 3025 4425
NoConn ~ 3025 4775
NoConn ~ 3025 4975
$Comp
L C C1
U 1 1 5A86ECB2
P 5200 5525
F 0 "C1" H 5225 5625 50  0000 L CNN
F 1 "10uF" H 5225 5425 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5238 5375 50  0001 C CNN
F 3 "" H 5200 5525 50  0000 C CNN
	1    5200 5525
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 5A86EDEB
P 5475 5525
F 0 "C2" H 5500 5625 50  0000 L CNN
F 1 "100nF" H 5500 5425 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5513 5375 50  0001 C CNN
F 3 "" H 5475 5525 50  0000 C CNN
	1    5475 5525
	1    0    0    -1  
$EndComp
Text Label 4900 5275 0    60   ~ 0
+3.3V
Wire Wire Line
	4900 5275 5475 5275
Text Label 4900 5775 0    60   ~ 0
GND
Wire Wire Line
	4900 5775 5475 5775
Wire Wire Line
	5475 5275 5475 5375
Wire Wire Line
	5200 5375 5200 5275
Connection ~ 5200 5275
Wire Wire Line
	5200 5675 5200 5775
Wire Wire Line
	5475 5775 5475 5675
Connection ~ 5200 5775
$Comp
L C C3
U 1 1 5A870469
P 5200 2200
F 0 "C3" H 5225 2300 50  0000 L CNN
F 1 "10uF" H 5225 2100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5238 2050 50  0001 C CNN
F 3 "" H 5200 2200 50  0000 C CNN
	1    5200 2200
	1    0    0    -1  
$EndComp
$Comp
L C C4
U 1 1 5A87046F
P 5475 2200
F 0 "C4" H 5500 2300 50  0000 L CNN
F 1 "100nF" H 5500 2100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5513 2050 50  0001 C CNN
F 3 "" H 5475 2200 50  0000 C CNN
	1    5475 2200
	1    0    0    -1  
$EndComp
Text Label 4900 1950 0    60   ~ 0
+3.3V
Wire Wire Line
	4900 1950 5475 1950
Text Label 4900 2450 0    60   ~ 0
GND
Wire Wire Line
	4900 2450 5475 2450
Wire Wire Line
	5475 1950 5475 2050
Wire Wire Line
	5200 2050 5200 1950
Connection ~ 5200 1950
Wire Wire Line
	5200 2350 5200 2450
Wire Wire Line
	5475 2450 5475 2350
Connection ~ 5200 2450
NoConn ~ 4875 4275
NoConn ~ 4375 4275
Text Label 4000 3775 0    60   ~ 0
MISO_1
Wire Wire Line
	4375 3775 4000 3775
Wire Wire Line
	5925 1950 6300 1950
Wire Wire Line
	5925 2050 6300 2050
Text Label 5925 2650 0    60   ~ 0
RESET_2
Text Label 5925 4975 0    60   ~ 0
RESET_1
Wire Wire Line
	4875 3875 5300 3875
Wire Wire Line
	4875 3675 5300 3675
Text Label 5300 3875 2    60   ~ 0
RESET_1
Text Label 5300 3675 2    60   ~ 0
RESET_2
$EndSCHEMATC