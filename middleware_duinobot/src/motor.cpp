#include "motor.h"

int motor(String &args)
{
	int ret = 0;

	int separatorPos = args.indexOf(' ');
	if(separatorPos == -1) {
		return -1;
	}

    String motorId = args.substring(0, separatorPos);
    String motorVal = args.substring(separatorPos + 1);

    if(motorId == "0")
	    motor0.setPower(motorVal.toInt());
    else if(motorId == "1")
	    motor1.setPower(motorVal.toInt());
    else
        return -1;


	return ret;
}
