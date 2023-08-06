#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import numba


# In[ ]:


#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_fqid_first_last_counts_and_times(fqid, elapsed_time):
    
    # 129 => FQIDS.__len__
    first_occurrence_index = np.full(129, np.nan, dtype=np.float32)
    last_occurrence_index = np.full(129, np.nan, dtype=np.float32)
    first_occurrence_time = np.full(129, np.nan, dtype=np.float32)
    last_occurrence_time = np.full(129, np.nan, dtype=np.float32)
    n = fqid.shape[0]
    
    for i in range(n):
        slot_i = fqid[i]
        # 129 => FQIDS.__len__
        if slot_i < 129:
            last_occurrence_index[slot_i] = i
            last_occurrence_time[slot_i] = elapsed_time[i]

            if np.isnan(first_occurrence_index[slot_i]):
                first_occurrence_index[slot_i] = i
                first_occurrence_time[slot_i] = elapsed_time[i]
                
    # first_occurrence_index => [ 14.  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  60.  nan  nan  nan  nan  nan  nan 163. 164.  nan  nan  nan  nan  nan  nan  nan  72.  67.  nan  nan  nan  nan  nan  nan  nan  nan   1.  40.  nan   0.  36.  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  25. 107.  12. 143. 144.  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  50.  28.  nan  nan   6.  35.  nan 113.  nan  71.  nan  39.  nan 150.  nan 126.  nan 105.  nan  nan  nan  nan  81. 162.  nan  nan  nan  nan 127.  84.  nan 128.  nan  nan  nan  62.  nan  nan  nan]
    
    # last_occurrence_index => [158.  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  61.  nan  nan  nan  nan  nan  nan 163. 164.  nan  nan  nan  nan  nan  nan  nan  80.  68.  nan  nan  nan  nan  nan  nan  nan  nan  98.  59.  nan   0. 112.  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  27. 108.  13. 149. 148.  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  nan  51.  33.  nan  nan 120. 124.  nan 113.  nan  71.  nan 160.  nan 151.  nan 126.  nan 105.  nan  nan  nan  nan  88. 162.  nan  nan  nan  nan 127.  87.  nan 161.  nan  nan  nan  63.  nan  nan  nan]
    
    # first_occurrence_time =>  [ 14814.     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan  66460.     nan     nan     nan     nan     nan     nan 164023. 194860.     nan     nan     nan     nan     nan     nan     nan  77926.  71943.     nan     nan     nan     nan     nan     nan     nan     nan    831.  44196.     nan      0.  39845.     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan  22996. 108924.  12030. 144805.  147973.     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan  57277.  28113.     nan     nan   5197.  37445.     nan 117625.     nan   75711.     nan  43413.     nan 154971.     nan 133289.     nan 105775.     nan     nan     nan     nan  87213. 162438.     nan     nan     nan     nan 135124.  89383.     nan 135256.     nan     nan     nan  68627.     nan     nan     nan]
        
    # last_occurrence_time =>  [160023.     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan  68110.     nan     nan     nan     nan     nan     nan 164023. 194860.     nan     nan     nan     nan     nan     nan     nan  85893.  73927.     nan     nan     nan     nan     nan     nan     nan     nan 100713.  65459.     nan      0. 117142.     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan  25766. 109825.  13030. 154188. 153655.     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan     nan  58244.  36433.     nan     nan 126323. 128640.     nan 117625.     nan  75711.     nan 161405.     nan 155754.     nan 133289.     nan 105775.     nan     nan     nan     nan  93883. 162438.     nan     nan     nan     nan 135124.  92242.     nan 161822.     nan     nan     nan  69893.     nan     nan     nan]

    return first_occurrence_index, last_occurrence_index, first_occurrence_time, last_occurrence_time

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_fqid_based_features(out, fqid, elapsed_time):

    n = fqid.shape[0]
    
    start_elapsed_time = elapsed_time[0]
    end_elapsed_time = elapsed_time[-1]
    total_time = end_elapsed_time - start_elapsed_time

    (
        first_occurrence_index,
        last_occurrence_index,
        first_occurrence_time,
        last_occurrence_time,
    ) = generate_fqid_first_last_counts_and_times(fqid, elapsed_time)
    

    # 554 => FN.fqid_chap1_finale_first_occurrence_num_event_from_start
    out[:, 554] = first_occurrence_index[20]
    
    # 555 => FN.fqid_chap1_finale_last_occurrence_num_event_from_start
    out[:, 555] = last_occurrence_index[20]
    
    # 556 => FN.fqid_chap1_finale_first_occurrence_num_event_from_end
    out[:, 556] = n - first_occurrence_index[20]
    
    # 557 => FN.fqid_chap1_finale_last_occurrence_num_event_from_end
    out[:, 557] = n - last_occurrence_index[20]
    
    # 558 => FN.fqid_chap1_finale_first_occurrence_time
    out[:, 558] = first_occurrence_time[20]
    
    # 559 => FN.fqid_chap1_finale_last_occurrence_time
    out[:, 559] = last_occurrence_time[20]
    
    # 560 => FN.fqid_chap1_finale_first_occurrence_duration_from_start
    out[:, 560] = first_occurrence_time[20] - start_elapsed_time
    
    # 561 => FN.fqid_chap1_finale_last_occurrence_duration_from_start
    out[:, 561] = last_occurrence_time[20] - start_elapsed_time
    
    # 562 => FN.fqid_chap1_finale_first_occurrence_duration_from_end
    out[:, 562] = end_elapsed_time - first_occurrence_time[20]
    
    # 563 => FN.fqid_chap1_finale_last_occurrence_duration_from_end
    out[:, 563] = end_elapsed_time - last_occurrence_time[20] 
    
    
    
    # 564 => FN.fqid_directory_first_occurrence_num_event_from_start
    out[:, 564] = first_occurrence_index[30]
    
    # 565 => FN.fqid_directory_last_occurrence_num_event_from_start
    out[:, 565] = last_occurrence_index[30]
    
    # 566 => FN.fqid_directory_first_occurrence_num_event_from_end
    out[:, 566] = n - first_occurrence_index[30]
    
    # 567 => FN.fqid_directory_last_occurrence_num_event_from_end
    out[:, 567] = n - last_occurrence_index[30]
    
    # 568 => FN.fqid_directory_first_occurrence_time
    out[:, 568] = first_occurrence_time[30]
    
    # 569 => FN.fqid_directory_last_occurrence_time
    out[:, 569] = last_occurrence_time[30]
    
    # 570 => FN.fqid_directory_first_occurrence_duration_from_start
    out[:, 570] = first_occurrence_time[30] - start_elapsed_time
    
    # 571 => FN.fqid_directory_last_occurrence_duration_from_start
    out[:, 571] = last_occurrence_time[30] - start_elapsed_time
    
    # 572 => FN.fqid_directory_first_occurrence_duration_from_end
    out[:, 572] = end_elapsed_time - first_occurrence_time[30]
    
    # 573 => FN.fqid_directory_last_occurrence_duration_from_end
    out[:, 573] = end_elapsed_time - last_occurrence_time[30] 
    
    
    
    # 574 => FN.fqid_directory_closeup_archivist_first_occurrence_num_event_from_start
    out[:, 574] = first_occurrence_index[31]
    
    # 575 => FN.fqid_directory_closeup_archivist_last_occurrence_num_event_from_start
    out[:, 575] = last_occurrence_index[31]
    
    # 576 => FN.fqid_directory_closeup_archivist_first_occurrence_num_event_from_end
    out[:, 576] = n - first_occurrence_index[31]
    
    # 577 => FN.fqid_directory_closeup_archivist_last_occurrence_num_event_from_end
    out[:, 577] = n - last_occurrence_index[31]
    
    # 578 => FN.fqid_directory_closeup_archivist_first_occurrence_time
    out[:, 578] = first_occurrence_time[31]
    
    # 579 => FN.fqid_directory_closeup_archivist_last_occurrence_time
    out[:, 579] = last_occurrence_time[31]
    
    # 580 => FN.fqid_directory_closeup_archivist_first_occurrence_duration_from_start
    out[:, 580] = first_occurrence_time[31] - start_elapsed_time
    
    # 581 => FN.fqid_directory_closeup_archivist_last_occurrence_duration_from_start
    out[:, 581] = last_occurrence_time[31] - start_elapsed_time
    
    # 582 => FN.fqid_directory_closeup_archivist_first_occurrence_duration_from_end
    out[:, 582] = end_elapsed_time - first_occurrence_time[31]
    
    # 583 => FN.fqid_directory_closeup_archivist_last_occurrence_duration_from_end
    out[:, 583] = end_elapsed_time - last_occurrence_time[31] 
    
    
    
    # 584 => FN.fqid_gramps_first_occurrence_num_event_from_start
    out[:, 584] = first_occurrence_index[39]
    
    # 585 => FN.fqid_gramps_last_occurrence_num_event_from_start
    out[:, 585] = last_occurrence_index[39]
    
    # 586 => FN.fqid_gramps_first_occurrence_num_event_from_end
    out[:, 586] = n - first_occurrence_index[39]
    
    # 587 => FN.fqid_gramps_last_occurrence_num_event_from_end
    out[:, 587] = n - last_occurrence_index[39]
    
    # 588 => FN.fqid_gramps_first_occurrence_time
    out[:, 588] = first_occurrence_time[39]
    
    # 589 => FN.fqid_gramps_last_occurrence_time
    out[:, 589] = last_occurrence_time[39]
    
    # 590 => FN.fqid_gramps_first_occurrence_duration_from_start
    out[:, 590] = first_occurrence_time[39] - start_elapsed_time
    
    # 591 => FN.fqid_gramps_last_occurrence_duration_from_start
    out[:, 591] = last_occurrence_time[39] - start_elapsed_time
    
    # 592 => FN.fqid_gramps_first_occurrence_duration_from_end
    out[:, 592] = end_elapsed_time - first_occurrence_time[39]
    
    # 593 => FN.fqid_gramps_last_occurrence_duration_from_end
    out[:, 593] = end_elapsed_time - last_occurrence_time[39] 
    
    
    
    # 594 => FN.fqid_journals_first_occurrence_num_event_from_start
    out[:, 594] = first_occurrence_index[44]
    
    # 595 => FN.fqid_journals_last_occurrence_num_event_from_start
    out[:, 595] = last_occurrence_index[44]
    
    # 596 => FN.fqid_journals_first_occurrence_num_event_from_end
    out[:, 596] = n - first_occurrence_index[44]
    
    # 597 => FN.fqid_journals_last_occurrence_num_event_from_end
    out[:, 597] = n - last_occurrence_index[44]
    
    # 598 => FN.fqid_journals_first_occurrence_time
    out[:, 598] = first_occurrence_time[44]
    
    # 599 => FN.fqid_journals_last_occurrence_time
    out[:, 599] = last_occurrence_time[44]
    
    # 600 => FN.fqid_journals_first_occurrence_duration_from_start
    out[:, 600] = first_occurrence_time[44] - start_elapsed_time
    
    # 601 => FN.fqid_journals_last_occurrence_duration_from_start
    out[:, 601] = last_occurrence_time[44] - start_elapsed_time
    
    # 602 => FN.fqid_journals_first_occurrence_duration_from_end
    out[:, 602] = end_elapsed_time - first_occurrence_time[44]
    
    # 603 => FN.fqid_journals_last_occurrence_duration_from_end
    out[:, 603] = end_elapsed_time - last_occurrence_time[44] 
    
    
    
    # 604 => FN.fqid_journals_pic_0_next_first_occurrence_num_event_from_start
    out[:, 604] = first_occurrence_index[46]
    
    # 605 => FN.fqid_journals_pic_0_next_last_occurrence_num_event_from_start
    out[:, 605] = last_occurrence_index[46]
    
    # 606 => FN.fqid_journals_pic_0_next_first_occurrence_num_event_from_end
    out[:, 606] = n - first_occurrence_index[46]
    
    # 607 => FN.fqid_journals_pic_0_next_last_occurrence_num_event_from_end
    out[:, 607] = n - last_occurrence_index[46]
    
    # 608 => FN.fqid_journals_pic_0_next_first_occurrence_time
    out[:, 608] = first_occurrence_time[46]
    
    # 609 => FN.fqid_journals_pic_0_next_last_occurrence_time
    out[:, 609] = last_occurrence_time[46]
    
    # 610 => FN.fqid_journals_pic_0_next_first_occurrence_duration_from_start
    out[:, 610] = first_occurrence_time[46] - start_elapsed_time
    
    # 611 => FN.fqid_journals_pic_0_next_last_occurrence_duration_from_start
    out[:, 611] = last_occurrence_time[46] - start_elapsed_time
    
    # 612 => FN.fqid_journals_pic_0_next_first_occurrence_duration_from_end
    out[:, 612] = end_elapsed_time - first_occurrence_time[46]
    
    # 613 => FN.fqid_journals_pic_0_next_last_occurrence_duration_from_end
    out[:, 613] = end_elapsed_time - last_occurrence_time[46] 
    
    
    
    # 614 => FN.fqid_tocloset_dirty_first_occurrence_num_event_from_start
    out[:, 614] = first_occurrence_index[98]
    
    # 615 => FN.fqid_tocloset_dirty_last_occurrence_num_event_from_start
    out[:, 615] = last_occurrence_index[98]
    
    # 616 => FN.fqid_tocloset_dirty_first_occurrence_num_event_from_end
    out[:, 616] = n - first_occurrence_index[98]
    
    # 617 => FN.fqid_tocloset_dirty_last_occurrence_num_event_from_end
    out[:, 617] = n - last_occurrence_index[98]
    
    # 618 => FN.fqid_tocloset_dirty_first_occurrence_time
    out[:, 618] = first_occurrence_time[98]
    
    # 619 => FN.fqid_tocloset_dirty_last_occurrence_time
    out[:, 619] = last_occurrence_time[98]
    
    # 620 => FN.fqid_tocloset_dirty_first_occurrence_duration_from_start
    out[:, 620] = first_occurrence_time[98] - start_elapsed_time
    
    # 621 => FN.fqid_tocloset_dirty_last_occurrence_duration_from_start
    out[:, 621] = last_occurrence_time[98] - start_elapsed_time
    
    # 622 => FN.fqid_tocloset_dirty_first_occurrence_duration_from_end
    out[:, 622] = end_elapsed_time - first_occurrence_time[98]
    
    # 623 => FN.fqid_tocloset_dirty_last_occurrence_duration_from_end
    out[:, 623] = end_elapsed_time - last_occurrence_time[98] 
    
    
    
    # 624 => FN.fqid_tomap_first_occurrence_num_event_from_start
    out[:, 624] = first_occurrence_index[105]
    
    # 625 => FN.fqid_tomap_last_occurrence_num_event_from_start
    out[:, 625] = last_occurrence_index[105]
    
    # 626 => FN.fqid_tomap_first_occurrence_num_event_from_end
    out[:, 626] = n - first_occurrence_index[105]
    
    # 627 => FN.fqid_tomap_last_occurrence_num_event_from_end
    out[:, 627] = n - last_occurrence_index[105]
    
    # 628 => FN.fqid_tomap_first_occurrence_time
    out[:, 628] = first_occurrence_time[105]
    
    # 629 => FN.fqid_tomap_last_occurrence_time
    out[:, 629] = last_occurrence_time[105]
    
    # 630 => FN.fqid_tomap_first_occurrence_duration_from_start
    out[:, 630] = first_occurrence_time[105] - start_elapsed_time
    
    # 631 => FN.fqid_tomap_last_occurrence_duration_from_start
    out[:, 631] = last_occurrence_time[105] - start_elapsed_time
    
    # 632 => FN.fqid_tomap_first_occurrence_duration_from_end
    out[:, 632] = end_elapsed_time - first_occurrence_time[105]
    
    # 633 => FN.fqid_tomap_last_occurrence_duration_from_end
    out[:, 633] = end_elapsed_time - last_occurrence_time[105] 
    
    
    
    # 634 => FN.fqid_tomicrofiche_first_occurrence_num_event_from_start
    out[:, 634] = first_occurrence_index[106]
    
    # 635 => FN.fqid_tomicrofiche_last_occurrence_num_event_from_start
    out[:, 635] = last_occurrence_index[106]
    
    # 636 => FN.fqid_tomicrofiche_first_occurrence_num_event_from_end
    out[:, 636] = n - first_occurrence_index[106]
    
    # 637 => FN.fqid_tomicrofiche_last_occurrence_num_event_from_end
    out[:, 637] = n - last_occurrence_index[106]
    
    # 638 => FN.fqid_tomicrofiche_first_occurrence_time
    out[:, 638] = first_occurrence_time[106]
    
    # 639 => FN.fqid_tomicrofiche_last_occurrence_time
    out[:, 639] = last_occurrence_time[106]
    
    # 640 => FN.fqid_tomicrofiche_first_occurrence_duration_from_start
    out[:, 640] = first_occurrence_time[106] - start_elapsed_time
    
    # 641 => FN.fqid_tomicrofiche_last_occurrence_duration_from_start
    out[:, 641] = last_occurrence_time[106] - start_elapsed_time
    
    # 642 => FN.fqid_tomicrofiche_first_occurrence_duration_from_end
    out[:, 642] = end_elapsed_time - first_occurrence_time[106]
    
    # 643 => FN.fqid_tomicrofiche_last_occurrence_duration_from_end
    out[:, 643] = end_elapsed_time - last_occurrence_time[106] 
    

