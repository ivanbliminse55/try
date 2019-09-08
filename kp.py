import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)




MATRIX=[[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]
ROW=[29,23,21,19]
COL=[31,33,35,37]
for j in range(4):
    GPIO.setup(COL[j],GPIO.OUT)
    GPIO.output(COL[j],True)
for i in range(4):
    GPIO.setup(ROW[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
oo=0
try:
    while True:
        for j in range(4):
            GPIO.output(COL[j],0)
            for i in range(4):
                if GPIO.input(ROW[i])==0:
                    print(MATRIX[i][j])
                    a=str(MATRIX[i][j])
                    oo=1
                
                    while(GPIO.input(ROW[i])==0):
                        pass
                    break;
            GPIO.output(COL[j],1)
        if oo==1:
            break;
        
except KeyboardInterrupt:
    GPIO.cleanup()


