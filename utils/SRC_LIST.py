#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import numba


# In[ ]:



# @numba.jit(nopython=True, nogil=True, error_model='numpy')
def get_microfiche_page_times(
    x_en,
    x_n,
    x_fqid,
    x_t,
):
    
    n = x_en.shape[0]
    
    in_microfiche_room = False
    in_reader = False
    
    current_page_number = 0
    current_page_start_time = 0
    page_durations = np.zeros(3)
    page_durations_first_look = np.zeros(3)
    looked_at_page = np.zeros(3, dtype=np.bool_)
    num_clicks_on_page = np.zeros(3)
    num_clicks_on_page_first_look = np.zeros(3)
    
    time_in_reader = 0
    time_entered_reader = 0
    
    for i in range(n):
        
        if not in_microfiche_room:
            # 106 => FQIDS.tomicrofiche
            if x_fqid[i] == 106:
                in_microfiche_room = True
        else:
            if in_reader:
                # 7, 2, 73 => EVENT_NAMES.object_click, NAMES.close, FQIDS.reader
                if x_en[i] == 7 and x_n[i] == 2 and x_fqid[i] == 73:
                    in_reader = False
                    
                    prev_page_duration = x_t[i] - current_page_start_time
                    page_durations[current_page_number] += prev_page_duration
                    
                    if not looked_at_page[current_page_number]:
                        page_durations_first_look[current_page_number] += prev_page_duration
                        looked_at_page[current_page_number] = True
                        
                    time_in_reader += x_t[i] - time_entered_reader
                
                # 7 => EVENT_NAMES.object_click
                elif x_en[i] == 7:
                
                    # 74 => FQIDS.reader_paper0_next
                    if x_fqid[i] == 74:
                        next_page = 1                    
                    elif x_fqid[i] == 75: # 75 => FQIDS.reader_paper0_prev
                        next_page = 2
                    elif x_fqid[i] == 76: # 76 => FQIDS.reader_paper1_next
                        next_page = 2
                    elif x_fqid[i] == 77: # 77 => FQIDS.reader_paper1_prev
                        next_page = 0
                    elif x_fqid[i] == 79: # 79 => FQIDS.reader_paper2_next
                        next_page = 0
                    elif x_fqid[i] == 80: # 80 => FQIDS.reader_paper2_prev
                        next_page = 1
                    else:
                        # next_page = -1
                        # print(x_fqid[i])
                        num_clicks_on_page[current_page_number] += 1
                        if not looked_at_page[current_page_number]:
                            num_clicks_on_page_first_look[current_page_number] += 1
                        continue
                    
                    prev_page_duration = x_t[i] - current_page_start_time
                    page_durations[current_page_number] += prev_page_duration
                    
                    if not looked_at_page[current_page_number]:
                        page_durations_first_look[current_page_number] += prev_page_duration
                        looked_at_page[current_page_number] = True
                    
                    current_page_number = next_page
                    current_page_start_time = x_t[i]
            else:
                # 4, 73 => EVENT_NAMES.navigate_click, FQIDS.reader
                if x_en[i] == 4 and x_fqid[i] == 73:
                    in_reader = True
                    current_page_number = 0
                    current_page_start_time = x_t[i]
                    time_entered_reader = x_t[i]
                
                # 4, 102 => EVENT_NAMES.navigate_click, FQIDS.tofrontdesk
                elif x_en[i] == 4 and x_fqid[i] == 102:
                    in_microfiche_room = False
            
    
    return page_durations, num_clicks_on_page, num_clicks_on_page_first_look, time_in_reader



# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy')
def lg0_counts(
    lg,
    history,
    x_en,
    x_n,
    x_fqid,
):
    
    assert lg == 0
    
    n = x_en.shape[0]
    
    # 50 => HIST.LG0_plaque_event_click_count
    history[50] = 0
    
    for i in range(n):                
        # 7, 71 => EVENT_NAMES.object_click, FQIDS.plaque
        if x_en[i] == 7 and x_fqid[i] == 71:
            history[50] += 1
            

# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_room_fqids_counts(room_fqids):
    
    # 13 => ROOMS.__len__
    counts = np.zeros(13, dtype=np.int32)
    n = room_fqids.shape[0]
    
    for i in range(n):
        slot_i = room_fqids[i]
        # 13 => ROOMS.__len__
        if slot_i < 13:
            counts[slot_i] += 1
               
    return counts

# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def lg0_per_level_fill_history(
    lg,
    level,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_room_coor_x,
    x_b,
    x_r,
    x_text_fqid,
):

    assert lg == 0
    
    # 70 => HIST.LG0_L0_start_elapsed_time
    history[70] = x_et[0]
    
    # 96 => HIST.LG0_L3_opened_notebook
    history[96] = 0
    
    # 102 => HIST.LG0_L2_fqid_cs_event_duration_count
    history[102] = 0
    
    # 101 => HIST.LG0_L2_fqid_cs_event_duration_sum
    history[101] = 0
    
    # 103 => HIST.LG0_L3_fqid_plaque_event_duration_sum
    history[103] = 0
    
    # 111 => HIST.LG0_L0_doorblock_message_count
    history[111] = 0
    
    # 13 => ROOMS.__len__
    L3_room_counts = np.zeros(13, dtype=np.int32)

    num_events = x_et.shape[0]
    for i in range(num_events):

        if level[i] == 0:
            # 4 => EVENT_NAMES.navigate_click
            if x_en[i] == 4:
                # 71 => HIST.LG0_L0_first_navigate_click_time
                if np.isnan(history[71]):
                    history[71] = x_et[i]
            
            # 33 => TEXT_FQIDS.tunic_historicalsociety_closet_doorblock
            if x_text_fqid[i] == 33:
                # 111 => HIST.LG0_L0_doorblock_message_count
                history[111] += 1
        
        elif level[i] == 1:
            # 40 => FQIDS.groupconvo
            if x_fqid[i] == 40:
                # 58 => HIST.LG0_L1_first_groupconvo_room_coor_x
                if np.isnan(history[58]):                
                    history[58] = x_room_coor_x[i]
            
            # 279 => TEXT.It_s_a_women_s_basketball_jersey_exclamation_
            if x_text_numerical[i] == 279:
                # 59 => HIST.LG0_L1_first_report_open_time
                if np.isnan(history[59]):
                    history[59] = x_et[i]
                    
            # 90, 7, 2 => FQIDS.report, EVENT_NAMES.object_click, NAMES.close
            if x_fqid[i] == 90 and x_en[i] == 7 and x_n[i] == 2:
                # 60 => HIST.LG0_L1_first_report_close_time
                if np.isnan(history[60]):
                    history[60] = x_et[i]
                    
        elif level[i] == 2:
            # 112, 2 => FQIDS.tunic, NAMES.close
            if x_fqid[i] == 112 and x_n[i] == 2:
                history[61] = x_et[i] # 61 => HIST.LG0_L2_last_tunic_close_time
                
            elif x_fqid[i] == 39: # 39 => FQIDS.gramps
                if np.isnan(history[62]): # 62 => HIST.LG0_L2_first_gramps_time
                    history[62] = x_et[i]  
                    
            elif x_fqid[i] == 29: # 29 => FQIDS.cs
                if (i + 1) < num_events:
                    history[101] += (x_et[i+1] - x_et[i]) # 101 => HIST.LG0_L2_fqid_cs_event_duration_sum
                    history[102] += 1 # 102 => HIST.LG0_L2_fqid_cs_event_duration_count
            
            # 112, 4 => FQIDS.tunic, EVENT_NAMES.navigate_click
            if x_fqid[i] == 112 and x_en[i] == 4:
                if np.isnan(history[104]): # 104 => HIST.LG0_L2_first_tunic_navigate_click_time
                    history[104] = x_et[i]
            
            # 51 => TEXT_FQIDS.tunic_historicalsociety_collection_cs
            if x_text_fqid[i] == 51:
                history[105] = x_et[i] # 105 => HIST.LG0_L2_last_text_fqid_cs_time
                if np.isnan(history[106]):
                    history[106] = x_et[i] # 106 => HIST.LG0_L2_first_text_fqid_cs_time
                    
        elif level[i] == 3:
            # 108 => HIST.LG0_L3_first_room_coord_x_click
            if np.isnan(history[108]):
                history[108] = x_room_coor_x[i]
            
            # 5, 3 => EVENT_NAMES.notebook_click, NAMES.open
            if x_en[i] == 5 and x_n[i] == 3:
                # 96 => HIST.LG0_L3_opened_notebook
                if history[96] == 0:
                    history[96] = 1
            
            # 71 => FQIDS.plaque
            if x_fqid[i] == 71:
                if (i + 1) < num_events:
                    # 103 => HIST.LG0_L3_fqid_plaque_event_duration_sum
                    history[103] += (x_et[i+1] - x_et[i])
                    
            slot_i = x_r[i]
            if slot_i < 13: # 13 => ROOMS.__len__
                L3_room_counts[slot_i] += 1
                    
        elif level[i] == 4:
            # 20, 4 => FQIDS.chap1_finale, EVENT_NAMES.navigate_click
            if x_fqid[i] == 20 and x_en[i] == 4:
                # 63 => HIST.LG0_L4_first_chap1_finale_nagivation_click_room_coords_x
                if np.isnan(history[63]):
                    history[63] = x_room_coor_x[i]
            
            
    L3_nunique_room = (L3_room_counts != 0).sum()
    history[107] = L3_nunique_room
                

# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def lg0_fill_history(
    lg,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_text_fqid,
):
    
    assert lg == 0
    
    num_events = x_et.shape[0]
    
    for i in range(num_events):
        # 472 => TEXT.We_need_to_talk_about_that_missing_paperwork_
        if x_text_numerical[i] == 472:
            # 0 => HIST.LG0_first_We_need_to_talk_about_that_missing_paperwork_time
            if np.isnan(history[0]):
                # 0 => HIST.LG0_first_We_need_to_talk_about_that_missing_paperwork_time
                history[0] = x_et[i]
                if i != (num_events - 1):
                    # 2 => HIST.LG0_first_We_need_to_talk_about_that_missing_paperwork_duration
                    history[2] = x_et[i+1] - x_et[i]
                # 1 => HIST.LG0_first_We_need_to_talk_about_that_missing_paperwork_index
                history[1] = x_index[i]
            
        elif x_text_numerical[i] == 304:
            # 304 => TEXT.Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_question_
            # 3 => HIST.LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_time
            if np.isnan(history[3]):
                history[3] = x_et[i]
                if i != (num_events - 1):
                    # 5 => HIST.LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_duration
                    history[5] = x_et[i+1] - x_et[i]
                # 4 => HIST.LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_index
                history[4] = x_index[i]
                
        elif x_text_numerical[i] == 279:
            # 279 => TEXT.It_s_a_women_s_basketball_jersey_exclamation_
            # 6 => HIST.LG0_first_It_s_a_women_s_basketball_jersey_time
            if np.isnan(history[6]):
                history[6] = x_et[i]
                if i != (num_events - 1):
                    history[8] = x_et[i+1] - x_et[i]
                history[7] = x_index[i]
                
        elif x_text_numerical[i] == 534:
            # 534 => TEXT.Why_don_t_you_head_to_the_Basketball_Center_and_rustle_up_some_clues_question_
            # 9 => HIST.LG0_first_event_after_first_Why_don_t_you_head_to_the_Basketball_Center_and_rustle_up_some_clues_question__time
            if np.isnan(history[9]):
                if i != (num_events - 1):
                    history[9] = x_et[i+1]
                    if i != (num_events - 2):
                        history[11] = x_et[i+2] - x_et[i+1]
                    history[10] = x_index[i+1]
                    
        elif x_text_numerical[i] == 220:
            # 220 => TEXT.I_need_to_get_to_the_Capitol_and_tell_Gramps_exclamation_
            # 12 => HIST.LG0_I_need_to_get_to_the_Capitol_and_tell_Gramps_exclamation__time
            if np.isnan(history[12]):
                history[12] = x_et[i]
                if i != (num_events - 1):
                    history[14] = x_et[i+1] - x_et[i]
                history[13] = x_index[i]
                
        elif x_text_numerical[i] == 299:
            # 299 => TEXT.Just_talking_to_Teddy_
            # 15 => HIST.LG0_first_Just_talking_to_Teddy__time
            if np.isnan(history[15]):
                history[15] = x_et[i]
                if i != (num_events - 1):
                    history[17] = x_et[i+1] - x_et[i]
                history[16] = x_index[i]
                
        elif x_text_numerical[i] == 177:
            # 177 => TEXT.Hot_Dog_exclamation__I_knew_it_exclamation_
            # 18 => HIST.LG0_first_Hot_Dog_exclamation__I_knew_it_exclamation__time
            if np.isnan(history[18]):
                history[18] = x_et[i]
                if i != (num_events - 1):
                    history[20] = x_et[i+1] - x_et[i]
                history[19] = x_index[i]
                
        elif x_text_numerical[i] == 69:
            # 69 => TEXT.Could_be__But_we_need_evidence_exclamation_
            # 24 => HIST.LG0_first_Could_be__But_we_need_evidence_exclamation__time
            if np.isnan(history[24]):
                history[24] = x_et[i]
                if i != (num_events - 1):
                    history[26] = x_et[i+1] - x_et[i]
                history[25] = x_index[i]
        
        # 20 => FQIDS.chap1_finale
        if x_fqid[i] == 20:
            # 74 => HIST.LG0_last_chap1_finale_time
            history[74] = x_et[i]
    
    # 42 => HIST.LG0_last_event_time
    history[42] = x_et[-1]
    # 43 => HIST.LG0_last_event_index
    history[43] = x_index[-1]

# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def calculate_LG0_features(
    lg,
    level,
    out,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_room_coor_x,
    x_b,
    x_r,
    x_text_fqid,
):
    
    if lg == 0:
        lg0_fill_history(
            lg,
            history,
            x_et,
            x_index,
            x_text_numerical,
            x_en,
            x_n,
            x_fqid,
            x_text_fqid,
        )
        
        lg0_counts(
            lg,
            history,
            x_en,
            x_n,
            x_fqid,
        )
        
        lg0_per_level_fill_history(
            lg,
            level,
            history,
            x_et,
            x_index,
            x_text_numerical,
            x_en,
            x_n,
            x_fqid,
            x_room_coor_x,
            x_b,
            x_r,
            x_text_fqid,
        )
    
    # 146 => FN.LG0_plaque_event_click_count
    out[:, 146] = (
        history[50] 
    )  # 50 => HIST.LG0_plaque_event_click_count
    
    # 137 => FN.LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_duration
    out[:, 137] = (
        history[5]
    ) # 5 => HIST.LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_duration
    
    # 138 => FN.LG0_first_It_s_a_women_s_basketball_jersey_duration
    out[:, 138] = (
        history[8]
    ) # 8 => HIST.LG0_first_It_s_a_women_s_basketball_jersey_duration
    
    # 139 => FN.LG0_first_event_after_first_Why_don_t_you_head_to_the_Basketball_Center_and_rustle_up_some_clues_duration
    out[:, 139] = (
        history[11]
    ) 
    
    # 140 => FN.LG0_time_before_end_of_LG_first_read_I_need_to_get_to_the_Capitol_and_tell_Gramps_exclamation_
    out[:, 140] = (
        history[42] - history[12]
    ) # 42, 12 => HIST.LG0_last_event_time, HIST.LG0_I_need_to_get_to_the_Capitol_and_tell_Gramps_exclamation__time
    
    # 141 => FN.LG0_first_Just_talking_to_Teddy_duration
    out[:, 141] = (
        history[17]
    ) # 17 => HIST.LG0_first_Just_talking_to_Teddy__duration
    
    # 142 => FN.LG0_first_Hot_Dog_exclamation__I_knew_it_exclamation_duration
    out[:, 142] = (
        history[20]
    )
    
    # 156 => FN.LG0_L1_first_groupconvo_room_coor_x
    out[:, 156] = (
        history[58]
    )
    
    # 157 => FN.LG0_L1_first_report_open_duration
    out[:, 157] = (
        history[60] - history[59]
    ) # 60, 59 => HIST.LG0_L1_first_report_close_time, HIST.LG0_L1_first_report_open_time
    
    # 158 => FN.LG0_L2_first_time_between_closing_tunic_and_gramps
    out[:, 158] = (
        history[62] - history[61]
    ) # 62, 61 => HIST.LG0_L2_first_gramps_time, HIST.LG0_L2_last_tunic_close_time
    
    # 159 = FN.LG0_L4_first_chap1_finale_nagivation_click_room_coords_x
    out[:, 159] = history[63]
    
    # 163 => FN.LG0_L0_elapsed_time_to_start_of_open_play
    out[:, 163] = (
        history[71] - history[70]
    ) # 71, 70 => HIST.LG0_L0_first_navigate_click_time, HIST.LG0_L0_start_elapsed_time
    
    # 147 => FN.LG0_first_Could_be__But_we_need_evidence_exclamation_duration
    out[:, 147] = (
        history[26]
    )
    
    # 165 => FN.LG0_fqid_chap1_finale_last_occurrence_duration_from_end
    out[:, 165] = (
        history[42] - history[74]
    ) # 42, 74 => HIST.LG0_last_event_time, HIST.LG0_last_chap1_finale_time
    
    # 178 => FN.LG0_L3_opened_notebook
    out[:, 178] = history[96]
    
    # 183 => FN.LG0_L2_fqid_cs_event_duration_mean
    out[:, 183] = history[101]/history[102]
    # 101, 102 => HIST.LG0_L2_fqid_cs_event_duration_sum, HIST.LG0_L2_fqid_cs_event_duration_count
    
    # 184 => FN.LG0_L3_fqid_plaque_event_duration_sum
    out[:, 184] = history[103]
    
    # 185 => FN.LG0_L2_time_between_reading_cs_text_and_first_tunic_navigate_click_time
    out[:, 185] = (
        history[104] - history[105]
    ) # 104, HIST.LG0_L2_last_text_fqid_cs_time => HIST.LG0_L2_first_tunic_navigate_click_time, HIST.LG0_L2_last_text_fqid_cs_time
    
    # 186 => FN.LG0_L3_first_room_coord_x_click
    out[:, 186] = history[108]
    
    # 187 => FN.LG0_L3_nunique_room
    out[:, 187] = history[107]
    
    # 190 => FN.LG0_L0_doorblock_message_count
    out[:, 190] = history[111]
    


# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def lg1_fill_history(
    lg,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_fqid,
    x_text_fqid_numerical,
    x_en,
):
    
    assert lg == 1
    
    num_events = x_et.shape[0]
    
    for i in range(num_events):
        # 577 => TEXT.Youmans_was_a_suffragist_here_in_Wisconsin_
        if x_text_numerical[i] == 577:
            # 21 => HIST.LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_time
            if np.isnan(history[21]):
                history[21] = x_et[i]
                if i != (num_events - 1):
                    # 23 => HIST.LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_duration
                    history[23] = x_et[i+1] - x_et[i]
                # 22 => HIST.LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_index
                history[22] = x_index[i]
                
        elif x_text_numerical[i] == 524:
            # 524 => TEXT.Who_could_ve_done_this_question_
            # 30 => HIST.LG1_first_Who_could_ve_done_this_question__time
            if np.isnan(history[30]):
                history[30] = x_et[i]
                if i != (num_events - 1):
                    history[32] = x_et[i+1] - x_et[i]
                history[31] = x_index[i]
                
        elif x_text_numerical[i] == 333:
            # 333 => TEXT.Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that
            # 33 => HIST.LG1_first_Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that__time
            if np.isnan(history[33]):
                history[33] = x_et[i]
                if i != (num_events - 1):
                    history[35] = x_et[i+1] - x_et[i]
                history[34] = x_index[i]
                
        elif x_text_numerical[i] == 268:
            # 268 => TEXT.I_ve_got_a_stack_of_business_cards_from_my_favorite_cleaners_
            # 36 => HIST.LG1_first_I_ve_got_a_stack_of_business_cards_from_my_favorite_cleaners__time
            if np.isnan(history[36]):
                history[36] = x_et[i]
                if i != (num_events - 1):
                    history[38] = x_et[i+1] - x_et[i]
                history[37] = x_index[i]
                
        elif x_text_numerical[i] == 521:
            # 521 => TEXT.Where_did_you_get_that_coffee_question_
            # 39 => HIST.LG1_first_Where_did_you_get_that_coffee_question__time
            if np.isnan(history[39]):
                history[39] = x_et[i]
                if i != (num_events - 1):
                    history[41] = x_et[i+1] - x_et[i]
                history[40] = x_index[i]
        
        # 66 => FQIDS.magnify
        if x_fqid[i] == 66:
            if i != (num_events - 1):
                event_duration = x_et[i+1] - x_et[i]
                # 55 => HIST.LG1_max_fqid_magnify_duration
                if np.isnan(history[55]) or event_duration > history[55]:
                    history[55] = event_duration
                   
        elif x_fqid[i] == 16: # 16 => FQIDS.businesscards_card_1_next
            if i != (num_events - 1):
                # 56 => HIST.LG1_first_fqid_businesscards_card_1_next_duration
                if np.isnan(history[56]):
                    history[56] = x_et[i+1] - x_et[i]
                   
        elif x_fqid[i] == 44: # 44 => FQIDS.journals
            if i != (num_events - 1):
                event_duration = x_et[i+1] - x_et[i]
                # 57 => HIST.LG1_max_fqid_journals_duration
                if np.isnan(history[57]) or event_duration > history[57]:
                    history[57] = event_duration
        
        # 153, 65 => TEXT.Here_s_the_log_book_, FQIDS.logbook_page_bingo
        if (x_text_numerical[i] == 153) or (x_fqid[i] == 65):
            # 113 => HIST.LG1_logbook_page_bingo_start_time
            if np.isnan(history[113]):
                history[113] = x_et[i]                
            # 114 => HIST.LG1_logbook_page_bingo_end_time
            history[114] = x_et[i]
        
        # 4, 73, 78 => EVENT_NAMES.navigate_click, FQIDS.reader, FQIDS.reader_paper2_bingo
        if ((x_en[i] == 4) and (x_fqid[i] == 73)) or (x_fqid[i] == 78):
            # 115 => HIST.LG1_reader_paper2_bingo_start_time
            if np.isnan(history[115]):
                history[115] = x_et[i]
            # 116 => HIST.LG1_reader_paper2_bingo_end_time
            history[116] = x_et[i]
    
    history[44] = x_et[0] # 44 => HIST.LG1_first_event_time
    history[45] = x_index[0] # 45 => HIST.LG1_first_event_index
    history[46] = x_et[-1] # 46 => HIST.LG1_last_event_time
    history[47] = x_index[-1] # 47 => HIST.LG1_last_event_index

# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def lg1_per_level_fill_history(
    lg,
    level,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_room_coor_x,
    x_room_coor_y,
    x_b,
    x_r,
):

    assert lg == 1

    num_events = x_et.shape[0]
    for i in range(num_events):

        if level[i] == 6:
            # 66 => FQIDS.magnify
            if x_fqid[i] == 66:
                # 65 => HIST.LG1_L6_last_magnify_time
                history[65] = x_et[i]
                
            elif x_fqid[i] == 95: # 95 => FQIDS.tobasement
                # 67 => HIST.LG1_L6_first_time_leave_closet_dirty
                if np.isnan(history[67]):
                    history[67] = x_et[i]
            
            # 15 => TEXT.Ah__that_s_better_exclamation_
            if x_text_numerical[i] == 15:
                # 64 => HIST.LG1_L6_Ah__that_s_better_exclamation__previous_time
                if np.isnan(history[64]):
                    if i > 0:
                        history[64] = x_et[i - 1]    
                        
            elif x_text_numerical[i] == 139:
                # 139 => TEXT.He_s_our_expert_record_keeper_
                if np.isnan(history[66]):
                    # 66 => HIST.LG1_L6_first_finished_talking_to_gramps
                    history[66] = x_et[i]
                        
            if x_fqid[i] == 111: # 111 => FQIDS.trigger_scarf
                # 75 => HIST.LG1_L6_last_trigger_scarf_time
                history[75] = x_et[i]            
                if np.isnan(history[76]):
                    if (i - 1) >= 0:
                        history[76] = x_et[i - 1]
                        
                if (i + 1) < num_events:
                    # 77 => HIST.LG1_L6_last_trigger_scarf_next_room_coor_x
                    history[77] = x_room_coor_x[i + 1]
                   
            if x_fqid[i] == 101: # 101 => FQIDS.toentry
                # 78 => HIST.LG1_L6_first_toentry_time
                if np.isnan(history[78]):
                    history[78] = x_et[i]
            
            # 181 => TEXT.I_bet_the_archivist_could_use_this_exclamation_
            if x_text_numerical[i] == 181:
                if i + 1 < num_events:
                    # 98 => HIST.LG1_L6_first_y_room_coords_of_next_click_after_finding_magnifying_glass
                    if np.isnan(history[98]):
                        history[98] = x_room_coor_y[i + 1]
            
            # 343 => TEXT.Now_if_only_I_could_read_this_thing_
            # 344 => TEXT.Now_if_only_I_could_read_this_thing__Blasted_tiny_letters___
            if (
                x_text_numerical[i] == 343
                or x_text_numerical[i] == 344
            ):
                if i + 1 < num_events:
                    # 99 => HIST.LG1_L6_first_y_room_coords_of_next_click_after_archivist_mentions_difficulty_reading
                    if np.isnan(history[99]):
                        history[99] = x_room_coor_y[i + 1]
                    
            if x_fqid[i] == 0: # 0 => FQIDS.NaN
                # 109 => HIST.LG1_L6_first_y_room_coords_for_non_nan_fqid
                if np.isnan(history[109]):
                        history[109] = x_room_coor_y[i]
                
            
        elif level[i] == 7:
            # 107 => FQIDS.tostacks
            if x_fqid[i] == 107:
                # 84 => HIST.LG1_L7_first_tostacks_time
                if np.isnan(history[84]):
                    history[84] = x_et[i]
            elif x_fqid[i] == 101: # 101 => FQIDS.toentry
                # 85 => HIST.LG1_L7_first_toentry_time
                if np.isnan(history[85]):
                    history[85] = x_et[i]
            elif x_fqid[i] == 14: # 14 => FQIDS.businesscards
                # 88 => HIST.LG1_L7_first_businesscards_time
                if np.isnan(history[88]):
                    history[88] = x_et[i]
                    
            
            # 148 => TEXT.Hello_there_exclamation_
            if x_text_numerical[i] == 148:
                # 86 => HIST.LG1_L7_first_Hello_there_exclamation_prev_time
                if np.isnan(history[86]):
                    if (i - i) >= 0:
                        history[86] = x_et[i - 1]
            elif x_text_numerical[i] == 536:
                # 536 => TEXT.Why_don_t_you_take_a_look_question_
                # 87 => HIST.LG1_L7_first_Why_don_t_you_take_a_look_question__time
                if np.isnan(history[87]):
                    history[87] = x_et[i]
            
            # 6, 8 => BUILDINGS.humanecology, ROOMS.frontdesk
            if x_b[i] == 6 and x_r[i] == 8:
                if i + 1 < num_events:
                    # 100 => HIST.LG1_L7_first_y_room_coords_of_next_click_after_arriving_at_humanecology_frontdesk
                    if np.isnan(history[100]):
                        history[100] = x_room_coor_y[i + 1]
            
            
        elif level[i] == 8:
            # 153 => TEXT.Here_s_the_log_book_
            if x_text_numerical[i] == 153:
                # 79 => HIST.LG1_L8_first_time_told_about_logbook
                if np.isnan(history[79]):
                    history[79] = x_et[i]
                    
            if x_fqid[i] == 64: # 64 => FQIDS.logbook
                # 80 => HIST.LG1_L8_first_logbook_time
                if np.isnan(history[80]):
                    history[80] = x_et[i]
                    
        elif level[i] == 9:
            
            if x_fqid[i] == 73: # 73 => FQIDS.reader
                # 68 => HIST.LG1_L9_first_reader_index
                if np.isnan(history[68]):
                    history[68] = x_index[i]    
            elif x_fqid[i] == 78 and x_en[i] == 7:
                # 78, 7 => FQIDS.reader_paper2_bingo, EVENT_NAMES.object_click
                # 69 => HIST.LG1_L9_first_click_reader_paper2_bingo_index
                if np.isnan(history[69]):
                    history[69] = x_index[i]
                    
                    
                    
        elif level[i] == 10:
            # 491 => TEXT.Wells_exclamation__What_was_he_doing_here_question__I_should_ask_the_librarian_
            if x_text_numerical[i] == 491:
                # 73 => HIST.LG1_L10_first_Wells_exclamation__What_was_he_doing_here_question__I_should_ask_the_librarian_time
                if np.isnan(history[73]):
                    history[73] = x_et[i]
            
            # 128, 4 => FQIDS.worker, EVENT_NAMES.navigate_click
            if x_fqid[i] == 128 and x_en[i] == 4:
                # 72 => HIST.LG1_L10_starts_speaking_to_librarian_time
                if np.isnan(history[72]):
                    history[72] = x_et[i]
                    
        elif level[i] == 11:
            # 162 => TEXT.Hey__this_is_Youmans_exclamation_
            if x_text_numerical[i] == 162:
                # 81 => HIST.LG1_L11_first_Hey__this_is_Youmans_exclamation__time
                if np.isnan(history[81]):
                    history[81] = x_et[i]
                    
                if (i - 1) >= 0:
                    # 82 => HIST.LG1_L11_first_Hey__this_is_Youmans_exclamation__prev_time
                    if np.isnan(history[82]):
                        history[82] = x_et[i - 1]
            
            # 232 => TEXT.I_should_go_to_the_Capitol_and_tell_everyone_exclamation_
            if x_text_numerical[i] == 232:
                # 83 => HIST.LG1_L11_first_I_should_go_to_the_Capitol_and_tell_everyone_exclamation__time
                if np.isnan(history[83]):
                    history[83] = x_et[i]
                    
                    
        elif level[i] == 12:
            # 94 => HIST.LG1_L12_start_time
            if np.isnan(history[94]):
                history[94] = x_et[i]
            
            # 1, 9 => BUILDINGS.capitol_1, ROOMS.hall
            if x_b[i] == 1 and x_r[i] == 9:
                # 93 => HIST.LG1_L12_first_reach_capitol_1_hall_time
                if np.isnan(history[93]):
                    history[93] = x_et[i]
        
            if x_en[i] == 2:
                # 95 => HIST.LG1_L12_first_map_click_room_coord_x
                if np.isnan(history[95]):
                    history[95] = x_room_coor_x[i]
                    
            if np.isnan(history[110]):
                # 110 => HIST.LG1_L12_first_x_room_coords
                history[110] = x_room_coor_x[i]
                
# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def calculate_LG1_features(
    lg,
    level,
    out,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_t,
    x_room_coor_x,
    x_room_coor_y,
    x_b,
    x_r,
    x_text_fqid_numerical,
):
    
    if lg == 1:
        
        microfiche_page_durations, microfiche_num_clicks_on_page, _, _ = get_microfiche_page_times(
            x_en,
            x_n,
            x_fqid,
            x_t,
        )
        
        # 48 => HIST.LG1_microfiche_page_2_duration
        history[48] = microfiche_page_durations[2]
        # 49 => HIST.LG1_microfiche_total_clicks
        history[49] = microfiche_num_clicks_on_page.sum()
        
        lg1_fill_history(
            lg,
            history,
            x_et,
            x_index,
            x_text_numerical,
            x_fqid,
            x_text_fqid_numerical,
            x_en,
        )
        
        lg1_per_level_fill_history(
            lg,
            level,
            history,
            x_et,
            x_index,
            x_text_numerical,
            x_en,
            x_n,
            x_fqid,
            x_room_coor_x,
            x_room_coor_y,
            x_b,
            x_r,
        )
        

    if lg >= 1:
        # 143, 44 => FN.LG0_to_LG1_gap_duration, HIST.LG1_first_event_time
        # 42 => HIST.LG0_last_event_time
        out[:, 143] = history[44] - history[42]
        
        # 149 => FN.LG1_first_Who_could_ve_done_this_question__duration
        out[:, 149] = history[32]
        
        # 151 => FN.LG1_first_I_ve_got_a_stack_of_business_cards_from_my_favorite_cleaners__duration
        out[:, 151] = (
            history[38]
        )
        
        # 152 => FN.LG1_first_Where_did_you_get_that_coffee_question__duration
        out[:, 152] = (
            history[41]
        )
        
        # 145 => FN.LG1_microfiche_total_clicks
        out[:, 145] = history[49]
        
        # 155 => FN.LG1_max_fqid_journals_duration
        out[:, 155] = history[57]
        
        # 153 => FN.LG1_max_fqid_magnify_duration
        out[:, 153] = history[55]
        
        # 154 => FN.LG1_first_fqid_businesscards_card_1_next_duration
        out[:, 154] = history[56]
        
        # 160 => FN.LG1_L6_time_between_clicking_on_magnifying_glass_and_then_clicking_on_archivist_again
        out[:, 160] = (
            history[64] - history[65]
        ) # 64, 65 => HIST.LG1_L6_Ah__that_s_better_exclamation__previous_time, HIST.LG1_L6_last_magnify_time
        
        # 161 => FN.LG1_L6_time_between_first_finish_talking_to_gramps_and_leaving_closet_dirty
        out[:, 161] = (
            history[67] - history[66]
        ) # 67, 66 => HIST.LG1_L6_first_time_leave_closet_dirty, HIST.LG1_L6_first_finished_talking_to_gramps
        
        # 162 => FN.LG1_L6_number_of_events_between_opening_reader_and_clicking_on_paper2_bingo
        out[:, 162] = (
            history[69] - history[68]
        ) # 69, 68 => HIST.LG1_L9_first_click_reader_paper2_bingo_index, HIST.LG1_L9_first_reader_index
        
        # 164 => FN.LG1_L10_time_between_being_told_to_talk_to_librarian_and_speaking_to_librarian
        out[:, 164] = (
            history[72]
            - history[73]
        ) # 72 => HIST.LG1_L10_starts_speaking_to_librarian_time
        # 73 => HIST.LG1_L10_first_Wells_exclamation__What_was_he_doing_here_question__I_should_ask_the_librarian_time
        
        # 150 => FN.LG1_first_Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that__duration
        out[:, 150] = (
            history[35]
        ) # 35 => HIST.LG1_first_Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that__duration
        
        # 144 => FN.LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_duration
        out[:, 144] = (
            history[23]
        ) # 23 => HIST.LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_duration
        
        # 48 => HIST.LG1_microfiche_page_2_duration
        # out[:, ] = history[48]
        
        # 166 => FN.LG1_L6_trigger_scarf_duration
        out[:, 166] = (
            history[76] - history[75]
        ) # 76 => HIST.LG1_L6_first_trigger_scarf_prev_time
        # 75 => HIST.LG1_L6_last_trigger_scarf_time
        
        # 167 => FN.LG1_L6_last_trigger_scarf_next_room_coor_x
        out[:, 167] = history[77]
        
        # 167 => FN.LG1_L6_last_trigger_scarf_next_room_coor_x
        out[:, 168] = (
            history[78] - history[66]
        ) # 78 => HIST.LG1_L6_first_toentry_time
        # 66 => HIST.LG1_L6_first_finished_talking_to_gramps
        
        # 169 => FN.LG1_L6_time_between_first_being_told_about_logbook_and_getting_to_logbook
        out[:, 169] = (
            history[80] - history[79]
        ) # 80 => HIST.LG1_L8_first_logbook_time
        # HIST.LG1_L8_first_time_told_about_logbook
        
        # 170 => FN.LG1_L11_time_spent_reading_bingo_text
        out[:, 170] = (
            history[83]
            - history[82]
        ) # 83 => HIST.LG1_L11_first_I_should_go_to_the_Capitol_and_tell_everyone_exclamation__time
        # 82 => HIST.LG1_L11_first_Hey__this_is_Youmans_exclamation__prev_time
        
        # 171 => FN.LG1_L7_first_time_to_get_from_stacks_to_entry
        out[:, 171] = (
            history[85] - history[84]
        ) # 85, 84 => HIST.LG1_L7_first_toentry_time, HIST.LG1_L7_first_tostacks_time
        
        # 172 => FN.LG1_L7_first_time_to_read_workers_text
        out[:, 172] = (
            history[87] - history[86]
        ) # 87 => HIST.LG1_L7_first_Why_don_t_you_take_a_look_question__time
        # 86 => HIST.LG1_L7_first_Hello_there_exclamation_prev_time
        
        # 173 => FN.LG1_L7_first_time_from_being_told_about_business_cards_to_clicking_on_business_cards
        out[:, 173] = (
            history[88] - history[87]
        ) # 88 => HIST.LG1_L7_first_businesscards_time
        # 87 => HIST.LG1_L7_first_Why_don_t_you_take_a_look_question__time
        
        # 176 => FN.LG1_L12_time_to_reach_capitol_1_hall_from_start_of_level
        out[:, 176] = (
            history[93] - history[94]
        ) # 93, 94 => HIST.LG1_L12_first_reach_capitol_1_hall_time, HIST.LG1_L12_start_time
        
        # 177 => FN.LG1_L12_first_map_click_room_coord_x
        out[:, 177] = history[95]
        
        # 180 => FN.LG1_L6_first_y_room_coords_of_next_click_after_finding_magnifying_glass
        out[:, 180] = (
            history[98]
        ) # 98 => HIST.LG1_L6_first_y_room_coords_of_next_click_after_finding_magnifying_glass
        
        # 181 => FN.LG1_L6_first_y_room_coords_of_next_click_after_archivist_mentions_difficulty_reading
        out[:, 181] = (
            history[99]
        ) # 99 => HIST.LG1_L6_first_y_room_coords_of_next_click_after_archivist_mentions_difficulty_reading
        
        # 182 => FN.LG1_L7_first_y_room_coords_of_next_click_after_arriving_at_humanecology_frontdesk
        out[:, 182] = (
            history[100]
        ) # 100 => HIST.LG1_L7_first_y_room_coords_of_next_click_after_arriving_at_humanecology_frontdesk
        
        # 188 => FN.LG1_L6_first_y_room_coords_for_non_nan_fqid
        out[:, 188] =  history[109]
        
        # 189 => FN.LG1_L12_first_x_room_coords
        out[:, 189] =  history[110]
        
        # 193 => FN.LG1_logbook_page_bingo_time_duration
        out[:, 193] = (
            history[114] - history[113]
        ) # 114, 113 => HIST.LG1_logbook_page_bingo_end_time, HIST.LG1_logbook_page_bingo_start_time
        
        # 194 => FN.LG1_reader_paper2_bingo_time_duration
        out[:, 194] = (
            history[116] - history[115]
        ) # 116, 115 => HIST.LG1_reader_paper2_bingo_end_time, HIST.LG1_reader_paper2_bingo_start_time


# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def lg2_fill_history(
    lg,
    history,
    x_et,
    x_index,
    x_text_numerical,
):
    
    assert lg == 2
    
    num_events = x_et.shape[0]
    
    for i in range(num_events):
        # 168 => TEXT.Hmm__You_could_try_the_Aldo_Leopold_Wildlife_Center_
        if x_text_numerical[i] == 168:
            # 27 => HIST.LG2_first_Hmm__You_could_try_the_Aldo_Leopold_Wildlife_Center__time
            if np.isnan(history[27]):
                history[27] = x_et[i]
                if i != (num_events - 1):
                    # 29 => HIST.LG2_first_Hmm__You_could_try_the_Aldo_Leopold_Wildlife_Center__duration
                    history[29] = x_et[i+1] - x_et[i]
                # 28 => HIST.LG2_first_Hmm__You_could_try_the_Aldo_Leopold_Wildlife_Center__index
                history[28] = x_index[i]
    
    history[51] = x_et[0] # 51 => HIST.LG2_first_event_time
    history[52] = x_index[0] # 52 => HIST.LG2_first_event_index
    history[53] = x_et[-1] # 53 => HIST.LG2_last_event_time
    history[54] = x_index[-1] # 54 => HIST.LG2_last_event_index

# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def lg2_per_level_fill_history(
    lg,
    level,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_room_coor_x,
    x_room_coor_y,
    x_b,
    x_r,
):

    assert lg == 2

    num_events = x_et.shape[0]
    for i in range(num_events):

        if level[i] == 15:
            # 30, 31, 7 => FQIDS.directory, FQIDS.directory_closeup_archivist, EVENT_NAMES.object_click
            if (x_fqid[i] == 30 or x_fqid[i] == 31) and x_en[i] == 7:
                # 97 => HIST.LG1_L15_first_directory_y_coord_click
                if np.isnan(history[97]):
                    history[97] = x_room_coor_y[i]

        elif level[i] == 18:
            # 9,2 => BUILDINGS.wildlife, ROOMS.center
            if x_b[i] == 9 and x_r[i] == 2:
                # 89 => HIST.LG2_L18_first_reach_wildlife_center_time
                if np.isnan(history[89]):
                    history[89] = x_et[i]
                    
            if x_fqid[i] == 25: # 25 => FQIDS.coffee
                # 90 => HIST.LG2_L18_first_coffee_time
                if np.isnan(history[90]):
                    history[90] = x_et[i]
                    
        elif level[i] == 21:
            # 50, 7, 2 => FQIDS.journals_flag, EVENT_NAMES.object_click, NAMES.close
            if x_fqid[i] == 50 and x_en[i] == 7 and x_n[i] == 2:
                # 91 => HIST.LG2_L21_first_journals_close_time
                if np.isnan(history[91]):
                    history[91] = x_et[i]
            
        elif level[i] == 22:
            
            # 2, 9 => BUILDINGS.capitol_2, ROOMS.hall
            if x_b[i] == 2 and x_r[i] == 9:
                # 92 => HIST.LG2_L22_first_reach_capitol_2_hall_time
                if np.isnan(history[92]):
                    history[92] = x_et[i]
        


# In[ ]:


# @numba.jit(nopython=True, nogil=True, error_model='numpy', parallel=False)
def calculate_LG2_features(
    lg,
    level,
    out,
    history,
    x_et,
    x_index,
    x_text_numerical,
    x_en,
    x_n,
    x_fqid,
    x_t,
    x_room_coor_x,
    x_room_coor_y,
    x_b,
    x_r,
):
    
    if lg == 2:

        lg2_fill_history(
            lg,
            history,
            x_et,
            x_index,
            x_text_numerical,
        )
        
        lg2_per_level_fill_history(
            lg,
            level,
            history,
            x_et,
            x_index,
            x_text_numerical,
            x_en,
            x_n,
            x_fqid,
            x_room_coor_x,
            x_room_coor_y,
            x_b,
            x_r,
        )
        
        # 148 => FN.LG2_first_Hmm__You_could_try_the_Aldo_Leopold_Wildlife_Center__duration
        out[:, 148] = (
            history[29]
        )
        
        # 174 => FN.LG2_L18_first_time_between_reaching_wildlife_center_and_clicking_on_coffee
        out[:, 174] = (
            history[90] - history[89]
        ) # 90, 89 => HIST.LG2_L18_first_coffee_time, HIST.LG2_L18_first_reach_wildlife_center_time
        
        # 175 => FN.LG2_L21_first_time_between_closing_journals_and_reaching_capitol_2_hall
        out[:, 175] = (
            history[92] - history[91]
        ) # 92, 91 => HIST.LG2_L22_first_reach_capitol_2_hall_time, HIST.LG2_L21_first_journals_close_time
        
        # 179 => FN.LG1_L15_first_directory_y_coord_click
        out[:, 179] = history[97]
    

# In[ ]:

