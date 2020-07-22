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
L BeagleBone Beagle101
U 2 1 595E8410
P 2625 3600
F 0 "Beagle101" H 2625 4915 50  0000 C CNN
F 1 "BeagleBone" H 2625 4824 50  0000 C CNN
F 2 "Controle:BEAGLEBONEBLACK" H 2625 2500 60  0001 C CNN
F 3 "" H 2625 2500 60  0000 C CNN
	2    2625 3600
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X07 P102
U 1 1 595E84AA
P 8475 4250
F 0 "P102" H 8394 3725 50  0000 C CNN
F 1 "CONN_01X07" H 8394 3816 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x07_Pitch2.54mm" H 8475 4250 50  0001 C CNN
F 3 "" H 8475 4250 50  0000 C CNN
	1    8475 4250
	0    1    1    0   
$EndComp
$Comp
L CONN_01X05 P101
U 1 1 595E84FC
P 8575 2600
F 0 "P101" H 8653 2641 50  0000 L CNN
F 1 "CONN_01X05" H 8653 2550 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 8575 2600 50  0001 C CNN
F 3 "" H 8575 2600 50  0000 C CNN
	1    8575 2600
	0    -1   -1   0   
$EndComp
Text Label 1800 3300 0    60   ~ 0
SPI0_CS
Text Label 3450 3300 2    60   ~ 0
SPI0_MISO
Text Label 1800 3500 0    60   ~ 0
SPI0_MOSI
Text Label 3450 3500 2    60   ~ 0
SPI0_SCLK
Text Label 3450 3800 2    60   ~ 0
SPI1_CS0
Text Label 1800 3900 0    60   ~ 0
SPI1_MOSI
Text Label 3450 3900 2    60   ~ 0
SPI1_MISO
Text Label 1800 4000 0    60   ~ 0
SPI1_SCLK
$Comp
L GND #PWR01
U 1 1 595F81E4
P 3000 4750
F 0 "#PWR01" H 3000 4500 50  0001 C CNN
F 1 "GND" H 3005 4577 50  0000 C CNN
F 2 "" H 3000 4750 50  0000 C CNN
F 3 "" H 3000 4750 50  0000 C CNN
	1    3000 4750
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 595F8226
P 2250 4750
F 0 "#PWR02" H 2250 4500 50  0001 C CNN
F 1 "GND" H 2255 4577 50  0000 C CNN
F 2 "" H 2250 4750 50  0000 C CNN
F 3 "" H 2250 4750 50  0000 C CNN
	1    2250 4750
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 595F8555
P 3475 2550
F 0 "#PWR03" H 3475 2300 50  0001 C CNN
F 1 "GND" H 3480 2377 50  0000 C CNN
F 2 "" H 3475 2550 50  0000 C CNN
F 3 "" H 3475 2550 50  0000 C CNN
	1    3475 2550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 595F85AC
P 1775 2550
F 0 "#PWR04" H 1775 2300 50  0001 C CNN
F 1 "GND" H 1780 2377 50  0000 C CNN
F 2 "" H 1775 2550 50  0000 C CNN
F 3 "" H 1775 2550 50  0000 C CNN
	1    1775 2550
	-1   0    0    -1  
$EndComp
Text Label 3150 2700 2    60   ~ 0
+5V
Text Label 2100 2700 0    60   ~ 0
+5V
Text Label 8775 3575 3    60   ~ 0
DAC_LDAC
Text Label 8675 3575 3    60   ~ 0
DAC_CLR
Text Label 8575 3575 3    60   ~ 0
DAC_RST
Text Label 8475 3575 3    60   ~ 0
DAC_MOSI
Text Label 8375 3575 3    60   ~ 0
DAC_MISO
Text Label 8275 3575 3    60   ~ 0
DAC_CLK
Text Label 8175 3575 3    60   ~ 0
DAC_CS
Text Label 8375 3250 1    60   ~ 0
ADC_MISO
Text Label 8475 3250 1    60   ~ 0
ADC_CLK
Text Label 8575 3250 1    60   ~ 0
ADC_BUSY
Text Label 8675 3250 1    60   ~ 0
ADC_CS
Text Label 8775 3250 1    60   ~ 0
ADC_CNV
$Comp
L GND #PWR05
U 1 1 595F9977
P 6600 4950
F 0 "#PWR05" H 6600 4700 50  0001 C CNN
F 1 "GND" H 6605 4777 50  0000 C CNN
F 2 "" H 6600 4950 50  0000 C CNN
F 3 "" H 6600 4950 50  0000 C CNN
	1    6600 4950
	1    0    0    -1  
$EndComp
$Comp
L CONN_02X02 P103
U 1 1 595F9D9E
P 8525 5400
F 0 "P103" H 8525 5665 50  0000 C CNN
F 1 "CONN_02X02" H 8525 5574 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x02_Pitch2.54mm" H 8525 4200 50  0001 C CNN
F 3 "" H 8525 4200 50  0000 C CNN
	1    8525 5400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 595F9E66
P 8150 5500
F 0 "#PWR06" H 8150 5250 50  0001 C CNN
F 1 "GND" H 8155 5327 50  0000 C CNN
F 2 "" H 8150 5500 50  0000 C CNN
F 3 "" H 8150 5500 50  0000 C CNN
	1    8150 5500
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 595F9F24
P 8900 5500
F 0 "#PWR07" H 8900 5250 50  0001 C CNN
F 1 "GND" H 8905 5327 50  0000 C CNN
F 2 "" H 8900 5500 50  0000 C CNN
F 3 "" H 8900 5500 50  0000 C CNN
	1    8900 5500
	1    0    0    -1  
$EndComp
Text Label 4525 4175 0    60   ~ 0
SPI1_MOSI
Text Label 4525 3975 0    60   ~ 0
SPI1_SCLK
Text Label 4525 3875 0    60   ~ 0
SPI1_CS0
Text Label 6975 4175 2    60   ~ 0
DAC_MOSI
Text Label 6975 4075 2    60   ~ 0
DAC_MISO
Text Label 6975 3975 2    60   ~ 0
DAC_CLK
Text Label 6975 3875 2    60   ~ 0
DAC_CS
Text Label 4525 2725 0    60   ~ 0
SPI0_MISO
Text Label 4525 2625 0    60   ~ 0
SPI0_SCLK
Text Label 4525 2425 0    60   ~ 0
SPI0_CS
Text Notes 2475 1925 0    120  ~ 24
SPI0: ADC\nSPI1: DAC
$Comp
L GND #PWR08
U 1 1 595FB600
P 6600 3100
F 0 "#PWR08" H 6600 2850 50  0001 C CNN
F 1 "GND" H 6605 2927 50  0000 C CNN
F 2 "" H 6600 3100 50  0000 C CNN
F 3 "" H 6600 3100 50  0000 C CNN
	1    6600 3100
	1    0    0    -1  
$EndComp
Text Label 4525 4075 0    60   ~ 0
SPI1_MISO
Text Label 6975 4475 2    60   ~ 0
DAC_LDAC
Text Label 6975 4375 2    60   ~ 0
DAC_CLR
Text Label 6975 4275 2    60   ~ 0
DAC_RST
Text Label 4525 4475 0    60   ~ 0
GPIO_LDAC
Text Label 4525 4275 0    60   ~ 0
GPIO_RST
Text Label 4525 4375 0    60   ~ 0
GPIO_CLR
Text Label 3450 3600 2    60   ~ 0
GPIO_LDAC
Text Label 3450 3700 2    60   ~ 0
GPIO_RST
Text Label 6950 2725 2    60   ~ 0
ADC_MISO
Text Label 6950 2625 2    60   ~ 0
ADC_CLK
Text Label 6950 2525 2    60   ~ 0
ADC_BUSY
Text Label 6950 2425 2    60   ~ 0
ADC_CS
Text Label 6950 2325 2    60   ~ 0
ADC_CNV
Text Label 4525 2525 0    60   ~ 0
GPIO_BUSY
Text Label 4525 2325 0    60   ~ 0
GPIO_CNV
Text Label 3450 3100 2    60   ~ 0
GPIO_CNV
Text Label 3450 3200 2    60   ~ 0
GPIO_BUSY
NoConn ~ 6525 5600
NoConn ~ 6525 5775
NoConn ~ 6525 5950
NoConn ~ 6525 6125
$Comp
L CONN_01X01 P104
U 1 1 595F9DE9
P 6725 5600
F 0 "P104" H 6803 5641 50  0000 L CNN
F 1 "CONN_01X01" H 6803 5550 50  0000 L CNN
F 2 "Controle:ground_plane_via" H 6725 5600 50  0001 C CNN
F 3 "" H 6725 5600 50  0000 C CNN
	1    6725 5600
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X01 P105
U 1 1 595F9E73
P 6725 5775
F 0 "P105" H 6803 5816 50  0000 L CNN
F 1 "CONN_01X01" H 6803 5725 50  0000 L CNN
F 2 "Controle:ground_plane_via" H 6725 5775 50  0001 C CNN
F 3 "" H 6725 5775 50  0000 C CNN
	1    6725 5775
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X01 P106
U 1 1 595F9EBB
P 6725 5950
F 0 "P106" H 6803 5991 50  0000 L CNN
F 1 "CONN_01X01" H 6803 5900 50  0000 L CNN
F 2 "Controle:ground_plane_via" H 6725 5950 50  0001 C CNN
F 3 "" H 6725 5950 50  0000 C CNN
	1    6725 5950
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X01 P107
U 1 1 595F9F01
P 6725 6125
F 0 "P107" H 6803 6166 50  0000 L CNN
F 1 "CONN_01X01" H 6803 6075 50  0000 L CNN
F 2 "Controle:ground_plane_via" H 6725 6125 50  0001 C CNN
F 3 "" H 6725 6125 50  0000 C CNN
	1    6725 6125
	1    0    0    -1  
$EndComp
$Comp
L HC245 U102
U 1 1 595FB4FA
P 5800 2525
F 0 "U102" H 5800 3250 50  0000 C CNN
F 1 "HC245" H 5800 3159 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-20W_7.5x12.8mm_Pitch1.27mm" H 5800 2525 50  0001 C CNN
F 3 "" H 5800 2525 50  0000 C CNN
	1    5800 2525
	-1   0    0    -1  
$EndComp
$Comp
L HC245 U101
U 1 1 595FB6C1
P 5800 4375
F 0 "U101" H 5800 5100 50  0000 C CNN
F 1 "HC245" H 5800 5009 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-20W_7.5x12.8mm_Pitch1.27mm" H 5800 4375 50  0001 C CNN
F 3 "" H 5800 4375 50  0000 C CNN
	1    5800 4375
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR09
U 1 1 595FB88D
P 5175 4950
F 0 "#PWR09" H 5175 4700 50  0001 C CNN
F 1 "GND" H 5180 4777 50  0000 C CNN
F 2 "" H 5175 4950 50  0000 C CNN
F 3 "" H 5175 4950 50  0000 C CNN
	1    5175 4950
	-1   0    0    -1  
$EndComp
Text Label 5075 4775 0    60   ~ 0
+5V
Text Label 5075 2925 0    60   ~ 0
+5V
$Comp
L GND #PWR010
U 1 1 595FBD34
P 5200 3100
F 0 "#PWR010" H 5200 2850 50  0001 C CNN
F 1 "GND" H 5205 2927 50  0000 C CNN
F 2 "" H 5200 3100 50  0000 C CNN
F 3 "" H 5200 3100 50  0000 C CNN
	1    5200 3100
	-1   0    0    -1  
$EndComp
NoConn ~ 6500 2025
NoConn ~ 6500 2125
NoConn ~ 6500 2225
NoConn ~ 5100 2025
NoConn ~ 5100 2125
NoConn ~ 5100 2225
NoConn ~ 5100 4575
NoConn ~ 6500 4575
NoConn ~ 2375 2600
NoConn ~ 2875 2600
NoConn ~ 2375 2800
NoConn ~ 2375 2900
NoConn ~ 2375 3000
NoConn ~ 2375 3100
NoConn ~ 2375 3200
NoConn ~ 2375 3400
NoConn ~ 2875 3000
NoConn ~ 2875 2900
NoConn ~ 2875 2800
NoConn ~ 2375 3800
NoConn ~ 2375 4100
NoConn ~ 2375 4200
NoConn ~ 2375 4300
NoConn ~ 2375 4400
NoConn ~ 2375 4500
NoConn ~ 2875 4500
NoConn ~ 2875 4400
NoConn ~ 2875 4300
Text Label 4525 1575 0    60   ~ 0
SPI0_MOSI
NoConn ~ 5100 1575
Text Label 1800 3700 0    60   ~ 0
GPIO_CLR
NoConn ~ 2875 3400
NoConn ~ 2875 4200
NoConn ~ 2875 4100
NoConn ~ 2875 4000
Text Label 8100 6025 0    60   ~ 0
+5V
$Comp
L CONN_01X02 P108
U 1 1 5964DAF5
P 8675 6075
F 0 "P108" H 8753 6116 50  0000 L CNN
F 1 "CONN_01X02" H 8753 6025 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm" H 8675 6075 50  0001 C CNN
F 3 "" H 8675 6075 50  0000 C CNN
	1    8675 6075
	1    0    0    -1  
$EndComp
Wire Wire Line
	2375 3300 1800 3300
Wire Wire Line
	3450 3300 2875 3300
Wire Wire Line
	2375 3500 1800 3500
Wire Wire Line
	2875 3500 3450 3500
Wire Wire Line
	2875 3800 3450 3800
Wire Wire Line
	2375 3900 1800 3900
Wire Wire Line
	2375 4000 1800 4000
Wire Wire Line
	3450 3900 2875 3900
Wire Wire Line
	2875 4700 3000 4700
Wire Wire Line
	3000 4600 3000 4750
Wire Wire Line
	2875 4600 3000 4600
Connection ~ 3000 4700
Wire Wire Line
	2375 4700 2250 4700
Wire Wire Line
	2250 4600 2250 4750
Wire Wire Line
	2375 4600 2250 4600
Connection ~ 2250 4700
Wire Wire Line
	3475 2550 3475 2500
Wire Wire Line
	3475 2500 2875 2500
Wire Wire Line
	1775 2550 1775 2500
Wire Wire Line
	1775 2500 2375 2500
Wire Wire Line
	2875 2700 3150 2700
Wire Wire Line
	2375 2700 2100 2700
Wire Wire Line
	8775 4050 8775 3575
Wire Wire Line
	8675 4050 8675 3575
Wire Wire Line
	8575 4050 8575 3575
Wire Wire Line
	8475 4050 8475 3575
Wire Wire Line
	8375 4050 8375 3575
Wire Wire Line
	8275 4050 8275 3575
Wire Wire Line
	8175 4050 8175 3575
Wire Wire Line
	8375 2800 8375 3250
Wire Wire Line
	8475 2800 8475 3250
Wire Wire Line
	8575 2800 8575 3250
Wire Wire Line
	8675 2800 8675 3250
Wire Wire Line
	8775 2800 8775 3250
Wire Wire Line
	6500 4875 6600 4875
Wire Wire Line
	6600 4775 6600 4950
Wire Wire Line
	8275 5450 8150 5450
Wire Wire Line
	8150 5350 8150 5500
Wire Wire Line
	8275 5350 8150 5350
Connection ~ 8150 5450
Wire Wire Line
	8775 5450 8900 5450
Wire Wire Line
	8900 5350 8900 5500
Wire Wire Line
	8775 5350 8900 5350
Connection ~ 8900 5450
Wire Wire Line
	5100 4175 4525 4175
Wire Wire Line
	5100 3975 4525 3975
Wire Wire Line
	5100 3875 4525 3875
Wire Wire Line
	6500 4175 6975 4175
Wire Wire Line
	6500 4075 6975 4075
Wire Wire Line
	6500 3975 6975 3975
Wire Wire Line
	6500 3875 6975 3875
Wire Wire Line
	5100 2725 4525 2725
Wire Wire Line
	5100 2625 4525 2625
Wire Wire Line
	5100 2425 4525 2425
Wire Bus Line
	2450 1525 3425 1525
Wire Bus Line
	3425 1525 3425 1950
Wire Bus Line
	3425 1950 2450 1950
Wire Bus Line
	2450 1950 2450 1525
Wire Wire Line
	6600 4775 6500 4775
Connection ~ 6600 4875
Wire Wire Line
	6500 3025 6600 3025
Wire Wire Line
	6600 2925 6600 3100
Wire Wire Line
	6600 2925 6500 2925
Connection ~ 6600 3025
Wire Wire Line
	4525 4075 5100 4075
Wire Wire Line
	6500 4475 6975 4475
Wire Wire Line
	6500 4375 6975 4375
Wire Wire Line
	6500 4275 6975 4275
Wire Wire Line
	5100 4475 4525 4475
Wire Wire Line
	5100 4275 4525 4275
Wire Wire Line
	4525 4375 5100 4375
Wire Wire Line
	2875 3700 3450 3700
Wire Wire Line
	6500 2725 6950 2725
Wire Wire Line
	6500 2625 6950 2625
Wire Wire Line
	6500 2525 6950 2525
Wire Wire Line
	6500 2425 6950 2425
Wire Wire Line
	6500 2325 6950 2325
Wire Wire Line
	5100 2525 4525 2525
Wire Wire Line
	5100 2325 4525 2325
Wire Wire Line
	2875 3100 3450 3100
Wire Wire Line
	2875 3200 3450 3200
Wire Wire Line
	5175 4875 5175 4950
Wire Wire Line
	5275 4875 5175 4875
Wire Wire Line
	5275 4775 5075 4775
Wire Wire Line
	5275 2925 5075 2925
Wire Wire Line
	5275 3025 5200 3025
Wire Wire Line
	5200 3025 5200 3100
Wire Wire Line
	5100 1575 4525 1575
Wire Wire Line
	3450 3600 2875 3600
Wire Wire Line
	1800 3700 2375 3700
Wire Wire Line
	8100 6025 8475 6025
Wire Wire Line
	8475 6125 8400 6125
Wire Wire Line
	8400 6125 8400 6025
Connection ~ 8400 6025
$Comp
L CONN_01X01 P109
U 1 1 5964E12B
P 5450 5875
F 0 "P109" H 5528 5916 50  0000 L CNN
F 1 "CONN_01X01" H 5528 5825 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x01_Pitch2.54mm" H 5450 5875 50  0001 C CNN
F 3 "" H 5450 5875 50  0000 C CNN
	1    5450 5875
	1    0    0    -1  
$EndComp
Wire Wire Line
	2375 3600 1800 3600
Text Label 1800 3600 0    60   ~ 0
PWR_SYS
Wire Wire Line
	5250 5875 4675 5875
Text Label 4675 5875 0    60   ~ 0
PWR_SYS
$EndSCHEMATC