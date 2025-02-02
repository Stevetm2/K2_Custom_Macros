# K2_Custom_Macros
Creaity K2 Plus improvements

1) BED_MESH_CALIBRATE: In preparation for adaptive bed mesh. These macros disable bed mesh calibrate, by default, and then can be enabled when needed. Waiting on the K2 Bed mesh calibration to allow a grid smaller than 9x9.
2) FIL_RFID_APPLY : Allow the creation of a filament DB containing PA, Flow and z_ffsets, utilizing the RFID tags.  These DB values will be applied on each filament change.  Enable FIL_FRID_AUTO_SAVE to save the PA/flow settings, after completing a Calibration print.  Also, the z_offset can be saved by enabling FIL_FRID_AUTO_SAVE_WITH_Z. When you plan to tune the z_offset, enable this before a print begins.
3) CUT_PRE_RETRACT : Testing pre_cut_retract, unfortunately I haven't yet found an appropriate macro override to use.  Currently testing.
4) RESUME_EXTRUDE : Reduce RESUME_EXTRUDE amount to 30mm from 80mm, as the default is excessive.
5) M1177 : Added M1177 command to output to the Klipper log and the heads up display on the page.
6) CFS : Mods to default CFS retrude speed etc. more modest values and the cut xpos can be further to the left.
