#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import numba

# In[ ]:


#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_building_first_last_counts_and_times(buildings, elapsed_time):
    
    first_occurrence_index = np.full(10, np.nan, dtype=np.float32)
    last_occurrence_index = np.full(10, np.nan, dtype=np.float32)
    first_occurrence_time = np.full(10, np.nan, dtype=np.float32)
    last_occurrence_time = np.full(10, np.nan, dtype=np.float32)
    
    n = buildings.shape[0]
    
    for i in range(n):
        slot_i = buildings[i]
        if slot_i < 10:
            
            last_occurrence_index[slot_i] = i
            last_occurrence_time[slot_i] = elapsed_time[i]

            if np.isnan(first_occurrence_index[slot_i]):
                
                first_occurrence_index[slot_i] = i
                first_occurrence_time[slot_i] = elapsed_time[i]
    
    # first_occurrence_index => [163.  nan  nan  nan  nan   0.  nan 130.  nan  nan]
    # last_occurrence_index => [164.  nan  nan  nan  nan 129.  nan 162.  nan  nan]
    # first_occurrence_time => [164023.     nan     nan     nan     nan      0.     nan 137223.     nan     nan]
    # last_occurrence_time =>    [194860.     nan     nan     nan     nan 135990.     nan 162438.     nan     nan]

    return first_occurrence_index, last_occurrence_index, first_occurrence_time, last_occurrence_time


# In[ ]:


#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_building_based_features(out, building, elapsed_time):
    
    # n => number of building events in the same level group (per session).
    n = building.shape[0]
    
    start_elapsed_time = elapsed_time[0]
    end_elapsed_time = elapsed_time[-1]
    total_time = end_elapsed_time - start_elapsed_time

    (
        first_occurrence_index,
        last_occurrence_index,
        first_occurrence_time,
        last_occurrence_time,
    ) = generate_building_first_last_counts_and_times(building, elapsed_time)
    

    
    # 324 => FN.building_capitol_0_first_occurrence_num_event_from_start
    out[:, 324] = first_occurrence_index[0]
    
    # 325 => FN.building_capitol_0_last_occurrence_num_event_from_start
    out[:, 325] = last_occurrence_index[0]
    
    # 326 => FN.building_capitol_0_first_occurrence_num_event_from_end
    out[:, 326] = n - first_occurrence_index[0]
    
    # 327 => FN.building_capitol_0_last_occurrence_num_event_from_end
    out[:, 327] = n - last_occurrence_index[0]
    
    # 328 => FN.building_capitol_0_first_occurrence_time
    out[:, 328] = first_occurrence_time[0]
    
    # 329 => FN.building_capitol_0_last_occurrence_time
    out[:, 329] = last_occurrence_time[0]
    
    # 330 => FN.building_capitol_0_first_occurrence_duration_from_start
    out[:, 330] = first_occurrence_time[0] - start_elapsed_time
    
    # 331 => FN.building_capitol_0_last_occurrence_duration_from_start
    out[:, 331] = last_occurrence_time[0] - start_elapsed_time
    
    # 332 => FN.building_capitol_0_first_occurrence_duration_from_end
    out[:, 332] = end_elapsed_time - first_occurrence_time[0]
    
    # 333 => FN.building_capitol_0_last_occurrence_duration_from_end
    out[:, 333] = end_elapsed_time- last_occurrence_time[0]
    
    
    
    # 334 => FN.building_capitol_1_first_occurrence_num_event_from_start
    out[:, 334] = first_occurrence_index[1]
    
    # 335 => FN.building_capitol_1_last_occurrence_num_event_from_start
    out[:, 335] = last_occurrence_index[1]
    
    # 336 => FN.building_capitol_1_first_occurrence_num_event_from_end
    out[:, 336] = n - first_occurrence_index[1]
    
    # 337 => FN.building_capitol_1_last_occurrence_num_event_from_end
    out[:, 337] = n - last_occurrence_index[1]
    
    # 338 => FN.building_capitol_1_first_occurrence_time
    out[:, 338] = first_occurrence_time[1]
    
    # 339 => FN.building_capitol_1_last_occurrence_time
    out[:, 339] = last_occurrence_time[1]
    
    # 340 => FN.building_capitol_1_first_occurrence_duration_from_start
    out[:, 340] = first_occurrence_time[1] - start_elapsed_time
    
    # 341 => FN.building_capitol_1_last_occurrence_duration_from_start
    out[:, 341] = last_occurrence_time[1] - start_elapsed_time
    
    # 342 => FN.building_capitol_1_first_occurrence_duration_from_end
    out[:, 342] = end_elapsed_time - first_occurrence_time[1]
    
    # 343 => FN.building_capitol_1_last_occurrence_duration_from_end
    out[:, 343] = end_elapsed_time- last_occurrence_time[1]
    
    
    
    # 344 => FN.building_capitol_2_first_occurrence_num_event_from_start
    out[:, 344] = first_occurrence_index[2]
    
    # 345 => FN.building_capitol_2_last_occurrence_num_event_from_start
    out[:, 345] = last_occurrence_index[2]
    
    # 346 => FN.building_capitol_2_first_occurrence_num_event_from_end
    out[:, 346] = n - first_occurrence_index[2]
    
    # 347 => FN.building_capitol_2_last_occurrence_num_event_from_end
    out[:, 347] = n - last_occurrence_index[2]
    
    # 348 => FN.building_capitol_2_first_occurrence_time
    out[:, 348] = first_occurrence_time[2]
    
    # 349 => FN.building_capitol_2_last_occurrence_time
    out[:, 349] = last_occurrence_time[2]
    
    # 350 => FN.building_capitol_2_first_occurrence_duration_from_start
    out[:, 350] = first_occurrence_time[2] - start_elapsed_time
    
    # 351 => FN.building_capitol_2_last_occurrence_duration_from_start
    out[:, 351] = last_occurrence_time[2] - start_elapsed_time
    
    # 352 => FN.building_capitol_2_first_occurrence_duration_from_end
    out[:, 352] = end_elapsed_time - first_occurrence_time[2]
    
    # 353 => FN.building_capitol_2_last_occurrence_duration_from_end
    out[:, 353] = end_elapsed_time- last_occurrence_time[2]
    
    
    
    # 354 => FN.building_drycleaner_first_occurrence_num_event_from_start
    out[:, 354] = first_occurrence_index[3]
    
    # 355 => FN.building_drycleaner_last_occurrence_num_event_from_start
    out[:, 355] = last_occurrence_index[3]
    
    # 356 => FN.building_drycleaner_first_occurrence_num_event_from_end
    out[:, 356] = n - first_occurrence_index[3]
    
    # 357 => FN.building_drycleaner_last_occurrence_num_event_from_end
    out[:, 357] = n - last_occurrence_index[3]
    
    # 358 => FN.building_drycleaner_first_occurrence_time
    out[:, 358] = first_occurrence_time[3]
    
    # 359 => FN.building_drycleaner_last_occurrence_time
    out[:, 359] = last_occurrence_time[3]
    
    # 360 => FN.building_drycleaner_first_occurrence_duration_from_start
    out[:, 360] = first_occurrence_time[3] - start_elapsed_time
    
    # 361 => FN.building_drycleaner_last_occurrence_duration_from_start
    out[:, 361] = last_occurrence_time[3] - start_elapsed_time
    
    # 362 => FN.building_drycleaner_first_occurrence_duration_from_end
    out[:, 362] = end_elapsed_time - first_occurrence_time[3]
    
    # 363 => FN.building_drycleaner_last_occurrence_duration_from_end
    out[:, 363] = end_elapsed_time- last_occurrence_time[3]
    
    
    
    # 364 => FN.building_flaghouse_first_occurrence_num_event_from_start
    out[:, 364] = first_occurrence_index[4]
    
    # 365 => FN.building_flaghouse_last_occurrence_num_event_from_start
    out[:, 365] = last_occurrence_index[4]
    
    # 366 => FN.building_flaghouse_first_occurrence_num_event_from_end
    out[:, 366] = n - first_occurrence_index[4]
    
    # 367 => FN.building_flaghouse_last_occurrence_num_event_from_end
    out[:, 367] = n - last_occurrence_index[4]
    
    # 368 => FN.building_flaghouse_first_occurrence_time
    out[:, 368] = first_occurrence_time[4]
    
    # 369 => FN.building_flaghouse_last_occurrence_time
    out[:, 369] = last_occurrence_time[4]
    
    # 370 => FN.building_flaghouse_first_occurrence_duration_from_start
    out[:, 370] = first_occurrence_time[4] - start_elapsed_time
    
    # 371 => FN.building_flaghouse_last_occurrence_duration_from_start
    out[:, 371] = last_occurrence_time[4] - start_elapsed_time
    
    # 372 => FN.building_flaghouse_first_occurrence_duration_from_end
    out[:, 372] = end_elapsed_time - first_occurrence_time[4]
    
    # 373 => FN.building_flaghouse_last_occurrence_duration_from_end
    out[:, 373] = end_elapsed_time- last_occurrence_time[4]
    
    
    
    # 374 => FN.building_historicalsociety_first_occurrence_num_event_from_start
    out[:, 374] = first_occurrence_index[5]
    
    # 375 => FN.building_historicalsociety_last_occurrence_num_event_from_start
    out[:, 375] = last_occurrence_index[5]
    
    # 376 => FN.building_historicalsociety_first_occurrence_num_event_from_end
    out[:, 376] = n - first_occurrence_index[5]
    
    # 377 => FN.building_historicalsociety_last_occurrence_num_event_from_end
    out[:, 377] = n - last_occurrence_index[5]
    
    # 378 => FN.building_historicalsociety_first_occurrence_time
    out[:, 378] = first_occurrence_time[5]
    
    # 379 => FN.building_historicalsociety_last_occurrence_time
    out[:, 379] = last_occurrence_time[5]
    
    # 380 => FN.building_historicalsociety_first_occurrence_duration_from_start
    out[:, 380] = first_occurrence_time[5] - start_elapsed_time
    
    # 381 => FN.building_historicalsociety_last_occurrence_duration_from_start
    out[:, 381] = last_occurrence_time[5] - start_elapsed_time
    
    # 382 => FN.building_historicalsociety_first_occurrence_duration_from_end
    out[:, 382] = end_elapsed_time - first_occurrence_time[5]
    
    # 383 => FN.building_historicalsociety_last_occurrence_duration_from_end
    out[:, 383] = end_elapsed_time- last_occurrence_time[5]
    
    
    
    # 384 => FN.building_humanecology_first_occurrence_num_event_from_start
    out[:, 384] = first_occurrence_index[6]
    
    # 385 => FN.building_humanecology_last_occurrence_num_event_from_start
    out[:, 385] = last_occurrence_index[6]
    
    # 386 => FN.building_humanecology_first_occurrence_num_event_from_end
    out[:, 386] = n - first_occurrence_index[6]
    
    # 387 => FN.building_humanecology_last_occurrence_num_event_from_end
    out[:, 387] = n - last_occurrence_index[6]
    
    # 388 => FN.building_humanecology_first_occurrence_time
    out[:, 388] = first_occurrence_time[6]
    
    # 389 => FN.building_humanecology_last_occurrence_time
    out[:, 389] = last_occurrence_time[6]
    
    # 390 => FN.building_humanecology_first_occurrence_duration_from_start
    out[:, 390] = first_occurrence_time[6] - start_elapsed_time
    
    # 391 => FN.building_humanecology_last_occurrence_duration_from_start
    out[:, 391] = last_occurrence_time[6] - start_elapsed_time
    
    # 392 => FN.building_humanecology_first_occurrence_duration_from_end
    out[:, 392] = end_elapsed_time - first_occurrence_time[6]
    
    # 393 => FN.building_humanecology_last_occurrence_duration_from_end
    out[:, 393] = end_elapsed_time- last_occurrence_time[6]
    
    
    
    # 394 => FN.building_kohlcenter_first_occurrence_num_event_from_start
    out[:, 394] = first_occurrence_index[7]
    
    # 395 => FN.building_kohlcenter_last_occurrence_num_event_from_start
    out[:, 395] = last_occurrence_index[7]
    
    # 396 => FN.building_kohlcenter_first_occurrence_num_event_from_end
    out[:, 396] = n - first_occurrence_index[7]
    
    # 397 => FN.building_kohlcenter_last_occurrence_num_event_from_end
    out[:, 397] = n - last_occurrence_index[7]
    
    # 398 => FN.building_kohlcenter_first_occurrence_time
    out[:, 398] = first_occurrence_time[7]
    
    # 399 => FN.building_kohlcenter_last_occurrence_time
    out[:, 399] = last_occurrence_time[7]
    
    # 400 => FN.building_kohlcenter_first_occurrence_duration_from_start
    out[:, 400] = first_occurrence_time[7] - start_elapsed_time
    
    # 401 => FN.building_kohlcenter_last_occurrence_duration_from_start
    out[:, 401] = last_occurrence_time[7] - start_elapsed_time
    
    # 402 => FN.building_kohlcenter_first_occurrence_duration_from_end
    out[:, 402] = end_elapsed_time - first_occurrence_time[7]
    
    # 403 => FN.building_kohlcenter_last_occurrence_duration_from_end
    out[:, 403] = end_elapsed_time- last_occurrence_time[7]
    
    
    
    # 404 => FN.building_library_first_occurrence_num_event_from_start
    out[:, 404] = first_occurrence_index[8]
    
    # 405 => FN.building_library_last_occurrence_num_event_from_start
    out[:, 405] = last_occurrence_index[8]
    
    # 406 => FN.building_library_first_occurrence_num_event_from_end
    out[:, 406] = n - first_occurrence_index[8]
    # first_occurrence_index[8] is building "library" first occurrence position/number (from n) from start.
    # 8 is an index of a building named "library".
    
    # 407 => FN.building_library_last_occurrence_num_event_from_end
    out[:, 407] = n - last_occurrence_index[8]
    
    # 408 => FN.building_library_first_occurrence_time
    out[:, 408] = first_occurrence_time[8]
    
    # 409 => FN.building_library_last_occurrence_time
    out[:, 409] = last_occurrence_time[8]
    
    # 410 => FN.building_library_first_occurrence_duration_from_start
    out[:, 410] = first_occurrence_time[8] - start_elapsed_time
    
    # 411 => FN.building_library_last_occurrence_duration_from_start
    out[:, 411] = last_occurrence_time[8] - start_elapsed_time
    
    # 412 => FN.building_library_first_occurrence_duration_from_end
    out[:, 412] = end_elapsed_time - first_occurrence_time[8]
    
    # 413 => FN.building_library_last_occurrence_duration_from_end
    out[:, 413] = end_elapsed_time- last_occurrence_time[8]
    
    
    
    # 414 => FN.building_wildlife_first_occurrence_num_event_from_start
    out[:, 414] = first_occurrence_index[9]
    
    # 415 => FN.building_wildlife_last_occurrence_num_event_from_start
    out[:, 415] = last_occurrence_index[9]
    
    # 416 => FN.building_wildlife_first_occurrence_num_event_from_end
    out[:, 416] = n - first_occurrence_index[9]
    
    # 417 => FN.building_wildlife_last_occurrence_num_event_from_end
    out[:, 417] = n - last_occurrence_index[9]
    
    # 418 => FN.building_wildlife_first_occurrence_time
    out[:, 418] = first_occurrence_time[9]
    
    # 419 => FN.building_wildlife_last_occurrence_time
    out[:, 419] = last_occurrence_time[9]
    
    # 420 => FN.building_wildlife_first_occurrence_duration_from_start
    out[:, 420] = first_occurrence_time[9] - start_elapsed_time
    
    # 421 => FN.building_wildlife_last_occurrence_duration_from_start
    out[:, 421] = last_occurrence_time[9] - start_elapsed_time
    
    # 422 => FN.building_wildlife_first_occurrence_duration_from_end
    out[:, 422] = end_elapsed_time - first_occurrence_time[9]
    
    # 423 => FN.building_wildlife_last_occurrence_duration_from_end
    out[:, 423] = end_elapsed_time- last_occurrence_time[9]

