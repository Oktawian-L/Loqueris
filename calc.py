#return the sum of two number arguments
def add(num1,num2):
    return num1 + num2
#*,-,/
def sub(num1,num2):
    return num1 - num2

def main():
    #czy udalo sie wprowadzic dane
    validInput = False
    while not validInput:           
        try:
            operar = input("choose 1,2,3,4")
            validInput = True
        except:
            print 'nieprawidlowa komenda',
            return #exit the program w/w arguemnts
    if (operar == 1):
        print(add(12,3))
    elif(operar == 2):
        print(sub(12,3))
    else:
        print 'nie rozpoznano metody'

    #ask user to continue
    #user_yn = input("Continue?0/1")
    #if(user_yn != 1):
    #    break
    #else:
     #   continue
main()