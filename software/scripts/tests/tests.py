#!/usr/bin/python3

from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
import selection
import dac
import adc
import sys
import math
import time
import matplotlib.pyplot as plt
#-------------------------------------------------------
# initialize the bus and device /dev/spidev1.0
spi = SPI(0,0)
#defining mode (CPOL = 0; CPHA = 1)
spi.mode = 1
#defining speed (in bps)
spi.msh = 10000000
#=======================================================
#    linearity test with multimeter
#=======================================================
def linearity_multimeter(board):
    time.sleep(1)
#=======================================================
#    linearity test without multimeter
#=======================================================
def linearity(board):
    time.sleep(1)
#=======================================================
#    repetibility test with multimeter
#=======================================================
def repetibility_multimeter(board):
    time.sleep(1)
#=======================================================
#    repetibility test without multimeter
#=======================================================
def repetibility(board):
    # select DAC of the board requested
    selection.dac(board)
    dac.config()

    print "  ======================================================\n"
    from time import gmtime, strftime

    timestr = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    filename = "repetibility/" + timestr + "_"

    tensoes = [-9, -5, 0, 5, 9]
    # total time of the test (in seconds)
    # total_time = 12*60*60
    total_time = 0.07 * 60 * 60
    # save time when test started
    startTime = time.time()
    ############################################################
    for x in tensoes:
        if (x > 0):
            log = open(filename + "+" + str(x) + "V.csv", "a+")
        else:
            log = open(filename + str(x) + "V.csv", "a+")
        # set tabs of .csv file
        log.write(';Valor lido no multimetro (V)')
        log.write(';Valor lido no multimetro (LSB)')
        log.write(';ADC - Leitura do valor integrado (V)')
        log.write(';ADC - Leitura do valor integrado (LSB)')
        log.write(';MBTemp1:Channel5 (graus C)')
        log.write('\n')
        # Update the file
        log.close()
    print "  ============================================================================"
    print "  |                             REPETIBILIDADE                               |"
    print "  ============================================================================"
    print "  | DAC\t\tMULT.\t\tMULT.(LSB)\tADC\tADC(V)\t\tTEMP.|"
    print "  |--------------------------------------------------------------------------|"
    while ((time.time() - startTime) < total_time):
        for x in tensoes:
            base = int(((x + 10) / (20 / float(262144))))
            # select DAC and write correspondent value
            selection.dac(board)
            dac.write(base)
            time.sleep(0.01)
            # ---------------------------------------------------
            if (x > 0):
                log = open(filename + "+" + str(x) + "V.csv", "a+")
            else:
                log = open(filename + str(x) + "V.csv", "a+")
            # ---------------------------------------------------
            selection.adc(board)
            adc_value = adc.read()
            '''
            measure = []
            for j in range(100):
                measure.append(adc.read())
            #	#print numpy.mean(measure)
            adc_value = sum(measure) / len(measure)
            '''
            if (abs(adc_value - base) > 1000):
                error += 1
                print error

            # adc = "{:1}".format(adc)
            # adc = numpy.mean(measure)
            adc_volt = float(adc_value) / 262143 * 20 - 10
            adc_volt_str = '{:.8f}'.format(adc_volt)
            #adc_volt_str = str(adc_volt)
            #adc_volt_str = adc_volt_str[0:adc_volt_str.find(".") + 8]
            # ---------------------------------------------------
            log.write(str(base) + ';' + ';' + str(adc_value) + ';' + str(adc_volt) + ';;')
            '''
            for j in range(100):
                log.write(str(measure[j]) + ';')
            log.write('\n')
            '''
            # Update the file
            log.close()
            # print data on terminal
            sys.stdout.write("  | " + str(base) + "\t" + "-----   " + "\t" + "  -----   " + "\t")
            # ---------------------------------------------------------
            sys.stdout.write(str(adc_value) + "\t")
            # ---------------------------------------------------------
            if (adc_volt < 0):
                sys.stdout.write(str(adc_volt_str) + "\t")
            else:
                sys.stdout.write("+" + str(adc_volt_str) + "\t")
            # ---------------------------------------------------------
            # sys.stdout.write(temp_str + "|" + "\n")
            sys.stdout.write('---\t' + "|" + "\n")
        print "  |--------------------------------------------------------------------------|"
    print "ERROR = " + str(error)
#=======================================================
#    repetibility ERROR test without multimeter
#=======================================================
def repetibility_error(board):
    # run calibration function and get the step that should be used
    #step = calibration(2)
    # turns on DAC and ADC circuit
    dac.on(board)
    adc.on(board)
    # select DAC of the board requested
    selection.dac(board)
    dac.config()

    print "  ======================================================\n"
    from time import gmtime, strftime

    timestr = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    filename = "repetibility/" + timestr + "_error_log_file.csv"
    log = open(filename, "a+")
    # set tabs of .csv file
    log.write('Iteracao')
    log.write(';Status')
    log.write(';Horario')
    log.write(';Valor setado [LSB]')
    log.write(';Valor lido [LSB]')
    log.write(';Valor lido [V]')
    log.write(';Diferenca [LSB]')
    log.write('\n')
    # Update the file
    log.close()

    # save time when test started
    startTime = time.time()
    ############################################################
    print "  ============================================================================"
    print "  |                             REPETIBILIDADE                               |"
    print "  ============================================================================"
    print "  | DAC\t\tMULT.\t\tMULT.(LSB)\tADC\tADC(V)\t\tTEMP.|"
    print "  |--------------------------------------------------------------------------|"
    iteration = 0
    error = 0
    while (1):
        # read current time
        startTime = time.time()
        #while ((time.time() - startTime) < 1*60*60):
        points = 1024
        while ((time.time() - startTime) < 1*60*60):
            for i in range(points):
                base = int((math.sin(i*1.0/points*2*math.pi) + 1)*131071.5)
                # select DAC and write correspondent value
                selection.dac(board)
                dac.write(base)
                #time.sleep(0.01)
                selection.adc(board)
                adc_value = adc.read()
                adc_volt = float(adc_value) / 262143 * 20 - 10
                adc_volt_str = '{:.8f}'.format(adc_volt)
                # check if an error occurred
                if (abs(adc_value - base) > 100):
                    error += 1
                    print error
                    # write in log file
                    log = open(filename, "a+")
                    timestr = strftime("%Y/%m/%d_%H:%M:%S", gmtime())
                    log.write(str(iteration) + ";erro;" + timestr + ';' + str(base) + ';' + str(adc_value) + ';' + str(adc_volt) + ';' + str((adc_value - base)) + "\n")
                    # Update the file
                    log.close()
                # print data on terminal
                sys.stdout.write("  | " + str(base) + "\t" + "-----   " + "\t" + "  -----   " + "\t")
                # ---------------------------------------------------------
                sys.stdout.write(str(adc_value) + "\t")
                # ---------------------------------------------------------
                if (adc_volt < 0):
                    sys.stdout.write(str(adc_volt_str) + "\t")
                else:
                    sys.stdout.write("+" + str(adc_volt_str) + "\t")
                # ---------------------------------------------------------
                # sys.stdout.write(temp_str + "|" + "\n")
                sys.stdout.write('---\t' + "|" + "\n")
            print "  |--------------------------------------------------------------------------|"
        print "ERROR = " + str(error)
        # write in log file
        log = open(filename, "a+")
        timestr = strftime("%Y/%m/%d_%H:%M:%S", gmtime())
        log.write(str(iteration) + ";fim de ciclo;" + timestr + "\n")
        # Update the file
        log.close()
        iteration += 1
    print "ERRO = " + str(error)
#=======================================================
#    stability test with multimeter
#=======================================================
def stability_multimeter(board):
    # turns on DAC and ADC circuit
    dac.on(board)
    adc.on(board)
    # set up DAC
    selection.dac(board)
    dac.config()

    from time import gmtime, strftime
    timestr = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    filename = "stability/" + timestr + "_"

    #from epics import caput
    #from epics import caget
    #import Agilent34420A

    #voltage = [-9, -5, 0, 5, 9]
    voltage = [9, -5]
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
        print "  ============================================================================"
    #    sys.stdout.write("  |                         ESTABILIDADE: ")
        sys.stdout.write("  |                           STABILITY: ")
        if(x < 0):
            sys.stdout.write(str(x) + "V" + "                                 |\n")
        elif(x > 0):
            sys.stdout.write("+" + str(x) + "V" + "                                 |\n")
        else:
            sys.stdout.write(str(x) + "V" + "                                  |\n")
        print "  ============================================================================"
        print "  | INDEX\tMULT.\t\tMULT.[LSB]\tADC\tADC(V)\t\tTEMP.|"
        print "  |--------------------------------------------------------------------------|"

        # select DAC and write correspondent value
        base = int(((x+10)/(20/float(262144))))
        selection.dac(board)
        dac.write(base)
        time.sleep(2)

        measure = []
        for i in range (total_measures):
            if (x > 0):
                log = open(filename + "+" + str(x) + "V.csv", "a+")
            else:
                log = open(filename + str(x) + "V.csv", "a+")
            #---------------------------------------------------

    #        for k in range(100):
    #            measure.append(adc.read())
    #        #    #print numpy.mean(measure)
    #        adc_value = sum(measure) / len(measure)

            selection.adc(board)
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

    #        for k in range(100):
    #            log.write(str(measure[k]) + ';')
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
        print "  |                                                                          |"

    #    #calculate standard deviation
    #    part_sum = 0
    #    for i in range(len(measure)):
    #        part_sum = part_sum + (measure[i] - mean_adc[j])**2
    #    std_var[j] = part_sum/(len(measure)*1.0)
    #    std_var[j] = math.sqrt(std_var[j])
    #    std_var[j] = "{0:.4f}".format(std_var[j])
    #    mean_adc[j] = "{0:.2f}".format(mean_adc[j])
        #---------------------------------------------------
        # plot and save Histogram
        std_var[j] = plot_hist_multimeter(board, x, measure, mean_adc[j])
        mean_adc[j] = "{0:.2f}".format(mean_adc[j])
        print "  ============================================================================"
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
        sys.stdout.write('   |\n')
        #---------------------------------------------------
        # print difference between max and min (histogram thickness)
        sys.stdout.write("  |        diff = %s" %(max_adc[j] - min_adc[j]))
        for i in range (0, (6 - len(str(max_adc[j] - min_adc[j])))):
            sys.stdout.write(' ')
        sys.stdout.write('      |\n')
        #---------------------------------------------------
        print "  ============================="
        j += 1

    # Print it all again after all the data were acquired
    j = 0
    for x in voltage:
        sys.stdout.write("  |       STABILITY: ")
        if(x > 0):
            sys.stdout.write("+")
        if(x == 0):
            sys.stdout.write(" ")
        sys.stdout.write(str(x) + "V      |\n")
        print "  ============================="
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
        sys.stdout.write('   |\n')
        #---------------------------------------------------
        # print difference between max and min (histogram thickness)
        sys.stdout.write("  |        diff = %s" %(max_adc[j] - min_adc[j]))
        for i in range (0, (6 - len(str(max_adc[j] - min_adc[j])))):
            sys.stdout.write(' ')
        sys.stdout.write('      |\n')
        #---------------------------------------------------
        print "  ============================="
        j += 1
#-------------------------------------------------------
#    function that plot histogram for stability test
#-------------------------------------------------------
def plot_hist_multimeter(board, voltage, data, mu):
    #calculate standard deviation
    part_sum = 0
    for i in range(len(data)):
        part_sum = part_sum + (data[i] - mu)**2
    sigma = part_sum/(len(data)*1.0)
    sigma = math.sqrt(sigma)
    # plot histogram
    plt.clf()
    plt.title(r'$\mathrm{Histogram\ for\ Board\ %d:}\ \mu=%.2f,\ \sigma=%.4f$' %(board, mu, sigma))
    plt.ylabel('Counts')
    plt.xlabel('Code in decimal')
    # disable scientific notation for numbers in X-axis
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    plt.hist(data, bins = range(min(data), max(data) + 1))
    plt.show()
    if(voltage >= 0):
        voltage_str = "+" + str(voltage)
    else:
        voltage_str = str(voltage)
    plt.savefig('/root/scripts/stability/board_' + str(board) + '_voltage_' + voltage_str)
    # return stardard deviation (string format)
    sigma = "{0:.4f}".format(sigma)
    return sigma
#=======================================================
#    stability test without multimeter
#=======================================================
def stability(board):
    # turns on DAC and ADC circuit
    dac.on(board)
    adc.on(board)
    # set up DAC
    selection.dac(board)
    dac.config(board)

    from time import gmtime, strftime
    timestr = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    filename = "stability/" + timestr + "_"

    #from epics import caput
    #from epics import caget
    #import Agilent34420A

    voltage = [-9, -5, 0, 5, 9]
    #voltage = [9]
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
        print "  ============================================================================"
    #    sys.stdout.write("  |                         ESTABILIDADE: ")
        sys.stdout.write("  |                           STABILITY: ")
        if(x < 0):
            sys.stdout.write(str(x) + "V" + "                                 |\n")
        elif(x > 0):
            sys.stdout.write("+" + str(x) + "V" + "                                 |\n")
        else:
            sys.stdout.write(str(x) + "V" + "                                  |\n")
        print "  ============================================================================"
        print "  | INDEX\tMULT.\t\tMULT.[LSB]\tADC\tADC(V)\t\tTEMP.|"
        print "  |--------------------------------------------------------------------------|"

        # select DAC and write correspondent value
        base = int(((x+10)/(20/float(262144))))
        selection.dac(board)
        dac.write(base)
        time.sleep(30)

        measure = []
        for i in range (total_measures):
            if (x > 0):
                log = open(filename + "+" + str(x) + "V.csv", "a+")
            else:
                log = open(filename + str(x) + "V.csv", "a+")
            #---------------------------------------------------

            selection.adc(board)
            mean_measure = []
            for k in range(3):
                mean_measure.append(adc.read())
            #    #print numpy.mean(measure)
            adc_value = sum(mean_measure) / len(mean_measure)

#            adc_value = adc.read()
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

    #        for k in range(100):
    #            log.write(str(measure[k]) + ';')
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
        print "  |                                                                          |"

    #    #calculate standard deviation
    #    part_sum = 0
    #    for i in range(len(measure)):
    #        part_sum = part_sum + (measure[i] - mean_adc[j])**2
    #    std_var[j] = part_sum/(len(measure)*1.0)
    #    std_var[j] = math.sqrt(std_var[j])
    #    std_var[j] = "{0:.4f}".format(std_var[j])
    #    mean_adc[j] = "{0:.2f}".format(mean_adc[j])
        #---------------------------------------------------
        # plot and save Histogram
        std_var[j] = plot_hist(board, x, measure, mean_adc[j])
        mean_adc[j] = "{0:.2f}".format(mean_adc[j])
        print "  ============================================================================"
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
        sys.stdout.write('   |\n')
        #---------------------------------------------------
        # print difference between max and min (histogram thickness)
        sys.stdout.write("  |        diff = %s" %(max_adc[j] - min_adc[j]))
        for i in range (0, (6 - len(str(max_adc[j] - min_adc[j])))):
            sys.stdout.write(' ')
        sys.stdout.write('      |\n')
        #---------------------------------------------------
        print "  ============================="
        j += 1

    # Print it all again after all the data were acquired
    j = 0
    for x in voltage:
        sys.stdout.write("  |       STABILITY: ")
        if(x > 0):
            sys.stdout.write("+")
        if(x == 0):
            sys.stdout.write(" ")
        sys.stdout.write(str(x) + "V      |\n")
        print "  ============================="
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
        sys.stdout.write('   |\n')
        #---------------------------------------------------
        # print difference between max and min (histogram thickness)
        sys.stdout.write("  |        diff = %s" %(max_adc[j] - min_adc[j]))
        for i in range (0, (6 - len(str(max_adc[j] - min_adc[j])))):
            sys.stdout.write(' ')
        sys.stdout.write('      |\n')
        #---------------------------------------------------
        print "  ============================="
        j += 1
#-------------------------------------------------------
#    function that plot histogram for stability test
#-------------------------------------------------------
def plot_hist(board, voltage, data, mu):
    #calculate standard deviation
    part_sum = 0
    for i in range(len(data)):
        part_sum = part_sum + (data[i] - mu)**2
    sigma = part_sum/(len(data)*1.0)
    sigma = math.sqrt(sigma)
    # plot histogram
    plt.clf()
    plt.title(r'$\mathrm{Histogram\ for\ Board\ %d:}\ \mu=%.2f,\ \sigma=%.4f$' %(board, mu, sigma))
    plt.ylabel('Counts')
    plt.xlabel('Code in decimal')
    # disable scientific notation for numbers in X-axis
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    plt.hist(data, bins = range(min(data), max(data) + 1))
    plt.show()
    if(voltage >= 0):
        voltage_str = "+" + str(voltage)
    else:
        voltage_str = str(voltage)
    plt.savefig('/root/scripts/stability/board_' + str(board) + '_voltage_' + voltage_str)
    # return stardard deviation (string format)
    sigma = "{0:.4f}".format(sigma)
    return sigma
