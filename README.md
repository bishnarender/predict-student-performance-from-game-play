# predict-student-performance-from-game-play



There was extensive use of numba and C for the "feature generation" code. But there is separate file (features_generation_my_.ipynb) available to bypass numba and C and to <b>view in-line code explanation</b>.

1590 features were generated for each question (out of 18) per session.

There are three level groups. Further, there are 3 questions to level_group 0 (0-4), 10 questions to level_group 1 (5-12) and 5 questions to level_group 2 (13-22).


feature <b>=></b> question_number <b>=></b> feature value is the same for the questions of the same level_group (per session), and is equal to array of question numbers.<br>
<code>
#c FN denotes feature names class.
out[:, FN.question_number] = np.arange(questions_start_number, questions_end_number)
</code>


feature <b>=></b> building_library_first_occurrence_num_event_from_end <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
// FN denotes feature names class.
out[:, FN.building_library_first_occurrence_num_event_from_end] = n - first_occurrence_index[8]
# n is the number of building events in the same level_group (per session).
# first_occurrence_index[8] is building "library" first occurrence position/number (in n) from start.
# 8 is an index of a building named "library".
</code>

feature <b>=></b> fqid_tomicrofiche_first_occurrence_num_event_from_end <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
out[:, FN.fqid_tomicrofiche_first_occurrence_num_event_from_end] = n - first_occurrence_index[106]
# n is the number of fqid events in the same level_group (per session).
# first_occurrence_index[106] is fqid "tomicrofiche" first occurrence position/number (in n) from start.
# 106 is an index of a building named "tomicrofiche".
</code>


feature <b>=></b> name_basic_0_count <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
out[:, FN.name_basic_0_count] = name_counts[0]
# name_counts[0] is the count of "index 0 name events" in the same level_group (per session).
# 0 is an index of a name named "basic".
</code>


feature <b>=></b> room_microfiche_last_occurrence_num_event_from_end <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
out[:, FN.room_microfiche_last_occurrence_num_event_from_end] = n - last_occurrence_index[11]
# n is the number of room events in the same level_group (per session).
# last_occurrence_index[11] is room "microfiche" last occurrence position/number (in n) from start.
# 11 is an index of a room named "microfiche".
</code>


feature <b>=></b> LG0_L1_first_report_open_duration <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
out[:, FN.LG0_L1_first_report_open_duration] = history[60] - history[59]
# history[60] is the time elapsed when the event has a "level_group==0 (0-4), level==1, fqid==report, event_name== object_click, and  name=close" for the first time. LG0_L1_first_report_close_time.
# history[59] is the time elapsed when the event has a "level_group==0 (0-4), level==1 and text==It_s_a_women_s_basketball_jersey_exclamation_" for the first time. LG0_L1_first_report_open_time.
</code>


feature <b>=></b> LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_duration <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
history[5] = x_et[i+1] - x_et[i]
out[:, FN.LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_duration] = history[5]
# history[5] is the difference between "time elapsed" when the event has a "level_group==0 (0-4) and text==Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_question_" for the first time and "time elapsed" to the next event. LG0_first_Leopold__why_don_t_you_help_me_set_up_in_the_Capitol_duration.
</code>


feature <b>=></b> LG1_first_Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that__duration <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
history[35] = x_et[i+1] - x_et[i]
out[:, FN.LG1_first_Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that__duration] = history[35]
# history[35] is the difference between "time elapsed" when the event has a "level_group==1 (5-12) and text==Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that" for the first time and "time elapsed" to the next event. LG1_first_Nope__But_Youmans_and_other_suffragists_worked_hard_to_change_that__time.
</code>


feature <b>=></b> level_11_event_count <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
out[:, FN.level_11_event_count] = level_counts[11]
# level_counts[11] is the count of "index 11 level events" in the same level_group (per session).
# 11 is an index of a level referring "11th level".
</code>


feature <b>=></b> LG1__LNone__name__undefined__index__count <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
out[:,FN.LG1__LNone__name__undefined__index__count] = history[786]
# history[786] is the count of indexes under the name "undefined" events in the level_group 1 (per session).
LG1__LNone__name__undefined__index__count.
</code>


feature <b>=></b> LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_duration <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
history[23] = x_et[i+1] - x_et[i]
out[:,FN.LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_duration] = history[23]
# history[23] is the difference between "time elapsed" when the event has a "level_group==1 (5-12) and text==Youmans_was_a_suffragist_here_in_Wisconsin_" for the first time and "time elapsed" to the next event. LG1_first_Youmans_was_a_suffragist_here_in_Wisconsin_duration.
</code>


feature <b>=></b> LG0_L2_fqid_cs_event_duration_mean <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
history[101] += (x_et[i+1] - x_et[i])
history[102] += 1
out[:,FN.LG0_L2_fqid_cs_event_duration_mean] = history[101]/history[102]
# history[101] is the sum of all duration when the event has a "level_group==1, level==2 and fqid==cs". LG0_L2_fqid_cs_event_duration_sum.
# history[102] is count of "level_group==1, level==2 and fqid==cs" events. LG0_L2_fqid_cs_event_duration_count.
</code>


feature <b>=></b> LG1__L10__None__None__elapsed_time__diff__between__first__event_name__person_click__elapsed_time__and__subsequent__last__fqid__worker__elapsed_time <b>=></b> feature value is the same for the questions of the same level_group (per session).<br>
<code>
# FN denotes feature names class.
history[2891] = x_et[i]
history[1447] = x_et[i]
out[:FN.LG1__L10__None__None__elapsed_time__diff__between__first__event_name__person_click__elapsed_time__and__subsequent__last__fqid__worker__elapsed_time] = history[2891] - history[1447]
# history[2891] is the "time elapsed" when the event has fqid==worker after the first event with event_name==person_click has happened, under the "level_group==1 and level==10". LG1__L10__fqid__worker__elapsed_time__last__after__first__event_name__person_click__index.
# history[1447] is the "time elapsed" when the event has event_name==worker for the first time under the "level_group==1 and level==10". LG1__L10__event_name__person_click__elapsed_time__first.
</code>
