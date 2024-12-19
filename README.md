FLASH is a PDP-8 program to rotate the AC and MQ lights on a PDP-8 front panel - for example the PiDP-8 simulation.

It uses several different pattersn switching between them every 20-30 seconds.

The timing is right for a PiDP8 running on a Raspberry Pi. To run on a real machine, you will need
to change the definition of the symbol cti2 (line 10) to something muich smaller, probably around -20.

The source is here in two forms, flash.pal which is the original source, and flash.pa8 which is in
upper case suitable for downloading to OS/8 for assembly.

There are also two little Python utilities:

to8.py - convert a lowercase, Unix-format file to uppercase and PDP-8 format (CR/LF line termination)
format-pal.py - adjust columns to produce nice-looking code

To move the program to a PiDP8 and run it:

1. Run pidp8i and attach to it
2. Type ctrl-E to break out into the emulator command line
3. Type: attach ptr <file path> (e.g. attach ptr /home/pi/pdp8.pa8 )
4. Type c to return to the PDP-8
5. Type R PIP
6. Now type FLASH.PA<PTR: and then hit escape twice, to transfer the file as an emulated paper tape
7. Type PAL FLASH to assemble the code, then LOPAD/G FLASH to run it
8. If you want to stop he program and return to the OS/8 prompt, set the high bit of the switch register

Enjoy!
