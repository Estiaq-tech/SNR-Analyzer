#This is a simple Python project for oneNAV. It will read nmea log files from Beidou satellite and calculate average SNRs


def read_lines(path):       #Read all lines of the file as a list of strings
    with open(path) as nmea_log:
        return nmea_log.readlines()


def main():
    lines = read_lines("logs/example-1.nmea")

    count_gngga = 0
    for line in lines:
        if line.startswith("$GNGGA"):
            count_gngga+=1

    print("Total lines:", len(lines))
    print("GNGGA messages (epochs):", count_gngga)


if __name__ == '__main__':
    main()
