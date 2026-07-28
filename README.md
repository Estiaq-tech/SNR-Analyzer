# SNR-Analyzer
A project as part of the interview with OneNAV. This project is a command-line tool that reads NMEA log files and prints the average SNR of BeiDou satellites for each epoch.

# Instructions for running the tool
    ./run.sh logs/Example-1.nmea logs/Example-2.nmea ........
    python3 analyze_snr.py logs/Example-1.nmea logs/Example-2.nmea ........

It needs only Python 3.

# How it works
The tool "analyze_snr.py" is one file with few small functions:

- read_lines(path) : reads the file's lines
- epoch_time(line) : reads the time from a GNGGA message and sorts them by this format (HH:MM:SS.ss)
- beidou_snrs(line) : extracts SNR values from a BeiDou satellite ($GBGSV) message
- analyze_file(path) : groups messages into epochs with their BeiDou SNRs
- print_report(path, epochs) : Make an average of SNRs per epoch and prints the result table
- main() : command line and error handling

# Error handling
- Missing or unreadable files gives a clear message and a non-zero exit status.
- A broken or malformed line is skipped so that the tool doesn't crashes the run.
- Empty epochs are reported clearly with No BeiDou Observation

# AI Usage Statement
I used AI (Claude and Gemini) as a part of my learning progress and review aid while building this tool. It explained overall approach and structure of an NMEA parser. It helped me understand the GSV message format (blocks of four fields and the trailing signal ID field). I wrote the code myself function by function, and verified each part against the real log file given to me. When I hit bugs, AI helped me to diagnose them (eg: an indentation error), which I fixed by myself.

AI usage statement is also included in the individual commit messages.
