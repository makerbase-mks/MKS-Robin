# Marlin2.0-MKS-Robin2

For mks robin2 mainboard,currently this code only implements online printing, and the sd card and display are still under development.
<br>
<br>
This folder contains the source code for marlin2.0 and can be used on the robin motherboard.The compilation environment used is Atom+platformio;<br>
Specific methods can refer to the following links:<br>
http://marlinfw.org/docs/basics/install_platformio.html#installing-marlin-(platformio)<br>
http://docs.platformio.org/en/latest/ide/atom.html#installation<br>
<br>
After compiling, there will be Robin2.bin firmware in the folder(folder path:\.pioenvs\mks_robin2), then follow the steps below to update the firmware：

+ 1.copy Robin2.bin to SD card<br>
+ 2.insert SD card to MKS Robin2 board<br>
+ 3.reboot MKS Robin2 board<br>
+ 4.wait until firmware upgrade is completed<br>

