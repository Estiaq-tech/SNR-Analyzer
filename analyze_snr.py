#This is a simple Python project for oneNAV. It will read nmea log files from Beidou satellite and calculate average SNRs


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

def main():
    lines = read_lines("logs/example-1.nmea")

    for line in lines:
        if line.startswith("$GNGGA"):
            print (epoch_time(line))


if __name__ == '__main__':
    main()
