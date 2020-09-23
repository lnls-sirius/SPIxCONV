# SPIxCONV

This project consists of an 18-bit analog input (ADC) and output (DAC) within a range of 20 V (± 10 V) and 32 digital pins that can be either as inputs or outputs. This system interfaces with pulsed power electronics hardware in order to control the output voltage for pulsed magnets as well as read and write status commands to their power supplies. An operator interface (OPI) software based on Qt was also developed for remote control.

<!--========================================-->
## Hardware
<!--========================================-->

<!--==============================-->
### Main Board
<!--==============================-->

![Main Board](./documentation/figures/SPIxCONV.jpeg)

<!--====================-->
#### Circuit
<!--====================-->

  - Board
<p float="left">
  <img align="center" src="./documentation/figures/main_board_front.jpeg" width="400" />
  <img align="center" src="./documentation/figures/circuit_0_board.jpeg" width="400" /> 
</p>

  - CPLD
<p float="left">
  <img align="center" src="./documentation/figures/main_board_cpld.jpeg" width="400" />
  <img align="center" src="./documentation/figures/circuit_1_cpld.jpeg" width="400" /> 
</p>

  - DAC
<p float="left">
  <img align="center" src="./documentation/figures/main_board_dac.jpeg" width="400" />
  <img align="center" src="./documentation/figures/circuit_2_dac.jpeg" width="400" /> 
</p>

  - ADC
<p float="left">
  <img align="center" src="./documentation/figures/main_board_adc.jpeg" width="400" />
  <img align="center" src="./documentation/figures/circuit_3_adc.jpeg" width="400" /> 
</p>

  - Digital I/O
<p float="left">
  <img align="center" src="./documentation/figures/main_board_digital.jpeg" width="400" />
  <img align="center" src="./documentation/figures/circuit_4_digital.jpeg" width="400" /> 
</p>

<!--====================-->
#### PCB
<!--====================-->

<p float="left">
  <img align="center" src="./documentation/figures/pcb_top_layer.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/pcb_bot_layer.jpeg" width="400" />
</p>

<!--====================-->
#### Connectors
<!--====================-->

  - SPIxxCON
<p float="left">
  <img align="center" src="./documentation/figures/main_board_conn_SPIxxCON.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/conn_SPIxxCON.jpeg" width="400" />
</p>

  - CPLD
<p float="left">
  <img align="center" src="./documentation/figures/main_board_conn_CPLD.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/conn_CPLD.jpeg" width="400" />
</p>

  - Board Connection Link
<p float="left">
  <img align="center" src="./documentation/figures/main_board_conn_link.jpeg" width="280" /> 
  <img align="center" src="./documentation/figures/conn_board_link.jpeg" width="250" />
  <img align="center" src="./documentation/figures/gpio_front_conn_link.jpeg" width="280" />
</p>

<!--====================-->
#### Test Points
<!--====================-->

  - SPI
<p float="left">
  <img align="center" src="./documentation/figures/main_board_testpoint_spi.jpeg" width="400" />
</p>

  - Power Voltage
<p float="left">
  <img align="center" src="./documentation/figures/main_board_testpoint_voltage.jpeg" width="400" />
</p>

  - Analog In/Out
<p float="left">
  <img align="center" src="./documentation/figures/main_board_testpoint_analog.jpeg" width="400" />
</p>

<!--====================-->
#### BOM
<!--====================-->
Bill of materials

<!--==============================-->
### GPIO Expander Board
<!--==============================-->

![GPIO Expander Board](./documentation/figures/gpio_image.jpeg)

<!--====================-->
#### Circuit
<!--====================-->
![GPIO board circuit](./documentation/figures/gpio_schematic.jpeg)

<!--====================-->
#### PCB
<!--====================-->
<p float="left">
  <img align="center" src="./documentation/figures/gpio_pcb_top.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/gpio_pcb_bot.jpeg" width="400" />
</p>

<!--====================-->
#### Connectors
<!--====================-->

  - Interface A/B
<p float="left">
  <img align="center" src="./documentation/figures/gpio_front_conn_AB.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/conn_interface_AB.jpeg" width="400" />
</p>

  - Interface C/D
<p float="left">
  <img align="center" src="./documentation/figures/gpio_front_conn_CD.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/conn_interface_CD.jpeg" width="400" />
</p>

<!--====================-->
#### Test Points
<!--====================-->

  - Power Voltage
<p float="left">
  <img align="center" src="./documentation/figures/gpio_testpoint_voltage.jpeg" width="400" />
</p>

  - Analog In/Out
<p float="left">
  <img align="center" src="./documentation/figures/gpio_testpoint_analog.jpeg" width="400" />
</p>

<!--====================-->
#### BOM
<!--====================-->
Bill of materials

<!--====================-->
### Identification
<!--====================-->
<p float="left">
  <img align="center" src="./documentation/figures/main_board_ID.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/gpio_ID.jpeg" width="400" />
</p>

<!--========================================-->
### Software
<!--========================================-->

The software files of this project related to the server-side (IOC) is now available at [streamdevice-ioc](https://github.com/lnls-sirius/streamdevice-ioc) GitHub's repository under the "spixconv" directory.

The software files related to the OPI (Operator Interface) is now at [pydm-opi](https://github.com/lnls-sirius/pydm-opi) GitHub's repository.

Finally, the client-side (Python code) is at this repository under the [scripts](https://github.com/lnls-sirius/SPIxCONV/tree/master/software/scripts) directory.

<!--====================-->
#### Brief Description
<!--====================-->
To remotely control the board an [EPICS](https://epics-controls.org/about-epics/) IOC with an OPI was developed.

The IOC was built using [asynDriver](https://epics.anl.gov/modules/soft/asyn/) and [StreamDevice](http://epics.web.psi.ch/software/streamdevice/) on top of it. The application is launched in a form of a Docker container. The Docker image can be found at [Docker Hub](https://hub.docker.com/repository/docker/lnlscon/streamdevice-ioc) with the tag "SPIxCONV" followed by the version (eg: SPIxCONV-v1.9.6).

To configure the parameters of the IOC a [spreadsheet](https://cnpemcamp.sharepoint.com/:x:/s/controle/EUG0_4JUaz9Au7kZNcMZwZQB1x5OJBN_1QMdbbCGJ1Driw?e=Po8LNr) is used (available for CNPEM accounts only). PV's prefix, Power Supply voltage, host IP to connect to, scan rate and other settings can be adjusted. 

<!--====================-->
#### OPI (Operator Interface)
<!--====================-->

Previously, [Control System Studio](http://controlsystemstudio.org/) was used to develop the OPI. The windows can still be found under the [CSS](https://github.com/lnls-sirius/SPIxCONV/tree/master/software/CSS) directory. Lately, we have been using [PyDM (Python Display Manager)](https://slaclab.github.io/pydm/) to develop the windows. As stated before, the files related to the PyDM OPI is located in [pydm-opi](https://github.com/lnls-sirius/pydm-opi) repository.

![OPI](./documentation/figures/OPI.jpeg)

<!--====================-->
#### CPLD
<!--====================-->

<p float="left">
  <img align="center" src="./documentation/figures/cpld_setup.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/cpld_usb_blaster.jpeg" width="400" />
</p>



<!--====================-->
#### DAC & ADC Calibration
<!--====================-->

<p float="left">
  <img align="center" src="./documentation/figures/calibration_overview.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/calibration_setup.jpeg" width="400" />
</p>


<p float="left">
  <img align="center" src="./documentation/figures/calibration_usb_rs232_converter.jpeg" width="400" /> 
  <img align="center" src="./documentation/figures/calibration_multimeter_cable.jpeg" width="400" />
</p>




<!--====================-->
#### Code
<!--====================-->
[https://lnls-sirius.github.io/SPIxCONV/](https://lnls-sirius.github.io/SPIxCONV/)

<!--========================================-->
### Known Problems
<!--========================================-->

<!--========================================-->
### FAQ
<!--========================================-->

