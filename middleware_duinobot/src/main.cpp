#include <mbq.h>
#include <PingIRReceiver.h>

#include "motor.h"
#include "servo.h"

#define DEFAULT_SERIAL_TIMEOUT_MILLISECONDS 100
#define MAX_SERVOS 2

String incomingData;
String cmd;
String args;
SERVO servos[MAX_SERVOS];


void setup()
{
	initBoard();
	Serial.setTimeout(DEFAULT_SERIAL_TIMEOUT_MILLISECONDS);

    servos[0].pin = -1;
    servos[1].pin = -1;

	while(1) {

		if(Serial.available() > 0) {
			incomingData = Serial.readString();

			int spacePos = incomingData.indexOf(' ');
			if(spacePos == -1) {
				//El comando esta mal armado
				continue;
			}

			cmd = incomingData.substring(0, spacePos);
			args = incomingData.substring(spacePos + 1);

			if(cmd == "MOTOR") {
				Serial.println("El CMD es MOTOR");
				if(motor(args) != 0) {
					Serial.println("Error en comando");
					Serial.println(incomingData);
				}
			} else if(cmd == "LED") {
				Serial.println("El CMD tiene LED");
				Serial.println(cmd);
				Serial.println(args);
			} else if(cmd == "SERVO") {
                if(servo(args, servos) != 0) {
                	Serial.println("Error en comando");
					Serial.println(incomingData);
                }
            } else {
				Serial.println("Comando no reconocido");

			}
			
			//Serial.println(cmd);

		}


	}
}

void loop()
{
}
