#ifndef mbq_h
#define mbq_h


#include <Arduino.h>
#include <pins_arduino.h>
#include <stdlib.h>
#include <miniBloq.h>
#include <board.h>
#include <IRRemote.h>
#include <Servo.h>
#include <Ping.h>
#include <pitches.h>
#include <toneDelay.h>
#include <HCSR0x.h>
#include <IRRanger.h>
#include <DCMotor.h>


extern IRrecv irReceiver;
extern Servo servo0;
extern Servo servo1;
extern PingSensor ping;
extern HCSRSensor hcsr;
extern IRRanger irRanger20to150;
extern IRRanger irRanger10to80;
extern DCMotor motor0;
extern DCMotor motor1;

#endif
