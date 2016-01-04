#include <mbq.h>
#include <PingIRReceiver.h>

#include "motor.h"

#define DEFAULT_SERIAL_TIMEOUT_MILLISECONDS 100

String incomingData;
String cmd;
String args;

void setup()
{
	initBoard();
	Serial.setTimeout(DEFAULT_SERIAL_TIMEOUT_MILLISECONDS);

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
				if(motor(args) != 0) {
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
