#include <Arduino.h>
#include <Servo.h>


struct servo {
    Servo s;
    int pin;
};
typedef struct servo SERVO;

int servo(String &args, SERVO *servos);

//extern Servo servo0;
//extern Servo servo1;
