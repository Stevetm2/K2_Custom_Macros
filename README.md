# K2_Custom_Macros
K2_FIL_DB+ : Creaity K2 Plus improvements

__FEATURES__. (based on FW 1.1.0.65)

1. FIL_RFID_APPLY : Allow the creation of a filament DB containing PA, Flow and z_ffsets, utilizing the RFID tags.  These DB values will be applied on each filament change.  Enable FIL_FRID_AUTO_SAVE to save the PA/flow settings, after completing a Calibration print.  Also, the z_offset can be saved by enabling FIL_FRID_AUTO_SAVE_WITH_Z. When you plan to tune the z_offset, enable this before a print begins.  The z_offset will be applied oncw per print, for the first filament in use.

2. RESUME_EXTRUDE : Reduce RESUME_EXTRUDE amount to 10mm from 80mm, as the default is excessive.

3. M1177 : Added M1177 command to output to the Klipper log and the heads up display on the page.  Also added DUMP_VARIABLES and DUMP_SAVEVARS for debugging.

4. CFS : Mods to default CFS retrude speed etc. more modest values and the cut xpos can be further to the left.

5. BED_MESH_CALIBRATE: In preparation for adaptive bed mesh. These macros disable bed mesh calibrate, by default, and then can be enabled when needed. Waiting on the K2 Bed mesh calibration to allow a grid smaller than 9x9 before we can use the adaptive meshing.

6. CUT_PRE_RETRACT : Testing pre_cut_retract, unfortunately I haven't yet found an appropriate macro override to use.  Currently testing.




__INSTALATION into Fluidd__


1. Open your Fluidd web page

Open your browser with your printer IP address followed by :4408 as shown below, only with your pinter IP.

eg,  10.0.0.30:4408


2. Adding files

Download the following files from the printer_cfg folder.  On the Fluidd web page, open your config page by clicking on the hamburger icon on the top left then clicking on the {} icon.  Now click on the + button above the first file in the file list.  Now add these downloaded files to your printer.

_macros_general.cfg_
_macros_fil.cfg_
_macros_test_speed.cfg_

NOTE : DO NOT directly copy over any other files on your printer.  Please follow the below instructions regarding the other required changes.


3. Edit Printer.cfg

Now add the below line to your printer.cfg under the [include box.cfg] line,

_[include macros_general]_


4. Edit gcode_macros.cfg

Under the variable_z_safe_pause line add,

variable_e_purge_resume: 80

Then replace the following single line,

  {% set E = printer["gcode_macro PAUSE"].extrude|float + 80 %}

with these two lines,

  {% set e_purge_resume = printer['gcode_macro PRINTER_PARAM'].e_purge_resume|int %}

  {% set E = printer["gcode_macro PAUSE"].extrude|float + e_purge_resume %}

5. Optional CFS parameter changes

Have a look through the box.cfg file to see what I have gathered from other K2 users (check my commit history on that file).  I've not really noticed any improvements with these changes, but you may.


__USAGE__

1. Macro Buttons

1.1. FIL_RFID_AUTO_SAVE_ON

After clicking this macro, the user can initiate a print with filament Calibation enabled.  On completion of that print, the printer will store the Calibrated PA and Flow parameters into the RFID filament database.  After which, the printer will use these settings every time that same filament (or filament with the same RFID) is used in a single or multi-color print.

Technical note : These settings are stored in a database file in the file list, the file is called variables_macro_settings.txt and can be modified if needed (but you should allow the macros to do that work).  In the file, in json format, the right most 6 hex digits of the 16 digit RFID code represents the filament color, this will help a little to spot which filament is which.

I would recommend disabling PA in your slicer filament settings and also setting the filament flow to 0.95 (95%) in the slicer filament settings.

1.2. FIL_RFID_AUTO_SAVE_WITH_Z_ON

THIS IS EXPERIMENTAL AND MAY CRASH THE NOZZLE INTO THE BED, I DO NOT TAKE RESPONSIBILITY FOR BED COLLISIONS.  This has the same features as FIL_RFID_AUTO_SAVE_ON.  However. on completion of the Calibration print, it also stores the last z_offset which you tuned in Fluidd for that filament.

Be sure NOT to save your config after it completes the print, or alternatively, reset the z_offset back to zero before any follow up print.  There are safeguards for this,, but be vigilant the first few uses.  This stored filament z_offset will ONLY be used on the first filament change of the first layer.  The the PA and Flow settings are still applied for every filament change throughoutthe print.

Technical note : Again you can edit the setting for a filament in the variables_macro_settings.txt file, if you wish to set it back to zero for example.  Be very careful with this feature!

1.3. FIL_HEAT

This heats the nozzle to 220 degrees.

1.4. BED_HEAT

This heats the bed to 55 degrees.

1.5. DUMP_VARIABLES 

This outputs all the variables to the console output for debugging purposes. 

1.6. DUMP_SAVEVARS 

This outputs all the save vars to the console output for debugging purposes. 

1.7. FIL_SET_PURGE_RESUME

By default this is set to 10 in these macros.  This can be permanently changed in the macro files, or modified temporarily via this macro button.  The original value was 80, which was excessive if the user was only pausing and not doing a color change.

1.8. BED_MESH_CALIBRATE_FULL

By default the bed mesh calibrate is switched off.  So even if it is checked on in the Creality App it will not perform a bed mesh calibration.  Use this macro to switch it on for the follow up prints.  Use BED_MESH_CALIBRATE_OFF to disable again.  

1.9. _BED_MESH_CALIBRATE_ADAPTIVE

Work in progress, DO NOT USE


__LIMITATIONS__

1. Filament RFID Database implementation.

Currently I only support a single CFS.  I also do not support the external filament roll.  These features will come in time.

2. There is the possibility that creality will remove the ability for the printer to read user created RFID tags, but hopefully this will not happen.

3. Only tested on FW 1.1.0.65.


