# K2 OrcaSlicer Filament Sync

## General

This script, when copied to the K2 extras folder, will.

- Simulate the return vales from an MMU equipped printer, allowing Orca to sync the CFS filament colors and types.
- This allows for better Filament Flush values to be auto calculated, especially when combined with custom RFID tagged filament spools.
- It works with version v2.3.2-beta2 of OrcaSlicer, and will be test with future versions as they are released.
- It has been tested on the K2 Plus and should work on other K2 printers.  It may also work on the K1 with CFS, if installed to the correct folder.
- Other features may be added in the future.


## Setup

- Enable root access on your K2 printr.
- Add the supplied mmu.py script to the below K2 klipper folder, using WinSCP or your favorate "copy using SCP" program.

```sh
/usr/share/klipper/klippy/extras
```

- Add the below to your printer.cfg file.

```sh
[mmu]
```

## Usage

In OrcaSlicer, set the Printer Agent to Moonraker in the Orca network settings for your K2 printer, then save your printer config.  A new Filament Sync icon will appear on the Filament tab.  Click that to sync the Filaments from your K2 to OrcaSlicer.

In preferences you can choose enabling sync of just the filament colors or both colors and filament type.
