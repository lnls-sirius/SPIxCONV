#==========================
# SPIxCONV pins exported
#==========================
config-pin P9_17 spi_cs         # CS
config-pin P9_21 spi            # DO
config-pin P9_18 spi            # DI
config-pin P9_22 spi_sclk       # CLK

config-pin P8_37 gpio           # BUSY
config-pin P9_24 gpio           # LDAC / CNVST
config-pin P9_26 gpio           # RS

#==========================
# Pulsed Magnets IOC
#==========================
python /root/SPIxCONV/software/scripts/spixconv_unix_socket.py &
sleep 5

#====================================================================================
# septum de injeção no Booster
procServ --chdir /root/stream-ioc/iocBoot/SPIxCONV/ 20400 ./TB-injection_septum.cmd
#====================================================================================
#./TB-injection_septum.cmd              # septum de injeção no Booster
#./TS-ejection_thick_septum.cmd         # septum grosso de extração do Booster
#./TS-ejection_thin_septum.cmd          # septum fino de extração do Booster
#./TS-injection_thick_septum_1.cmd      # septum grosso de injeção no anel 1
#./TS-injection_thick_septum_2.cmd      # septum grosso de injeção no anel 2
#./TS-injection_thin_septum.cmd         # septum de injeção no anel
#./BO-injection_kicker.cmd              # kicker do Booster (injeção)
#./BO-ejection_kicker.cmd               # kicker do Booster (extração)
#./SI-vertical_pinger.cmd               # pinger (vertical)
#./SI-injection_non_linear_kicker.cmd   # kicker do anel (NLK or OnAxis)
#./SI-injection_dipolar_kicker.cmd      # pinger (horizontal)
