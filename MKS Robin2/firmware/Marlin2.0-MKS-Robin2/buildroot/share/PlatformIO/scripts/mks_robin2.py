import os,shutil
from SCons.Script import DefaultEnvironment
from platformio import util

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoststm32")
CMSIS_DIR = os.path.join(FRAMEWORK_DIR, "CMSIS", "CMSIS")
assert os.path.isdir(FRAMEWORK_DIR)
assert os.path.isdir(CMSIS_DIR)
assert os.path.isdir("buildroot/share/PlatformIO/variants")

mcu_type = board.get("build.mcu")[:-2]      #stm32f407ze
variant = board.get("build.variant")        #MKS_Robin2
series = mcu_type[:7].upper() + "xx"        #stm32f4xx
variant_dir = os.path.join(FRAMEWORK_DIR, "variants", variant)  #framework-arduinoststm32/variants/MKS_Robin2

source_dir = os.path.join("buildroot/share/PlatformIO/variants", variant)#buildroot/share/PlatformIO/variants/MKS_Robin2
assert os.path.isdir(source_dir)

if not os.path.isdir(variant_dir):
    os.mkdir(variant_dir)
for file_name in os.listdir(source_dir):
    full_file_name = os.path.join(source_dir, file_name)#full_file_name = buildroot/share/PlatformIO/variants/MKS_Robin2/ldscript.ld
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, variant_dir)
