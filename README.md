# K2_Custom_Macros
Creaity K2 Plus improvements

_FEATURES_

1 FIL_RFID_APPLY : Allow the creation of a filament DB containing PA, Flow and z_ffsets, utilizing the RFID tags.  These DB values will be applied on each filament change.  Enable FIL_FRID_AUTO_SAVE to save the PA/flow settings, after completing a Calibration print.  Also, the z_offset can be saved by enabling FIL_FRID_AUTO_SAVE_WITH_Z. When you plan to tune the z_offset, enable this before a print begins.
2 RESUME_EXTRUDE : Reduce RESUME_EXTRUDE amount to 10mm from 80mm, as the default is excessive.
3 M1177 : Added M1177 command to output to the Klipper log and the heads up display on the page.  Also added DUMP_VARIABLES and DUMP_SAVEVARS for debugging.
4 CFS : Mods to default CFS retrude speed etc. more modest values and the cut xpos can be further to the left.
5 BED_MESH_CALIBRATE: In preparation for adaptive bed mesh. These macros disable bed mesh calibrate, by default, and then can be enabled when needed. Waiting on the K2 Bed mesh calibration to allow a grid smaller than 9x9.
6 CUT_PRE_RETRACT : Testing pre_cut_retract, unfortunately I haven't yet found an appropriate macro override to use.  Currently testing.




INSTALATION into Fluidd


1 Open your Fluidd web page

Open your browser with your printer IP address followed by :4408 as shown below, only with your pinter IP.

eg,  10.0.0.30:4408


2 Adding files

Download the following files from the printer_cfg folder.  Click on the + button above the first file in the file list.  Now add these downloaded files to your printer.

macros_general.cfg
macros_fil.cfg
macros_test_speed.cfg


3 Edit Printer.cfg

Open your config page by clicking on the hamburger icon on the top left then clicking on the {} icon.  Now edit and add the below line to your printer.cfg under the [include box.cfg] line,

[include macros_general]


4 Edit gcode_macros.cfg
Under the variable_z_safe_pause line add,

variable_e_purge_resume: 80

Then replace the following line,

  {% set E = printer["gcode_macro PAUSE"].extrude|float + 80 %}

with,

  {% set E = printer["gcode_macro PAUSE"].extrude|float + e_purge_resume %}


USAGE

1 Macro Buttons

1.1 FIL_RFID_AUTO_SAVE_ON 

When clicked, on completion of a print with filament Calibation enabled, the printer will store the PA and Flow parameters.  After which, the printer will use these settings every time that same filament (with the same RFID) is used in a single or multi-color print.

These settings are stored in a database file in the file list, the file is called variables_macro_settings.txt and can be modified if needed (but you should allow the macros to do that work).

1.2 FIL_RFID_AUTO_SAVE_WITH_Z_ON

THIS IS EXPERIMENTAL AND MAY CRASH THE NOZZLE INTO THE BED.  This does the same as FIL_RFID_AUTO_SAVE_ON only it also stored the last z_offset which you tuned in Fluid.  Be sure NOT to save your config after, or reset the z offset back to zero before any follow up print.  Again you can edit the setting for a filament in the variables_macro_settings.txt file, if you wish to set it back to zero for example.

1.3 FIL_HEAT

This heats the nozzle to 220 defrees.

1.4 BED_HEAT

This heats the bed to 55 degrees.

1.5 DUMP_VARIABLES 

This outputs all the variables to the console output for debugging purposes. 

1.6 DUMP_SAVEVARS 

This outputs all the save vars to the console output for debugging purposes. 

1.7 FIL_SET_PURGE_RESUME

By default this is set to 10 and can be changed in the macro files, or modified temporarily via this macro button.  The originalvalue was 80 which was excessive when only pausing without a color change.

1.8 BED_MESH_CALIBRATE_FULL

By default the bed mesh calibrate is switched off.  So even if it is checked on in the Creality App it will not perform a bed mesh calibration.  Use this macro to switch it on for the follow up prints.  Use BED_MESH_CALIBRATE_OFF to disable again.  

1.9 BED_MESH_CALIBRATE_ADAPTIVE

Work in progress, DO NOT USE



