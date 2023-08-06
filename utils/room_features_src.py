#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import numba

# In[ ]:


#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_room_first_last_counts_and_times(room, elapsed_time):
    
    # 13 => ROOMS.__len__
    first_occurrence_index = np.full(13, np.nan, dtype=np.float32)    
    last_occurrence_index = np.full(13, np.nan, dtype=np.float32)
    first_occurrence_time = np.full(13, np.nan, dtype=np.float32)
    last_occurrence_time = np.full(13, np.nan, dtype=np.float32)
    n = room.shape[0]
    
    for i in range(n):
        slot_i = room[i]
        # 13 => ROOMS.__len__
        if slot_i < 13:
    
            last_occurrence_index[slot_i] = i
            last_occurrence_time[slot_i] = elapsed_time[i]

            if np.isnan(first_occurrence_index[slot_i]):
                first_occurrence_index[slot_i] = i
                first_occurrence_time[slot_i] = elapsed_time[i]
                
    # first_occurrence_index => [ 36.  nan  nan   0.  nan  72.  nan  40.  nan 163. 130.  nan 106.]
    # last_occurrence_index => [125.  nan  nan 124.  nan 101.  nan 129.  nan 164. 162.  nan 109.]
    # first_occurrence_time =>  [ 39845.     nan     nan      0.     nan  77926.     nan  44196.     nan  164023.  137223.     nan   108090.]
    # last_occurrence_time =>  [130863.     nan     nan 128640.     nan 102324.     nan 135990.     nan   194860.  162438.     nan 110975.]
 
    return first_occurrence_index, last_occurrence_index, first_occurrence_time, last_occurrence_time

#@numba.jit(nopython=True, nogil=True, error_model='numpy')
def generate_room_based_features(out, room, elapsed_time):

    n = room.shape[0]
    
    start_elapsed_time = elapsed_time[0]
    end_elapsed_time = elapsed_time[-1]
    total_time = end_elapsed_time - start_elapsed_time

    (
        first_occurrence_index,
        last_occurrence_index,
        first_occurrence_time,
        last_occurrence_time,
    ) = generate_room_first_last_counts_and_times(room, elapsed_time)
    
    
    # 424 => FN.room_basement_first_occurrence_num_event_from_start
    out[:, 424] = first_occurrence_index[0]
    
    # 425 => FN.room_basement_last_occurrence_num_event_from_start
    out[:, 425] = last_occurrence_index[0]
    
    # 426 => FN.room_basement_first_occurrence_num_event_from_end
    out[:, 426] = n - first_occurrence_index[0]
    
    # 427 => FN.room_basement_last_occurrence_num_event_from_end
    out[:, 427] = n - last_occurrence_index[0]
    
    # 428 => FN.room_basement_first_occurrence_time
    out[:, 428] = first_occurrence_time[0]
    
    # 429 => FN.room_basement_last_occurrence_time
    out[:, 429] = last_occurrence_time[0]
    
    # 430 => FN.room_basement_first_occurrence_duration_from_start
    out[:, 430] = first_occurrence_time[0] - start_elapsed_time
    
    # 431 => FN.room_basement_last_occurrence_duration_from_start
    out[:, 431] = last_occurrence_time[0] - start_elapsed_time
    
    # 432 => FN.room_basement_first_occurrence_duration_from_end
    out[:, 432] = end_elapsed_time - first_occurrence_time[0]
    
    # 433 => FN.room_basement_last_occurrence_duration_from_end
    out[:, 433] = end_elapsed_time- last_occurrence_time[0]
    

    
    
    # 434 => FN.room_cage_first_occurrence_num_event_from_start
    out[:, 434] = first_occurrence_index[1]
    
    # 435 => FN.room_cage_last_occurrence_num_event_from_start
    out[:, 435] = last_occurrence_index[1]
    
    # 436 => FN.room_cage_first_occurrence_num_event_from_end
    out[:, 436] = n - first_occurrence_index[1]
    
    # 437 => FN.room_cage_last_occurrence_num_event_from_end
    out[:, 437] = n - last_occurrence_index[1]
    
    # 438 => FN.room_cage_first_occurrence_time
    out[:, 438] = first_occurrence_time[1]
    
    # 439 => FN.room_cage_last_occurrence_time
    out[:, 439] = last_occurrence_time[1]
    
    # 440 => FN.room_cage_first_occurrence_duration_from_start
    out[:, 440] = first_occurrence_time[1] - start_elapsed_time
    
    # 441 => FN.room_cage_last_occurrence_duration_from_start
    out[:, 441] = last_occurrence_time[1] - start_elapsed_time
    
    # 442 => FN.room_cage_first_occurrence_duration_from_end
    out[:, 442] = end_elapsed_time - first_occurrence_time[1]
    
    # 443 => FN.room_cage_last_occurrence_duration_from_end
    out[:, 443] = end_elapsed_time- last_occurrence_time[1]
    

    
    
    # 444 => FN.room_center_first_occurrence_num_event_from_start
    out[:, 444] = first_occurrence_index[2]
    
    # 445 => FN.room_center_last_occurrence_num_event_from_start
    out[:, 445] = last_occurrence_index[2]
    
    # 446 => FN.room_center_first_occurrence_num_event_from_end
    out[:, 446] = n - first_occurrence_index[2]
    
    # 447 => FN.room_center_last_occurrence_num_event_from_end
    out[:, 447] = n - last_occurrence_index[2]
    
    # 448 => FN.room_center_first_occurrence_time
    out[:, 448] = first_occurrence_time[2]
    
    # 449 => FN.room_center_last_occurrence_time
    out[:, 449] = last_occurrence_time[2]
    
    # 450 => FN.room_center_first_occurrence_duration_from_start
    out[:, 450] = first_occurrence_time[2] - start_elapsed_time
    
    # 451 => FN.room_center_last_occurrence_duration_from_start
    out[:, 451] = last_occurrence_time[2] - start_elapsed_time
    
    # 452 => FN.room_center_first_occurrence_duration_from_end
    out[:, 452] = end_elapsed_time - first_occurrence_time[2]
    
    # 453 => FN.room_center_last_occurrence_duration_from_end
    out[:, 453] = end_elapsed_time- last_occurrence_time[2]
    

    
    
    # 454 => FN.room_closet_first_occurrence_num_event_from_start
    out[:, 454] = first_occurrence_index[3]
    
    # 455 => FN.room_closet_last_occurrence_num_event_from_start
    out[:, 455] = last_occurrence_index[3]
    
    # 456 => FN.room_closet_first_occurrence_num_event_from_end
    out[:, 456] = n - first_occurrence_index[3]
    
    # 457 => FN.room_closet_last_occurrence_num_event_from_end
    out[:, 457] = n - last_occurrence_index[3]
    
    # 458 => FN.room_closet_first_occurrence_time
    out[:, 458] = first_occurrence_time[3]
    
    # 459 => FN.room_closet_last_occurrence_time
    out[:, 459] = last_occurrence_time[3]
    
    # 460 => FN.room_closet_first_occurrence_duration_from_start
    out[:, 460] = first_occurrence_time[3] - start_elapsed_time
    
    # 461 => FN.room_closet_last_occurrence_duration_from_start
    out[:, 461] = last_occurrence_time[3] - start_elapsed_time
    
    # 462 => FN.room_closet_first_occurrence_duration_from_end
    out[:, 462] = end_elapsed_time - first_occurrence_time[3]
    
    # 463 => FN.room_closet_last_occurrence_duration_from_end
    out[:, 463] = end_elapsed_time- last_occurrence_time[3]
    

    
    
    # 464 => FN.room_closet_dirty_first_occurrence_num_event_from_start
    out[:, 464] = first_occurrence_index[4]
    
    # 465 => FN.room_closet_dirty_last_occurrence_num_event_from_start
    out[:, 465] = last_occurrence_index[4]
    
    # 466 => FN.room_closet_dirty_first_occurrence_num_event_from_end
    out[:, 466] = n - first_occurrence_index[4]
    
    # 467 => FN.room_closet_dirty_last_occurrence_num_event_from_end
    out[:, 467] = n - last_occurrence_index[4]
    
    # 468 => FN.room_closet_dirty_first_occurrence_time
    out[:, 468] = first_occurrence_time[4]
    
    # 469 => FN.room_closet_dirty_last_occurrence_time
    out[:, 469] = last_occurrence_time[4]
    
    # 470 => FN.room_closet_dirty_first_occurrence_duration_from_start
    out[:, 470] = first_occurrence_time[4] - start_elapsed_time
    
    # 471 => FN.room_closet_dirty_last_occurrence_duration_from_start
    out[:, 471] = last_occurrence_time[4] - start_elapsed_time
    
    # 472 => FN.room_closet_dirty_first_occurrence_duration_from_end
    out[:, 472] = end_elapsed_time - first_occurrence_time[4]
    
    # 473 => FN.room_closet_dirty_last_occurrence_duration_from_end
    out[:, 473] = end_elapsed_time- last_occurrence_time[4]
    

    
    
    # 474 => FN.room_collection_first_occurrence_num_event_from_start
    out[:, 474] = first_occurrence_index[5]
    
    # 475 => FN.room_collection_last_occurrence_num_event_from_start
    out[:, 475] = last_occurrence_index[5]
    
    # 476 => FN.room_collection_first_occurrence_num_event_from_end
    out[:, 476] = n - first_occurrence_index[5]
    
    # 477 => FN.room_collection_last_occurrence_num_event_from_end
    out[:, 477] = n - last_occurrence_index[5]
    
    # 478 => FN.room_collection_first_occurrence_time
    out[:, 478] = first_occurrence_time[5]
    
    # 479 => FN.room_collection_last_occurrence_time
    out[:, 479] = last_occurrence_time[5]
    
    # 480 => FN.room_collection_first_occurrence_duration_from_start
    out[:, 480] = first_occurrence_time[5] - start_elapsed_time
    
    # 481 => FN.room_collection_last_occurrence_duration_from_start
    out[:, 481] = last_occurrence_time[5] - start_elapsed_time
    
    # 482 => FN.room_collection_first_occurrence_duration_from_end
    out[:, 482] = end_elapsed_time - first_occurrence_time[5]
    
    # 483 => FN.room_collection_last_occurrence_duration_from_end
    out[:, 483] = end_elapsed_time- last_occurrence_time[5]
    

    
    
    # 484 => FN.room_collection_flag_first_occurrence_num_event_from_start
    out[:, 484] = first_occurrence_index[6]
    
    # 485 => FN.room_collection_flag_last_occurrence_num_event_from_start
    out[:, 485] = last_occurrence_index[6]
    
    # 486 => FN.room_collection_flag_first_occurrence_num_event_from_end
    out[:, 486] = n - first_occurrence_index[6]
    
    # 487 => FN.room_collection_flag_last_occurrence_num_event_from_end
    out[:, 487] = n - last_occurrence_index[6]
    
    # 488 => FN.room_collection_flag_first_occurrence_time
    out[:, 488] = first_occurrence_time[6]
    
    # 489 => FN.room_collection_flag_last_occurrence_time
    out[:, 489] = last_occurrence_time[6]
    
    # 490 => FN.room_collection_flag_first_occurrence_duration_from_start
    out[:, 490] = first_occurrence_time[6] - start_elapsed_time
    
    # 491 => FN.room_collection_flag_last_occurrence_duration_from_start
    out[:, 491] = last_occurrence_time[6] - start_elapsed_time
    
    # 492 => FN.room_collection_flag_first_occurrence_duration_from_end
    out[:, 492] = end_elapsed_time - first_occurrence_time[6]
    
    # 493 => FN.room_collection_flag_last_occurrence_duration_from_end
    out[:, 493] = end_elapsed_time- last_occurrence_time[6]
    

    
    
    # 494 => FN.room_entry_first_occurrence_num_event_from_start
    out[:, 494] = first_occurrence_index[7]
    
    # 495 => FN.room_entry_last_occurrence_num_event_from_start
    out[:, 495] = last_occurrence_index[7]
    
    # 496 => FN.room_entry_first_occurrence_num_event_from_end
    out[:, 496] = n - first_occurrence_index[7]
    
    # 497 => FN.room_entry_last_occurrence_num_event_from_end
    out[:, 497] = n - last_occurrence_index[7]
    
    # 498 => FN.room_entry_first_occurrence_time
    out[:, 498] = first_occurrence_time[7]
    
    # 499 => FN.room_entry_last_occurrence_time
    out[:, 499] = last_occurrence_time[7]
    
    # 500 => FN.room_entry_first_occurrence_duration_from_start
    out[:, 500] = first_occurrence_time[7] - start_elapsed_time
    
    # 501 => FN.room_entry_last_occurrence_duration_from_start
    out[:, 501] = last_occurrence_time[7] - start_elapsed_time
    
    # 502 => FN.room_entry_first_occurrence_duration_from_end
    out[:, 502] = end_elapsed_time - first_occurrence_time[7]
    
    # 503 => FN.room_entry_last_occurrence_duration_from_end
    out[:, 503] = end_elapsed_time- last_occurrence_time[7]
    

    
    
    # 504 => FN.room_frontdesk_first_occurrence_num_event_from_start
    out[:, 504] = first_occurrence_index[8]
    
    # 505 => FN.room_frontdesk_last_occurrence_num_event_from_start
    out[:, 505] = last_occurrence_index[8]
    
    # 506 => FN.room_frontdesk_first_occurrence_num_event_from_end
    out[:, 506] = n - first_occurrence_index[8]
    
    # 507 => FN.room_frontdesk_last_occurrence_num_event_from_end
    out[:, 507] = n - last_occurrence_index[8]
    
    # 508 => FN.room_frontdesk_first_occurrence_time
    out[:, 508] = first_occurrence_time[8]
    
    # 509 => FN.room_frontdesk_last_occurrence_time
    out[:, 509] = last_occurrence_time[8]
    
    # 510 => FN.room_frontdesk_first_occurrence_duration_from_start
    out[:, 510] = first_occurrence_time[8] - start_elapsed_time
    
    # 511 => FN.room_frontdesk_last_occurrence_duration_from_start
    out[:, 511] = last_occurrence_time[8] - start_elapsed_time
    
    # 512 => FN.room_frontdesk_first_occurrence_duration_from_end
    out[:, 512] = end_elapsed_time - first_occurrence_time[8]
    
    # 513 => FN.room_frontdesk_last_occurrence_duration_from_end
    out[:, 513] = end_elapsed_time- last_occurrence_time[8]
    

    
    
    # 514 => FN.room_hall_first_occurrence_num_event_from_start
    out[:, 514] = first_occurrence_index[9]
    
    # 515 => FN.room_hall_last_occurrence_num_event_from_start
    out[:, 515] = last_occurrence_index[9]
    
    # 516 => FN.room_hall_first_occurrence_num_event_from_end
    out[:, 516] = n - first_occurrence_index[9]
    
    # 517 => FN.room_hall_last_occurrence_num_event_from_end
    out[:, 517] = n - last_occurrence_index[9]
    
    # 518 => FN.room_hall_first_occurrence_time
    out[:, 518] = first_occurrence_time[9]
    
    # 519 => FN.room_hall_last_occurrence_time
    out[:, 519] = last_occurrence_time[9]
    
    # 520 => FN.room_hall_first_occurrence_duration_from_start
    out[:, 520] = first_occurrence_time[9] - start_elapsed_time
    
    # 521 => FN.room_hall_last_occurrence_duration_from_start
    out[:, 521] = last_occurrence_time[9] - start_elapsed_time
    
    # 522 => FN.room_hall_first_occurrence_duration_from_end
    out[:, 522] = end_elapsed_time - first_occurrence_time[9]
    
    # 523 => FN.room_hall_last_occurrence_duration_from_end
    out[:, 523] = end_elapsed_time- last_occurrence_time[9]
    

    
    
    # 524 => FN.room_halloffame_first_occurrence_num_event_from_start
    out[:, 524] = first_occurrence_index[10]
    
    # 525 => FN.room_halloffame_last_occurrence_num_event_from_start
    out[:, 525] = last_occurrence_index[10]
    
    # 526 => FN.room_halloffame_first_occurrence_num_event_from_end
    out[:, 526] = n - first_occurrence_index[10]
    
    # 527 => FN.room_halloffame_last_occurrence_num_event_from_end
    out[:, 527] = n - last_occurrence_index[10]
    
    # 528 => FN.room_halloffame_first_occurrence_time
    out[:, 528] = first_occurrence_time[10]
    
    # 529 => FN.room_halloffame_last_occurrence_time
    out[:, 529] = last_occurrence_time[10]
    
    # 530 => FN.room_halloffame_first_occurrence_duration_from_start
    out[:, 530] = first_occurrence_time[10] - start_elapsed_time
    
    # 531 => FN.room_halloffame_last_occurrence_duration_from_start
    out[:, 531] = last_occurrence_time[10] - start_elapsed_time
    
    # 532 => FN.room_halloffame_first_occurrence_duration_from_end
    out[:, 532] = end_elapsed_time - first_occurrence_time[10]
    
    # 533 => FN.room_halloffame_last_occurrence_duration_from_end
    out[:, 533] = end_elapsed_time- last_occurrence_time[10]
    

    
    
    # 534 => FN.room_microfiche_first_occurrence_num_event_from_start
    out[:, 534] = first_occurrence_index[11]
    
    # 535 => FN.room_microfiche_last_occurrence_num_event_from_start
    out[:, 535] = last_occurrence_index[11]
    
    # 536 => FN.room_microfiche_first_occurrence_num_event_from_end
    out[:, 536] = n - first_occurrence_index[11]
    
    # 537 => FN.room_microfiche_last_occurrence_num_event_from_end
    out[:, 537] = n - last_occurrence_index[11]
    
    # 538 => FN.room_microfiche_first_occurrence_time
    out[:, 538] = first_occurrence_time[11]
    
    # 539 => FN.room_microfiche_last_occurrence_time
    out[:, 539] = last_occurrence_time[11]
    
    # 540 => FN.room_microfiche_first_occurrence_duration_from_start
    out[:, 540] = first_occurrence_time[11] - start_elapsed_time
    
    # 541 => FN.room_microfiche_last_occurrence_duration_from_start
    out[:, 541] = last_occurrence_time[11] - start_elapsed_time
    
    # 542 => FN.room_microfiche_first_occurrence_duration_from_end
    out[:, 542] = end_elapsed_time - first_occurrence_time[11]
    
    # 543 => FN.room_microfiche_last_occurrence_duration_from_end
    out[:, 543] = end_elapsed_time- last_occurrence_time[11]
    

    
    
    # 544 => FN.room_stacks_first_occurrence_num_event_from_start
    out[:, 544] = first_occurrence_index[12]
    
    # 545 => FN.room_stacks_last_occurrence_num_event_from_start
    out[:, 545] = last_occurrence_index[12]
    
    # 546 => FN.room_stacks_first_occurrence_num_event_from_end
    out[:, 546] = n - first_occurrence_index[12]
    
    # 547 => FN.room_stacks_last_occurrence_num_event_from_end
    out[:, 547] = n - last_occurrence_index[12]
    
    # 548 => FN.room_stacks_first_occurrence_time
    out[:, 548] = first_occurrence_time[12]
    
    # 549 => FN.room_stacks_last_occurrence_time
    out[:, 549] = last_occurrence_time[12]
    
    # 550 => FN.room_stacks_first_occurrence_duration_from_start
    out[:, 550] = first_occurrence_time[12] - start_elapsed_time
    
    # 551 => FN.room_stacks_last_occurrence_duration_from_start
    out[:, 551] = last_occurrence_time[12] - start_elapsed_time
    
    # 552 => FN.room_stacks_first_occurrence_duration_from_end
    out[:, 552] = end_elapsed_time - first_occurrence_time[12]
    
    # 553 => FN.room_stacks_last_occurrence_duration_from_end
    out[:, 553] = end_elapsed_time- last_occurrence_time[12]

