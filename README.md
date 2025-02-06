# K2_Custom_Macros
Creaity K2 Plus improvements


1) FIL_RFID_APPLY : Allow the creation of a filament DB containing PA, Flow and z_ffsets, utilizing the RFID tags.  These DB values will be applied on each filament change.  Enable FIL_FRID_AUTO_SAVE to save the PA/flow settings, after completing a Calibration print.  Also, the z_offset can be saved by enabling FIL_FRID_AUTO_SAVE_WITH_Z. When you plan to tune the z_offset, enable this before a print begins.
2) RESUME_EXTRUDE : Reduce RESUME_EXTRUDE amount to 30mm from 80mm, as the default is excessive.
3) M1177 : Added M1177 command to output to the Klipper log and the heads up display on the page.  Also added DUMP_VARIABLES and DUMP_SAVEVARS for debugging.
4) CFS : Mods to default CFS retrude speed etc. more modest values and the cut xpos can be further to the left.
5) BED_MESH_CALIBRATE: In preparation for adaptive bed mesh. These macros disable bed mesh calibrate, by default, and then can be enabled when needed. Waiting on the K2 Bed mesh calibration to allow a grid smaller than 9x9.
6) CUT_PRE_RETRACT : Testing pre_cut_retract, unfortunately I haven't yet found an appropriate macro override to use.  Currently testing.


Insulation into Fluidd

1) Open your Fluid web page

Open your browser with your printer IP address followed by :4408 as shown below, only with your pinter IP.

eg,10.0.0.30:4408

2) Adding files

Download the following files from the printer_cfg folder.  Click on the + button above the first file in the list.  Now add these downloaded files to your printer.

macros_general.cfg
macros_fil.cfg
macros_test_speed.cfg


3) Edit Printer.cfg

Open your config page by clicking on the hamburger icon on the top left then clicking on the {} icon.  Now edit and add the below line to your printer.cfg under the [include box.cfg] line.

[include macros_general]

4) Edit printer_params.cfg

