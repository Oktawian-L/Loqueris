#return the sum of two number arguments
def add(num1,num2):
    return num1 + num2
#*,-,/
def sub(num1,num2):
    return num1 - num2

def main():
    try:
        operar = input("choose 1,2,3,4")
    except:
        print 'nieprawidlowa komenda',
        return #exit the program w/w arguemnts
    if (operar == 1):
        print(add(12,3))
    elif(operar == 2):
        print(sub(12,3))
    else:
        print 'nie rozpoznano metody'
main()