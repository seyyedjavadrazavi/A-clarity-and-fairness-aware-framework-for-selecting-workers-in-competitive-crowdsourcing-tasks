import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import gc

# number0 = Success rate
# number1 = Reputation
# number2 = Comment ratio
# number3 = Edit ratio
def fuzziModel(number0, number1, number2, number3):

    x_succ_rt = np.arange(0, 1.01, 0.01)
    x_rep = np.arange(0, 1.01, 0.01)
    x_cmmnt_rt = np.arange(0, 1.01, 0.01)
    x_edit_rt = np.arange(0, 1.01, 0.01)

    x_clarity  = np.arange(0, 1.01, 0.01)

    # Generate fuzzy membership functions
    succ_lo = fuzz.trapmf(x_succ_rt, [-1, -1, 0.2, 0.4])
    succ_md = fuzz.trimf(x_succ_rt, [0.3, 0.5, 0.7])
    succ_hi = fuzz.trapmf(x_succ_rt, [0.6, 0.8, 1, 1])

    rep_lo = fuzz.trapmf(x_rep, [-1, -1, 0.2, 0.4])
    rep_md = fuzz.trimf(x_rep, [0.3, 0.5, 0.7])
    rep_hi = fuzz.trapmf(x_rep, [0.6, 0.8, 1, 1])

    cmmnt_lo = fuzz.trapmf(x_cmmnt_rt, [-1, -1, 0.2, 0.4])
    cmmnt_md = fuzz.trimf(x_cmmnt_rt, [0.3, 0.5, 0.7])
    cmmnt_hi = fuzz.trapmf(x_cmmnt_rt, [0.6, 0.8, 1, 1])

    edit_lo = fuzz.trapmf(x_edit_rt, [-1, -1, 0.2, 0.4])
    edit_md = fuzz.trimf(x_edit_rt, [0.3, 0.5, 0.7])      
    edit_hi = fuzz.trapmf(x_edit_rt, [0.6, 0.8, 1, 1])

    clarity_VL = fuzz.trapmf(x_clarity, [-1, -1, 0.1, 0.2])
    clarity_L = fuzz.trapmf(x_clarity, [0.1, 0.2, 0.3, 0.4])
    clarity_M = fuzz.trapmf(x_clarity, [0.3, 0.4, 0.6, 0.7])
    clarity_H = fuzz.trapmf(x_clarity, [0.58, 0.7, 0.85, 0.94])
    clarity_VH = fuzz.trapmf(x_clarity, [0.9, 0.95, 1, 1])

    # Visualize these universes and membership functions
    
    # fig, (ax0, ax1, ax6) = plt.subplots(nrows=3, figsize=(10, 10))

    # ax0.plot(x_succ_rt, AcAn_lo, 'r', linewidth=3, label='Low')
    # ax0.plot(x_succ_rt, AcAn_hi, 'b', linewidth=3, label='High')
    # ax0.set_title('AcAn')
    # ax0.legend()

    # ax1.plot(x_rep, edit_lo, 'r', linewidth=3, label='High')
    # ax1.plot(x_rep, edit_hi, 'b', linewidth=3, label='High')
    # ax1.set_title('Edit')
    # ax1.legend()
    
    # ax2.plot(x_cmmnt_rt, cmmnt_lo, 'r', linewidth=3, label='Low')
    # ax2.plot(x_cmmnt_rt, cmmnt_md, 'g', linewidth=3, label='Medium')
    # ax2.plot(x_cmmnt_rt, cmmnt_hi, 'b', linewidth=3, label='High')
    # ax2.set_title('cmmnt')
    # ax2.legend()

    # ax3.plot(x_time, time_lo, 'r', linewidth=3, label='Low')
    # ax3.plot(x_time, time_md, 'g', linewidth=3, label='Medium')
    # ax3.plot(x_time, time_hi, 'b', linewidth=3, label='High')
    # ax3.set_title('Time')
    # ax3.legend()

    # ax4.plot(x_edit_rt, comment_lo, 'r', linewidth=3, label='Low')
    # ax4.plot(x_edit_rt, comment_md, 'g', linewidth=3, label='Medium')
    # ax4.plot(x_edit_rt, comment_hi, 'b', linewidth=3, label='High')
    # ax4.set_title('Comment')
    # ax4.legend()

    # ax5.plot(x_view, view_lo, 'r', linewidth=3, label='Low')
    # ax5.plot(x_view, view_md, 'g', linewidth=3, label='Medium')
    # ax5.plot(x_view, view_hi, 'b', linewidth=3, label='High')
    # ax5.set_title('Time To View')
    # ax5.legend()

    # ax6.plot(x_repAfterAcAn, editAfterAcAn_lo, 'r', linewidth=3, label='Low')
    # ax6.plot(x_repAfterAcAn, editAfterAcAn_hi, 'b', linewidth=3, label='High')
    # ax6.set_title('Edit After AcAn')
    # ax6.legend()

    # ax7.plot(x_completionRate, completionRate_lo, 'r', linewidth=3, label='Low')
    # ax7.plot(x_completionRate, completionRate_md, 'g', linewidth=3, label='Medium')
    # ax7.plot(x_completionRate, completionRate_hi, 'b', linewidth=3, label='High')
    # ax7.set_title('TCR')
    # ax7.legend()

    # ax8.plot(x_sameQuestionrate, sameQuestionrate_lo, 'r', linewidth=3, label='Low')
    # ax8.plot(x_sameQuestionrate, sameQuestionrate_md, 'g', linewidth=3, label='Medium')
    # ax8.plot(x_sameQuestionrate, sameQuestionrate_hi, 'b', linewidth=3, label='High')
    # ax8.set_title('CRS')
    # ax8.legend()

    # ax9.plot(x_clarity, clarity_VL, 'blue', linewidth=3, label='Very_Low')
    # ax9.plot(x_clarity, clarity_L, 'green', linewidth=3, label='Low')
    # ax9.plot(x_clarity, clarity_M, 'brown', linewidth=3, label='Medium')
    # ax9.plot(x_clarity, clarity_H, 'black', linewidth=3, label='High')
    # ax9.plot(x_clarity, clarity_VH, 'red', linewidth=3, label='Very_High')
    # ax9.set_title('Clarity Amount')
    # ax9.legend()

    # Turn off top/right axes
    # for ax in (ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9):
    #     ax.spines['top'].set_visible(False)
    #     ax.spines['right'].set_visible(False)
    #     ax.get_xaxis().tick_bottom()
    #     ax.get_yaxis().tick_left()

    # plt.tight_layout()
    # plt.show()

    succ_level_lo = fuzz.interp_membership(x_succ_rt, succ_lo, number0)
    succ_level_md = fuzz.interp_membership(x_succ_rt, succ_md, number0)
    succ_level_hi = fuzz.interp_membership(x_succ_rt, succ_hi, number0)

    rep_level_lo = fuzz.interp_membership(x_rep, rep_lo, number1)
    rep_level_md = fuzz.interp_membership(x_rep, rep_md, number1)
    rep_level_hi = fuzz.interp_membership(x_rep, rep_hi, number1)

    cmmnt_level_lo = fuzz.interp_membership(x_cmmnt_rt, cmmnt_lo, number2)
    cmmnt_level_md = fuzz.interp_membership(x_cmmnt_rt, cmmnt_md, number2)
    cmmnt_level_hi = fuzz.interp_membership(x_cmmnt_rt, cmmnt_hi, number2)

    edit_level_lo = fuzz.interp_membership(x_edit_rt, edit_lo, number3)
    edit_level_md = fuzz.interp_membership(x_edit_rt, edit_md, number3)
    edit_level_hi = fuzz.interp_membership(x_edit_rt, edit_hi, number3)

    ####################### Rules #################################################
    
    ############# rule 1
    a1 = np.fmin(succ_level_hi, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_hi)
    active_rule1 = np.fmin(a2, edit_level_lo)
    clarity_activation_H = np.fmin(active_rule1, clarity_H)

    a1 = np.fmin(succ_level_lo, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_hi)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_lo)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_md)
    a2 = np.fmin(a1, cmmnt_level_hi)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_md)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_lo)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_lo)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_lo)
    a2 = np.fmin(a1, cmmnt_level_lo)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_md, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_hi)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_md, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_md, rep_level_hi)
    a2 = np.fmin(a1, cmmnt_level_lo)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_md, rep_level_md)
    a2 = np.fmin(a1, cmmnt_level_md)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_md, rep_level_md)
    a2 = np.fmin(a1, cmmnt_level_lo)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_hi, rep_level_md)
    a2 = np.fmin(a1, cmmnt_level_lo)
    active_rule1 = np.fmin(a2, edit_level_md)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

    a1 = np.fmin(succ_level_md, rep_level_lo)
    a2 = np.fmin(a1, cmmnt_level_lo)
    active_rule1 = np.fmin(a2, edit_level_lo)
    a4 = np.fmin(active_rule1, clarity_H)
    clarity_activation_H = np.fmax(a4, clarity_activation_H)

##############################################################################
    m1 = np.fmin(succ_level_hi, rep_level_hi)
    m2 = np.fmin(m1, cmmnt_level_hi)
    active_rule2 = np.fmin(m2, edit_level_md)
    clarity_activation_VH = np.fmin(active_rule2, clarity_VH)

    m1 = np.fmin(succ_level_hi, rep_level_hi)
    m2 = np.fmin(m1, cmmnt_level_hi)
    active_rule2 = np.fmin(m2, edit_level_hi)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

    m1 = np.fmin(succ_level_hi, rep_level_hi)
    m2 = np.fmin(m1, cmmnt_level_md)
    active_rule2 = np.fmin(m2, edit_level_lo)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

    m1 = np.fmin(succ_level_hi, rep_level_hi)
    m2 = np.fmin(m1, cmmnt_level_md)
    active_rule2 = np.fmin(m2, edit_level_md)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

    m1 = np.fmin(succ_level_hi, rep_level_hi)
    m2 = np.fmin(m1, cmmnt_level_lo)
    active_rule2 = np.fmin(m2, edit_level_lo)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

    m1 = np.fmin(succ_level_hi, rep_level_md)
    m2 = np.fmin(m1, cmmnt_level_md)
    active_rule2 = np.fmin(m2, edit_level_md)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

    m1 = np.fmin(succ_level_hi, rep_level_md)
    m2 = np.fmin(m1, cmmnt_level_lo)
    active_rule2 = np.fmin(m2, edit_level_lo)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

    m1 = np.fmin(succ_level_lo, rep_level_hi)
    m2 = np.fmin(m1, cmmnt_level_lo)
    active_rule2 = np.fmin(m2, edit_level_lo)
    m4 = np.fmin(active_rule2, clarity_VH)
    clarity_activation_VH = np.fmax(m4, clarity_activation_VH)

###################################################### MMMM

    s1 = np.fmin(succ_level_hi, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_lo)
    active_rule3 = np.fmin(s2, edit_level_hi)
    clarity_activation_M = np.fmin(active_rule3, clarity_M)

    s1 = np.fmin(succ_level_hi, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_hi, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_hi)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_hi, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_hi)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_hi, rep_level_lo)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_hi, rep_level_lo)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_hi)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_hi)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_hi)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_lo)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_lo)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_md, rep_level_lo)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_lo, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_hi)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_lo, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_lo, rep_level_hi)
    s2 = np.fmin(s1, cmmnt_level_lo)
    active_rule3 = np.fmin(s2, edit_level_md)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_lo, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_md)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_lo, rep_level_md)
    s2 = np.fmin(s1, cmmnt_level_lo)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

    s1 = np.fmin(succ_level_lo, rep_level_lo)
    s2 = np.fmin(s1, cmmnt_level_lo)
    active_rule3 = np.fmin(s2, edit_level_lo)
    s5 = np.fmin(active_rule3, clarity_M)
    clarity_activation_M = np.fmax(s5, clarity_activation_M)

###################################################################### Low

    e1 = np.fmin(succ_level_hi, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_hi)
    clarity_activation_L = np.fmin(active_rule4, clarity_L)

    e1 = np.fmin(succ_level_hi, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_hi, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_hi, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_hi, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_md, rep_level_hi)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)            

    e1 = np.fmin(succ_level_md, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)            

    e1 = np.fmin(succ_level_md, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)            

    e1 = np.fmin(succ_level_md, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)            

    e1 = np.fmin(succ_level_md, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)            

    e1 = np.fmin(succ_level_md, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_md)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_md, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_md)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_md, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_hi)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_hi)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_hi)
    e2 = np.fmin(e1, cmmnt_level_md)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_hi)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_hi)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L) 

    e1 = np.fmin(succ_level_lo, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L) 

    e1 = np.fmin(succ_level_lo, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_hi)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L) 

    e1 = np.fmin(succ_level_lo, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_md)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_md)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_md)
    active_rule4 = np.fmin(e2, edit_level_lo)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_md)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

    e1 = np.fmin(succ_level_lo, rep_level_lo)
    e2 = np.fmin(e1, cmmnt_level_lo)
    active_rule4 = np.fmin(e2, edit_level_md)
    e3 = np.fmin(active_rule4, clarity_L)
    clarity_activation_L = np.fmax(e3, clarity_activation_L)

################################################################################### VL

    o1 = np.fmin(succ_level_md, rep_level_md)
    o2 = np.fmin(o1, cmmnt_level_md)
    active_rule5 = np.fmin(o2, edit_level_hi)
    clarity_activation_VL = np.fmin(active_rule5, clarity_VL)

    o1 = np.fmin(succ_level_md, rep_level_md)
    o2 = np.fmin(o1, cmmnt_level_lo)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_md, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_hi)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_md, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_lo)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_md)
    o2 = np.fmin(o1, cmmnt_level_hi)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_md)
    o2 = np.fmin(o1, cmmnt_level_md)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_md)
    o2 = np.fmin(o1, cmmnt_level_lo)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_hi)
    active_rule5 = np.fmin(o2, edit_level_lo)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_hi)
    active_rule5 = np.fmin(o2, edit_level_md)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_hi)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_md)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)

    o1 = np.fmin(succ_level_lo, rep_level_lo)
    o2 = np.fmin(o1, cmmnt_level_lo)
    active_rule5 = np.fmin(o2, edit_level_hi)
    o3 = np.fmin(active_rule5, clarity_VL)
    clarity_activation_VL = np.fmax(o3, clarity_activation_VL)


########################### End of rules.


    clarity0 = np.zeros_like(x_clarity)
    
    # Visualize this
    # fig1, ax9 = plt.subplots(figsize=(8, 3))
    # ax9.fill_between(x_clarity, clarity0, clarity_activation_VL, facecolor='pink', alpha=0.7)
    # ax9.plot(x_clarity, clarity_VL, 'pink', linewidth=0.5, linestyle='--', )
    # ax9.fill_between(x_clarity, clarity0, clarity_activation_lo, facecolor='b', alpha=0.7)
    # ax9.plot(x_clarity, clarity_L, 'b', linewidth=0.5, linestyle='--', )
    # ax9.fill_between(x_clarity, clarity0, clarity_activation_M, facecolor='g', alpha=0.7)
    # ax9.plot(x_clarity, clarity_M, 'g', linewidth=0.5, linestyle='--')
    # ax9.fill_between(x_clarity, clarity0, clarity_activation_H, facecolor='brown', alpha=0.7)
    # ax9.plot(x_clarity, clarity_H, 'black', linewidth=0.5, linestyle='--')
    # ax9.fill_between(x_clarity, clarity0, clarity_activation_VH, facecolor='r', alpha=0.7)
    # ax9.plot(x_clarity, clarity_VH, 'r', linewidth=0.5, linestyle='--')
    
    # ax9.set_title('Output membership activity')

    # Turn off top/right axes
    # for ax in (ax9,):
    #    ax.spines['top'].set_visible(False)
    #    ax.spines['right'].set_visible(False)
    #    ax.get_xaxis().tick_bottom()
    #    ax.get_yaxis().tick_left()

    # plt.tight_layout()

    # plt.show()

    # Aggregate all three output membership functions together
    aggregated = np.fmax(clarity_activation_VH, np.fmax(clarity_activation_H,np.fmax(clarity_activation_M,
                         np.fmax(clarity_activation_L, clarity_activation_VL))))

    # Calculate defuzzified result
    tip = fuzz.defuzz(x_clarity, aggregated, 'centroid')
    tip_activation = fuzz.interp_membership(x_clarity, aggregated, tip)  # for plot
    
    # Visualize this
    plt.close('all')
    gc.collect()

    # fig1, ax0 = plt.subplots(figsize=(8, 3))
    
    # ax0.plot(x_clarity, clarity_VL, 'pink', linewidth=0.5, linestyle='--', )
    # ax0.plot(x_clarity, clarity_L, 'b', linewidth=0.5, linestyle='--', )
    # ax0.plot(x_clarity, clarity_M, 'g', linewidth=0.5, linestyle='--')
    # ax0.plot(x_clarity, clarity_H, 'black', linewidth=0.5, linestyle='--')
    # ax0.plot(x_clarity, clarity_VH, 'r', linewidth=0.5, linestyle='--')
    # ax0.fill_between(x_clarity, clarity0, aggregated, facecolor='Orange', alpha=0.7)
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
