# BLVL
A soon2be addon for level creation in blender.


At the moment, there is no complete documentation of how it functions, but most of things are on the side panels called "BLVL" and "BLVL_I/E".
It's best to follow constructure of set importing for exporting. 

Set Object:
Data is equivalent of Game Object, it holds crucial part of determening what will this object represent. You must reuse data block if it already exists. GUI Shortcut will be **Alt+D** instead of Shift+D

BLVL.Stage_Orientation:
It's an Empty that I use to cheat Game's orientation into Blender's. Best to keep one on scene, or add a fake user for it and unlink if you like tidyness

## What can it do?
- Sonic Unleashed NAVI: Import .NAVI.XML and .NAVI.xml, Export .NAVI.XML
- Sonic Unleashed Level Set Editing: Import of all set files connected in .stg.xml, Export of .set.xml files (no .stg.xml files yet)

## What is planned?
- Expansion of set objects with interactive looks
- Stage GI Importing, Exporting and Baking
- Stage geometry Import and Export


## Contributors
- Hedgeturd - helped with understanding hex editing
- Skyth - helped with understanding how NAVIs stored
- Starlight - original code of .NAVI.XML export was made by them, I expanded and finished it; contributor to Unleashed-Glvl
- Archxe - Unleashed database from their fork of Glvl
