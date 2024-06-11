import re

# a regular expression pattern to extract information from each log entry
log_pattern = re.compile(r'(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\w+)\s+(\w+)\[(\d+)\]: \[(\d+\.\d+)\] (\S+)\s+\{(.*?)\}')

# Function to parse a single log entry
def parse_log_entry(log_entry):
    """
    Parses a single log entry string into a dictionary containing log entry details.
    
    Parameters:
    - log_entry (str): A single log entry string.
    
    Returns:
    - Dictionary containing the parsed log entry details, or None if the entry doesn't match the pattern.
    """
    match = log_pattern.match(log_entry)
    if match:
        return {
            "datetime": match.group(1),
            "hostname": match.group(2),
            "process_name": match.group(3),
            "process_id": int(match.group(4)),
            "timestamp": float(match.group(5)),
            "syslog_error_level": match.group(6),
            "log_contents": match.group(7)
        }
    else:
        return None

# Function to read and parse the log file
def parse_log_file(hardware_log):
    """
    Reads and parses the log file line by line, printing the details of each log entry.
    
    Parameters:
    - hardware_log (str): The path to the log file to be parsed.
    """
    with open(hardware_log, 'r') as file:
        for line in file:
            log_entry = parse_log_entry(line)
            if log_entry:
                print("Datetime:", log_entry["datetime"])
                print("Hostname:", log_entry["hostname"])
                print("Process Name:", log_entry["process_name"])
                print("Process ID:", log_entry["process_id"])
                print("Timestamp:", log_entry["timestamp"])
                print("Syslog Error Level:", log_entry["syslog_error_level"])
                print("Log Contents:", log_entry["log_contents"])
                print("--------------------------------------------")


parse_log_file("hardware_log.log")

