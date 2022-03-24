import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode (GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while(1):
        value = input("Введите число от 0 до 255\n")
        GPIO.output(dac, decimal2binary(int(value)))
        print("Предполагаемое значение напряжения:", (3.3 * int(value))/256)
    if ((int(value) > 256) | (int (value) < 0 )):
        print("Ошибочный ввод")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
