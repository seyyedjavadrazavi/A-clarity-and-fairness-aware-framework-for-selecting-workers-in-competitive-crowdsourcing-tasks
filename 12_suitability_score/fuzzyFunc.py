import numpy as np
import skfuzzy as fuzz
# import matplotlib.pyplot as plt
import gc

def fuzziModel(number0, number1, val0, val1):
    if val0 > number0:
        val0 = number0
    
    if val1 > number1:
        val1 = number1
    
    x_reputation = np.arange(0, number0+0.1, 1)
    x_wrkr_tsk_sim = np.arange(0, number1+0.1, 1)

    x_siutability_scr  = np.arange(0, 1.01, 0.01)

    # Generate fuzzy membership functions
    reputation_lo = fuzz.trapmf(x_reputation, [-1, -1, number0*0.2, number0*0.4])
    reputation_md = fuzz.trimf(x_reputation, [number0*0.3, number0*0.5, number0*0.7])
    reputation_hi = fuzz.trapmf(x_reputation, [number0*0.6, number0*0.8, number0, number0])

    wrkr_tsk_sim_lo = fuzz.trapmf(x_wrkr_tsk_sim, [-1, -1, number1*0.2, number1*0.4])
    wrkr_tsk_sim_md = fuzz.trimf(x_wrkr_tsk_sim, [number1*0.3, number1*0.5, number1*0.7])      
    wrkr_tsk_sim_hi = fuzz.trapmf(x_wrkr_tsk_sim, [number1*0.6, number1*0.8, number1, number1])

    # siutability_scr_VL = fuzz.zmf(x_siutability_scr, 0.1, 0.2)
    siutability_scr_VL = fuzz.trapmf(x_siutability_scr, [-1, -1, 0.1, 0.2])
    siutability_scr_L = fuzz.trapmf(x_siutability_scr, [0.1, 0.2, 0.3, 0.4])
    siutability_scr_M = fuzz.trapmf(x_siutability_scr, [0.3, 0.4, 0.6, 0.7])
    siutability_scr_H = fuzz.trapmf(x_siutability_scr, [0.58, 0.7, 0.85, 0.94])
    siutability_scr_VH = fuzz.trapmf(x_siutability_scr, [0.9, 0.95, 1, 1])

    # # Visualize these universes and membership functions
    
    # fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(10, 10))

    # ax0.plot(x_AcAn, AcAn_lo, 'r', linewidth=3, label='Low')
    # ax0.plot(x_AcAn, AcAn_hi, 'b', linewidth=3, label='High')
    # ax0.set_title('AcAn')
    # ax0.legend()

    # ax1.plot(x_reputation, reputation_lo, 'r', linewidth=3, label='Low')
    # ax1.plot(x_reputation, reputation_md, 'g', linewidth=3, label='Medium')
    # ax1.plot(x_reputation, reputation_hi, 'b', linewidth=3, label='High')
    # ax1.set_title('reputation')
    # ax1.legend()

    # ax2.plot(x_wrkr_tsk_sim, wrkr_tsk_sim_lo, 'r', linewidth=3, label='Low')
    # ax2.plot(x_wrkr_tsk_sim, wrkr_tsk_sim_md, 'g', linewidth=3, label='Medium')
    # ax2.plot(x_wrkr_tsk_sim, wrkr_tsk_sim_hi, 'b', linewidth=3, label='High')
    # ax2.set_title('wrkr_tsk_sim')
    # ax2.legend()

    # # Turn off top/right axes
    # for ax in (ax0, ax1, ax2):
    #     ax.spines['top'].set_visible(False)
    #     ax.spines['right'].set_visible(False)
    #     ax.get_xaxis().tick_bottom()
    #     ax.get_yaxis().tick_left()

    # plt.tight_layout()
    # plt.show()

    reputation_level_lo = fuzz.interp_membership(x_reputation, reputation_lo, val0)
    reputation_level_md = fuzz.interp_membership(x_reputation, reputation_md, val0)
    reputation_level_hi = fuzz.interp_membership(x_reputation, reputation_hi, val0)

    wrkr_tsk_sim_level_lo = fuzz.interp_membership(x_wrkr_tsk_sim, wrkr_tsk_sim_lo, val1)
    wrkr_tsk_sim_level_md = fuzz.interp_membership(x_wrkr_tsk_sim, wrkr_tsk_sim_md, val1)
    wrkr_tsk_sim_level_hi = fuzz.interp_membership(x_wrkr_tsk_sim, wrkr_tsk_sim_hi, val1)

    ####################### Rules #################################################
    
    a1 = np.fmin(wrkr_tsk_sim_level_lo, reputation_level_lo)
    siutability_scr_activation_VL = np.fmin(a1, siutability_scr_VL)

    e1 = np.fmin(wrkr_tsk_sim_level_lo, reputation_level_md)
    siutability_scr_activation_L = np.fmin(e1, siutability_scr_L)

    c1 = np.fmin(wrkr_tsk_sim_level_md, reputation_level_lo)
    c4 = np.fmin(c1, siutability_scr_L)
    siutability_scr_activation_L = np.fmax(c4, siutability_scr_activation_L)


    j1 = np.fmin(wrkr_tsk_sim_level_lo, reputation_level_hi)
    siutability_scr_activation_M = np.fmin(j1, siutability_scr_M)

    c1 = np.fmin(wrkr_tsk_sim_level_md, reputation_level_md)
    c4 = np.fmin(c1, siutability_scr_M)
    siutability_scr_activation_M = np.fmax(c4, siutability_scr_activation_M)

    c1 = np.fmin(wrkr_tsk_sim_level_hi, reputation_level_lo)
    c4 = np.fmin(c1, siutability_scr_M)
    siutability_scr_activation_M = np.fmax(c4, siutability_scr_activation_M)

    j1 = np.fmin(wrkr_tsk_sim_level_md, reputation_level_hi)
    siutability_scr_activation_H = np.fmin(j1, siutability_scr_H)

    c1 = np.fmin(wrkr_tsk_sim_level_hi, reputation_level_md)
    c4 = np.fmin(c1, siutability_scr_H)
    siutability_scr_activation_H = np.fmax(c4, siutability_scr_activation_H)

    j1 = np.fmin(wrkr_tsk_sim_level_hi, reputation_level_hi)
    siutability_scr_activation_VH = np.fmin(j1, siutability_scr_VH)

########################### End of rules.

    siutability_scr0 = np.zeros_like(x_siutability_scr)
    
    # # Visualize this
    # fig1, ax9 = plt.subplots(figsize=(8, 3))
    # ax9.plot(x_siutability_scr, siutability_scr_VL, 'pink', linewidth=0.5, linestyle='--', )
    # ax9.fill_between(x_siutability_scr, siutability_scr0, siutability_scr_activation_L, facecolor='b', alpha=0.7)
    # ax9.plot(x_siutability_scr, siutability_scr_L, 'b', linewidth=0.5, linestyle='--', )
    # ax9.fill_between(x_siutability_scr, siutability_scr0, siutability_scr_activation_M, facecolor='g', alpha=0.7)
    # ax9.plot(x_siutability_scr, siutability_scr_M, 'g', linewidth=0.5, linestyle='--')
    # ax9.fill_between(x_siutability_scr, siutability_scr0, siutability_scr_activation_H, facecolor='brown', alpha=0.7)
    # ax9.plot(x_siutability_scr, siutability_scr_H, 'black', linewidth=0.5, linestyle='--')
    # ax9.fill_between(x_siutability_scr, siutability_scr0, siutability_scr_activation_VH, facecolor='r', alpha=0.7)
    # ax9.plot(x_siutability_scr, siutability_scr_VH, 'r', linewidth=0.5, linestyle='--')
    
    # ax9.set_title('Output membership activity')

    # # Turn off top/right axes
    # for ax in (ax9,):
    #    ax.spines['top'].set_visible(False)
    #    ax.spines['right'].set_visible(False)
    #    ax.get_xaxis().tick_bottom()
    #    ax.get_yaxis().tick_left()

    # plt.tight_layout()

    # plt.show()

    # Aggregate all three output membership functions together
    aggregated = np.fmax(siutability_scr_activation_VH, np.fmax(siutability_scr_activation_H,
                np.fmax(siutability_scr_activation_M, 
                np.fmax(siutability_scr_activation_L, siutability_scr_activation_VL))))

    # Calculate defuzzified result
    tip = fuzz.defuzz(x_siutability_scr, aggregated, 'centroid')
    # print(tip)
    tip_activation = fuzz.interp_membership(x_siutability_scr, aggregated, tip)  # for plot
    
    # # Visualize this
    # plt.close('all')
    gc.collect()

    # fig1, ax0 = plt.subplots(figsize=(8, 3))
    
    # ax0.plot(x_siutability_scr, siutability_scr_VL, 'pink', linewidth=0.5, linestyle='--', )
    # ax0.plot(x_siutability_scr, siutability_scr_L, 'b', linewidth=0.5, linestyle='--', )
    # ax0.plot(x_siutability_scr, siutability_scr_M, 'g', linewidth=0.5, linestyle='--')
    # ax0.plot(x_siutability_scr, siutability_scr_H, 'black', linewidth=0.5, linestyle='--')
    # ax0.plot(x_siutability_scr, siutability_scr_VH, 'r', linewidth=0.5, linestyle='--')
    # ax0.fill_between(x_siutability_scr, siutability_scr0, aggregated, facecolor='Orange', alpha=0.7)
    # ax0.plot([tip, tip], [0, tip_activation], 'k', linewidth=1.5, alpha=0.9)
    # ax0.set_title('Aggregated membership and result (line)')
    
    # # Turn off top/right axes
    # for ax in (ax0,):
    #    ax.spines['top'].set_visible(False)
    #    ax.spines['right'].set_visible(False)
    #    ax.get_xaxis().tick_bottom()
    #    ax.get_yaxis().tick_left()
    
    # plt.tight_layout()
    # plt.show()

    return tip
