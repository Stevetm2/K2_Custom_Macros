# K2 Orca Filament Sync

## General

This script, when copied to the K2 extras foder, will.

- Simulate the return vales from an MMU equiped printer, allowing Orca to sync te CFS filament colors an types.
- Other features may be added in the future.


## Setup

- Add the mmu.py script to the below K2 klipper folder, using WinSCP or your favorate copy-over-scp program.

```sh
/usr/share/klipper/klippy/extras
```

- Add the below to your printer.cfg file.

```sh
[mmu]
```

## Usage

In OrcaSlicer, set the Printer Agent to Moonraker in the Orca network settings for your K2 printer, and save your printer config.  A new Filament Sync icon will appear on the Filament tab.  Click that to sync the Filaments from your K2 to OrcaSlicer.

In preferences you can choose enabling sync of just the filament colors or both colors and filament type.
