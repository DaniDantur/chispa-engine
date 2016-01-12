#include "servo.h"
#include <Arduino.h>

#define MIN_SERVO 0
#define MAX_SERVO 175

//Al parecer el Futaba S3003 solo rota hasta 175 grados
//forum.allaboutcircuits.com/threads/standard-analog-servos-able-to-rotate-180.47833/

int servo(String &args, SERVO *servos)
{
	int ret = 0;

	int separatorPos = args.indexOf(' ');
	if(separatorPos == -1) {
		return -1;
	}

    String servoId = args.substring(0, separatorPos);
    String servoVal = args.substring(separatorPos + 1);

    int servoIndex = servoId.toInt();
    int servoValInt = servoVal.toInt();

    if(servos[servoIndex].pin == -1) {

        if(servoIndex == 0) {
            servos[servoIndex].pin = 16;
        } else if(servoIndex == 1) {
            servos[servoIndex].pin = 17;
        }

        servos[servoIndex].s.attach(servos[servoIndex].pin);
    } 


    if(servoValInt > MAX_SERVO) {
        servoValInt = 175;
    }

    if(servoValInt < MIN_SERVO) {
        servoValInt = 0;
    }


    servos[servoIndex].s.write(servoValInt);


	return ret;
}
