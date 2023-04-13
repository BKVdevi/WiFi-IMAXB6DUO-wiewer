
def worker(code, pos, prevs):
    #a = "pos ->"+str(pos)
    a = ""
    match pos:
        case 1:
            a += "Zoomer ->"
            if code & (1<<2):
                a += "ON "
            else:
                a += "OFF "
            a+="\nButt_sig ->"
            if code & (1<<3):
                a += "ON "
            else:
                a += "OFF "
            a+="\nOFF by CAP ->"
            if code & (1<<4):
                a += "ON "
            else:
                a += "OFF "
            a+="\nOFF by time ->"
            if code & (1<<5):
                a += "ON "
            else:
                a += "OFF "
            a+="\nOFF by temp ->"
            if code & (1<<6):
                a += "ON "
            else:
                a += "OFF "
        case 2:
            a += "NiMh sensitivity ->"
            a += str(code -128) + "mV"
        case 3:
            a += "NiCd sensitivity ->"
            a += str(code -128) + "mV"
        case 4:
            a += "Off temp ->"
            a += str(code -128) + "deg C"
        case 5:
            a += "CHG>DCHG pause ->"
            a += str(code -128) + "min"
        case 7:
            a += "Min input voltage ->"
            a += str((code -128)/10.0) + "V"
        case 8:
            a += "Mode ->"
            if code & (1<<5):
                a += "CHG>DSC "
            else:
                a += "DSC>CHG "
            a+="Process ->"
            if code & (1<<6):
                a += "CHG "
            else:
                a += "DSC "
        case 9:
            a += "NiCD charge current ->"
            a += str((code -128)/10.0) + "A"
        case 10:
            a += "NiCD dischg current ->"
            a += str((code -128)/10.0) + "A"
        case 11:
            a += "NiCD mode ->"
            a += str(hex(code)) + "\t\t\t---no info---"
        case 12:
            a += "NiCD cycles ->"
            a += str((code -128)) + "cycles"
        case 13:
            a += "NiMH charge current ->"
            a += str((code -128)/10.0) + "A"
        case 14:
            a += "NiMH dischg current ->"
            a += str((code -128)/10.0) + "A"
        case 15:
            a += "NiMH mode ->"
            a += str(hex(code)) + "\t\t\t---no info---"
        case 16:
            a += "NiMH cycles ->"
            a += str((code -128)) + "cycles"
        case 17:
            a += "Lipo charge current ->"
            a += str((code -128)/10.0) + "A"
        case 18:
            a += "Lipo carge cells ->"
            a += str(code - 128)
        case 19:
            a += "NiMH dischg current ->"
            a += str((code -128)/10.0) + "A"
        case 20:
            a += "Lipo discarge cells ->"
            a += str(code - 128)
        case 21:
            a += "Pb charge current ->"
            a += str((code -128)/10.0) + "A"
        case 22:
            a += "Pb cells ->"
            a += str(code - 128)+"cells"
        case 23:
            a += "Charger MODE ->"
            match code:
                case 128:
                    a+= "USER"
                case 129:
                    a+= "LiPo"
                case 130:
                    a+= "NiMh"
                case 131:
                    a+= "NiCd"
                case 132:
                    a+= "Pb"
                case 133:
                    a+= "save batt"
                case 134:
                    a+= "load"
        case 24:
            a += "plot mode->"
            match code:
                case 128:
                    a+= "WAIT"
                case 129:
                    a+= "ACTIVE"
        case 26:
            a += "NiMh discahge end voltage->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 28:
            a += "NiCd discahge end voltage->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 30:
            a += "Save timer ->"
            a += str((code - 128)*10)+"min"
        case 32:
            a += "End capacyty for turn off->"
            a += str(((code - 128)*100 + prev - 128)/100)+"mA/h"
        case 34:
            a += "Log. accum Current->"
            a += str(((code - 128)*100 + prev - 128)/100)+"A"
        case 36:
            a += "Log. accum Voltage->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 38:
            a += "Log. ext Temp->"
            a += str(((code - 128)*100 + prev - 128))+"degCels"
        case 40:
            a += "Log. int Temp->"
            a += str(((code - 128)*100 + prev - 128)/100.0)+"degCels"
        case 42:
            a += "Log. inp Voltage->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 44:
            a += "Log. now Capacyty->"
            a += str(((code - 128)*100 + prev - 128))+"mAh"
        case 46:
            a += "Log. LiPo Cell 1->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 48:
            a += "Log. LiPo Cell 2->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 50:
            a += "Log. LiPo Cell 3->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 52:
            a += "Log. LiPo Cell 4->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 54:
            a += "Log. LiPo Cell 5->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 56:
            a += "Log. LiPo Cell 6->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 58:
            a += "Log. LiPo Cell 7->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 60:
            a += "Log. LiPo Cell 8->"
            a += str(((code - 128)*100 + prev - 128)/100)+"V"
        case 70:
            a += "Time displayed->"
            a += str(((code - 128)*100 + prev - 128)/100)+"min"

    return a

file_read = open("log-dynamic.txt", "r");
file_write = open("decode_log-full.txt", "w");
writed = 0;
line = 0
prev = 0
mode = "none"
byte_num = 0;
for a in file_read.read().replace("\n", " ").split(" "):
    if a == '': continue
    b = int(a, 16)
    if b == int("0x7b", 16) and prev == int("0x7d", 16):
        if mode == "stay":
            file_write.write("\n}"+mode+"\n\n")
        writed = 1
        line = 0
        file_write.write("{\n")
        byte_num = 1;
        mode = "normal"
    if b == int("0x7d", 16) and prev == int("0x7b", 16):
        if mode == "normal":
            file_write.write("\n}"+mode+"\n\n")
        writed = 1
        line = 0
        file_write.write("{\n")
        byte_num = 1;
        mode = "stay"
    if b == int("0x7d", 16) and mode == "normal":
        writed = 0
        file_write.write("\n}"+mode+"\n\n")
        mode = "none"
    if b == int("0x7b", 16) and mode == "stay":
        writed = 0
        file_write.write("\n}"+mode+"\n\n")
        mode = "none"
    if writed == 1 and b != int("0x7b", 16) and b != int("0x7d", 16) :
        htt = worker(b, byte_num, prev)
        if htt != '':
            file_write.write(str(htt))
            if byte_num != 70: file_write.write('\n')
        byte_num += 1
    prev = b
file_read.close()
file_write.close()