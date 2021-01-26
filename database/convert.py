#Martin Bernard and Kevin Chen 
import csv 


def create_athletes_csv(athlete_events):
    """
        Write the id, name, age, height, weight, and sport columns from athlete_events.csv into Athletes.csv

        input: athlete_events.csv
        output: None
    """
    athlete_events_csv = athlete_events
    duplication_dict = {}

    #open athlete_event.csv
    with open(athlete_events_csv, mode ='r') as file:
        csv_file = csv.reader(file)

        #write into Athletes.csv
        with open('Athletes.csv', mode='w') as athlete_info:
            athlete_writer = csv.writer(athlete_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            print("Creating Athletes.csv file...")

            for csv_row in csv_file:
                if csv_row[0] not in duplication_dict:
                    duplication_dict[csv_row[0]] = ""
                    athlete_writer.writerow([csv_row[0], csv_row[1], csv_row[3], csv_row[4], csv_row[5], csv_row[12]])

            print("...complete\n")

def create_nocs_csv(noc_regions):
    """
        Write NOC column from noc_regions.csv into NOCs.csv and create a unique id for each noc 
        
        input: nocs_regions.csv
        output: None
    """
    noc_regions_csv = noc_regions
    noc_id = 0
    
    #open noc_regions.csv and reads it
    with open(noc_regions_csv, mode = 'r') as file: 
        csv_file = csv.reader(file)
        
        #writes into NOCs.csv
        with open('NOCs.csv', mode = 'w') as noc_info:
            noc_writer = csv.writer(noc_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            print("Creating NOCs.csv file...")
            noc_writer.writerow(["ID", "NOC"])

            for csv_row in csv_file:
                if csv_row[0] != "NOC":
                    noc_writer.writerow([noc_id, csv_row[0]])
                noc_id += 1
            print("...complete\n")

def create_athlete_noc_csv(athlete_event_file, nocs_file):
    """
        Write the id, name, age, height, weight, and sport columns from athlete_events.csv into Athletes.csv

        input: athlete_events.csv
        output: None

        2: Match the athlete_id to ID in athlete_events.csv
        3: If match get the NOC of the ID in athlete_events.csv
        4: Get the noc_id from NOCs.csv 
        4: Add athlete_id and noc_id to Athletes_NOCs.csv 
    """

    athlete_event_csv = athlete_event_file
    noc_csv = nocs_file 

    athlete_id = 0
    noc = ""
    noc_id = 0
    noc_id_dict = {}


    with open(athlete_event_csv, mode='r') as open_athlete_event:
        athlete_event_reader = csv.reader(open_athlete_event)

        with open(noc_csv, mode='r') as open_noc:
            noc_reader = csv.reader(open_noc)
            
            for noc_row in noc_reader:
                if noc_row[0] != "ID" and noc_row[1] != "NOC":
                    noc_id_dict[noc_row[1]] = noc_row[0]

            with open('Athletes_NOCs.csv', mode='w') as open_athlete_noc:
                athlete_noc_writer = csv.writer(open_athlete_noc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                #create field header column
                athlete_noc_writer.writerow(["athlete_id", "noc_id"])

                print("Creating Athletes_NOCs.csv...")
                for id_and_noc in athlete_event_reader:
                    if id_and_noc[0] != "ID" and id_and_noc[7] != "NOC":
                        athlete_id = id_and_noc[0]
                        noc = id_and_noc[7]
                        noc_id = noc_id_dict[noc]

                        athlete_noc_writer.writerow([athlete_id, noc_id])
                print("...complete\n")

def medal_id(athlete_events):
    athlete_event_csv = athlete_events

    with open(athlete_event_csv, mode='r') as open_athlete_event:
        pass

def main():
    #create_athletes_csv('athlete_events.csv')
    #create_nocs_csv('noc_regions.csv')
    create_athlete_noc_csv('athlete_events.csv', 'NOCs.csv')

if __name__ == "__main__":
    main()