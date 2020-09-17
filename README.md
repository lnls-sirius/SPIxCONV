# SPIxCONV

This project consists of an 18-bit analog input (ADC) and output (DAC) within a range of 20 V (± 10 V) and 32 digital pins that can be either as inputs or outputs. This system interfaces with pulsed power electronics hardware in order to control the output voltage for pulsed magnets as well as read and write status commands to their power supplies. An operator interface (OPI) software based on Qt was also developed for remote control.

<!--========================================-->
## Hardware
<!--========================================-->

<!--==============================-->
### Main Board
<!--==============================-->

![Main Board](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/SPIxCONV.png)

<!--====================-->
#### Circuit
<!--====================-->

  - Board
![Board circuit](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/circuit_0_board.png)

  - CPLD
![CPLD circuit](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/circuit_1_cpld.png)

  - DAC
![DAC circuit](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/circuit_2_dac.png)

  - ADC
![ADC circuit](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/circuit_3_adc.png)

  - Digital I/O
![Digital circuit](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/circuit_4_digital.png)

<!--====================-->
#### PCB
<!--====================-->

  - Top layer
![PCB top layer](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/pcb_top_layer.png)

  - Bottom layer layer
![PCB bottom layer](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/pcb_bot_layer.png)

<!--====================-->
#### Connectors
<!--====================-->

  - SPIxxCON
![SPIxxCON connector](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/main_board_conn_SPIxxCON.jpg)
![SPIxxCON pinout](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/conn_SPIxxCON.png)

  - Board Connection Link
![Main Board Connection Link](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/main_board_conn_link.jpg)
![GPIO Board Connection Link](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/gpio_front_conn_link.jpg)
![Board Connection Link](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/conn_board_link.png)

<!--==============================-->
### GPIO Expander Board
<!--==============================-->

<!--====================-->
#### Circuit
<!--====================-->
![GPIO board circuit](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/gpio_schematic.png)

<!--====================-->
#### PCB
<!--====================-->
  - Top Layer
![Top Layer](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/gpio_pcb_top.png)

  - Bottom Layer
![Bottom Layer](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/gpio_pcb_bot.png)

<!--====================-->
#### Connectors
<!--====================-->

  - Interface A/B
![GPIO Interface A/B](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/gpio_front_conn_AB.jpg)
![GPIO Interface A/B pinout](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/conn_interface_AB.png)

  - Interface C/D
![GPIO Interface C/D](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/gpio_front_conn_CD.jpg)
![GPIO Interface C/D pinout](https://raw.githubusercontent.com/lnls-sirius/SPIxCONV/master/documentation/figures/hardware/conn_interface_CD.png)

<!--========================================-->
### Software
<!--========================================-->

[https://lnls-sirius.github.io/SPIxCONV/](https://lnls-sirius.github.io/SPIxCONV/)
