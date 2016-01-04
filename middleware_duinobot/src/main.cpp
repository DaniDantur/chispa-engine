#include <mbq.h>
#include <PingIRReceiver.h>

#define DEFAULT_TIMEOUT_MILLISECONDS 100

String incomingData;

void setup()
{
	initBoard();
	Serial.setTimeout(DEFAULT_TIMEOUT_MILLISECONDS);

	while(1) {

		if(Serial.available() > 0) {
			incomingData = Serial.readString();
			Serial.println(incomingData);

		}


	}
}

void loop()
{
}
