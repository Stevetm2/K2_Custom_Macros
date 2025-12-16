# K2_Custom_Macros
__K2_FIL_DB+ : Creaity K2 Plus improvements.__

__OVERVIEW__

The provided macros allows saving of filament PA and Flow settings, with Z offset if requested, to an internal FIL_DB.  To be recalled on each future filament change.

When you enable the save feature, and enable the Creality K2 filament PA and Flow calibration options on the printer, these PA and Flow values will be stored to this custom FIL_DB.  The macros will then automatically use these values during each filament change.  This solved a problem I was seeing, I found that these values did not updated for non-Creality filament, until now!

__UPDATE__ 7/20/25 New Version

1. There is now support for multiple CFS's, performiing settings changes during any filament change.

2. There is now support for side spool RFID reading.
   * Just swipe the filaments RFID on the side of the printer, just before loading the filament, then on the next Start Print it will set the approprite PA and Flow settings for the loaded side spool.

3. CUT_PRE_RETRACT is now supported.  The macros now perform a 20mm retraction before each filament change, which saves filament.

4. There are now 'helper' popup dialog macros (SHOW_PROMPT_) for :

   * Bed Home Soak      : For various temps - SHOW_PROMPT_BED_TEMP_SOAK

   * Bed Mesh Calibrate : Enabe/disable for next print - SHOW_PROMPT_BED_MESH_CALIBRATE

   * Filament Settings  : PA and Flow save triggering for RFID filaments - SHOW_PROMPT_FIL_SETTINGS

   * Filament Status    : Show the status of loaded slots and their RFID tag data.  As well filament sensor status. - SHOW_PROMPT_FIL_SETTINGS


__UPDATE__ (FW 1.1.2.6 and re-install)

1. The macros are now confirmed to work on FW 1.1.2.6.  So you can reinstall the macros if you upgrade.
2. IMPORTANT : Please backup your variables_macro_settings.txt file before installing the new FW.  As well as any file you changed.  Note, a future FW update or hardware changes may require further filament tuning.
3. Next install your new FW, and follow the install instructions below, but Do Not copy the variables_macro_settings.txt file back.  Instead, after installing, perform a K2 reboot.  After which you will have a new default variables_macro_settings.txt file.  You must then copy the text content of your backup over the default content of this file, save and then reboot the K2 again.  Now all of your calibrations will be recovered.


__FEATURES__

1. FIL_RFID_APPLY : Allow the creation of a filament DB entries containing PA, Flow and z_ffsets, utilizing the RFID tags.  These stored DB values will be applied on each filament change, for each RFID tagged filament.  Enable FIL_RFID_AUTO_SAVE to save the PA/flow settings, after completing a Calibration print.  Also, the z_offset can be saved by enabling FIL_RFID_AUTO_SAVE_WITH_Z. When you plan to tune the z_offset, enable this before a print begins.  The z_offset will be applied oncw per print, for the first filament in use.

2. RESUME_EXTRUDE : Reduce RESUME_EXTRUDE amount to 10mm from 80mm, as the default is excessive.  Also user editable.

3. M1177 : Added M1177 command to output to the Klipper log and the heads up display on the page.  Also added DUMP_VARIABLES and DUMP_SAVEVARS for debugging.

4. CFS : Mods to default CFS retrude speed etc. in box.cfg. Changes include more modest values and the cut xpos is now further to the left.

5. BED_MESH_CALIBRATE: In preparation for adaptive bed mesh. These macros disable bed mesh calibrate, by default, which can then can be enabled as needed. Currently waiting on the K2 Bed mesh calibration code to allow a grid smaller than 9x9 before we can use the adaptive meshing.

6. CUT_PRE_RETRACT : Testing pre_cut_retract, unfortunately I haven't yet found an appropriate macro override to use.  Currently testing.  See UPDATE above.




__INSTALATION into Fluidd__


1. Open your Fluidd web page

Open your browser with your printer IP address followed by :4408 as shown below, replacing my IP with your pinter IP address.

eg,  10.0.0.30:4408


2. Adding files

Download the following files from the printer_cfg folder.  On the Fluidd web page, open your config page by clicking on the hamburger icon on the top left.  Now click on the {} icon.  Next click on the + button above the first file in the file list.  Now add these downloaded files to your printer.

- _macros_general.cfg_
- _macros_fil.cfg_
- _macros_test_speed.cfg_

NOTE : DO NOT directly copy over any other files on your printer.  Please follow the below instructions regarding the other required changes.  Also, don't be tempted to copy my variables_macro_settings.txt file. A new one will be generated on first K2 reboot after instalation, ready to be populated with your filament calibrations.


3. Edit Printer.cfg

Now add the below line to your printer.cfg under the [include box.cfg] line,

```
[include macros_general]
```


4. Edit gcode_macros.cfg

Under the variable_z_safe_pause line add,

```
variable_e_purge_resume: 80
```

Then replace the following single line,

```
  {% set E = printer["gcode_macro PAUSE"].extrude|float + 80 %}
```

with these two lines,

```
  {% set e_purge_resume = printer['gcode_macro PRINTER_PARAM'].e_purge_resume|int %}

  {% set E = printer["gcode_macro PAUSE"].extrude|float + e_purge_resume %}
```

5. Optional CFS parameter changes

Have a look through the box.cfg file to see what I have gathered from other K2 users (check my commit history on that file).  I've not really noticed any specific improvements with these changes, but you may.  At the same time, I've never had filament grinding when using these settings, which is common for other K2 users.

__INSTALATION - IMPORTANT Setting Number of CFS tool macros__

You will see that in the macros_fil.cfg file there is support for 2 CFS's (search for T0.1 for the first macro of the 8).  I have defined T0 thru T7.  However, if you have only one CFS then remove the macro defines for tools T4 thru T7.  I have now noticed that if they remain the Creality Clowd app has problems connecting to the printer.  Conversely, if you have three CFS's, just define the remaining T8 thru T12, or if you have four CFS's then define T8 thru T16, in the same pattern as in the file.  NOTE : dont make any typo's :)


__USAGE__

1. Macro Buttons

1.1. FIL_RFID_AUTO_SAVE_ON

When the user clicks this macro and then initiates a print which utizes the built in K2 filament Calibation feature, the PA and Flow calibrations will be performed.  On completion of this print, with this Clibration enbled, the macros will automatically store the Calibrated PA and Flow parameters into the RFID filament database.  After which, the printer will use these settings every time that same filament (or filament with the same RFID) is used in a single or multi-color print.

Technical note : These settings are stored in a database file which is in json format.  This file is stored in the config file folder on the printer, named variables_macro_settings.txt.  It can be modified if needed, allowing you to enter your own PA and Flow values (but you should allow the macros to do that work automatically).  In the file, the right most 6 hex digits of each 16 digit RFID code, represents the filament color, this will help you a little to recognize a filament for editing.

I would recommend disabling PA in your slicer filament settings (as it will override those slicer values) and also set the filament flow to 0.95 (95%) in the slicer filament settings as I do.

1.2. FIL_RFID_AUTO_SAVE_WITH_Z_ON

THIS IS EXPERIMENTAL AND MAY CRASH THE NOZZLE INTO THE BED, I DO NOT TAKE RESPONSIBILITY FOR BED COLLISIONS.  This has the same features as FIL_RFID_AUTO_SAVE_ON.  However, on completion of the Calibration print, it also stores the last z_offset, which you tuned in Fluidd for that filament.

Be sure NOT to save your printer config after it completes the print, or alternatively, confirm that the z_offset is reset back to zero before any follow up print.  There are safeguards, but be vigilant the first few times you use the save z offset feature.  This stored filament z_offset will ONLY be used on the first filament change of the first layer.  The the PA and Flow settings are still applied for every filament change throughout the print.

Technical note : Again, you can edit the setting for a filament in the variables_macro_settings.txt file, if you wish to set the z offset back to zero for example.  Be very careful with this feature!

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

By default the bed mesh calibrate is switched off.  By using this feature, even if it is checked on in the Creality App, it will not by default perform a bed mesh calibration.  Use this macro to switch it on for your follow up prints.  Use BED_MESH_CALIBRATE_OFF to disable again.  The last bed mesh created will be used there after and after each reboot.

1.9. _BED_MESH_CALIBRATE_ADAPTIVE

Work in progress, DO NOT USE



__RFID TAG WRITER__

I use this tag writer from the Google Play Store : https://play.google.com/store/apps/details?id=dngsoftware.spoolid


__LIMITATIONS__

1. Filament RFID Database implementation. 

2. There is the possibility that creality will remove the ability for the printer to read user created RFID tags, but hopefully this will not happen.  User generated encrypted tags have been confirmed to work with FW 1.1.2.6 and below.

3. Currently tested on FW 1.1.0.65 and 1.1.2.6.  See UPDATE above.


