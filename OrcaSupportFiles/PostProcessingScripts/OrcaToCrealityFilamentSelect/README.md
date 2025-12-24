# Creality Selected Filament

## General

This script will modify a saved Creality K2 GCode file from Orca Slicer, to allow it to be more compatible with the Creality Cloud App for printing using your phone or tablet.

- It will remove unused filaments from the list of mapped filaments in the app.  This allows you to have PLA, PETG etc in your filament list in Orca but not have them currently loaded in your CFS.  Then when selecting the file to print in Creality Cloud App, only the filament/s which are in use in that file will appear as mappable filaments, before the print is started.
- It resets the Filament Flush Multiplier to 1.0.  I have noticed that smaller values for this cause strange flushing behaviour, so by setting your value to 0.5 in the slicer and clicking calculate will reduce each filament combination correctly, then this scrit will reset the multiplier to 1.0 so the printer uses those individual values directly, with no fiurther modifications.
- Other features may be added in the future.


## Setup

Add this script to the Orca Slicer Post processing script.  First Enable Advanced Mode, then navigate to Others → Post-processing Scripts.

```sh
"C:\path\to\python.exe" "C:\path\to\CrealitySelectedFilament.py"
```

## Usage

Use the "Export G-Code" option to save the file to disc and then upload the newly modified file.  The "Print" option should also work if setup correctly for your K2 printer.
