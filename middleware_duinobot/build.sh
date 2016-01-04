#!/bin/bash

set -e

MIDDLEWARE_PATH=$(pwd)
MINIBLOQ_PATH=/opt/minibloq #Asumo que si no existe, no esta instalado miniBloq

CPP_MAIN=main.cpp
CPP_INITBOARD=initBoard.cpp

if [ ! -d $MINIBLOQ_PATH ]; then
	echo "No se encontro $MINIBLOQ_PATH"
	echo "miniBloq no parece estar instalado"
	exit -1
fi

rm -rf $MIDDLEWARE_PATH/output
mkdir $MIDDLEWARE_PATH/output

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -MMD -mmcu=atmega1284p -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/IRRemote/v1.2" \
	"/opt/minibloq/v0.84.0/libs/Arduino/IRRemote/v1.2/IRRemote.cpp" \
	-o "$MIDDLEWARE_PATH/output/IRRemote.cpp.o"

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -MMD -mmcu=atmega1284p -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Servo/v1.2" \
	"/opt/minibloq/v0.84.0/libs/Arduino/Servo/v1.2/Servo.cpp" \
	-o "$MIDDLEWARE_PATH/output/Servo.cpp.o"

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -MMD -mmcu=atmega1284p -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Buzzer/v1.2"\
	"/opt/minibloq/v0.84.0/libs/Arduino/Buzzer/v1.2/toneDelay.cpp" \
	-o "$MIDDLEWARE_PATH/output/toneDelay.cpp.o"

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -MMD -mmcu=atmega1284p -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/DCMotor/v1.0" \
	"/opt/minibloq/v0.84.0/libs/Arduino/DCMotor/v1.0/DCMotor.cpp" \
	-o "$MIDDLEWARE_PATH/output/DCMotor.cpp.o"

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega1284p -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"/opt/minibloq/v0.84.0/hard/DuinoBot.v2.3.CDC/lib" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/DCMotor/v1.0" \
	"$MIDDLEWARE_PATH/src/motor.cpp" \
	-o "$MIDDLEWARE_PATH/output/motor.cpp.o"

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega1284p -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"/opt/minibloq/v0.84.0/hard/DuinoBot.v2.3.CDC/lib" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/miniBloq/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/PingIRReceiver/v1.0"\
	-I"/opt/minibloq/v0.84.0/libs/Arduino/IRRemote/v1.2" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Servo/v1.2" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Ping/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Buzzer/v1.2" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/HCSR0x/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/IRRanger/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/DCMotor/v1.0" \
	"$MIDDLEWARE_PATH/src/$CPP_INITBOARD" \
	-o "$MIDDLEWARE_PATH/output/$CPP_INITBOARD".o

avr-g++ -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega1284p  -DF_CPU=16000000L -DARDUINO=154 \
	-I"/opt/minibloq/v0.84.0/lang/avrlinux/i386/v4.3.5/bin" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/avr-libc" \
	-I"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/variants/duinobot.v2.x" \
	-I"/opt/minibloq/v0.84.0/hard/DuinoBot.v2.3.CDC/lib" \
	-I"$MIDDLEWARE_PATH/src" \
	-I"$MIDDLEWARE_PATH/output" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/miniBloq/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/PingIRReceiver/v1.0"  \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/IRRemote/v1.2" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Servo/v1.2" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Ping/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/Buzzer/v1.2" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/HCSR0x/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/IRRanger/v1.0" \
	-I"/opt/minibloq/v0.84.0/libs/Arduino/DCMotor/v1.0" \
	-I"$MIDDLEWARE_PATH/output/motor.cpp.o" \
	"$MIDDLEWARE_PATH/src/$CPP_MAIN" \
	-o "$MIDDLEWARE_PATH/output/$CPP_MAIN".o

avr-gcc -Os -Wl,--gc-sections -mmcu=atmega1284p \
	-o"$MIDDLEWARE_PATH/output/main.cpp.elf" \
	"$MIDDLEWARE_PATH/output/DCMotor.cpp.o" \
	"$MIDDLEWARE_PATH/output/Servo.cpp.o" \
	"$MIDDLEWARE_PATH/output/IRRemote.cpp.o" \
	"$MIDDLEWARE_PATH/output/toneDelay.cpp.o" \
	"$MIDDLEWARE_PATH/output/initBoard.cpp.o" \
	"$MIDDLEWARE_PATH/output/motor.cpp.o" \
	"$MIDDLEWARE_PATH/output/$CPP_MAIN".o \
	"/opt/minibloq/v0.84.0/cores/Arduino.v1.5.4.r2/avr/obj/mega1284.a" -L ./ -lm

avr-objcopy -O ihex -j .eeprom --set-section-flags=.eeprom=alloc,load \
	--no-change-warnings \
	--change-section-lma .eeprom=0 \
	"$MIDDLEWARE_PATH/output/main.cpp.elf" \
	"$MIDDLEWARE_PATH/output/main.cpp.epp"

avr-objcopy -O ihex -R .eeprom \
	"$MIDDLEWARE_PATH/output/main.cpp.elf" \
	"$MIDDLEWARE_PATH/output/main.cpp.hex"

avr-size --mcu=atmega1284p --format=avr "$MIDDLEWARE_PATH/output/main.cpp.elf"

avrdude -C/etc/avrdude.conf -q -q -patmega1284p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:"$MIDDLEWARE_PATH/output/main.cpp.hex":i
