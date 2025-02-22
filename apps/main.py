from sync_analysis import sync_analysis 
import matplotlib.pyplot as plt
import numpy as np
# import thread   

if False:
    ###################################################################################
    ##### Compile data and metadata #####
    print("## - Start data and metadata collection")
    REMARK = "1 sensor"
    sa = sync_analysis(local = False, 
                    task = "19024", 
                    sig = "raw")
    sa.set_data_files()
    sp = sa.get_file_samples()
    metadata = sa.get_metadata(len(sp))
    print("## - Data and metadata collected")
    print("Samples length : %s" % (len(sp)))


    ###################################################################################
    print("## - Start analysis")
    ###################################################################################


    ###### Analyse de la puissance des échantillons par trames et par status  ######
    ## PRODUCE : task_XXXX_frames_YY_to_ZZ.png ##
    print("## - Power over frame analysis")
    sa.set_analysis_parameters(nb_subplot_per_img = 20, 
                                hor_nbr_subplt = 4, 
                                zoom = True, 
                                symb_len = 40)

    # RX_sig_start, BUSY_sig_start, RX_sig_start_nomod, BUSY_sig_start_nomod = sa.anaylise_frame(metadata, sp, REMARK, sig_start_analysis = True)
    #sa.anaylise_IQ_frames(metadata, sp, REMARK)

    sa.anaylise_IQ_symb_one_frame(metadata, sp, REMARK, frame_nbr = 8, start = 680, end = 779)
    # sa.anaylise_IQ_symb_one_frame(metadata, sp, REMARK, frame_nbr = 9, start = 990, end = 1089)
    # sa.anaylise_IQ_symb_one_frame(metadata, sp, REMARK, frame_nbr = 14, start = 1115, end = 1214)
    # sa.anaylise_IQ_symb_one_frame(metadata, sp, REMARK, frame_nbr = 15, start = 605, end = 704)
    # sa.anaylise_IQ_symb_one_frame(metadata, sp, REMARK, frame_nbr = 147, start = 0, end = 2000)
    # sa.anaylise_IQ_symb_one_frame(metadata, sp, REMARK, frame_nbr = 148, start = 0, end = 2000)
    
    ###### Analyse de l'échantillon de départ du signal sur toute la trame - Basé sur une fourchette de valeur de threshold  ######
    ## PRODUCE : task_XXXX_samp_start_by_power_tresh.png ##
    print("## - Signal start over frame analysis")
    #sa.analyse_sig_start_nomod(REMARK, RX_sig_start_nomod, BUSY_sig_start_nomod)

    ###### Analyse de l'échantillon de départ du signal au sein d'un symbol - Basé sur une fourchette de valeur de threshold  ######
    ## PRODUCE : task_XXXX_thresh_YY_to_ZZ.png ##
    print("## - Signal start over symbol analysis")
    # sa.analyse_sig_start(REMARK, RX_sig_start, BUSY_sig_start)

    ##### Analyse des supposés quatre premiers symboles - Basé sur UNE valeur de Thresholhd ######
    ## PRODUCE : task_XXXX_SYMB_start_for_frames_YY_to_ZZ.png ##
    print("## - Presumed signal start analysis")
    sa.set_analysis_parameters(nb_subplot_per_img = 40, 
                                hor_nbr_subplt = 10, 
                                zoom = True, 
                                symb_len = 40)

    # Threshold value for signal start in dB
    if sa.local == True:
        sa.sig_tresh = 1 # For simulation
    else:
        sa.sig_tresh = -33 # For corteXlab

    # sa.analyse_symbol(metadata, sp, REMARK, "dB") 
    # sa.analyse_symbol(metadata, sp, REMARK, "IQ")


if False:

    ##### Analyse des valeurs de symboles pour chaque porteuse ######
    
    ###################################################################################
    ##### Compile data and metadata #####
    print("## - Start data and metadata collection")
    REMARK = "1 sensor"
    sa = sync_analysis(local = True, 
                    task = "carrier_1", 
                    sig = "fft_sn")
    sa.set_analysis_parameters(nb_subplot_per_img = 40, 
                hor_nbr_subplt = 10, 
                zoom = True, 
                symb_len = 40,
                fft_len = 32)
    sa.set_data_files()
    sp = sa.get_file_samples()
    metadata = sa.get_metadata(len(sp))
    print("## - Data and metadata collected")
    print("Samples length : %s" % (len(sp)))

    sa.analyse_fft(metadata, sp, REMARK)

if True:
    sa = sync_analysis(local = True, 
                    task = "", 
                    sig = "lora")
    sa.set_data_files()
    sp = sa.get_file_samples()
    print("Lora len : %s" % (len(sp)))   
    print("Ex : %s" % (sp[0]))         



###################################################################################
print("Processing done - Task %s - Local %s - RAW %s" % (sa.task, sa.local, sa.sig))
###################################################################################

