#This is a simple Python project for oneNAV. It will read nmea log files from Beidou satellite and calculate average SNRs
from symbol import continue_stmt


def read_lines(path):       #Read all lines of the file as a list of strings
    with open(path) as nmea_log:
        return nmea_log.readlines()

def epoch_time(line):
    fields = line.split(",")
    raw_time = fields[1]    #Taking the first field as raw time data

    #Partition them by hours, minutes and seconds
    hours = raw_time[0:2]
    minutes = raw_time[2:4]
    seconds = raw_time[4:]
    return hours + ":" + minutes + ":" + seconds

def beidou_snrs(line):
    line = line.strip()     #remove invisible new line
    if not line.startswith("$GBGSV"):
        return[]            #non BeiDou lines return empty list

    #Example: $GBGSV,2,1,06,11,,,45,27,,,46,29,,,44,30,,,47,5*7A
    no_checksum = line.split("*")[0]    #Remove *7A checksum
    fields = no_checksum.split(",")    #Make individual fields
    data = fields[4:]   #Remove first 4 index to keep only snr related data

    if len(data) % 4 == 1:
        data = data[:-1]    #Remove the last item (signal ID)

    snrs = []
    for item in range(0, len(data), 4):
        prn_snr = data[item:item + 4]   #Keep only prn ID and SNRs from group of four's

        prn = prn_snr[0]    #Satellite ID
        snr = prn_snr[3]    #SNR value

        if prn == "" or snr == "":
            continue                   #Skip block if PRN or SNR is absent

        try:
            snrs.append(int(snr))
        except ValueError:
            continue
    return snrs

def main():
    lines = read_lines("logs/example-1.nmea")

    for line in lines:
        if line.startswith("$GBGSV"):
            print (beidou_snrs(line))


if __name__ == '__main__':
    main()
