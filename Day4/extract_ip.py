ip_address = []
with open("sample_logs.log","r") as log:
    lines=log.readlines()

    for line in lines:
        if "reverse mapping" in line:
            words=line.split("[")
            ip_addr=words[2].split("]")
            ip_address.append(ip_addr[0])
with open("ip_addr_out.txt","w") as ip:
    for addr in ip_address:
        ip.write(addr+"\n")
print("Ip addresses extracted successfully.")
#csv
#Texxt extraction
#Text file(same pgm)
#Questions for automated scripting
# 1.Disk usage monitoring script
# 2.Automatic file backup script
# 3.Log file error extractor
# 4.system resource monitor(memory,disc usage)(Total,used , free storage)(disk,memory,cpu usage)
#5.folder cleaner automation
#6.csv report generator
#7.password strength checker
#8.pinging multiple server checker
#9.file renamer script
#10.file manager(inside folder pdf images and stuff)
