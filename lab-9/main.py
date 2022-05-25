from models.Devices.Analog import Analog
from models.Devices.Digital import Digital
from models.Devices.Pulse import Pulse
from models.Devices.OperationalAmplifier import OperationalAmplifier
from models.Source.Current import Current
from models.Source.Voltage import Voltage
from models.Binary.Decoder import Decoder
from models.Binary.Adder import Adder

def main():
    print("Electronics devices: ")
    instrument1 = Analog("Analog Device", 50, "a2621452s", 10)
    print(instrument1)
    instrument2 = Digital("Digital Device", 30, "a8278594u", 12)
    print(instrument2)
    instrument3 = Pulse("Pulse Device", 45, "a4876206p", 1.50)
    print(instrument3)
    instrument4 = OperationalAmplifier("Operational Amplifier", 35, "a2324532g", 220, 15)
    print(instrument4)
    instrument5 = Current("Current Source", "p6368423x", 5)
    print(instrument5)
    instrument6 = Voltage("Voltage Source", "p6288222b", 56)
    print(instrument6)
    instrument7 = Decoder("Binary-decimal Decoder", 20, "123cod123")
    print(instrument7)
    instrument8 = Adder("Binary Adder", 25, 50)
    print(instrument8)

if __name__ == '__main__':
    main()
