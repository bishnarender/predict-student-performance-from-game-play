#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import numba

# In[ ]:


#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_level_counts(level):
    
    counts = np.zeros(23, dtype=np.int32)
    n = level.shape[0]
    
    for i in range(n):
        slot_i = level[i]
        if slot_i < 23:
            counts[slot_i] += 1
               
    return counts

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_level_based_features(out, level):
    level_counts = generate_level_counts(level)
    
    out[:, 93] = np.argmax(level_counts)
    out[:, 94] = np.argmin(level_counts)
    
    
    # 644 => FN.level_0_event_count
    out[:, 644] = level_counts[0]    
        
    # 645 => FN.level_1_event_count
    out[:, 645] = level_counts[1]    
        
    # 646 => FN.level_2_event_count
    out[:, 646] = level_counts[2]    
        
    # 647 => FN.level_3_event_count
    out[:, 647] = level_counts[3]    
        
    # 648 => FN.level_4_event_count
    out[:, 648] = level_counts[4]    
        
    # 649 => FN.level_5_event_count
    out[:, 649] = level_counts[5]    
        
    # 650 => FN.level_6_event_count
    out[:, 650] = level_counts[6]    
        
    # 651 => FN.level_7_event_count
    out[:, 651] = level_counts[7]    
        
    # 652 => FN.level_8_event_count
    out[:, 652] = level_counts[8]    
        
    # 653 => FN.level_9_event_count
    out[:, 653] = level_counts[9]    
        
    # 654 => FN.level_10_event_count
    out[:, 654] = level_counts[10]    
        
    # 655 => FN.level_11_event_count
    out[:, 655] = level_counts[11]    
        
    # 656 => FN.level_12_event_count
    out[:, 656] = level_counts[12]    
        
    # 657 => FN.level_13_event_count
    out[:, 657] = level_counts[13]    
        
    # 658 => FN.level_14_event_count
    out[:, 658] = level_counts[14]    
        
    # 659 => FN.level_15_event_count
    out[:, 659] = level_counts[15]    
        
    # 660 => FN.level_16_event_count
    out[:, 660] = level_counts[16]    
        
    # 661 => FN.level_17_event_count
    out[:, 661] = level_counts[17]    
        
    # 662 => FN.level_18_event_count
    out[:, 662] = level_counts[18]    
        
    # 663 => FN.level_19_event_count
    out[:, 663] = level_counts[19]    
        
    # 664 => FN.level_20_event_count
    out[:, 664] = level_counts[20]    
        
    # 665 => FN.level_21_event_count
    out[:, 665] = level_counts[21]    
        
    # 666 => FN.level_22_event_count
    out[:, 666] = level_counts[22] 

