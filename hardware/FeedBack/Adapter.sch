EESchema Schematic File Version 4
EELAYER 30 0
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
L Connector_Generic:Conn_01x02 J1
U 1 1 6047EE90
P 821 1792
F 0 "J1" H 739 1467 50  0000 C CNN
F 1 "Conn_01x02" H 739 1558 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x02_P2.54mm_Vertical" H 821 1792 50  0001 C CNN
F 3 "~" H 821 1792 50  0001 C CNN
	1    821  1792
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J2
U 1 1 6047F319
P 826 2226
F 0 "J2" H 744 1901 50  0000 C CNN
F 1 "Conn_01x02" H 744 1992 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x02_P2.54mm_Vertical" H 826 2226 50  0001 C CNN
F 3 "~" H 826 2226 50  0001 C CNN
	1    826  2226
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J3
U 1 1 6047F66F
P 826 2586
F 0 "J3" H 744 2261 50  0000 C CNN
F 1 "Conn_01x02" H 744 2352 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x02_P2.54mm_Vertical" H 826 2586 50  0001 C CNN
F 3 "~" H 826 2586 50  0001 C CNN
	1    826  2586
	-1   0    0    1   
$EndComp
Text Label 1021 1692 0    50   ~ 0
AnIn
Text Label 1021 1792 0    50   ~ 0
AGND
Text Label 1026 2126 0    50   ~ 0
+10
Text Label 1026 2226 0    50   ~ 0
-10
Text Label 1026 2486 0    50   ~ 0
+15
Text Label 1026 2586 0    50   ~ 0
-15
$Comp
L Device:D_Schottky D2
U 1 1 6048BAAF
P 7500 1835
F 0 "D2" V 7454 1915 50  0000 L CNN
F 1 "SD0805S020S0R5" V 7545 1915 50  0000 L CNN
F 2 "Diode_SMD:D_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 7500 1835 50  0001 C CNN
F 3 "~" H 7500 1835 50  0001 C CNN
	1    7500 1835
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 60490A17
P 7500 2891
F 0 "R2" H 7570 2937 50  0000 L CNN
F 1 "2k2" H 7570 2846 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 7430 2891 50  0001 C CNN
F 3 "~" H 7500 2891 50  0001 C CNN
	1    7500 2891
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 60490ADB
P 7500 2490
F 0 "R1" H 7570 2536 50  0000 L CNN
F 1 "10k" H 7570 2445 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 7430 2490 50  0001 C CNN
F 3 "~" H 7500 2490 50  0001 C CNN
	1    7500 2490
	1    0    0    -1  
$EndComp
Wire Wire Line
	7500 2640 7500 2707
Wire Wire Line
	7846 2707 7500 2707
Connection ~ 7500 2707
Wire Wire Line
	7500 2707 7500 2741
Text Label 7500 1685 1    50   ~ 0
+10
$Comp
L Connector_Generic:Conn_01x01 J4
U 1 1 604A8EC6
P 8046 2707
F 0 "J4" H 8126 2749 50  0000 L CNN
F 1 "Conn_01x01" H 8126 2658 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x01_P2.54mm_Vertical" H 8046 2707 50  0001 C CNN
F 3 "~" H 8046 2707 50  0001 C CNN
	1    8046 2707
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:OPA2277 U1
U 1 1 604B7427
P 6008 2131
F 0 "U1" H 5958 2133 50  0000 C CNN
F 1 "OPA2277" H 6008 2407 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 6008 2131 50  0001 C CNN
F 3 "https://www.ti.com/lit/ds/symlink/opa2277.pdf" H 6008 2131 50  0001 C CNN
	1    6008 2131
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2277 U1
U 2 1 604C8E0C
P 4488 2031
F 0 "U1" H 4466 2030 50  0000 C CNN
F 1 "OPA2277" H 4521 1844 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 4488 2031 50  0001 C CNN
F 3 "https://www.ti.com/lit/ds/symlink/opa2277.pdf" H 4488 2031 50  0001 C CNN
	2    4488 2031
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2277 U1
U 3 1 604DAB92
P 6554 2992
F 0 "U1" H 6512 3038 50  0000 L CNN
F 1 "OPA2277" H 6512 2947 50  0000 L CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 6554 2992 50  0001 C CNN
F 3 "https://www.ti.com/lit/ds/symlink/opa2277.pdf" H 6554 2992 50  0001 C CNN
	3    6554 2992
	1    0    0    -1  
$EndComp
Text Label 6454 3292 0    50   ~ 0
-15
Text Label 6454 2692 0    50   ~ 0
+15
Text Label 7500 3041 3    50   ~ 0
AGND
$Comp
L Device:D D1
U 1 1 604E45F6
P 5927 1646
F 0 "D1" H 5927 1429 50  0000 C CNN
F 1 "BAT165E63" H 5927 1520 50  0000 C CNN
F 2 "Diode_SMD:D_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 5927 1646 50  0001 C CNN
F 3 "~" H 5927 1646 50  0001 C CNN
	1    5927 1646
	-1   0    0    1   
$EndComp
$Comp
L Device:D D3
U 1 1 604ECE91
P 6627 2131
F 0 "D3" H 6627 1914 50  0000 C CNN
F 1 "BAT165E63" H 6627 2005 50  0000 C CNN
F 2 "Diode_SMD:D_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 6627 2131 50  0001 C CNN
F 3 "~" H 6627 2131 50  0001 C CNN
	1    6627 2131
	-1   0    0    1   
$EndComp
Wire Wire Line
	6308 2131 6324 2131
Wire Wire Line
	6077 1646 6324 1646
Wire Wire Line
	6324 1646 6324 2131
Connection ~ 6324 2131
Wire Wire Line
	6324 2131 6477 2131
Wire Wire Line
	5708 2031 5626 2031
Wire Wire Line
	5626 2031 5626 1646
Wire Wire Line
	5626 1646 5777 1646
Wire Wire Line
	5626 2031 5541 2031
Connection ~ 5626 2031
Text Label 5708 2231 2    50   ~ 0
AGND
$Comp
L Device:R R3
U 1 1 6050F9B5
P 5391 2031
F 0 "R3" V 5184 2031 50  0000 C CNN
F 1 "1k" V 5275 2031 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 5321 2031 50  0001 C CNN
F 3 "~" H 5391 2031 50  0001 C CNN
	1    5391 2031
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 605110C9
P 5960 1257
F 0 "R4" V 5753 1257 50  0000 C CNN
F 1 "1k" V 5844 1257 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 5890 1257 50  0001 C CNN
F 3 "~" H 5960 1257 50  0001 C CNN
	1    5960 1257
	0    1    1    0   
$EndComp
Wire Wire Line
	6110 1257 6872 1257
Wire Wire Line
	6872 1257 6872 2131
Wire Wire Line
	6872 2131 6777 2131
Wire Wire Line
	5810 1257 5626 1257
Wire Wire Line
	5626 1257 5626 1646
Connection ~ 5626 1646
Text Label 3672 1931 2    50   ~ 0
AnIn
$Comp
L Device:C C2
U 1 1 6047E281
P 1588 3080
F 0 "C2" H 1703 3126 50  0000 L CNN
F 1 "100nF" H 1703 3035 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 1626 2930 50  0001 C CNN
F 3 "~" H 1588 3080 50  0001 C CNN
	1    1588 3080
	1    0    0    -1  
$EndComp
$Comp
L Device:C C3
U 1 1 6048116D
P 2036 3081
F 0 "C3" H 2151 3127 50  0000 L CNN
F 1 "100nF" H 2151 3036 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 2074 2931 50  0001 C CNN
F 3 "~" H 2036 3081 50  0001 C CNN
	1    2036 3081
	1    0    0    -1  
$EndComp
Text Label 1588 3230 3    50   ~ 0
AGND
Text Label 2036 3231 3    50   ~ 0
AGND
Text Label 1588 2930 0    50   ~ 0
+15
Text Label 2036 2931 0    50   ~ 0
-15
$Comp
L Device:C C1
U 1 1 60486958
P 1145 3077
F 0 "C1" H 1260 3123 50  0000 L CNN
F 1 "100nF" H 1260 3032 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 1183 2927 50  0001 C CNN
F 3 "~" H 1145 3077 50  0001 C CNN
	1    1145 3077
	1    0    0    -1  
$EndComp
Text Label 1145 2927 0    50   ~ 0
+10
Text Label 1145 3227 3    50   ~ 0
AGND
Wire Wire Line
	4788 2031 4819 2031
Connection ~ 4819 2031
Wire Wire Line
	4819 2031 5241 2031
Wire Wire Line
	4145 1931 4188 1931
Text Label 4188 2131 2    50   ~ 0
AGND
Wire Wire Line
	7500 1985 7500 2131
Wire Wire Line
	6872 2131 7500 2131
Connection ~ 6872 2131
Connection ~ 7500 2131
Wire Wire Line
	7500 2131 7500 2340
$Comp
L Device:R R6
U 1 1 605227AF
P 4508 1601
F 0 "R6" V 4301 1601 50  0000 C CNN
F 1 "1k" V 4392 1601 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 4438 1601 50  0001 C CNN
F 3 "~" H 4508 1601 50  0001 C CNN
	1    4508 1601
	0    1    1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 60523BB1
P 3882 1931
F 0 "R5" V 3675 1931 50  0000 C CNN
F 1 "1k" V 3766 1931 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 3812 1931 50  0001 C CNN
F 3 "~" H 3882 1931 50  0001 C CNN
	1    3882 1931
	0    1    1    0   
$EndComp
Wire Wire Line
	4032 1931 4145 1931
Connection ~ 4145 1931
Wire Wire Line
	3732 1931 3672 1931
Wire Wire Line
	4145 1601 4358 1601
Wire Wire Line
	4145 1601 4145 1931
Wire Wire Line
	4819 1601 4658 1601
Wire Wire Line
	4819 1601 4819 2031
$EndSCHEMATC
