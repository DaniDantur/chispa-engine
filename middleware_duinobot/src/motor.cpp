#include "motor.h"

int motor(String &args)
{
	int ret = 0;

	int separatorPos = args.indexOf(' ');
	if(separatorPos == -1) {
		return -1;
	}

	String motor0Val = args.substring(0, separatorPos);
	String motor1Val = args.substring(separatorPos + 1);

	motor0.setPower(motor0Val.toInt());
	motor1.setPower(motor1Val.toInt());



	return ret;
}
