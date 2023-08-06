#!/usr/bin/env python
# coding: utf-8

# In[1]:

# C Foreign Function Interface for Python. Interact with almost any C code from Python, based on C-like declarations that you can often copy-paste from header files or documentation.
from cffi import FFI

from collections import defaultdict
from functools import cmp_to_key
import json

def str_int_None_compare(aa, bb):
    # aa => (0, None, 'fqid', 'tomap', 'min', 'ETsinceprev', None, None, None, None, None, None)
    # bb => (0, None, 'fqid', 'tomap', 'std', 'ETsinceprev', None, None, None, None, None, None)
            
    n = len(aa)
    
    for i in range(n):
        
        a = aa[i]
        b = bb[i]
    
        if a is None:
            if b is None:
                continue # return 0
            else:
                return -1
        elif b is None:
            return 1
        elif a > b:
            return 1
        elif a == b:
            continue # return 0
        else:
            return -1
        
    return 0
    
groupby_src_lookup = {
    'fqid': ('x_fqids', 'FQIDS'),
    'name': ('x_n', 'NAMES'),
    'event_name': ('x_en', 'EVENT_NAMES'),
    'text_fqid': ('x_text_fqid_numerical', 'TEXT_FQIDS'),
    'room_fqid': ('x_room_fqid_numerical', 'ROOM_FQIDS'),
    'NONE': ('NONE', 'NONE'),
}

value_src_lookup = {
    'ETsinceprev': ('et_since_prev', ''),
    'index': ('x_index', '[i]'),
    'screen_coor_x': ('x_sc_x', '[i]'),
    'screen_coor_y': ('x_sc_y', '[i]'),
    'page': ('x_page', '[i]'),
    'room_coor_x': ('x_rc_x', '[i]'),
    'room_coor_y': ('x_rc_y', '[i]'),
    'hover_duration': ('x_hover_duration', '[i]'),
    'elapsed_time': ('x_et', '[i]'),
    
    'screen_coor_y_abs_diff1': ('screen_coor_y_abs_diff1', ''),
    'screen_coor_x_abs_diff1': ('screen_coor_x_abs_diff1', ''),
}

FEATURE_DEFS = []

# Add simple filtered agg featues.
FEATURE_DEFS.extend([
    (0, None, 'fqid', 'tomap', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tomap', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'directory', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'directory', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'directory', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'directory', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'directory', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'outtolunch', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic_kohlcenter', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic_kohlcenter', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'chap1_finale_c', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'chap1_finale_c', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'chap1_finale_c', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'teddy', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'photo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'photo', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'toentry', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic_historicalsociety', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic_historicalsociety', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'fqid', 'notebook', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'notebook', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tunic_hub_slip', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'retirement_letter', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'togrampa', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'togrampa', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'chap1_finale', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'boss', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'fqid', 'tocollection', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'fqid', 'report', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_groupconvo', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_plaque_face_date', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_plaque_face_date', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_plaque_face_date', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_plaque_face_date', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_togrampa', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_togrampa', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_togrampa', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_kohlcenter_halloffame_togrampa', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_capitol_0_hall_chap1_finale_c', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_photo', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_photo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_photo', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_block_tomap1', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_block_tomap1', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_block_tomap1', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_collection_gramps_found', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_collection_gramps_found', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_wells_talktogramps', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_wells_talktogramps', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_entry_wells_talktogramps', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_doorblock', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_closet_gramps_intro_0_cs_0', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_basement_janitor', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'text_fqid', 'tunic_historicalsociety_stacks_outtolunch', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'room_fqid', 'tunic_capitol_0_hall', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'room_fqid', 'tunic_kohlcenter_halloffame', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'room_fqid', 'tunic_kohlcenter_halloffame', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'room_fqid', 'tunic_historicalsociety_collection', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'room_fqid', 'tunic_historicalsociety_stacks', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'room_fqid', 'tunic_historicalsociety_stacks', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'event_name', 'person_click', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'person_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'navigate_click', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'object_hover', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'object_hover', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'object_hover', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'event_name', 'notebook_click', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'notebook_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'notebook_click', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'observation_click', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'observation_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'observation_click', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'event_name', 'observation_click', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'event_name', 'object_click', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'undefined', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'undefined', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'close', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'close', 'count', 'index', None, None, None, None, None, None),
    (0, None, 'name', 'prev', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'prev', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'prev', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'prev', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'prev', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'next', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'name', 'open', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'std', 'screen_coor_x_abs_diff1', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'std', 'screen_coor_y_abs_diff1', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'mean', 'page', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'sum', 'page', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'mean', 'room_coor_x', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'sum', 'room_coor_x', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'mean', 'room_coor_y', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'sum', 'room_coor_y', None, None, None, None, None, None),
    (0, None, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (0, 4, 'NONE', 'NONE', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (0, 4, 'NONE', 'NONE', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (0, 4, 'room_fqid', 'tunic_capitol_0_hall', 'count', 'index', None, None, None, None, None, None),
    (0, 1, 'room_fqid', 'tunic_historicalsociety_closet', 'count', 'index', None, None, None, None, None, None),
    (0, 3, 'room_fqid', 'tunic_historicalsociety_stacks', 'count', 'index', None, None, None, None, None, None),
    (1, None, 'fqid', 'tunic_library', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_0_next', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_0_next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_0_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_0_next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_0_next', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_0_next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_0_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_0_next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'logbook_page_bingo', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'logbook_page_bingo', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'logbook_page_bingo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'logbook_page_bingo', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_1_next', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_1_next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_1_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_1_next', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_1_next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_2_next', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_2_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_2_next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_1_next', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_1_next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_1_next', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper2_bingo', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper2_bingo', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper2_bingo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper2_bingo', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper2_bingo', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'block_badge', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'block_badge', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tostacks', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals', 'count', 'index', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'trigger_coffee', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'trigger_coffee', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'trigger_coffee', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'wellsbadge', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tocloset_dirty', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tocloset_dirty', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tocloset_dirty', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tocloset_dirty', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_bingo_bingo', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_bingo_bingo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'photo', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'photo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper1_next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper1_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper1_next', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper1_next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper2_next', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper0_prev', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper0_prev', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_hub_topics', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_hub_topics', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'businesscards_card_bingo_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'toentry', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'toentry', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tomap', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tomap', 'count', 'index', None, None, None, None, None, None),
    (1, None, 'fqid', 'what_happened', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'journals_pic_2_bingo', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tohallway', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'reader_paper1_prev', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'gramps', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'tobasement', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'directory', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'fqid', 'door_block_clean', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_coffee', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_coffee', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_coffee', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_coffee', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_coffee', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_helpclean', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_helpclean', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_helpclean', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_helpclean', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_helpclean', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_foundtheodora', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_foundtheodora', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_library_frontdesk_worker_hello_short', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_newspaper', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_newspaper', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_drycleaner_frontdesk_logbook_page_bingo', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_capitol_0_hall_boss_talktogramps', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_capitol_0_hall_boss_talktogramps', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_stacks_block', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_what_happened', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_what_happened', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_stacks_journals_pic_2_bingo', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_library_microfiche_reader_paper2_bingo', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_library_microfiche_reader_paper2_bingo', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass_recap', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_basement_janitor', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'text_fqid', 'tunic_historicalsociety_closet_dirty_door_block_clean', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_historicalsociety_closet_dirty', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_historicalsociety_closet_dirty', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_historicalsociety_closet_dirty', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_historicalsociety_closet_dirty', 'count', 'index', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_library_microfiche', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_drycleaner_frontdesk', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'room_fqid', 'tunic_library_frontdesk', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'notebook_click', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'notebook_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'cutscene_click', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'cutscene_click', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'observation_click', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'observation_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'observation_click', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'navigate_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'event_name', 'object_click', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'name', 'close', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'name', 'close', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, None, 'name', 'undefined', 'count', 'index', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'std', 'screen_coor_x_abs_diff1', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'max', 'screen_coor_x_abs_diff1', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'std', 'hover_duration', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'mean', 'hover_duration', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'sum', 'hover_duration', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'mean', 'room_coor_y', None, None, None, None, None, None),
    (1, None, 'NONE', 'NONE', 'sum', 'room_coor_y', None, None, None, None, None, None),
    (1, 6, 'NONE', 'NONE', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, 6, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, 10, 'NONE', 'NONE', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (1, 10, 'NONE', 'NONE', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (1, 8, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, 11, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (1, 7, 'room_fqid', 'tunic_historicalsociety_stacks', 'count', 'index', None, None, None, None, None, None),
    (1, 12, 'room_fqid', 'tunic_historicalsociety_frontdesk', 'count', 'index', None, None, None, None, None, None),
    (1, 12, 'room_fqid', 'tunic_historicalsociety_stacks', 'count', 'index', None, None, None, None, None, None),
    (2, None, 'fqid', 'tunic_flaghouse', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'journals_flag_pic_0_next', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'journals_flag_pic_0_next', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'journals_flag_pic_2_bingo', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'reader_flag_paper2_prev', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'journals_flag_pic_0_old_next', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'journals_flag_hub_topics_old', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'fqid', 'journals_flag_pic_1_bingo', 'count', 'index', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_historicalsociety_entry_groupconvo_flag', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_library_frontdesk_worker_nelson', 'std', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_wildlife_center_expert_recap', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_flaghouse_entry_colorbook', 'mean', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_flaghouse_entry_colorbook', 'max', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_flaghouse_entry_colorbook', 'min', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_flaghouse_entry_colorbook', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (2, None, 'text_fqid', 'tunic_library_frontdesk_worker_nelson_recap', 'sum', 'ETsinceprev', None, None, None, None, None, None),
    (2, 14, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None),
])

# agg between two events features
FEATURE_DEFS.extend([
    (0, 0, None, None, 'max', 'hover_duration', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'fqid', 'NaN'),
    (0, 0, None, None, 'max', 'hover_duration', 'last', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'event_name', 'navigate_click'),
    (0, 0, None, None, 'max', 'hover_duration', 'last', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'max', 'index', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'last', 'text_fqid', 'tunic_historicalsociety_closet_photo'),
    (0, 0, None, None, 'max', 'room_coor_x', 'first', 'event_name', 'notification_click', 'last', 'name', 'close'),
    (0, 0, None, None, 'max', 'room_coor_y', 'first', 'fqid', 'photo', 'first', 'fqid', 'doorblock'),
    (0, 0, None, None, 'max', 'room_coor_y', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'last', 'fqid', 'photo'),
    (0, 0, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'intro', 'first', 'text_fqid', 'tunic_historicalsociety_closet_photo'),
    (0, 0, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'intro', 'last', 'name', 'undefined'),
    (0, 0, None, None, 'max', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_notebook', 'last', 'fqid', 'gramps'),
    (0, 0, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'first', 'event_name', 'object_click'),
    (0, 0, None, None, 'mean', 'hover_duration', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'first', 'text_fqid', 'tunic_historicalsociety_closet_notebook'),
    (0, 0, None, None, 'mean', 'hover_duration', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'event_name', 'object_hover'),
    (0, 0, None, None, 'mean', 'hover_duration', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'mean', 'hover_duration', 'last', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'name', 'basic'),
    (0, 0, None, None, 'mean', 'index', 'first', 'event_name', 'object_hover', 'last', 'fqid', 'NaN'),
    (0, 0, None, None, 'mean', 'room_coor_y', 'first', 'fqid', 'NaN', 'last', 'name', 'undefined'),
    (0, 0, None, None, 'mean', 'room_coor_y', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'last', 'fqid', 'photo'),
    (0, 0, None, None, 'mean', 'room_coor_y', 'last', 'fqid', 'intro', 'first', 'text_fqid', 'tunic_historicalsociety_closet_notebook'),
    (0, 0, None, None, 'mean', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_0', 'last', 'event_name', 'object_hover'),
    (0, 0, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'last', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub'),
    (0, 0, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'text_fqid', 'tunic_historicalsociety_closet_intro', 'first', 'text_fqid', 'NaN'),
    (0, 0, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'text_fqid', 'tunic_historicalsociety_closet_photo', 'first', 'event_name', 'notification_click'),
    (0, 0, None, None, 'min', 'ETsinceprev', 'first', 'text_fqid', 'tunic_historicalsociety_closet_gramps_intro_0_cs_0', 'last', 'fqid', 'notebook'),
    (0, 0, None, None, 'min', 'hover_duration', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'event_name', 'notification_click'),
    (0, 0, None, None, 'min', 'room_coor_x', 'first', 'event_name', 'person_click', 'last', 'fqid', 'notebook'),
    (0, 0, None, None, 'min', 'room_coor_x', 'first', 'name', 'undefined', 'last', 'room_fqid', 'tunic_historicalsociety_closet'),
    (0, 0, None, None, 'min', 'room_coor_x', 'last', 'event_name', 'notification_click', 'last', 'event_name', 'object_click'),
    (0, 0, None, None, 'min', 'room_coor_x', 'last', 'text_fqid', 'tunic_historicalsociety_closet_notebook', 'last', 'name', 'close'),
    (0, 0, None, None, 'min', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'min', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'teddy', 'first', 'event_name', 'object_click'),
    (0, 0, None, None, 'min', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'teddy', 'last', 'event_name', 'navigate_click'),
    (0, 0, None, None, 'min', 'screen_coor_x_abs_diff1', 'last', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_0', 'last', 'event_name', 'notification_click'),
    (0, 0, None, None, 'std', 'index', 'first', 'event_name', 'navigate_click', 'last', 'event_name', 'cutscene_click'),
    (0, 0, None, None, 'std', 'room_coor_y', 'first', 'event_name', 'navigate_click', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub'),
    (0, 0, None, None, 'std', 'room_coor_y', 'first', 'fqid', 'teddy', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub'),
    (0, 0, None, None, 'std', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_closet_gramps_intro_0_cs_0', 'first', 'event_name', 'notification_click'),
    (0, 0, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_doorblock', 'first', 'event_name', 'notification_click'),
    (0, 0, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_doorblock', 'last', 'fqid', 'NaN'),
    (0, 0, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_0', 'last', 'text_fqid', 'tunic_historicalsociety_closet_gramps_intro_0_cs_0'),
    (0, 0, None, None, 'sum', 'ETsinceprev', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_0', 'last', 'event_name', 'object_hover'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'first', 'fqid', 'gramps', 'last', 'event_name', 'object_hover'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'first', 'fqid', 'teddy', 'first', 'text_fqid', 'NaN'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'last', 'event_name', 'object_hover'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_0', 'first', 'name', 'undefined'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'gramps', 'last', 'event_name', 'object_hover'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'teddy', 'first', 'text_fqid', 'tunic_historicalsociety_closet_notebook'),
    (0, 0, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'teddy', 'last', 'fqid', 'NaN'),
    (0, 0, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'first', 'event_name', 'object_click'),
    (0, 0, None, None, 'sum', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'notification_click', 'first', 'name', 'close'),
    (0, 0, None, None, 'sum', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'notification_click', 'last', 'name', 'basic'),
    (0, 0, None, None, 'sum', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'observation_click', 'first', 'event_name', 'object_click'),
    (0, 1, None, None, 'max', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'first', 'fqid', 'tobasement'),
    (0, 1, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'notification_click', 'last', 'event_name', 'object_click'),
    (0, 1, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'groupconvo', 'last', 'room_fqid', 'tunic_historicalsociety_closet'),
    (0, 1, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'name', 'close', 'last', 'fqid', 'retirement_letter'),
    (0, 1, None, None, 'mean', 'room_coor_x', 'first', 'event_name', 'notification_click', 'last', 'event_name', 'notification_click'),
    (0, 1, None, None, 'mean', 'room_coor_x', 'last', 'name', 'undefined', 'last', 'text_fqid', 'NaN'),
    (0, 1, None, None, 'mean', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'groupconvo', 'last', 'room_fqid', 'tunic_historicalsociety_closet'),
    (0, 1, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'janitor', 'first', 'text_fqid', 'tunic_historicalsociety_entry_block_tocollection'),
    (0, 1, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'report', 'last', 'name', 'basic'),
    (0, 1, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'name', 'open', 'last', 'room_fqid', 'tunic_historicalsociety_closet'),
    (0, 1, None, None, 'min', 'room_coor_y', 'first', 'event_name', 'cutscene_click', 'last', 'fqid', 'groupconvo'),
    (0, 1, None, None, 'min', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'retirement_letter', 'first', 'room_fqid', 'tunic_historicalsociety_basement'),
    (0, 1, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'navigate_click', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 1, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'object_hover', 'first', 'fqid', 'groupconvo'),
    (0, 1, None, None, 'std', 'room_coor_x', 'first', 'text_fqid', 'NaN', 'last', 'fqid', 'boss'),
    (0, 1, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'event_name', 'notification_click', 'last', 'fqid', 'tocloset'),
    (0, 1, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'name', 'basic', 'first', 'fqid', 'tobasement'),
    (0, 1, None, None, 'sum', 'room_coor_x', 'first', 'name', 'basic', 'last', 'fqid', 'groupconvo'),
    (0, 1, None, None, 'sum', 'room_coor_y', 'first', 'event_name', 'navigate_click', 'last', 'fqid', 'toentry'),
    (0, 2, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'block_tomap2', 'last', 'event_name', 'notification_click'),
    (0, 2, None, None, 'max', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_entry_block_tomap2', 'last', 'fqid', 'tunic_hub_slip'),
    (0, 2, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'text_fqid', 'tunic_historicalsociety_collection_cs', 'last', 'event_name', 'navigate_click'),
    (0, 2, None, None, 'mean', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_collection_cs', 'last', 'event_name', 'notification_click'),
    (0, 2, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'NaN', 'last', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 2, None, None, 'min', 'ETsinceprev', 'first', 'fqid', 'block_tomap2', 'last', 'fqid', 'block_tomap2'),
    (0, 2, None, None, 'min', 'index', 'last', 'name', 'open', 'first', 'fqid', 'wells'),
    (0, 2, None, None, 'min', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_collection_gramps_look_0', 'last', 'text_fqid', 'tunic_historicalsociety_collection_gramps_found'),
    (0, 2, None, None, 'min', 'screen_coor_x_abs_diff1', 'last', 'event_name', 'object_click', 'first', 'text_fqid', 'tunic_historicalsociety_collection_gramps_found'),
    (0, 2, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'object_click', 'last', 'room_fqid', 'tunic_historicalsociety_collection'),
    (0, 2, None, None, 'std', 'ETsinceprev', 'last', 'fqid', 'tocollection', 'last', 'fqid', 'NaN'),
    (0, 2, None, None, 'std', 'room_coor_x', 'first', 'name', 'basic', 'first', 'text_fqid', 'tunic_historicalsociety_collection_gramps_found'),
    (0, 2, None, None, 'std', 'room_coor_x', 'first', 'text_fqid', 'tunic_historicalsociety_collection_gramps_found', 'last', 'name', 'basic'),
    (0, 2, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'fqid', 'tocollection'),
    (0, 2, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_collection_cs', 'first', 'fqid', 'tunic'),
    (0, 2, None, None, 'sum', 'room_coor_x', 'first', 'event_name', 'cutscene_click', 'last', 'event_name', 'navigate_click'),
    (0, 2, None, None, 'sum', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'NaN', 'first', 'room_fqid', 'tunic_historicalsociety_collection'),
    (0, 3, None, None, 'max', 'room_coor_x', 'first', 'event_name', 'object_click', 'first', 'fqid', 'tocollection'),
    (0, 3, None, None, 'max', 'room_coor_x', 'first', 'fqid', 'NaN', 'first', 'fqid', 'tunic'),
    (0, 3, None, None, 'max', 'room_coor_y', 'first', 'event_name', 'object_hover', 'first', 'fqid', 'tunic_historicalsociety'),
    (0, 3, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tomap', 'first', 'event_name', 'object_hover'),
    (0, 3, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tunic_historicalsociety', 'last', 'fqid', 'NaN'),
    (0, 3, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_teddy_intro_0_cs_5', 'last', 'fqid', 'tobasement'),
    (0, 3, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_basement', 'last', 'fqid', 'NaN'),
    (0, 3, None, None, 'mean', 'ETsinceprev', 'first', 'event_name', 'object_hover', 'first', 'fqid', 'gramps'),
    (0, 3, None, None, 'mean', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'tunic', 'last', 'event_name', 'notebook_click'),
    (0, 3, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_collection', 'last', 'fqid', 'tocloset'),
    (0, 3, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'NaN', 'last', 'fqid', 'tostacks'),
    (0, 3, None, None, 'min', 'index', 'first', 'fqid', 'toentry', 'first', 'text_fqid', 'tunic_historicalsociety_collection_gramps_lost'),
    (0, 3, None, None, 'min', 'room_coor_x', 'first', 'event_name', 'map_hover', 'last', 'name', 'close'),
    (0, 3, None, None, 'min', 'room_coor_x', 'first', 'fqid', 'tomap', 'last', 'event_name', 'navigate_click'),
    (0, 3, None, None, 'min', 'room_coor_x', 'first', 'fqid', 'tostacks', 'last', 'event_name', 'object_click'),
    (0, 3, None, None, 'min', 'room_coor_x', 'first', 'name', 'open', 'first', 'text_fqid', 'tunic_historicalsociety_basement_janitor'),
    (0, 3, None, None, 'min', 'room_coor_x', 'last', 'event_name', 'map_hover', 'last', 'name', 'undefined'),
    (0, 3, None, None, 'min', 'room_coor_x', 'last', 'fqid', 'tunic_kohlcenter', 'first', 'event_name', 'cutscene_click'),
    (0, 3, None, None, 'min', 'room_coor_x', 'last', 'fqid', 'tunic_kohlcenter', 'first', 'fqid', 'togrampa'),
    (0, 3, None, None, 'min', 'room_coor_y', 'first', 'event_name', 'notification_click', 'last', 'event_name', 'cutscene_click'),
    (0, 3, None, None, 'min', 'room_coor_y', 'first', 'fqid', 'plaque_face_date', 'last', 'event_name', 'object_click'),
    (0, 3, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tunic_historicalsociety', 'first', 'fqid', 'togrampa'),
    (0, 3, None, None, 'std', 'hover_duration', 'first', 'event_name', 'object_click', 'first', 'event_name', 'object_hover'),
    (0, 3, None, None, 'std', 'index', 'last', 'fqid', 'toentry', 'last', 'fqid', 'tomap'),
    (0, 3, None, None, 'std', 'room_coor_x', 'first', 'event_name', 'object_hover', 'first', 'fqid', 'gramps'),
    (0, 3, None, None, 'std', 'room_coor_x', 'first', 'text_fqid', 'tunic_kohlcenter_halloffame_plaque_face_date', 'last', 'text_fqid', 'tunic_kohlcenter_halloffame_togrampa'),
    (0, 3, None, None, 'std', 'room_coor_x', 'last', 'fqid', 'tocloset', 'last', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub'),
    (0, 3, None, None, 'std', 'room_coor_x', 'last', 'fqid', 'tostacks', 'last', 'text_fqid', 'tunic_historicalsociety_closet_photo'),
    (0, 3, None, None, 'std', 'room_coor_y', 'first', 'room_fqid', 'tunic_kohlcenter_halloffame', 'first', 'event_name', 'object_click'),
    (0, 3, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'event_name', 'observation_click', 'first', 'name', 'open'),
    (0, 3, None, None, 'std', 'screen_coor_x_abs_diff1', 'last', 'event_name', 'observation_click', 'first', 'event_name', 'notebook_click'),
    (0, 3, None, None, 'std', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'tunic_historicalsociety', 'last', 'fqid', 'plaque_face_date'),
    (0, 3, None, None, 'std', 'screen_coor_y_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_entry', 'first', 'fqid', 'plaque'),
    (0, 3, None, None, 'sum', 'hover_duration', 'last', 'event_name', 'navigate_click', 'last', 'event_name', 'object_hover'),
    (0, 3, None, None, 'sum', 'room_coor_y', 'first', 'fqid', 'tostacks', 'last', 'fqid', 'tocloset'),
    (0, 3, None, None, 'sum', 'room_coor_y', 'first', 'text_fqid', 'NaN', 'first', 'fqid', 'tocloset'),
    (0, 3, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'tostacks', 'first', 'fqid', 'tocloset'),
    (0, 3, None, None, 'sum', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tostacks', 'last', 'event_name', 'cutscene_click'),
    (0, 4, None, None, 'max', 'ETsinceprev', 'last', 'fqid', 'toentry', 'first', 'event_name', 'map_hover'),
    (0, 4, None, None, 'max', 'index', 'first', 'room_fqid', 'tunic_capitol_0_hall', 'last', 'room_fqid', 'tunic_capitol_0_hall'),
    (0, 4, None, None, 'max', 'room_coor_y', 'first', 'name', 'undefined', 'first', 'fqid', 'toentry'),
    (0, 4, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'NaN', 'first', 'fqid', 'chap1_finale'),
    (0, 4, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'tunic_capitol_0', 'last', 'name', 'undefined'),
    (0, 4, None, None, 'mean', 'room_coor_x', 'first', 'name', 'close', 'last', 'fqid', 'tunic_kohlcenter'),
    (0, 4, None, None, 'mean', 'room_coor_x', 'first', 'room_fqid', 'tunic_kohlcenter_halloffame', 'first', 'fqid', 'tunic_kohlcenter'),
    (0, 4, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'NaN', 'first', 'text_fqid', 'tunic_capitol_0_hall_chap1_finale_c'),
    (0, 4, None, None, 'min', 'screen_coor_x_abs_diff1', 'first', 'event_name', 'map_hover', 'last', 'text_fqid', 'NaN'),
    (0, 4, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'navigate_click', 'last', 'event_name', 'map_click'),
    (0, 4, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'navigate_click', 'last', 'fqid', 'tunic_capitol_0'),
    (0, 4, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'name', 'undefined', 'first', 'fqid', 'toentry'),
    (0, 4, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'room_fqid', 'tunic_kohlcenter_halloffame', 'first', 'room_fqid', 'tunic_capitol_0_hall'),
    (0, 4, None, None, 'std', 'ETsinceprev', 'first', 'fqid', 'NaN', 'first', 'name', 'basic'),
    (0, 4, None, None, 'std', 'hover_duration', 'last', 'fqid', 'NaN', 'last', 'room_fqid', 'tunic_kohlcenter_halloffame'),
    (0, 4, None, None, 'std', 'room_coor_x', 'first', 'fqid', 'toentry', 'first', 'event_name', 'map_hover'),
    (0, 4, None, None, 'std', 'room_coor_x', 'first', 'fqid', 'tunic_kohlcenter', 'first', 'fqid', 'chap1_finale_c'),
    (0, 4, None, None, 'std', 'room_coor_x', 'last', 'fqid', 'tunic_kohlcenter', 'last', 'text_fqid', 'NaN'),
    (0, 4, None, None, 'sum', 'ETsinceprev', 'last', 'fqid', 'tunic_kohlcenter', 'last', 'room_fqid', 'tunic_kohlcenter_halloffame'),
    (0, 4, None, None, 'sum', 'room_coor_x', 'first', 'room_fqid', 'tunic_capitol_0_hall', 'last', 'event_name', 'checkpoint'),
    (0, 4, None, None, 'sum', 'room_coor_x', 'last', 'fqid', 'tunic_capitol_0', 'last', 'name', 'basic'),
    (0, 4, None, None, 'sum', 'room_coor_x', 'last', 'room_fqid', 'tunic_kohlcenter_halloffame', 'last', 'room_fqid', 'tunic_capitol_0_hall'),
    (1, 10, None, None, 'max', 'room_coor_y', 'first', 'fqid', 'NaN', 'last', 'text_fqid', 'tunic_library_frontdesk_block_badge_2'),
    (1, 10, None, None, 'mean', 'hover_duration', 'first', 'fqid', 'reader_paper1_next', 'first', 'text_fqid', 'tunic_library_frontdesk_wellsbadge_hub'),
    (1, 10, None, None, 'mean', 'hover_duration', 'last', 'fqid', 'reader_paper1_next', 'last', 'event_name', 'navigate_click'),
    (1, 10, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'tofrontdesk', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_droppedbadge'),
    (1, 10, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_library_microfiche', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_wells'),
    (1, 10, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'reader_paper0_next', 'last', 'room_fqid', 'tunic_library_frontdesk'),
    (1, 10, None, None, 'min', 'room_coor_x', 'first', 'fqid', 'NaN', 'last', 'fqid', 'NaN'),
    (1, 10, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'navigate_click', 'last', 'fqid', 'tofrontdesk'),
    (1, 10, None, None, 'std', 'room_coor_y', 'first', 'fqid', 'tofrontdesk', 'last', 'fqid', 'block_badge_2'),
    (1, 10, None, None, 'std', 'room_coor_y', 'last', 'room_fqid', 'tunic_library_microfiche', 'last', 'fqid', 'wellsbadge'),
    (1, 10, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'event_name', 'notification_click', 'last', 'fqid', 'worker'),
    (1, 10, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'wellsbadge', 'last', 'text_fqid', 'NaN'),
    (1, 10, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'room_fqid', 'tunic_library_frontdesk', 'last', 'fqid', 'NaN'),
    (1, 10, None, None, 'std', 'screen_coor_y_abs_diff1', 'last', 'room_fqid', 'tunic_library_microfiche', 'last', 'event_name', 'person_click'),
    (1, 10, None, None, 'sum', 'hover_duration', 'last', 'fqid', 'reader_paper1_next', 'first', 'fqid', 'worker'),
    (1, 10, None, None, 'sum', 'hover_duration', 'last', 'fqid', 'reader_paper1_next', 'last', 'name', 'close'),
    (1, 10, None, None, 'sum', 'room_coor_x', 'last', 'event_name', 'object_hover', 'last', 'event_name', 'navigate_click'),
    (1, 10, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_library_microfiche', 'first', 'fqid', 'wellsbadge'),
    (1, 10, None, None, 'sum', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'NaN', 'last', 'event_name', 'notification_click'),
    (1, 10, None, None, 'sum', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'object_click', 'last', 'event_name', 'observation_click'),
    (1, 11, None, None, 'max', 'ETsinceprev', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_wells_recap', 'first', 'fqid', 'gramps'),
    (1, 11, None, None, 'max', 'hover_duration', 'first', 'fqid', 'journals_hub_topics', 'first', 'event_name', 'object_click'),
    (1, 11, None, None, 'max', 'hover_duration', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'event_name', 'notification_click'),
    (1, 11, None, None, 'max', 'hover_duration', 'last', 'event_name', 'map_click', 'last', 'fqid', 'NaN'),
    (1, 11, None, None, 'max', 'index', 'last', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_newspaper_recap', 'last', 'fqid', 'journals_pic_2_bingo'),
    (1, 11, None, None, 'max', 'room_coor_y', 'last', 'event_name', 'navigate_click', 'last', 'event_name', 'object_click'),
    (1, 11, None, None, 'max', 'screen_coor_x_abs_diff1', 'first', 'name', 'open', 'first', 'fqid', 'tomap'),
    (1, 11, None, None, 'mean', 'ETsinceprev', 'last', 'room_fqid', 'tunic_library_microfiche', 'last', 'fqid', 'tunic_historicalsociety'),
    (1, 11, None, None, 'mean', 'hover_duration', 'first', 'event_name', 'object_click', 'last', 'fqid', 'journals_hub_topics'),
    (1, 11, None, None, 'mean', 'room_coor_x', 'first', 'fqid', 'NaN', 'last', 'fqid', 'tomap'),
    (1, 11, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'navigate_click', 'first', 'event_name', 'notification_click'),
    (1, 11, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'journals_pic_0_next', 'last', 'text_fqid', 'tunic_historicalsociety_stacks_journals_pic_2_bingo'),
    (1, 11, None, None, 'mean', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'worker', 'first', 'fqid', 'tunic_capitol_1'),
    (1, 11, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tunic_drycleaner', 'last', 'fqid', 'worker'),
    (1, 11, None, None, 'min', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'navigate_click', 'first', 'fqid', 'journals_pic_1_next'),
    (1, 11, None, None, 'std', 'hover_duration', 'first', 'event_name', 'object_click', 'last', 'event_name', 'object_hover'),
    (1, 11, None, None, 'std', 'hover_duration', 'first', 'event_name', 'object_hover', 'last', 'name', 'undefined'),
    (1, 11, None, None, 'std', 'hover_duration', 'first', 'fqid', 'archivist', 'last', 'fqid', 'journals_pic_2_bingo'),
    (1, 11, None, None, 'std', 'hover_duration', 'last', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_newspaper_recap', 'last', 'fqid', 'NaN'),
    (1, 11, None, None, 'std', 'room_coor_x', 'first', 'name', 'basic', 'last', 'room_fqid', 'tunic_historicalsociety_basement'),
    (1, 11, None, None, 'std', 'room_coor_x', 'first', 'room_fqid', 'tunic_kohlcenter_halloffame', 'last', 'fqid', 'journals_hub_topics'),
    (1, 11, None, None, 'std', 'room_coor_y', 'first', 'fqid', 'tomicrofiche', 'last', 'fqid', 'tunic_kohlcenter'),
    (1, 11, None, None, 'std', 'room_coor_y', 'first', 'name', 'basic', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_wells_recap'),
    (1, 11, None, None, 'std', 'room_coor_y', 'last', 'fqid', 'journals_pic_2_next', 'last', 'text_fqid', 'NaN'),
    (1, 11, None, None, 'std', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'archivist', 'first', 'fqid', 'journals_pic_0_next'),
    (1, 11, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'janitor', 'first', 'fqid', 'journals_pic_2_next'),
    (1, 11, None, None, 'sum', 'index', 'first', 'event_name', 'notebook_click', 'last', 'name', 'open'),
    (1, 11, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'journals_pic_2_next', 'last', 'event_name', 'notification_click'),
    (1, 11, None, None, 'sum', 'room_coor_y', 'last', 'room_fqid', 'tunic_library_frontdesk', 'last', 'fqid', 'toentry'),
    (1, 11, None, None, 'sum', 'screen_coor_x_abs_diff1', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_wells_recap', 'last', 'fqid', 'gramps'),
    (1, 12, None, None, 'max', 'room_coor_x', 'first', 'name', 'close', 'last', 'fqid', 'tunic_kohlcenter'),
    (1, 12, None, None, 'max', 'room_coor_y', 'first', 'fqid', 'tostacks', 'last', 'event_name', 'map_hover'),
    (1, 12, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'first', 'event_name', 'checkpoint'),
    (1, 12, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_nothing', 'last', 'fqid', 'tunic_capitol_1'),
    (1, 12, None, None, 'mean', 'ETsinceprev', 'last', 'room_fqid', 'tunic_historicalsociety_stacks', 'first', 'fqid', 'NaN'),
    (1, 12, None, None, 'mean', 'index', 'first', 'room_fqid', 'tunic_historicalsociety_closet_dirty', 'last', 'name', 'open'),
    (1, 12, None, None, 'mean', 'room_coor_x', 'last', 'event_name', 'notebook_click', 'last', 'event_name', 'navigate_click'),
    (1, 12, None, None, 'mean', 'room_coor_x', 'last', 'name', 'open', 'first', 'room_fqid', 'tunic_capitol_1_hall'),
    (1, 12, None, None, 'mean', 'room_coor_y', 'first', 'event_name', 'notebook_click', 'last', 'fqid', 'NaN'),
    (1, 12, None, None, 'min', 'room_coor_y', 'first', 'event_name', 'map_hover', 'first', 'room_fqid', 'tunic_capitol_1_hall'),
    (1, 12, None, None, 'std', 'index', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_foundtheodora', 'last', 'event_name', 'map_click'),
    (1, 12, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tofrontdesk', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 12, None, None, 'sum', 'ETsinceprev', 'first', 'room_fqid', 'tunic_historicalsociety_basement', 'first', 'event_name', 'map_click'),
    (1, 12, None, None, 'sum', 'room_coor_x', 'last', 'fqid', 'tunic_drycleaner', 'first', 'fqid', 'tunic_capitol_1'),
    (1, 12, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'tofrontdesk', 'last', 'fqid', 'tunic_capitol_1'),
    (1, 5, None, None, 'max', 'ETsinceprev', 'first', 'event_name', 'map_hover', 'last', 'fqid', 'outtolunch'),
    (1, 5, None, None, 'max', 'ETsinceprev', 'first', 'room_fqid', 'tunic_historicalsociety_collection', 'first', 'fqid', 'tobasement'),
    (1, 5, None, None, 'max', 'hover_duration', 'first', 'fqid', 'tostacks', 'first', 'fqid', 'tocloset_dirty'),
    (1, 5, None, None, 'max', 'hover_duration', 'first', 'fqid', 'tostacks', 'last', 'name', 'undefined'),
    (1, 5, None, None, 'max', 'room_coor_x', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_what_happened', 'last', 'room_fqid', 'tunic_historicalsociety_closet_dirty'),
    (1, 5, None, None, 'max', 'room_coor_x', 'last', 'event_name', 'map_hover', 'last', 'fqid', 'tunic_hub_slip'),
    (1, 5, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'event_name', 'navigate_click', 'last', 'room_fqid', 'tunic_historicalsociety_closet_dirty'),
    (1, 5, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'boss', 'first', 'fqid', 'tomap'),
    (1, 5, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'tunic_hub_slip', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_what_happened'),
    (1, 5, None, None, 'max', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tostacks', 'first', 'room_fqid', 'tunic_historicalsociety_collection'),
    (1, 5, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'boss', 'last', 'fqid', 'tunic_kohlcenter'),
    (1, 5, None, None, 'mean', 'ETsinceprev', 'first', 'fqid', 'tunic_capitol_0', 'last', 'fqid', 'tocollection'),
    (1, 5, None, None, 'mean', 'room_coor_x', 'first', 'event_name', 'map_hover', 'last', 'event_name', 'object_hover'),
    (1, 5, None, None, 'mean', 'room_coor_x', 'first', 'fqid', 'tocloset_dirty', 'last', 'room_fqid', 'tunic_historicalsociety_closet_dirty'),
    (1, 5, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tunic', 'last', 'event_name', 'object_click'),
    (1, 5, None, None, 'min', 'ETsinceprev', 'first', 'room_fqid', 'tunic_historicalsociety_collection', 'first', 'fqid', 'tunic_hub_slip'),
    (1, 5, None, None, 'min', 'ETsinceprev', 'last', 'fqid', 'outtolunch', 'last', 'event_name', 'map_click'),
    (1, 5, None, None, 'min', 'ETsinceprev', 'last', 'fqid', 'tunic', 'last', 'fqid', 'tocloset_dirty'),
    (1, 5, None, None, 'min', 'room_coor_x', 'first', 'event_name', 'cutscene_click', 'last', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'min', 'room_coor_x', 'first', 'event_name', 'observation_click', 'last', 'room_fqid', 'tunic_capitol_0_hall'),
    (1, 5, None, None, 'min', 'room_coor_x', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'fqid', 'janitor'),
    (1, 5, None, None, 'min', 'room_coor_x', 'first', 'text_fqid', 'tunic_historicalsociety_stacks_outtolunch', 'last', 'event_name', 'map_click'),
    (1, 5, None, None, 'min', 'room_coor_x', 'last', 'event_name', 'map_click', 'first', 'fqid', 'what_happened'),
    (1, 5, None, None, 'min', 'room_coor_x', 'last', 'fqid', 'toentry', 'last', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'min', 'room_coor_x', 'last', 'name', 'undefined', 'last', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'min', 'room_coor_x', 'last', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'fqid', 'what_happened'),
    (1, 5, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tunic_hub_slip', 'last', 'fqid', 'toentry'),
    (1, 5, None, None, 'min', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'NaN', 'last', 'fqid', 'boss'),
    (1, 5, None, None, 'std', 'ETsinceprev', 'first', 'event_name', 'map_hover', 'last', 'fqid', 'tocollection'),
    (1, 5, None, None, 'std', 'ETsinceprev', 'first', 'fqid', 'tostacks', 'last', 'fqid', 'janitor'),
    (1, 5, None, None, 'std', 'hover_duration', 'first', 'name', 'basic', 'first', 'event_name', 'object_hover'),
    (1, 5, None, None, 'std', 'index', 'first', 'name', 'basic', 'first', 'event_name', 'object_hover'),
    (1, 5, None, None, 'std', 'room_coor_x', 'last', 'event_name', 'map_click', 'last', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'std', 'room_coor_y', 'first', 'event_name', 'map_hover', 'last', 'fqid', 'tunic_hub_slip'),
    (1, 5, None, None, 'std', 'room_coor_y', 'last', 'fqid', 'tocollection', 'first', 'event_name', 'object_hover'),
    (1, 5, None, None, 'std', 'room_coor_y', 'last', 'room_fqid', 'tunic_kohlcenter_halloffame', 'last', 'fqid', 'tostacks'),
    (1, 5, None, None, 'std', 'room_coor_y', 'last', 'text_fqid', 'tunic_capitol_0_hall_boss_talktogramps', 'last', 'fqid', 'outtolunch'),
    (1, 5, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'name', 'basic', 'first', 'room_fqid', 'tunic_historicalsociety_basement'),
    (1, 5, None, None, 'std', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_capitol_0_hall', 'last', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'fqid', 'tunic_historicalsociety', 'first', 'fqid', 'janitor'),
    (1, 5, None, None, 'std', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'tunic_capitol_0', 'last', 'room_fqid', 'tunic_historicalsociety_collection'),
    (1, 5, None, None, 'sum', 'ETsinceprev', 'last', 'fqid', 'tunic_capitol_0', 'first', 'fqid', 'tunic_hub_slip'),
    (1, 5, None, None, 'sum', 'hover_duration', 'first', 'event_name', 'map_click', 'last', 'room_fqid', 'tunic_kohlcenter_halloffame'),
    (1, 5, None, None, 'sum', 'room_coor_x', 'first', 'fqid', 'NaN', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 5, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'tostacks', 'last', 'room_fqid', 'tunic_historicalsociety_stacks'),
    (1, 5, None, None, 'sum', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_what_happened'),
    (1, 6, None, None, 'max', 'ETsinceprev', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_helpclean', 'first', 'fqid', 'tunic_historicalsociety'),
    (1, 6, None, None, 'max', 'hover_duration', 'first', 'room_fqid', 'tunic_capitol_1_hall', 'first', 'fqid', 'tunic_historicalsociety'),
    (1, 6, None, None, 'max', 'index', 'first', 'event_name', 'map_click', 'last', 'fqid', 'tocloset_dirty'),
    (1, 6, None, None, 'max', 'room_coor_x', 'last', 'event_name', 'observation_click', 'last', 'event_name', 'navigate_click'),
    (1, 6, None, None, 'max', 'room_coor_y', 'first', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'last', 'fqid', 'magnify'),
    (1, 6, None, None, 'max', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_door_block_talk', 'last', 'event_name', 'object_click'),
    (1, 6, None, None, 'max', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'text_fqid', 'NaN'),
    (1, 6, None, None, 'mean', 'hover_duration', 'first', 'event_name', 'map_hover', 'first', 'text_fqid', 'tunic_capitol_1_hall_boss_haveyougotit'),
    (1, 6, None, None, 'mean', 'hover_duration', 'first', 'text_fqid', 'NaN', 'last', 'name', 'close'),
    (1, 6, None, None, 'mean', 'room_coor_y', 'last', 'room_fqid', 'tunic_historicalsociety_basement', 'last', 'event_name', 'observation_click'),
    (1, 6, None, None, 'mean', 'room_coor_y', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_door_block_talk', 'last', 'fqid', 'tobasement'),
    (1, 6, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'event_name', 'cutscene_click', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news'),
    (1, 6, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_archivist', 'first', 'event_name', 'notebook_click'),
    (1, 6, None, None, 'mean', 'screen_coor_y_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_coffee', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_scarf'),
    (1, 6, None, None, 'min', 'room_coor_x', 'first', 'fqid', 'tobasement', 'last', 'fqid', 'tocloset_dirty'),
    (1, 6, None, None, 'min', 'room_coor_x', 'last', 'event_name', 'object_hover', 'last', 'fqid', 'toentry'),
    (1, 6, None, None, 'std', 'ETsinceprev', 'last', 'fqid', 'photo', 'last', 'fqid', 'tomap'),
    (1, 6, None, None, 'std', 'ETsinceprev', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_door_block_clean', 'last', 'text_fqid', 'tunic_historicalsociety_frontdesk_block_magnify'),
    (1, 6, None, None, 'std', 'index', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo', 'last', 'fqid', 'tunic_historicalsociety'),
    (1, 6, None, None, 'std', 'room_coor_y', 'first', 'fqid', 'photo', 'first', 'fqid', 'tunic_historicalsociety'),
    (1, 6, None, None, 'sum', 'hover_duration', 'first', 'event_name', 'map_hover', 'first', 'fqid', 'tunic_historicalsociety'),
    (1, 6, None, None, 'sum', 'hover_duration', 'last', 'text_fqid', 'tunic_capitol_1_hall_boss_haveyougotit', 'last', 'fqid', 'tunic_historicalsociety'),
    (1, 6, None, None, 'sum', 'index', 'first', 'name', 'close', 'last', 'fqid', 'trigger_scarf'),
    (1, 6, None, None, 'sum', 'room_coor_x', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'text_fqid', 'NaN'),
    (1, 6, None, None, 'sum', 'room_coor_y', 'first', 'name', 'close', 'first', 'fqid', 'trigger_scarf'),
    (1, 6, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo', 'last', 'fqid', 'magnify'),
    (1, 6, None, None, 'sum', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'cutscene_click', 'last', 'fqid', 'magnify'),
    (1, 7, None, None, 'max', 'ETsinceprev', 'first', 'fqid', 'businesscards_card_bingo_next', 'first', 'name', 'close'),
    (1, 7, None, None, 'max', 'ETsinceprev', 'first', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'last', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass_recap'),
    (1, 7, None, None, 'max', 'hover_duration', 'first', 'fqid', 'businesscards', 'first', 'event_name', 'notification_click'),
    (1, 7, None, None, 'max', 'hover_duration', 'first', 'name', 'open', 'first', 'event_name', 'observation_click'),
    (1, 7, None, None, 'max', 'hover_duration', 'first', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'last', 'event_name', 'object_hover'),
    (1, 7, None, None, 'max', 'hover_duration', 'last', 'fqid', 'worker', 'last', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'max', 'room_coor_x', 'first', 'fqid', 'businesscards', 'first', 'fqid', 'businesscards_card_0_next'),
    (1, 7, None, None, 'max', 'room_coor_y', 'first', 'name', 'basic', 'first', 'fqid', 'tostacks'),
    (1, 7, None, None, 'max', 'room_coor_y', 'first', 'name', 'basic', 'last', 'event_name', 'person_click'),
    (1, 7, None, None, 'max', 'room_coor_y', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'fqid', 'businesscards_card_0_next'),
    (1, 7, None, None, 'max', 'room_coor_y', 'last', 'event_name', 'object_hover', 'last', 'fqid', 'businesscards'),
    (1, 7, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'toentry', 'last', 'text_fqid', 'NaN'),
    (1, 7, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'tostacks', 'first', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'max', 'room_coor_y', 'last', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'event_name', 'object_hover'),
    (1, 7, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'toentry', 'first', 'name', 'close'),
    (1, 7, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_stacks', 'first', 'fqid', 'tomap'),
    (1, 7, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'room_fqid', 'tunic_humanecology_frontdesk'),
    (1, 7, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'map_click', 'first', 'fqid', 'worker'),
    (1, 7, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'tocollection', 'last', 'event_name', 'object_click'),
    (1, 7, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'name', 'undefined', 'last', 'event_name', 'notification_click'),
    (1, 7, None, None, 'mean', 'ETsinceprev', 'first', 'fqid', 'businesscards_card_bingo_next', 'last', 'fqid', 'businesscards'),
    (1, 7, None, None, 'mean', 'hover_duration', 'first', 'event_name', 'person_click', 'last', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'mean', 'hover_duration', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'mean', 'index', 'last', 'fqid', 'businesscards_card_bingo_bingo', 'last', 'event_name', 'object_hover'),
    (1, 7, None, None, 'mean', 'room_coor_x', 'last', 'fqid', 'tostacks', 'first', 'fqid', 'tomap'),
    (1, 7, None, None, 'mean', 'room_coor_y', 'last', 'fqid', 'archivist', 'first', 'room_fqid', 'tunic_historicalsociety_closet_dirty'),
    (1, 7, None, None, 'mean', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'businesscards_card_0_next', 'last', 'text_fqid', 'tunic_humanecology_frontdesk_businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'first', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'mean', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'last', 'event_name', 'map_click'),
    (1, 7, None, None, 'min', 'room_coor_y', 'first', 'event_name', 'person_click', 'first', 'room_fqid', 'tunic_historicalsociety_closet_dirty'),
    (1, 7, None, None, 'min', 'room_coor_y', 'last', 'fqid', 'businesscards_card_bingo_next', 'last', 'event_name', 'object_click'),
    (1, 7, None, None, 'min', 'room_coor_y', 'last', 'fqid', 'toentry', 'first', 'fqid', 'tomap'),
    (1, 7, None, None, 'min', 'room_coor_y', 'last', 'fqid', 'toentry', 'last', 'event_name', 'map_click'),
    (1, 7, None, None, 'min', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'businesscards', 'last', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'std', 'hover_duration', 'first', 'fqid', 'NaN', 'last', 'text_fqid', 'tunic_humanecology_frontdesk_businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'std', 'hover_duration', 'first', 'fqid', 'tostacks', 'first', 'event_name', 'notification_click'),
    (1, 7, None, None, 'std', 'hover_duration', 'first', 'name', 'basic', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'std', 'hover_duration', 'last', 'fqid', 'janitor', 'last', 'event_name', 'notification_click'),
    (1, 7, None, None, 'std', 'room_coor_y', 'first', 'event_name', 'navigate_click', 'last', 'fqid', 'tunic_humanecology'),
    (1, 7, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'name', 'undefined', 'last', 'fqid', 'NaN'),
    (1, 7, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'name', 'basic'),
    (1, 7, None, None, 'std', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'NaN', 'last', 'fqid', 'NaN'),
    (1, 7, None, None, 'std', 'screen_coor_x_abs_diff1', 'last', 'event_name', 'navigate_click', 'first', 'fqid', 'businesscards_card_1_next'),
    (1, 7, None, None, 'std', 'screen_coor_y_abs_diff1', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'event_name', 'notification_click'),
    (1, 7, None, None, 'std', 'screen_coor_y_abs_diff1', 'last', 'fqid', 'archivist', 'last', 'fqid', 'tocloset_dirty'),
    (1, 7, None, None, 'sum', 'ETsinceprev', 'last', 'room_fqid', 'tunic_historicalsociety_collection', 'last', 'event_name', 'person_click'),
    (1, 7, None, None, 'sum', 'hover_duration', 'first', 'event_name', 'map_hover', 'last', 'fqid', 'NaN'),
    (1, 7, None, None, 'sum', 'hover_duration', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'last', 'event_name', 'notification_click'),
    (1, 7, None, None, 'sum', 'hover_duration', 'last', 'event_name', 'person_click', 'first', 'event_name', 'notification_click'),
    (1, 7, None, None, 'sum', 'hover_duration', 'last', 'fqid', 'worker', 'first', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'sum', 'hover_duration', 'last', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'first', 'event_name', 'notification_click'),
    (1, 7, None, None, 'sum', 'room_coor_x', 'first', 'fqid', 'gramps', 'last', 'event_name', 'map_click'),
    (1, 7, None, None, 'sum', 'room_coor_x', 'last', 'fqid', 'tunic_humanecology', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_worker_intro'),
    (1, 7, None, None, 'sum', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_historicalsociety_entry', 'last', 'text_fqid', 'NaN'),
    (1, 8, None, None, 'max', 'room_coor_x', 'first', 'fqid', 'tohallway', 'first', 'fqid', 'logbook_page_bingo'),
    (1, 8, None, None, 'max', 'room_coor_x', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub', 'last', 'name', 'undefined'),
    (1, 8, None, None, 'max', 'room_coor_y', 'first', 'fqid', 'logbook_page_bingo', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_logbook_page_bingo'),
    (1, 8, None, None, 'max', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_drycleaner_frontdesk', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub'),
    (1, 8, None, None, 'max', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub', 'first', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_takealook'),
    (1, 8, None, None, 'mean', 'room_coor_x', 'first', 'event_name', 'object_click', 'last', 'event_name', 'object_click'),
    (1, 8, None, None, 'mean', 'room_coor_x', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub', 'last', 'room_fqid', 'tunic_drycleaner_frontdesk'),
    (1, 8, None, None, 'min', 'screen_coor_x_abs_diff1', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_hub', 'first', 'text_fqid', 'tunic_drycleaner_frontdesk_logbook_page_bingo'),
    (1, 8, None, None, 'std', 'room_coor_x', 'last', 'event_name', 'map_click', 'last', 'event_name', 'object_click'),
    (1, 8, None, None, 'sum', 'hover_duration', 'first', 'fqid', 'NaN', 'last', 'name', 'close'),
    (1, 8, None, None, 'sum', 'room_coor_x', 'first', 'fqid', 'logbook', 'last', 'fqid', 'logbook_page_bingo'),
    (1, 8, None, None, 'sum', 'room_coor_x', 'first', 'fqid', 'tohallway', 'first', 'name', 'basic'),
    (1, 8, None, None, 'sum', 'room_coor_y', 'first', 'fqid', 'logbook', 'last', 'text_fqid', 'NaN'),
    (1, 8, None, None, 'sum', 'room_coor_y', 'first', 'text_fqid', 'NaN', 'first', 'name', 'basic'),
    (1, 8, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'fqid', 'tunic_drycleaner', 'first', 'event_name', 'object_click'),
    (1, 8, None, None, 'sum', 'screen_coor_x_abs_diff1', 'last', 'room_fqid', 'tunic_humanecology_frontdesk', 'last', 'event_name', 'person_click'),
    (1, 9, None, None, 'max', 'ETsinceprev', 'first', 'fqid', 'tunic_drycleaner', 'first', 'event_name', 'object_hover'),
    (1, 9, None, None, 'max', 'hover_duration', 'first', 'event_name', 'object_click', 'first', 'event_name', 'notification_click'),
    (1, 9, None, None, 'max', 'hover_duration', 'first', 'fqid', 'tunic_library', 'last', 'fqid', 'reader_paper2_bingo'),
    (1, 9, None, None, 'max', 'hover_duration', 'first', 'text_fqid', 'NaN', 'first', 'room_fqid', 'tunic_library_frontdesk'),
    (1, 9, None, None, 'max', 'hover_duration', 'last', 'room_fqid', 'tunic_drycleaner_frontdesk', 'last', 'fqid', 'NaN'),
    (1, 9, None, None, 'max', 'hover_duration', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_done', 'last', 'fqid', 'NaN'),
    (1, 9, None, None, 'max', 'index', 'first', 'fqid', 'logbook', 'last', 'room_fqid', 'tunic_drycleaner_frontdesk'),
    (1, 9, None, None, 'max', 'index', 'last', 'fqid', 'logbook', 'last', 'event_name', 'object_hover'),
    (1, 9, None, None, 'max', 'index', 'last', 'fqid', 'logbook', 'last', 'fqid', 'toentry'),
    (1, 9, None, None, 'max', 'room_coor_x', 'first', 'fqid', 'tunic_drycleaner', 'last', 'fqid', 'reader_paper2_prev'),
    (1, 9, None, None, 'max', 'room_coor_y', 'last', 'fqid', 'tunic_library', 'last', 'fqid', 'reader_paper1_prev'),
    (1, 9, None, None, 'max', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_library_microfiche_reader_paper2_bingo', 'last', 'event_name', 'object_hover'),
    (1, 9, None, None, 'max', 'screen_coor_x_abs_diff1', 'last', 'fqid', 'tomicrofiche', 'first', 'event_name', 'object_hover'),
    (1, 9, None, None, 'mean', 'hover_duration', 'first', 'room_fqid', 'tunic_drycleaner_frontdesk', 'last', 'fqid', 'tunic_library'),
    (1, 9, None, None, 'mean', 'room_coor_x', 'first', 'event_name', 'map_hover', 'last', 'fqid', 'reader'),
    (1, 9, None, None, 'min', 'ETsinceprev', 'first', 'name', 'undefined', 'last', 'fqid', 'reader_paper0_next'),
    (1, 9, None, None, 'min', 'room_coor_x', 'first', 'fqid', 'tomicrofiche', 'last', 'name', 'close'),
    (1, 9, None, None, 'min', 'screen_coor_y_abs_diff1', 'last', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_done', 'last', 'room_fqid', 'tunic_drycleaner_frontdesk'),
    (1, 9, None, None, 'std', 'hover_duration', 'first', 'event_name', 'notebook_click', 'first', 'event_name', 'map_click'),
    (1, 9, None, None, 'std', 'hover_duration', 'first', 'fqid', 'tomicrofiche', 'last', 'fqid', 'reader_paper2_bingo'),
    (1, 9, None, None, 'std', 'hover_duration', 'first', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_done', 'first', 'text_fqid', 'tunic_library_microfiche_reader_paper2_bingo'),
    (1, 9, None, None, 'std', 'room_coor_x', 'last', 'fqid', 'tunic_library', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_hello'),
    (1, 9, None, None, 'sum', 'index', 'first', 'room_fqid', 'tunic_drycleaner_frontdesk', 'first', 'fqid', 'NaN'),
    (1, 9, None, None, 'sum', 'room_coor_x', 'first', 'fqid', 'reader_paper0_next', 'last', 'name', 'basic'),
    (1, 9, None, None, 'sum', 'room_coor_y', 'last', 'fqid', 'reader_paper1_next', 'last', 'event_name', 'object_click'),
    (1, 9, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'event_name', 'map_hover', 'last', 'text_fqid', 'tunic_library_microfiche_reader_paper2_bingo'),
    (1, 9, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_done', 'last', 'event_name', 'object_click'),
    (1, 9, None, None, 'sum', 'screen_coor_y_abs_diff1', 'last', 'event_name', 'notification_click', 'last', 'event_name', 'object_click'),
    (2, 13, None, None, 'mean', 'room_coor_x', 'last', 'name', 'close', 'first', 'room_fqid', 'tunic_historicalsociety_basement'),
    (2, 15, None, None, 'sum', 'room_coor_x', 'first', 'name', 'undefined', 'last', 'fqid', 'tostacks'),
    (2, 18, None, None, 'mean', 'ETsinceprev', 'last', 'fqid', 'expert', 'first', 'event_name', 'notification_click'),
    (2, 18, None, None, 'sum', 'index', 'first', 'event_name', 'person_click', 'last', 'fqid', 'tocage'),
    (2, 18, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'event_name', 'cutscene_click', 'last', 'room_fqid', 'tunic_historicalsociety_cage'),
    (2, 19, None, None, 'max', 'room_coor_x', 'first', 'fqid', 'expert', 'first', 'event_name', 'object_click'),
    (2, 19, None, None, 'sum', 'screen_coor_y_abs_diff1', 'last', 'text_fqid', 'tunic_wildlife_center_expert_recap', 'first', 'event_name', 'object_click'),
    (2, 20, None, None, 'max', 'screen_coor_y_abs_diff1', 'last', 'text_fqid', 'tunic_flaghouse_entry_flag_girl_symbol_recap', 'first', 'fqid', 'reader_flag'),
    (2, 21, None, None, 'mean', 'hover_duration', 'first', 'fqid', 'tunic_kohlcenter', 'last', 'fqid', 'journals_flag_pic_2_bingo'),
    (2, 21, None, None, 'mean', 'screen_coor_x_abs_diff1', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_glasses_confrontation_recap', 'last', 'event_name', 'notebook_click'),
    (2, 21, None, None, 'min', 'room_coor_x', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_glasses_confrontation_recap', 'last', 'event_name', 'object_click'),
    (2, 21, None, None, 'min', 'room_coor_x', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_nelson_recap', 'last', 'fqid', 'NaN'),
    (2, 22, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'name', 'close', 'last', 'fqid', 'tobasement'),
])

# time/count between an event and a subsequent event.
FEATURE_DEFS_TRIGGER2_SUBSEQUENT_TO_TRIGGER1 = [
    (0, 0, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'basic'),
    (0, 0, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'retirement_letter', 'first', 'event_name', 'observation_click'),
    (0, 0, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'retirement_letter', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'last', 'fqid', 'retirement_letter'),
    (0, 0, None, None, 'diff', 'index', 'first', 'text_fqid', 'tunic_historicalsociety_closet_notebook', 'last', 'text_fqid', 'NaN'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'name', 'basic'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'room_fqid', 'tunic_historicalsociety_basement'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'room_fqid', 'tunic_historicalsociety_closet'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notification_click', 'first', 'event_name', 'notebook_click'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notification_click', 'first', 'fqid', 'directory'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notification_click', 'first', 'name', 'open'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'event_name', 'cutscene_click'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'basic'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'open'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'undefined'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'groupconvo', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'report', 'first', 'text_fqid', 'tunic_historicalsociety_entry_groupconvo'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'basic', 'first', 'text_fqid', 'tunic_historicalsociety_basement_janitor'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'first', 'name', 'close'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'first', 'name', 'open'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'name', 'basic'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'name', 'undefined'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'room_fqid', 'tunic_historicalsociety_basement'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'room_fqid', 'tunic_historicalsociety_closet'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'first', 'event_name', 'notebook_click'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'first', 'fqid', 'wells'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_entry', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_basement_janitor', 'first', 'fqid', 'NaN'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'first', 'name', 'open'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_entry_groupconvo', 'first', 'event_name', 'notebook_click'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_entry_groupconvo', 'first', 'name', 'open'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_entry_groupconvo', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'toentry', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 1, None, None, 'diff', 'elapsed_time', 'last', 'name', 'close', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 1, None, None, 'diff', 'index', 'first', 'name', 'close', 'last', 'fqid', 'NaN'),
    (0, 2, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'name', 'undefined'),
    (0, 2, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_closet', 'first', 'name', 'close'),
    (0, 2, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub', 'first', 'text_fqid', 'NaN'),
    (0, 2, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_collection_tunic', 'first', 'name', 'close'),
    (0, 2, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'object_hover', 'last', 'text_fqid', 'NaN'),
    (0, 2, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'tunic_hub_slip', 'last', 'event_name', 'object_click'),
    (0, 2, None, None, 'diff', 'index', 'first', 'event_name', 'object_click', 'first', 'fqid', 'tunic_hub_slip'),
    (0, 2, None, None, 'diff', 'index', 'first', 'event_name', 'object_click', 'first', 'name', 'close'),
    (0, 2, None, None, 'diff', 'index', 'first', 'fqid', 'cs', 'last', 'event_name', 'object_hover'),
    (0, 2, None, None, 'diff', 'index', 'first', 'room_fqid', 'tunic_historicalsociety_collection', 'last', 'fqid', 'tunic_hub_slip'),
    (0, 2, None, None, 'diff', 'index', 'last', 'event_name', 'cutscene_click', 'last', 'text_fqid', 'tunic_historicalsociety_collection_tunic_slip'),
    (0, 2, None, None, 'diff', 'index', 'last', 'fqid', 'cs', 'last', 'event_name', 'object_hover'),
    (0, 2, None, None, 'diff', 'index', 'last', 'text_fqid', 'tunic_historicalsociety_collection_cs', 'first', 'fqid', 'tunic_hub_slip'),
    (0, 2, None, None, 'diff', 'index', 'last', 'text_fqid', 'tunic_historicalsociety_collection_cs', 'last', 'text_fqid', 'tunic_historicalsociety_collection_tunic_slip'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_click', 'first', 'fqid', 'NaN'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'first', 'name', 'open'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'navigate_click', 'first', 'text_fqid', 'tunic_historicalsociety_basement_janitor'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notification_click', 'first', 'text_fqid', 'tunic_historicalsociety_closet_retirement_letter_hub'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notification_click', 'first', 'text_fqid', 'tunic_kohlcenter_halloffame_plaque_face_date'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'fqid', 'plaque'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'last', 'room_fqid', 'tunic_historicalsociety_entry'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_kohlcenter_halloffame', 'first', 'name', 'open'),
    (0, 3, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'notebook_click', 'last', 'event_name', 'navigate_click'),
    (0, 3, None, None, 'diff', 'index', 'first', 'event_name', 'object_hover', 'first', 'fqid', 'plaque_face_date'),
    (0, 3, None, None, 'diff', 'index', 'first', 'event_name', 'object_hover', 'first', 'name', 'undefined'),
    (0, 3, None, None, 'diff', 'index', 'first', 'fqid', 'toentry', 'first', 'name', 'close'),
    (0, 3, None, None, 'diff', 'index', 'first', 'name', 'open', 'first', 'name', 'undefined'),
    (0, 3, None, None, 'diff', 'index', 'last', 'event_name', 'person_click', 'first', 'fqid', 'tomap'),
    (0, 4, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_kohlcenter_halloffame', 'first', 'text_fqid', 'tunic_capitol_0_hall_chap1_finale_c'),
    (0, 4, None, None, 'diff', 'index', 'first', 'fqid', 'toentry', 'last', 'fqid', 'tunic_capitol_0'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'last', 'name', 'basic'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'navigate_click', 'first', 'fqid', 'tunic_kohlcenter'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'navigate_click', 'last', 'fqid', 'tunic_capitol_0'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'fqid', 'NaN'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'text_fqid', 'NaN'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'janitor', 'first', 'fqid', 'janitor'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'janitor', 'first', 'name', 'basic'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'janitor', 'first', 'text_fqid', 'tunic_historicalsociety_basement_janitor'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'toentry', 'first', 'fqid', 'tunic_capitol_0'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'toentry', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_capitol_0', 'last', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_kohlcenter', 'first', 'event_name', 'cutscene_click'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_kohlcenter', 'first', 'fqid', 'NaN'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_kohlcenter', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_what_happened'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'event_name', 'notebook_click'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_capitol_0_hall', 'first', 'fqid', 'tunic_capitol_0'),
    (1, 5, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'tunic_capitol_0', 'first', 'fqid', 'what_happened'),
    (1, 5, None, None, 'diff', 'index', 'first', 'event_name', 'navigate_click', 'first', 'fqid', 'tunic_capitol_0'),
    (1, 5, None, None, 'diff', 'index', 'first', 'fqid', 'tunic_historicalsociety', 'last', 'name', 'basic'),
    (1, 5, None, None, 'diff', 'index', 'first', 'name', 'undefined', 'first', 'fqid', 'tunic_capitol_0'),
    (1, 5, None, None, 'diff', 'index', 'first', 'room_fqid', 'tunic_historicalsociety_basement', 'last', 'name', 'basic'),
    (1, 5, None, None, 'diff', 'index', 'last', 'fqid', 'NaN', 'last', 'event_name', 'map_click'),
    (1, 5, None, None, 'diff', 'index', 'last', 'fqid', 'tunic_capitol_0', 'last', 'event_name', 'cutscene_click'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'cutscene_click', 'first', 'name', 'open'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'archivist', 'first', 'event_name', 'map_click'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'next'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tobasement', 'last', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tostacks', 'first', 'fqid', 'magnify'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_hub_slip', 'first', 'fqid', 'block_magnify'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'name', 'undefined', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_basement', 'last', 'fqid', 'tostacks'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass', 'first', 'name', 'basic'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass', 'first', 'room_fqid', 'tunic_historicalsociety_frontdesk'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_hello', 'first', 'event_name', 'object_hover'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_need_glass_0', 'first', 'fqid', 'toentry'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'observation_click', 'first', 'event_name', 'person_click'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'observation_click', 'first', 'fqid', 'archivist'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'NaN', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_hello'),
    (1, 6, None, None, 'diff', 'elapsed_time', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_trigger_scarf', 'last', 'fqid', 'trigger_coffee'),
    (1, 6, None, None, 'diff', 'index', 'first', 'name', 'open', 'first', 'name', 'basic'),
    (1, 6, None, None, 'diff', 'index', 'first', 'name', 'open', 'last', 'fqid', 'tofrontdesk'),
    (1, 6, None, None, 'diff', 'index', 'last', 'fqid', 'trigger_scarf', 'first', 'name', 'basic'),
    (1, 6, None, None, 'diff', 'index', 'last', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_news', 'first', 'event_name', 'navigate_click'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'first', 'fqid', 'worker'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'first', 'name', 'close'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'last', 'fqid', 'worker'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'last', 'name', 'undefined'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'event_name', 'navigate_click'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'name', 'close'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'object_click', 'last', 'fqid', 'businesscards_card_0_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'person_click', 'last', 'fqid', 'toentry'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'businesscards', 'last', 'fqid', 'businesscards_card_0_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'businesscards_card_0_next', 'first', 'event_name', 'object_hover'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'businesscards_card_0_next', 'first', 'fqid', 'businesscards_card_1_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'businesscards_card_bingo_next', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'event_name', 'map_hover'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'gramps', 'first', 'event_name', 'observation_click'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_capitol_1', 'first', 'event_name', 'map_click'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_capitol_1', 'first', 'event_name', 'object_click'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'name', 'basic', 'first', 'fqid', 'tunic_capitol_1'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'name', 'basic', 'first', 'fqid', 'worker'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_humanecology_frontdesk', 'first', 'fqid', 'worker'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_humanecology_frontdesk', 'first', 'name', 'basic'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_gramps_nothing', 'first', 'fqid', 'janitor'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass_recap', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_worker_intro'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass_recap', 'last', 'fqid', 'toentry'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'map_hover', 'first', 'text_fqid', 'NaN'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'fqid', 'businesscards_card_0_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'businesscards_card_1_next', 'last', 'text_fqid', 'tunic_humanecology_frontdesk_businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'tomap', 'first', 'event_name', 'person_click'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'tunic_capitol_1', 'first', 'name', 'basic'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'tunic_capitol_1', 'last', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'name', 'open', 'first', 'name', 'close'),
    (1, 7, None, None, 'diff', 'elapsed_time', 'last', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_have_glass_recap', 'last', 'text_fqid', 'tunic_humanecology_frontdesk_worker_intro'),
    (1, 7, None, None, 'diff', 'index', 'first', 'event_name', 'map_click', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'index', 'first', 'event_name', 'map_click', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_worker_intro'),
    (1, 7, None, None, 'diff', 'index', 'first', 'event_name', 'map_hover', 'last', 'event_name', 'notification_click'),
    (1, 7, None, None, 'diff', 'index', 'first', 'event_name', 'object_hover', 'last', 'text_fqid', 'tunic_humanecology_frontdesk_businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'diff', 'index', 'first', 'fqid', 'businesscards', 'first', 'event_name', 'object_hover'),
    (1, 7, None, None, 'diff', 'index', 'first', 'fqid', 'businesscards_card_0_next', 'first', 'name', 'basic'),
    (1, 7, None, None, 'diff', 'index', 'first', 'fqid', 'businesscards_card_1_next', 'first', 'event_name', 'notification_click'),
    (1, 7, None, None, 'diff', 'index', 'first', 'fqid', 'businesscards_card_1_next', 'last', 'fqid', 'businesscards_card_bingo_bingo'),
    (1, 7, None, None, 'diff', 'index', 'first', 'fqid', 'businesscards_card_bingo_bingo', 'last', 'event_name', 'notification_click'),
    (1, 7, None, None, 'diff', 'index', 'first', 'fqid', 'tomap', 'last', 'event_name', 'map_click'),
    (1, 7, None, None, 'diff', 'index', 'first', 'name', 'close', 'first', 'event_name', 'person_click'),
    (1, 7, None, None, 'diff', 'index', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_worker_intro', 'first', 'fqid', 'NaN'),
    (1, 7, None, None, 'diff', 'index', 'last', 'event_name', 'map_click', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'index', 'last', 'event_name', 'map_hover', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'index', 'last', 'event_name', 'navigate_click', 'first', 'event_name', 'object_hover'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'event_name', 'object_hover'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'fqid', 'businesscards_card_0_next'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'businesscards_card_1_next', 'first', 'name', 'close'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'businesscards_card_1_next', 'last', 'text_fqid', 'NaN'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tomap', 'first', 'fqid', 'businesscards'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tomap', 'last', 'event_name', 'person_click'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tomap', 'last', 'fqid', 'worker'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tunic_capitol_1', 'last', 'fqid', 'worker'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tunic_humanecology', 'first', 'event_name', 'object_hover'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tunic_humanecology', 'first', 'event_name', 'person_click'),
    (1, 7, None, None, 'diff', 'index', 'last', 'fqid', 'tunic_humanecology', 'first', 'name', 'basic'),
    (1, 7, None, None, 'diff', 'index', 'last', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'first', 'fqid', 'businesscards_card_bingo_next'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'logbook_page_bingo', 'first', 'name', 'basic'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'worker', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_worker_badger'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'first', 'event_name', 'notification_click'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'first', 'fqid', 'logbook_page_bingo'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'last', 'event_name', 'notification_click'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_drycleaner_frontdesk', 'first', 'name', 'undefined'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_humanecology_frontdesk_worker_badger', 'first', 'room_fqid', 'tunic_humanecology_frontdesk'),
    (1, 8, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'map_hover', 'first', 'room_fqid', 'tunic_humanecology_frontdesk'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_click', 'first', 'room_fqid', 'tunic_library_frontdesk'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'object_click', 'first', 'name', 'basic'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'reader_paper0_next', 'first', 'fqid', 'reader_paper2_next'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tunic_library', 'first', 'event_name', 'person_click'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'first', 'text_fqid', 'tunic_drycleaner_frontdesk_worker_done'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'name', 'undefined', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_hello'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_frontdesk', 'last', 'event_name', 'person_click'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_microfiche', 'first', 'event_name', 'notebook_click'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'last', 'event_name', 'map_click', 'first', 'event_name', 'person_click'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'reader_paper0_next', 'last', 'fqid', 'NaN'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'last', 'room_fqid', 'tunic_drycleaner_frontdesk', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_hello'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'last', 'room_fqid', 'tunic_library_frontdesk', 'first', 'room_fqid', 'tunic_library_microfiche'),
    (1, 9, None, None, 'diff', 'elapsed_time', 'last', 'room_fqid', 'tunic_library_frontdesk', 'last', 'fqid', 'reader_paper0_prev'),
    (1, 9, None, None, 'diff', 'index', 'first', 'event_name', 'notification_click', 'last', 'fqid', 'reader'),
    (1, 9, None, None, 'diff', 'index', 'last', 'event_name', 'map_hover', 'first', 'name', 'basic'),
    (1, 9, None, None, 'diff', 'index', 'last', 'event_name', 'notification_click', 'last', 'event_name', 'object_hover'),
    (1, 9, None, None, 'diff', 'index', 'last', 'fqid', 'NaN', 'last', 'fqid', 'reader'),
    (1, 9, None, None, 'diff', 'index', 'last', 'fqid', 'reader_paper1_next', 'first', 'fqid', 'reader'),
    (1, 9, None, None, 'diff', 'index', 'last', 'room_fqid', 'tunic_drycleaner_frontdesk', 'last', 'text_fqid', 'tunic_library_frontdesk_worker_hello'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'cutscene_click', 'first', 'event_name', 'person_click'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'cutscene_click', 'first', 'fqid', 'worker'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'notebook_click', 'first', 'event_name', 'navigate_click'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'object_click', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_wells'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'person_click', 'last', 'fqid', 'worker'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'reader_paper0_prev', 'first', 'fqid', 'reader'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_frontdesk', 'last', 'room_fqid', 'tunic_library_frontdesk'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_microfiche', 'last', 'event_name', 'notebook_click'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'NaN', 'first', 'room_fqid', 'tunic_library_microfiche'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_library_frontdesk_block_badge', 'first', 'event_name', 'person_click'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_wells', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_wells'),
    (1, 10, None, None, 'diff', 'elapsed_time', 'last', 'name', 'undefined', 'first', 'event_name', 'person_click'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'businesscards_card_bingo_next', 'first', 'event_name', 'map_click'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'businesscards_card_bingo_next', 'first', 'fqid', 'tunic_drycleaner'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'event_name', 'map_hover'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'journals_pic_1_next', 'first', 'text_fqid', 'NaN'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'journals_pic_2_bingo', 'first', 'fqid', 'journals_pic_0_next'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'name', 'next', 'first', 'event_name', 'map_hover'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'name', 'next', 'first', 'fqid', 'journals_pic_2_bingo'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'name', 'next', 'first', 'fqid', 'tunic_library'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'name', 'next', 'first', 'name', 'close'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'name', 'close'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_capitol_1_hall', 'last', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_drycleaner_frontdesk', 'first', 'fqid', 'worker'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'first', 'room_fqid', 'tunic_historicalsociety_frontdesk'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_frontdesk', 'first', 'fqid', 'toentry'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_frontdesk', 'first', 'room_fqid', 'tunic_historicalsociety_closet_dirty'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_newspaper', 'first', 'name', 'basic'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_library_frontdesk_worker_wells_recap', 'first', 'text_fqid', 'tunic_historicalsociety_basement_janitor'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'journals_pic_0_next', 'first', 'fqid', 'journals_pic_1_next'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'last', 'fqid', 'journals_pic_0_next', 'last', 'event_name', 'object_hover'),
    (1, 11, None, None, 'diff', 'elapsed_time', 'last', 'name', 'open', 'first', 'event_name', 'notebook_click'),
    (1, 11, None, None, 'diff', 'index', 'first', 'event_name', 'map_click', 'first', 'name', 'basic'),
    (1, 11, None, None, 'diff', 'index', 'first', 'event_name', 'person_click', 'last', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 11, None, None, 'diff', 'index', 'first', 'fqid', 'NaN', 'first', 'name', 'undefined'),
    (1, 11, None, None, 'diff', 'index', 'first', 'fqid', 'journals_pic_1_next', 'first', 'fqid', 'journals'),
    (1, 11, None, None, 'diff', 'index', 'first', 'fqid', 'journals_pic_2_bingo', 'last', 'text_fqid', 'tunic_historicalsociety_stacks_journals_pic_2_bingo'),
    (1, 11, None, None, 'diff', 'index', 'first', 'name', 'undefined', 'last', 'fqid', 'tunic_humanecology'),
    (1, 11, None, None, 'diff', 'index', 'first', 'text_fqid', 'NaN', 'first', 'fqid', 'tunic_capitol_1'),
    (1, 11, None, None, 'diff', 'index', 'last', 'event_name', 'navigate_click', 'last', 'fqid', 'journals_hub_topics'),
    (1, 11, None, None, 'diff', 'index', 'last', 'fqid', 'journals_pic_0_next', 'last', 'room_fqid', 'tunic_historicalsociety_stacks'),
    (1, 11, None, None, 'diff', 'index', 'last', 'fqid', 'journals_pic_1_next', 'first', 'event_name', 'notification_click'),
    (1, 11, None, None, 'diff', 'index', 'last', 'room_fqid', 'tunic_historicalsociety_frontdesk', 'first', 'fqid', 'journals_pic_0_next'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'object_click', 'first', 'name', 'close'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'object_click', 'first', 'name', 'undefined'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'janitor', 'first', 'room_fqid', 'tunic_historicalsociety_entry'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'journals_hub_topics', 'first', 'fqid', 'tunic_capitol_1'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'name', 'basic', 'first', 'text_fqid', 'NaN'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'fqid', 'NaN'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'name', 'close'),
    (1, 12, None, None, 'diff', 'elapsed_time', 'first', 'name', 'undefined', 'first', 'text_fqid', 'tunic_historicalsociety_closet_dirty_photo'),
    (1, 12, None, None, 'diff', 'index', 'first', 'name', 'undefined', 'first', 'name', 'undefined'),
    (1, 12, None, None, 'diff', 'index', 'first', 'room_fqid', 'tunic_historicalsociety_stacks', 'first', 'name', 'undefined'),
    (2, 15, None, None, 'diff', 'elapsed_time', 'first', 'name', 'open', 'first', 'event_name', 'map_hover'),
    (2, 18, None, None, 'diff', 'elapsed_time', 'first', 'text_fqid', 'tunic_wildlife_center_crane_ranger_crane', 'first', 'name', 'close'),
    (2, 19, None, None, 'diff', 'elapsed_time', 'first', 'name', 'basic', 'first', 'text_fqid', 'tunic_wildlife_center_expert_recap'),
    (2, 20, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'first', 'event_name', 'notification_click'),
    (2, 20, None, None, 'diff', 'elapsed_time', 'first', 'event_name', 'map_hover', 'first', 'fqid', 'reader_flag_paper2_bingo'),
    (2, 20, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'tomap', 'first', 'event_name', 'object_hover'),
    (2, 21, None, None, 'diff', 'elapsed_time', 'first', 'name', 'close', 'first', 'text_fqid', 'tunic_historicalsociety_frontdesk_archivist_glasses_confrontation_recap'),
]

def get_features_info_container():
    # defaultdict() => defaultdict never raises a KeyError.
    # behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key, then defaultdict will automatically create the key and generate a default value for it.

    
    c = defaultdict(
            lambda: defaultdict( # level_group
            lambda: defaultdict( # level
            lambda: defaultdict( # groupby_type/filter_type
            lambda: defaultdict( # groupby_value/filter_value
            lambda: defaultdict( # col
            lambda: defaultdict( # trigger_start (groupby_type, groupby_value, method, hist_name)
            lambda: defaultdict( # trigger_end (groupby_type, groupby_value, method, hist_name)
            lambda: {
                'count': 0,      # method_agg
            }
    ))))))))
    
    return c

def process_type1_features(agg_defs, history_info, features_info):
    # agg_defs[0] => (0, None, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None)
    
    for level_group, level, filter_type, filter_value, method_agg, col, trigger_start_method0, trigger_start_t0, trigger_start_c0, trigger_end_method1, trigger_end_t1, trigger_end_c1 in agg_defs:

        trigger_start_info = None
        trigger_end_info = None

        if trigger_start_method0 is not None:

            assert trigger_start_method0 in ['first', 'last']
            assert trigger_end_method1 in ['first', 'last']

            trigger_col = 'index'
            if method_agg == 'diff':
                trigger_col = col

            trigger_start_key = history_info[level_group][level][trigger_start_t0][trigger_start_c0][trigger_col][None][None][trigger_start_method0]
            trigger_start_key['count'] += 1
            trigger_start_info = (trigger_start_t0, trigger_start_c0, trigger_start_method0, trigger_col, None)

            trigger_end_key = history_info[level_group][level][trigger_end_t1][trigger_end_c1][trigger_col][None][None][trigger_end_method1]
            trigger_end_key['count'] += 1
            trigger_end_info = (trigger_end_t1, trigger_end_c1, trigger_end_method1, trigger_col, None)

        if method_agg != 'diff':
            hist_key = history_info[level_group][level][filter_type][filter_value][col][trigger_start_info][trigger_end_info][method_agg]
            hist_key['count'] += 1
        
        # features_info[0][None]['None']['None']['ETsinceprev'][None][None]['max']
        feature_key = features_info[level_group][level][filter_type][filter_value][col][trigger_start_info][trigger_end_info][method_agg]
        feature_key['count'] += 1
        
        
def process_type2_features_trigger2_subsuquent_to_trigger_1(agg_defs, history_info, features_info):

    for level_group, level, filter_type, filter_value, method_agg, col, trigger_start_method0, trigger_start_t0, trigger_start_c0, trigger_end_method1, trigger_end_t1, trigger_end_c1 in agg_defs: 

        trigger_start_info = None
        trigger_end_info = None

        if trigger_start_method0 is not None:

            assert trigger_start_method0 in ['first', 'last']
            assert trigger_end_method1 in ['first', 'last']

            trigger_col = 'index'
            if method_agg == 'diff':
                trigger_col = col

            trigger_start_key = history_info[level_group][level][trigger_start_t0][trigger_start_c0][trigger_col][None][None][trigger_start_method0]
            trigger_start_key['count'] += 1
            trigger_start_info = (trigger_start_t0, trigger_start_c0, trigger_start_method0, trigger_col, None)
            
            trigger_start_index_key = history_info[level_group][level][trigger_start_t0][trigger_start_c0]['index'][None][None][trigger_start_method0]
            trigger_start_index_key['count'] += 1
            trigger_start_index_info = (trigger_start_t0, trigger_start_c0, trigger_start_method0, 'index', None)

            trigger_end_key = history_info[level_group][level][trigger_end_t1][trigger_end_c1][trigger_col][trigger_start_index_info][None][trigger_end_method1]
            trigger_end_key['count'] += 1
            trigger_end_info = (trigger_end_t1, trigger_end_c1, trigger_end_method1, trigger_col, trigger_start_index_info)

        if method_agg != 'diff':
            hist_key = history_info[level_group][level][filter_type][filter_value][col][trigger_start_info][trigger_end_info][method_agg]
            hist_key['count'] += 1

        feature_key = features_info[level_group][level][filter_type][filter_value][col][trigger_start_info][trigger_end_info][method_agg]
        feature_key['count'] += 1
        
        

def get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, method):
    
    if trigger_start_info is None and trigger_end_info is None:
        name = f"LG{level_group}__L{level}__{groupby_type}__{groupby}__{col}__{method}"
        
    elif trigger_start_info is not None and trigger_end_info is not None:
        trigger_start_groupby_type, trigger_start_groupby, trigger_start_method, trigger_start_col, trigger_start_trigger_info = trigger_start_info
        trigger_end_groupby_type, trigger_end_groupby, trigger_end_method, trigger_end_col, trigger_end_trigger_info = trigger_end_info
        
        assert trigger_start_trigger_info is None
        subsequent_trigger_string = ""
        if trigger_end_trigger_info is not None:
            #assert trigger_end_trigger_info == (trigger_start_groupby_type, trigger_start_groupby, trigger_start_method, trigger_start_col, None)
            subsequent_trigger_string = "__subsequent"
        
        
        # name = f"LG{level_group}__L{level}__{method}__{col}"
        name = f"LG{level_group}__L{level}__{groupby_type}__{groupby}__{col}__{method}"
        name += f"__between__{trigger_start_method}__{trigger_start_groupby_type}__{trigger_start_groupby}__{trigger_start_col}"
        name += f"__and{subsequent_trigger_string}__{trigger_end_method}__{trigger_end_groupby_type}__{trigger_end_groupby}__{trigger_end_col}"
    elif trigger_start_info is not None and trigger_end_info is None:
        trigger_start_groupby_type, trigger_start_groupby, trigger_start_method, trigger_start_col, trigger_start_trigger_info = trigger_start_info
        
        # name = f"LG{level_group}__L{level}__{method}__{col}"
        name = f"LG{level_group}__L{level}__{groupby_type}__{groupby}__{col}__{method}"
        name += f"__after__{trigger_start_method}__{trigger_start_groupby_type}__{trigger_start_groupby}__{trigger_start_col}"
    else:
        raise NotImplementedError
    
    return name

def inner_generate_features_c_code(history_info, features_src, features_history_init_src, history_names, loop_src):
    
    remaining_history_info = get_features_info_container()
    added_history_names = []
    
    for lg_i, (level_group, level_group_info) in enumerate(history_info.items()):        
        
        if lg_i == 0:
            features_src.append(f"    if (lg == {level_group}){{{{\n")
            features_src.append(loop_src)

            features_history_init_src.append(f"    if (lg == {level_group}){{{{\n")
        else:
            features_src.append(f"    }}}} else if (lg == {level_group}){{{{\n")
            features_src.append(loop_src)

            features_history_init_src.append(f"    }}}} else if (lg == {level_group}){{{{\n")

        is_first_level_if = True
        for level_i, (level, level_info) in enumerate(level_group_info.items()):

            need_to_close_level_if = False
            if level != 'NONE' and level is not None:

                need_to_close_level_if = True
                
                if is_first_level_if:
                    features_src.append(f"            if (level[i] == {level}){{{{\n")
                    default_indent_src = '    '
                    is_first_level_if = False
                else:
                    features_src.append(f"            }}}} else if (level[i] == {level}){{{{\n")
            else:
                assert level_i == 0
                default_indent_src = ''

            for groupby_type, groupby_type_info in level_info.items():

                if groupby_type is not None:
                    gbt_var_src, gbt_lookup_src = groupby_src_lookup[groupby_type]
                else:
                    gbt_var_src = ""
                    gbt_lookup_src = ""

                for gb_i, (groupby, groupby_info) in enumerate(groupby_type_info.items()):

                    if gb_i == 0:
                        if_src = 'if'
                    else:
                        if_src = 'else if'
                        
                    if groupby is not None:
                        groupby_cleaned = groupby.replace(" ", "_").replace(".", "_").replace("!", "_exclamation_").replace("?", "_question_").replace("\\", "_").replace("'", "_").replace(",", "_")
                    else:
                        groupby_cleaned = ""
                        
                    index_col_src = value_src_lookup['index'][0]
                    index_col_src_inc_indexing = "".join(value_src_lookup['index'])
                    
                    indent_src = ' '*(len(default_indent_src))
                    
                    need_to_close_groupby_if = False
                    if groupby_type != 'NONE' and groupby_type is not None:
                        features_src.append(f"{default_indent_src}            {if_src} ({gbt_var_src}[i] == {{{gbt_lookup_src}.{groupby_cleaned}}}){{{{\n")
                        indent_src += '    '
                        need_to_close_groupby_if = True
                    
                    for col, trigger_start_info_dict in groupby_info.items():
                        
                        for trigger_start_info, trigger_end_info_dict in trigger_start_info_dict.items():
                            
                            trigger_start_indent = ""
                            need_to_close_trigger_start_if = False
                            if trigger_start_info is not None:
                                
                                trigger_start_groupby_type, trigger_start_groupby, trigger_start_method, trigger_start_col, trigger_start_trigger_info = trigger_start_info
                                trigger_name = get_var_name(level_group, level, trigger_start_groupby_type, trigger_start_groupby, trigger_start_col, trigger_start_trigger_info, None, trigger_start_method)
                                
                                if trigger_name not in history_names:
                                    remaining_history_info[level_group][level][groupby_type][groupby][col][trigger_start_info] = history_info[level_group][level][groupby_type][groupby][col][trigger_start_info]
                                    continue
                                
                                features_src.append(f"{indent_src}            if (x_index[i] > (history[{{HIST.{trigger_name}}}] + 0.5)){{{{\n")
                                trigger_start_indent = "    "
                                need_to_close_trigger_start_if = True
                            
                            for trigger_end_info, aggs_info in trigger_end_info_dict.items():
                                
                                trigger_end_indent = ""
                                need_to_close_trigger_end_if = False
                                if trigger_end_info is not None:
                                    
                                    trigger_end_groupby_type, trigger_end_groupby, trigger_end_method, trigger_end_col, trigger_end_trigger_info = trigger_end_info
                                    trigger_name = get_var_name(level_group, level, trigger_end_groupby_type, trigger_end_groupby, trigger_end_col, trigger_end_trigger_info, None, trigger_end_method)
                                    
                                    if trigger_name not in history_names:
                                        remaining_history_info[level_group][level][groupby_type][groupby][col][trigger_start_info][trigger_end_info] = (
                                            history_info[level_group][level][groupby_type][groupby][col][trigger_start_info][trigger_end_info]
                                        )
                                        continue
                                
                                    features_src.append(f"{indent_src}{trigger_start_indent}            if (x_index[i] < (history[{{HIST.{trigger_name}}}] - 0.5)){{{{\n")
                                    trigger_end_indent = "    "
                                    need_to_close_trigger_end_if = True
                        
                                aggs = list(aggs_info.keys())

                                v_src = value_src_lookup[col][0]
                                v_src_inc_indexing = "".join(value_src_lookup[col])
                                
                                indent = indent_src + trigger_start_indent + trigger_end_indent

                                requires_count = True
                                
                                #if any(x in aggs for x in ['count', 'sum', 'mean', 'std']):
                                #    requires_count = True
                                #else:
                                #    requires_count = False
                                
                                if any(x in aggs for x in ['sum', 'mean', 'std']):
                                    requires_sum = True
                                else:
                                    requires_sum = False
                                    
                                if any(x in aggs for x in ['std']):
                                    requires_squared_sum = True
                                else:
                                    requires_squared_sum = False
                                
                                conditions = []
                                
                                if requires_count:
                                    
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'count')
                                    
                                    features_src.append(f"{indent}            if (isnan({v_src_inc_indexing}) == false){{{{\n")
                                    features_src.append(f"{indent}                history[{{HIST.{name}}}] += 1;\n")
                                    features_src.append(f"{indent}            }}}}\n")
                                    added_history_names.append(name)

                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = 0;\n")
                                
                                if 'first' in aggs:
                                    
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'first')

                                    features_src.append(f"{indent}            if (isnan(history[{{HIST.{name}}}])){{{{\n")
                                    features_src.append(f"{indent}                history[{{HIST.{name}}}] = {v_src_inc_indexing};\n")
                                    features_src.append(f"{indent}            }}}}\n")
                                    added_history_names.append(name)

                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = NAN;\n")

                                if 'last' in aggs:
                                    
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'last')

                                    features_src.append(f"{indent}            history[{{HIST.{name}}}] = {v_src_inc_indexing};\n")
                                    added_history_names.append(name)

                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = NAN;\n")

                                if 'min' in aggs:
                                    
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'min')
                                    
                                    conditions = []
                                    conditions.append(f"(isnan({v_src_inc_indexing}) == false)")
                                    conditions.append(f"({v_src_inc_indexing} < history[{{HIST.{name}}}])")

                                    conditions_src = "" + " & ".join(conditions)

                                    features_src.append(f"{indent}            if ({conditions_src}){{{{\n")
                                    features_src.append(f"{indent}                history[{{HIST.{name}}}] = {v_src_inc_indexing};\n")
                                    
                                    features_src.append(f"{indent}            }}}}\n")

                                    added_history_names.append(name)
                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = INFINITY;\n")

                                if 'max' in aggs:

                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'max')

                                    conditions = []
                                    conditions.append(f"(isnan({v_src_inc_indexing}) == false)")
                                    conditions.append(f"({v_src_inc_indexing} > history[{{HIST.{name}}}])")

                                    conditions_src = "" + " & ".join(conditions)

                                    features_src.append(f"{indent}            if ({conditions_src}){{{{\n")
                                    features_src.append(f"{indent}                history[{{HIST.{name}}}] = {v_src_inc_indexing};\n")
                                    
                                    features_src.append(f"{indent}            }}}}\n")

                                    added_history_names.append(name)
                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = -INFINITY;\n")

                                if requires_sum:

                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'sum')

                                    conditions = []
                                    conditions.append(f"(isnan({v_src_inc_indexing}) == false)")

                                    conditions_src = "" + " & ".join(conditions)

                                    features_src.append(f"{indent}            if ({conditions_src}){{{{\n")
                                    features_src.append(f"{indent}                history[{{HIST.{name}}}] += {v_src_inc_indexing};\n")
                                    
                                    features_src.append(f"{indent}            }}}}\n")

                                    added_history_names.append(name)
                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = 0;\n")

                                if requires_squared_sum:
                                    
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'squared_sum')

                                    conditions = []
                                    conditions.append(f"(isnan({v_src_inc_indexing}) == false)")

                                    conditions_src = "" + " & ".join(conditions)

                                    features_src.append(f"{indent}            if ({conditions_src}){{{{\n")
                                    features_src.append(f"{indent}                history[{{HIST.{name}}}] += pow({v_src_inc_indexing}, 2);\n")
                                    features_src.append(f"{indent}            }}}}\n")
                                    
                                    added_history_names.append(name)
                                    features_history_init_src.append(f"        history[{{HIST.{name}}}] = 0;\n")
                                    
                                if need_to_close_trigger_end_if:
                                    features_src.append(f"{indent_src}{trigger_start_indent}            }}}}\n")
                                    
                            if need_to_close_trigger_start_if:
                                features_src.append(f"{indent_src}            }}}}\n")
                                
                    if need_to_close_groupby_if:
                        features_src.append(f"{default_indent_src}            }}}}\n")
            
        if need_to_close_level_if:    
            features_src.append(f"            }}}}\n")
        
        
        features_src.append(f"        }}}}\n")
         
    features_src.append(f"    }}}}\n")
    features_history_init_src.append(f"    }}}}\n")
    
    history_names.extend(added_history_names)
    
    return remaining_history_info

def inner_generate_feature_setting_c_code(features_info, features_src, features_features_names):
    
    for level_group, level_group_info in features_info.items():

        if level_group == 'LG0':
            features_src.append(f"    if (lg >= {level_group}){{{{\n")
        else:
            features_src.append(f"    if (lg >= {level_group}){{{{\n")

        for level, level_info in level_group_info.items():

            for groupby_type, groupby_type_info in level_info.items():

                if groupby_type is not None:
                    gbt_var_src, gbt_lookup_src = groupby_src_lookup[groupby_type]
                else:
                    gbt_var_src = ""
                    gbt_lookup_src = ""

                for gb_i, (groupby, groupby_info) in enumerate(groupby_type_info.items()):

                    if groupby is not None:
                        groupby_cleaned = groupby.replace(" ", "_").replace(".", "_").replace("!", "_exclamation_").replace("?", "_question_").replace("\\", "_").replace("'", "_").replace(",", "_")
                    else:
                        groupby_cleaned = ""
                        
                    for col, trigger_start_info_dict in groupby_info.items():
                        
                        for trigger_start_info, trigger_end_info_dict in trigger_start_info_dict.items():
                            
                            for trigger_end_info, aggs_info in trigger_end_info_dict.items():    

                                v_src = value_src_lookup[col]

                                aggs = list(aggs_info.keys())

                                count_name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'count')

                                if 'count' in aggs and aggs_info['count']['count'] != 0:

                                    features_src.append(f"        out[{{FN.{count_name}}}] = history[{{HIST.{count_name}}}];\n")
                                    features_features_names.append(f"{count_name}")

                                if 'min' in aggs and aggs_info['min']['count'] != 0:

                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'min')

                                    features_src.append(f"        if (history[{{HIST.{count_name}}}] == 0){{{{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = NAN;\n")
                                    features_src.append("        }} else {{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = ((history[{{HIST.{name}}}] == INFINITY) ? NAN : history[{{HIST.{name}}}]);\n")
                                    features_src.append("        }}\n")

                                    features_features_names.append(f"{name}")

                                if 'max' in aggs and aggs_info['max']['count'] != 0:

                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'max')
       
                                    features_src.append(f"        if (history[{{HIST.{count_name}}}] == 0){{{{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = NAN;\n")
                                    features_src.append("        }} else {{\n")
                                    features_src.append(f"            temp = ((history[{{HIST.{name}}}] == -INFINITY) ? NAN : history[{{HIST.{name}}}]);\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = temp;\n")
                                    features_src.append("        }}\n")

                                    features_features_names.append(f"{name}")

                                if 'sum' in aggs and aggs_info['sum']['count'] != 0:

                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'sum')

                                    features_src.append(f"        if (history[{{HIST.{count_name}}}] == 0){{{{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = NAN;\n")
                                    features_src.append("        }} else {{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = history[{{HIST.{name}}}];\n")
                                    features_src.append("        }}\n")

                                    features_features_names.append(f"{name}")

                                if 'mean' in aggs and aggs_info['mean']['count'] != 0:

                                    sum_name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'sum')
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'mean')

                                    features_src.append(f"        if (history[{{HIST.{count_name}}}] == 0){{{{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = NAN;\n")
                                    features_src.append("        }} else {{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = history[{{HIST.{sum_name}}}]/history[{{HIST.{count_name}}}];\n")
                                    features_src.append("        }}\n")

                                    features_features_names.append(f"{name}")

                                if 'std' in aggs and aggs_info['std']['count'] != 0:

                                    sum_name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'sum')
                                    squared_sum_name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'squared_sum')
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'std')

                                    features_src.append(f"        if (history[{{HIST.{count_name}}}] == 0){{{{\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = NAN;\n")
                                    features_src.append("        }} else {{\n")
                                    features_src.append(f"            temp_mean = history[{{HIST.{sum_name}}}]/history[{{HIST.{count_name}}}];\n")
                                    features_src.append(f"            out[{{FN.{name}}}] = sqrt((\n")
                                    features_src.append(f"                history[{{HIST.{squared_sum_name}}}] - pow(temp_mean, 2) * history[{{HIST.{count_name}}}]\n")
                                    features_src.append(f"            )/(history[{{HIST.{count_name}}}]-1));\n")
                                    features_src.append("        }}\n")

                                    features_features_names.append(f"{name}")

                                if 'diff' in aggs:
                                    
                                    name = get_var_name(level_group, level, groupby_type, groupby, col, trigger_start_info, trigger_end_info, 'diff')
                                    
                                    trigger_start_groupby_type, trigger_start_groupby, trigger_start_method, trigger_start_col, trigger_start_trigger_info = trigger_start_info
                                    trigger_end_groupby_type, trigger_end_groupby, trigger_end_method, trigger_end_col, trigger_end_trigger_info = trigger_end_info
                                    
                                    assert trigger_start_trigger_info is None
                                    
                                    start_name = get_var_name(level_group, level, trigger_start_groupby_type, trigger_start_groupby, trigger_start_col, trigger_start_trigger_info, None, trigger_start_method)
                                    end_name = get_var_name(level_group, level, trigger_end_groupby_type, trigger_end_groupby, trigger_end_col, trigger_end_trigger_info, None, trigger_end_method)
                                    
                                    features_src.append(f"            out[{{FN.{name}}}] = history[{{HIST.{end_name}}}] - history[{{HIST.{start_name}}}];\n")
                                    features_features_names.append(f"{name}")
                                           
        features_src.append(f"    }}}}\n")

        
def generate_features_c_code(history_info, features_info):
    features_src = [f"""
void fill_history(
    long lg,
    long* level,
    double* history,
    long* x_index,
    long* x_text_numerical,
    long* x_en,
    long* x_n,
    long* x_fqids,
    long* x_et,
    double* x_rc_x,
    double* x_rc_y,
    double* x_sc_x,
    double* x_sc_y,
    long* x_b,
    long* x_r,
    long* x_room_fqid_numerical,
    long* x_text_fqid_numerical,
    double* x_page,
    double* x_hover_duration,
    long n
){{{{

    init_history(lg, history);
    
    double screen_coor_y_abs_diff1;
    double screen_coor_x_abs_diff1;
    double et_since_prev;
    float temp;
    double temp_mean;
    
"""]

    loop_src = """
        for (int i=0; i < n; i++){{
        
            
            if ((i != 0) & (level[i] == level[i-1])){{
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            }} else {{
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }}
                
            
            if ((i != 0) & (level[i] == level[i-1])){{
                et_since_prev = x_et[i] - x_et[i-1];
            }} else {{
                et_since_prev = NAN;
            }}

            if (isnan(et_since_prev)){{
                et_since_prev = 0;
            }}
            if (et_since_prev < 0){{
                et_since_prev = 0;
            }}
            if (et_since_prev > 1e9){{
                et_since_prev = 1e9;
            }}
                
"""

    features_history_init_src = ["""
void init_history(int lg, double* history){{
"""]
    
    features_output_src = ["""
    
void add_features(int lg, float* out, double* history){{

    float temp;
    double temp_mean;

"""]

    features_features_names = []
    history_names = []

    remains_history_info = inner_generate_features_c_code(history_info, features_src, features_history_init_src, history_names, loop_src)    
    
    if len(remains_history_info) != 0:
        remains_history_info = inner_generate_features_c_code(remains_history_info, features_src, features_history_init_src, history_names, loop_src)
    assert len(remains_history_info) == 0

    #################################################

    inner_generate_feature_setting_c_code(features_info, features_output_src, features_features_names)

    features_src.append(f"}}}}\n")
    features_history_init_src.append(f"}}}}\n")
    features_output_src.append(f"}}}}\n")
    
    features_output_src.append("""
    
void add_features_batch(int lg, float* out, double* history, int num_rows){{

    for (int i = 0; i < num_rows; i++){{
        add_features(lg, out + ({NUM_FEATURES} * i), history);
    }}
}}
    """)
    
    features_src = "".join(features_src)
    features_history_init_src = "".join(features_history_init_src)
    features_output_src = "".join(features_output_src)

    return features_src, features_history_init_src, features_output_src, features_features_names, history_names

c_defs = f"""

int check_if_double_is_nan(double value);

void init_history(int lg, double* history);


void fill_history(
    long lg,
    long* level,
    double* history,
    long* x_index,
    long* x_text_numerical,
    long* x_en,
    long* x_n,
    long* x_fqids,
    long* x_et,
    double* x_rc_x,
    double* x_rc_y,
    double* x_sc_x,
    double* x_sc_y,
    long* x_b,
    long* x_r,
    long* x_room_fqid_numerical,
    long* x_text_fqid_numerical,
    double* x_page,
    double* x_hover_duration,
    long n
);

void add_features_batch(
    int lg,
    float* out,
    double* history,
    int num_rows
);

void add_features(
    long lg,
    float* out,
    double* history
);

"""

def get_code():
    
    features_info = get_features_info_container()
    history_info = get_features_info_container()
    
    # features_info = history_info => defaultdict(<function get_features_info_container.<locals>.<lambda> at 0x7f5b55453cb0>, {})
    
    # list(set(FEATURE_DEFS)) => [(1, 10, None, None, 'sum', 'screen_coor_x_abs_diff1', 'first', 'room_fqid', 'tunic_library_microfiche', 'first', 'fqid', 'wellsbadge'), (1, None, 'fqid', 'reader_paper0_prev', 'max', 'ETsinceprev', None, None, None, None, None, None), ...]
        
    # key => key specifies a "function of one argument" that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).
    
    # cmp_to_key() => transform an old-style comparison function to a key function. a comparison function is any callable that accepts two arguments, compares them, and returns a negative number for less-than, zero for equality, or a positive number for greater-than. a key function is a callable that accepts one argument and returns another value to be used as the sort key.
    feat_defs = sorted(list(set(FEATURE_DEFS)), key=cmp_to_key(str_int_None_compare)) # my_ [0:2]
    
    # feat_defs => [(0, None, 'NONE', 'NONE', 'max', 'ETsinceprev', None, None, None, None, None, None), (0, None, 'NONE', 'NONE', 'mean', 'page', None, None, None, None, None, None), ...]
    
    # list(set(FEATURE_DEFS_TRIGGER2_SUBSEQUENT_TO_TRIGGER1)) => [(0, 1, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'basic'), (1, 11, None, None, 'diff', 'elapsed_time', 'first', 'room_fqid', 'tunic_library_frontdesk', 'first', 'room_fqid', 'tunic_historicalsociety_closet_dirty'), ...]
    
    feat_defs_trigger2_subsequent_to_trigger1 = sorted(list(set(FEATURE_DEFS_TRIGGER2_SUBSEQUENT_TO_TRIGGER1)), key=cmp_to_key(str_int_None_compare))
    
    # feat_defs_trigger2_subsequent_to_trigger1 => [(0, 0, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'NaN', 'first', 'name', 'basic'), (0, 0, None, None, 'diff', 'elapsed_time', 'first', 'fqid', 'retirement_letter', 'first', 'event_name', 'observation_click'), ...]
    
    process_type1_features(feat_defs, history_info, features_info) # my_ 
    # features_info[0][None]['None']['None']['ETsinceprev'][None][None]['max']
    # json.dumps(features_info) => {"0": {"null": {"NONE": {"NONE": {"ETsinceprev": {"null": {"null": {"max": {"count": 1}}}}, 
    #                                                                "page":       {"null": {"null": {"mean": {"count": 1}}}}
    #                               }}}}} ...    

    process_type2_features_trigger2_subsuquent_to_trigger_1(feat_defs_trigger2_subsequent_to_trigger1, history_info, features_info) # my_    
    
    # json.dumps(features_info) => 
    # {"0": 
    #      {"0": 
    #           {"null": 
    #                {"null": 
    #                     {"elapsed_time": 
    #                          {('fqid', 'NaN', 'first', 'elapsed_time', None): 
    #                               {('name', 'basic', 'first', 'elapsed_time', ('fqid', 'NaN', 'first', 'index', None)): 
    #                                    {"diff": 
    #                                         {"count": 1}}}, 
    #                           ('fqid', 'retirement_letter', 'first', 'elapsed_time', None): 
    #                               {('event_name', 'observation_click', 'first', 'elapsed_time', ('fqid', 'retirement_letter', 'first', 'index', None)): 
    #                                    {"diff": 
    #                                         {"count": 1}}}}}}}}} ...
    

    (
        features_c_src,
        features_history_init_c_src,
        features_output_src,
        features_c_features_names,
        c_history_names,
        
    ) = generate_features_c_code(
        history_info, 
        features_info,
    )
    
    assert len(features_c_features_names) == len(set(features_c_features_names))
    assert len(c_history_names) == len(set(c_history_names))
    
    c_src = """
#include <math.h>

int check_if_double_is_nan(double value) {{
    return isnan(value);
}}

"""
    c_src += features_history_init_c_src
    c_src += "\n"
    c_src += features_c_src
    c_src += "\n"
    c_src += features_output_src
    
    return c_src, features_c_features_names, c_history_names

def compile_module(c_src, module_name='JoWilder_C_features', module_dir=None):
    
    ffi = FFI()
    # cdef method allows you to specify C declarations.
    # after defining the C function signature using ffi.cdef, you can use the C function in your Python code through the ffi object.
    ffi.cdef(c_defs)

    if module_dir is None:
        import pathlib
        module_dir = str(pathlib.Path(__file__).parent.resolve())

    # Note: '-ffast-math' causes nan to not work
    
    # .set_source() => by itself does not write any file, but merely records its arguments for later.
    # module_name is the name of the Python module to generate.
    # extra_compile_args and extra_link_args can be used to specify additional command line options for the respective compiler and linker command lines.
    # if your extension requires header files in the include directory under your distribution root, use the include_dirs option.
    ffi.set_source(
        module_name=module_name,
        source=c_src,
        extra_compile_args=['-O3', '-march=x86-64', '-frounding-math', '-fsignaling-nans', '-fno-var-tracking-assignments'], # '-mavx' '-march=native'
        include_dirs=[module_dir],
        source_extension='.cpp',  # the file generated will be actually called module_name + source_extension.
    )

    ffi.compile(verbose=False, tmpdir=module_dir)

