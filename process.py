log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)

#There is a function called sales_reports. It takes in a param of log_file. Log_file opens the server.txt file. Then, there is a for loop that loops the list. R.stip method removes the white space. Then day equals the server.txt file. It has a starting index of zero. Then if day is true than print the line.


def numbers_reports(log_file):
    for line in log_file:
        line = line.rstrip().split(' ')
        count = int(line[2])
        if count > 10:
            print(line)
        
        