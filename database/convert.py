#Martin Bernard and Kevin Chen 
import csv 

def create_athletes_csv(athlete_events):
    """
        Write the id, name, age, height, weight, and sport columns from athlete_events.csv into Athletes.csv

        input: athlete_events.csv
        output: 
    """
    athlete_events_csv = athlete_events
    duplication_dict = {}

    #open athlete_event.csv
    with open(athlete_events_csv, mode ='r') as file:
        csv_file = csv.reader(file)

        #write into Athletes.csv
        with open('Athletes.csv', mode='w') as athlete_info:
            athlete_writer = csv.writer(athlete_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for csv_row in csv_file:
                if csv_row[0] not in duplication_dict:
                    duplication_dict[csv_row[0]] = ""
                    athlete_writer.writerow([csv_row[0], csv_row[1], csv_row[3], csv_row[4], csv_row[5], csv_row[12]])

def main():
    create_athletes_csv('athlete_events.csv')

if __name__ == "__main__":
    main()