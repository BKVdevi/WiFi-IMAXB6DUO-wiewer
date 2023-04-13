file_read = open("log-dynamic.txt", "r");
file_write = open("rev_log2.txt", "w");
writed = 0;
line = 0
prev = 0
mode = "none"
byte_num = 0;
for a in file_read.read().replace("\n", " ").split(" "):
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
        if line != 0:
            file_write.write(" "+hex(b)[2:])
        else:
            file_write.write(hex(b)[2:])
        line += 1
        if line == 16:
            file_write.write("\n")
            line = 0
        byte_num += 1
    prev = b
file_read.close()
file_write.close()
