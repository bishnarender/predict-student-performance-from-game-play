#!/usr/bin/env python
# coding: utf-8

import numpy as np
import numba

from . import fqids_features_src as fqids_features_src
from . import building_features_src as building_features_src
from . import room_features_src as room_features_src
from . import fqid_features_src as fqid_features_src
from . import level_based_features_src as level_based_features_src
from . import SRC_LIST as SRC_LIST


QUESTIONS_SPLITS_PER_LEVEL = np.array([0, 3, 13, 18])

# The error_model option controls the divide-by-zero behavior. Setting it to ‘python’ causes divide-by-zero to - 
# - raise exception like CPython. Setting it to ‘numpy’ causes divide-by-zero to set the result to +/-inf or nan.
#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_name_counts(names):
    
    counts = np.zeros(6, dtype=np.int32)
    
    n = names.shape[0]
    # names => [0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 2 1 0 0 0 1 2 1 1 1 ... 2 0 0 1 1 1 1 1 1 1 1 0 0 1 1 0]
    # names.shape => (165,)

    for i in range(n):
        slot_i = names[i]
        if slot_i < 6:
            counts[slot_i] += 1
            
    # counts => [74 85  6  0  0  0] (i.e., 74 zeros, 85 ones, 6 twos ...)
    return counts

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_event_name_counts(event_names):
    
    counts = np.zeros(11, dtype=np.int32)
    n = event_names.shape[0]
    
    for i in range(n):
        slot_i = event_names[i]
        if slot_i < 11:
            counts[slot_i] += 1
               
    return counts

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def coordinates_distance_travelled_sum(x, y):
    
    total = np.float32(0)
    
    n = x.shape[0]
    
    for i in range(n-1):
        d = np.sqrt(np.power(x[i+1] - x[i], 2) +  np.power(y[i+1] - y[i], 2))
        
        if not np.isnan(d):        
            total += d
        
    return total

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def calculate_read_speeds_of_text(text_length, elapsed_time):
    
    n = text_length.shape[0]
    out_i = 0
    read_speed = np.empty(n, dtype=np.float32)
    
    # text_length => [ 9. 22. 26. 29. 19. 53. 21. 32. 32. 24. nan 24. nan 36. nan nan nan nan ... nan nan nan]
    
    for i in range(n-1):
        
        tl = text_length[i]
        
        if ~np.isnan(tl):
            
            et0 = elapsed_time[i]
            et1 = elapsed_time[i+1]
            
            t = et1 - et0            
            rs = tl/t
            
            read_speed[out_i] = rs
            out_i += 1
         
    read_speed = read_speed[:out_i]
        
    return read_speed

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_building_counts(buildings):
    
    counts = np.zeros(10, dtype=np.int32)
    n = buildings.shape[0]
    
    for i in range(n):
        slot_i = buildings[i]
        if slot_i < 10:
            counts[slot_i] += 1
               
    return counts

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_room_counts(rooms):
    
    counts = np.zeros(13, dtype=np.int32)
    n = rooms.shape[0]
    
    for i in range(n):
        slot_i = rooms[i]
        if slot_i < 13:
            counts[slot_i] += 1
               
    return counts

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_building_visits_counts(buildings):
    
    counts = np.zeros(10, dtype=np.int32)
    n = buildings.shape[0]
    
    # buildings => [5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 ... 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 0 0]
    
    prev_b = -1
    for i in range(n):
        b = buildings[i]
        if b != prev_b:
            if b < 10:
                counts[b] += 1
            prev_b = b
            
    # counts => [1 0 0 0 0 1 0 1 0 0]
    return counts


#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_room_visits_counts(room):
    
    counts = np.zeros(13, dtype=np.int32)
    n = room.shape[0]
    
    prev_r = -1
    for i in range(n):
        r = room[i]
        if r != prev_r:
            if r < 13:
                counts[r] += 1
            prev_r = r
               
    return counts

#@numba.jit('(i8, i8[::1], i8[::1], i8[::1], f8[::1], u1[::1], i8[::1], i8[::1], i8[::1], i8[::1], i8[::1], f8[::1], f8[::1], f8[::1], f8[::1], f8[::1], i8[::1], i8[::1], i8[::1], f8[::1], u1[::1], f4[:, ::1], f8[::1])',    nopython=True,nogil=True,error_model='numpy',parallel=False)
def process_single(
    level_group_index,
    x_et,
    x_en,
    x_n,
    x_hover_duration,
    x_session_weekday,
    x_b,
    x_r,
    x_fqids,
    x_l,
    x_index,
    x_rc_x,
    x_rc_y,
    x_sc_x,
    x_sc_y,
    x_tl,
    x_text_numerical,
    x_text_fqid_numerical,
    x_room_fqid_numerical,
    x_page,
    x_hour,
    out,
    hist,
):
    number_of_events = x_et.shape[0]
    
    questions_start_number = QUESTIONS_SPLITS_PER_LEVEL[level_group_index]
    questions_end_number = QUESTIONS_SPLITS_PER_LEVEL[level_group_index + 1]
    question_number = np.arange(questions_start_number, questions_end_number)
    
    # np.nansum(a, axis=None,...) => return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero.
    total_hover_duration = np.nansum(x_hover_duration)
    average_hover_duration = np.nanmean(x_hover_duration)
    session_duration = x_et[-1] - x_et[0]
    
    # 191 => FN.session_hour
    out[:, 191] = x_hour[0]

    # .diff(a, n=1, axis=-1, ...) => calculate the n-th discrete difference along the given axis.
    # np.diff(np.array([1, 2, 4, 7, 0])) => array([ 1,  2,  3, -7])
    x_et_diff = np.diff(x_et)    
    
    # 103 => FN.session_index_level_group_first
    out[:, 103] = x_index[0]
    
    # 104 => FN.session_index_level_group_last
    out[:, 104] = x_index[-1]
    
    # 105 => FN.elapsed_time_sum
    out[:, 105] = x_et.sum()
    
    # 106 => FN.elapsed_time_in_increasing_order
    # .all(a, axis=None, ...) => test whether all array elements along a given axis evaluate to True.
    out[:, 106] = np.all(x_et_diff > 0)
    
    # 12 => FN.is_level_group_0
    out[:, 12] = level_group_index == 0
    
    # 13 => FN.is_level_group_1
    out[:, 13] = level_group_index == 1
    
    # 14 => FN.is_level_group_2
    out[:, 14] = level_group_index == 2
    
    # 34 => FN.is_question_0
    out[:, 34] = question_number == 0
    
    # 35 => FN.is_question_1
    out[:, 35] = question_number == 1
    
    # 36 => FN.is_question_2
    out[:, 36] = question_number == 2
    
    # 37 => FN.is_question_3
    out[:, 37] = question_number == 3
    
    # 38 => FN.is_question_4
    out[:, 38] = question_number == 4
    
    # 39 => FN.is_question_5
    out[:, 39] = question_number == 5
    
    # 40 => FN.is_question_6
    out[:, 40] = question_number == 6
    
    # 41 => FN.is_question_7
    out[:, 41] = question_number == 7
    
    # 42 => FN.is_question_8
    out[:, 42] = question_number == 8
    
    # 43 => FN.is_question_9
    out[:, 43] = question_number == 9
    
    # 44 => FN.is_question_10
    out[:, 44] = question_number == 10
    
    # 45 => FN.is_question_11
    out[:, 45] = question_number == 11
    
    # 46 => FN.is_question_12
    out[:, 46] = question_number == 12
    
    # 47 => FN.is_question_13
    out[:, 47] = question_number == 13
    
    # 48 => FN.is_question_14
    out[:, 48] = question_number == 14
    
    # 49 => FN.is_question_15
    out[:, 49] = question_number == 15
    
    # 50 => FN.is_question_16
    out[:, 50] = question_number == 16
    
    # 51 => FN.is_question_17
    out[:, 51] = question_number == 17
    
    # 52 => FN.is_question_18
    out[:, 52] = question_number == 18
    
    # 0 => FN.number_of_events
    out[:, 0] = number_of_events
    
    # 1 => FN.level_group
    out[:, 1] = level_group_index
    
    # 2 => FN.question_number
    out[:, 2] = np.arange(questions_start_number, questions_end_number)
    # out[:, 2] => [0. 1. 2.] 
    
    # 3 => FN.session_start_time
    out[:, 3] = x_et[0]
    
    # 4 => FN.session_end_time
    out[:, 4] = x_et[-1]
    
    # 5 => FN.session_duration
    out[:, 5] = session_duration
    
    # 98 => FN.average_duration_per_event
    out[:, 98] = session_duration/number_of_events
    
    # 32 => FN.total_hover_duration
    out[:, 32] = total_hover_duration
    
    # 33 => FN.average_hover_duration
    out[:, 33] = average_hover_duration

    name_counts = generate_name_counts(x_n)
    
    # 6 => FN.name_basic_0_count
    out[:, 6] = name_counts[0]
    
    # 7 => FN.name_undefined_1_count
    out[:, 7] = name_counts[1]
    
    # 8 => FN.name_close_2_count
    out[:, 8] = name_counts[2]
    
    # 9 => FN.name_open_3_count
    out[:, 9] = name_counts[3]
    
    # 10 => FN.name_prev_4_count
    out[:, 10] = name_counts[4]
    
    # 11 => FN.name_next_5_count
    out[:, 11] = name_counts[5]
    
    # 15 => FN.name_basic_0_proportion
    out[:, 15] = name_counts[0]/number_of_events
    
    # 16 => FN.name_undefined_1_proportion
    out[:, 16] = name_counts[1]/number_of_events
    
    # 17 => FN.name_close_2_proportion
    out[:, 17] = name_counts[2]/number_of_events
    
    # 18 => FN.name_open_3_proportion
    out[:, 18] = name_counts[3]/number_of_events
    
    # 19 => FN.name_prev_4_proportion
    out[:, 19] = name_counts[4]/number_of_events
    
    # 20 => FN.name_next_5_proportion
    out[:, 20] = name_counts[5]/number_of_events
    
    # 57 => FN.last_name
    # x_n.shape => (165,)
    out[:, 57] = x_n[-1]

    if level_group_index == 0:
        # LG0 => level group 0
        # 112 => HIST.LG0_name_num_unique_count 
        hist[112] = (name_counts != 0).sum()
        
    # 192 => FN.LG0_name_num_unique_count
    # 112 => HIST.LG0_name_num_unique_count
    out[:, 192] = hist[112]

    event_name_counts = generate_event_name_counts(x_en)
    
    # 21 => FN.event_name_cutscene_click_0_count
    out[:, 21] = event_name_counts[0]
    
    # 22 => FN.event_name_person_click_1_count
    out[:, 22] = event_name_counts[1]
    
    # 23 => FN.event_name_navigate_click_2_count
    out[:, 23] = event_name_counts[2]
    
    # 24 => FN.event_name_observation_click_3_count
    out[:, 24] = event_name_counts[3]
    
    # 25 => FN.event_name_notification_click_4_count
    out[:, 25] = event_name_counts[4]
    
    # 26 => FN.event_name_object_click_5_count
    out[:, 26] = event_name_counts[5]
    
    # 27 => FN.event_name_object_hover_6_count
    out[:, 27] = event_name_counts[6]
    
    # 28 => FN.event_name_map_hover_7_count
    out[:, 28] = event_name_counts[7]
    
    # 29 => FN.event_name_map_click_8_count
    out[:, 29] = event_name_counts[8]
    
    # 30 => FN.event_name_checkpoint_9_count
    out[:, 30] = event_name_counts[9]
    
    # 31 => FN.event_name_notebook_click_10_count
    out[:, 31] = event_name_counts[10]

    # 56 => FN.last_event_name
    out[:, 56] = x_en[-1]
    
    # 53 => FN.hover_duration_max
    out[:, 53] = np.nanmax(x_hover_duration)
    
    # 54 => FN.hover_duration_min
    out[:, 54] = np.nanmin(x_hover_duration)
    
    # x_session_weekday, x_session_weekday.shape => [3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 ... 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3]
    # x_session_weekday.shape => (165,)
    # 55 => FN.session_weekday
    out[:, 55] = x_session_weekday[0]
    
    fqids_features_src.generate_fqids_count_features(out, x_fqids)

    building_features_src.generate_building_based_features(out, x_b, x_et)
    
    room_features_src.generate_room_based_features(out, x_r, x_et)
    
    fqid_features_src.generate_fqid_based_features(out, x_fqids, x_et)
    
    # 91 => FN.level_mean
    out[:, 91] = x_l.mean()
    
    # 92 => FN.level_std
    out[:, 92] = x_l.std()
    
    level_based_features_src.generate_level_based_features(out, x_l)
    
    
    # 99 => FN.elapsed_time_diff_max
    out[:, 99] = x_et_diff.max()
    
    # 100 => FN.elapsed_time_diff_min
    out[:, 100] = x_et_diff.min()
    
    # 101 => FN.elapsed_time_diff_std
    out[:, 101] = x_et_diff.std()
    
    # 102 => FN.elapsed_time_diff_median
    out[:, 102] = np.median(x_et_diff)
    
    # .diff(a, n=1, axis=-1, ...) => calculate the n-th discrete difference along the given axis.
    # np.diff(np.array([1, 2, 4, 7, 0])) => array([ 1,  2,  3, -7])
    x_index_diff = np.diff(x_index)
    
    session_event_index_range = x_index.max() - x_index.min()
    
    # 107 => FN.session_index_diff_max
    out[:, 107] = x_index_diff.max()

    room_coord_distance_travelled = coordinates_distance_travelled_sum(x_rc_x, x_rc_y)
    
    # 133 => FN.room_coord_distance_travelled
    out[:, 133] = room_coord_distance_travelled

    screen_coord_distance_travelled = coordinates_distance_travelled_sum(x_sc_x, x_sc_y)
    
    # 134 => FN.screen_coord_distance_travelled
    out[:, 134] = screen_coord_distance_travelled


    text_read_speeds = calculate_read_speeds_of_text(x_tl, x_et) # tl => text length.
    
    # 135 => FN.text_read_speeds_mean
    out[:, 135] = text_read_speeds.mean()
    
    # 136 => FN.text_read_speeds_std
    out[:, 136] = text_read_speeds.std()

    ###############################################################################################

    building_counts = generate_building_counts(x_b)
    
    # 58 => FN.building_capitol_0_count
    out[:, 58] = building_counts[0]
    
    # 59 => FN.building_capitol_1_count
    out[:, 59] = building_counts[1]
    
    # 60 => FN.building_capitol_2_count
    out[:, 60] = building_counts[2]
    
    # 61 => FN.building_drycleaner_count
    out[:, 61] = building_counts[3]
    
    # 62 => FN.building_flaghouse_count
    out[:, 62] = building_counts[4]
    
    # 63 => FN.building_historicalsociety_count
    out[:, 63] = building_counts[5]
    
    # 64 => FN.building_humanecology_count
    out[:, 64] = building_counts[6]
    
    # 65 => FN.building_kohlcenter_count
    out[:, 65] = building_counts[7]
    
    # 66 => FN.building_library_count
    out[:, 66] = building_counts[8]
    
    # 67 => FN.building_wildlife_count
    out[:, 67] = building_counts[9]
    
    # 95 => FN.building_nunqiue
    out[:, 95] = np.sum(building_counts != 0)
    
    # 81 => FN.building_capitol_0_proportion_of_events
    out[:, 81] = building_counts[0]/number_of_events
    
    # 82 => FN.building_capitol_1_proportion_of_events
    out[:, 82] = building_counts[1]/number_of_events
    
    # 83 => FN.building_capitol_2_proportion_of_events
    out[:, 83] = building_counts[2]/number_of_events
    
    # 84 => FN.building_drycleaner_proportion_of_events
    out[:, 84] = building_counts[3]/number_of_events
    
    # 85 => FN.building_flaghouse_proportion_of_events
    out[:, 85] = building_counts[4]/number_of_events
    
    # 86 => FN.building_historicalsociety_proportion_of_events
    out[:, 86] = building_counts[5]/number_of_events
    
    # 87 => FN.building_humanecology_proportion_of_events
    out[:, 87] = building_counts[6]/number_of_events
    
    # 88 => FN.building_kohlcenter_proportion_of_events
    out[:, 88] = building_counts[7]/number_of_events
    
    # 89 => FN.building_library_proportion_of_events
    out[:, 89] = building_counts[8]/number_of_events
    
    # 90 => FN.building_wildlife_proportion_of_events
    out[:, 90] = building_counts[9]/number_of_events

    room_counts = generate_room_counts(x_r)
    
    # 68 => FN.room_basement_count
    out[:, 68] = room_counts[0]
    
    # 69 => FN.room_cage_count
    out[:, 69] = room_counts[1]
    
    # 70 => FN.room_center_count
    out[:, 70] = room_counts[2]
    
    # 71 => FN.room_closet_count
    out[:, 71] = room_counts[3]
    
    # 72 => FN.room_closet_dirty_count
    out[:, 72] = room_counts[4]
    
    # 73 => FN.room_collection_count
    out[:, 73] = room_counts[5]
    
    # 74 => FN.room_collection_flag_count
    out[:, 74] = room_counts[6]
    
    # 75 => FN.room_entry_count
    out[:, 75] = room_counts[7]
    
    # 76 => FN.room_frontdesk_count
    out[:, 76] = room_counts[8]
    
    # 77 => FN.room_hall_count
    out[:, 77] = room_counts[9]
    
    # 78 => FN.room_halloffame_count
    out[:, 78] = room_counts[10]
    
    # 79 => FN.room_microfiche_count
    out[:, 79] = room_counts[11]
    
    # 80 => FN.room_stacks_count
    out[:, 80] = room_counts[12]
    
    # 96 => FN.room_nunqiue
    out[:, 96] = np.sum(room_counts != 0)

    building_visits_counts = generate_building_visits_counts(x_b)
    
    # 108 => FN.building_capitol_0_visits_count
    out[:, 108] = building_visits_counts[0]
    
    # 109 => FN.building_capitol_1_visits_count
    out[:, 109] = building_visits_counts[1]
    
    # 110 => FN.building_capitol_2_visits_count
    out[:, 110] = building_visits_counts[2]
    
    # 111 => FN.building_drycleaner_visits_count
    out[:, 111] = building_visits_counts[3]
    
    # 112 => FN.building_flaghouse_visits_count
    out[:, 112] = building_visits_counts[4]
    
    # 113 => FN.building_historicalsociety_visits_count
    out[:, 113] = building_visits_counts[5]
    
    # 114 => FN.building_humanecology_visits_count
    out[:, 114] = building_visits_counts[6]
    
    # 115 => FN.building_kohlcenter_visits_count
    out[:, 115] = building_visits_counts[7]
    
    # 116 => FN.building_library_visits_count
    out[:, 116] = building_visits_counts[8]
    
    # 117 => FN.building_wildlife_visits_count
    out[:, 117] = building_visits_counts[9]

    # 118 => FN.building_visits_nunqiue
    out[:, 118] = np.sum(building_visits_counts != 0)

    room_visits_counts = generate_room_visits_counts(x_r)
    
    # 119 => FN.room_basement_visits_count
    out[:, 119] = room_visits_counts[0]
    
    # 120 => FN.room_cage_visits_count
    out[:, 120] = room_visits_counts[1]
    
    # 121 => FN.room_center_visits_count
    out[:, 121] = room_visits_counts[2]
    
    # 122 => FN.room_closet_visits_count
    out[:, 122] = room_visits_counts[3]
    
    # 123 => FN.room_closet_dirty_visits_count
    out[:, 123] = room_visits_counts[4]
    
    # 124 => FN.room_collection_visits_count
    out[:, 124] = room_visits_counts[5]
    
    # 125 => FN.room_collection_flag_visits_count
    out[:, 125] = room_visits_counts[6]
    
    # 126 => FN.room_entry_visits_count
    out[:, 126] = room_visits_counts[7]
    
    # 127 => FN.room_frontdesk_visits_count
    out[:, 127] = room_visits_counts[8]
    
    # 128 => FN.room_hall_visits_count
    out[:, 128] = room_visits_counts[9]
    
    # 129 => FN.room_halloffame_visits_count
    out[:, 129] = room_visits_counts[10]
    
    # 130 => FN.room_microfiche_visits_count
    out[:, 130] = room_visits_counts[11]
    
    # 131 => FN.room_stacks_visits_count
    out[:, 131] = room_visits_counts[12]

    # 132 => FN.room_visits_nunqiue
    out[:, 132] = np.sum(room_visits_counts != 0)

    ############################################################################################

    # hist => [nan nan nan ... nan nan nan]
    # len(hist) => 3183
    # np.unique(hist) => [ 3. nan]
    # hist[112] => 3.0
    
    SRC_LIST.calculate_LG0_features(
        level_group_index,
        x_l,
        out[:],
        hist,
        x_et,
        x_index,
        x_text_numerical,
        x_en,
        x_n,
        x_fqids,
        x_rc_x,
        x_b,
        x_r,
        x_text_fqid_numerical,
    )

    SRC_LIST.calculate_LG1_features(
        level_group_index,
        x_l,
        out[:],
        hist,
        x_et,
        x_index,
        x_text_numerical,
        x_en,
        x_n,
        x_fqids,
        x_et,
        x_rc_x,
        x_rc_y,
        x_b,
        x_r,
        x_text_fqid_numerical,
    )

    SRC_LIST.calculate_LG2_features(
        level_group_index,
        x_l,
        out[:],
        hist,
        x_et,
        x_index,
        x_text_numerical,
        x_en,
        x_n,
        x_fqids,
        x_et,
        x_rc_x,
        x_rc_y,
        x_b,
        x_r,
    )

    # num_input_rows = e-s

