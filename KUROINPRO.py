from KUROH import*
import time
def InPutProcess(InPut):
    Shut=0
    if InPut =='TL':
        Translate()
    elif InPut =='NNW':
        NeuralNetwork()
    elif InPut =='WT':
        Weather1 = Weather()
        print(Weather1)
        time.sleep(3)
    elif InPut == 'SD':
        Shut = 1

    else:
        print('Please Enter The Right Command ')
        time.sleep(2)
    return Shut