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
                    if csv_row[0] != "ID":
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

            for csv_row in csv_file:
                if csv_row[0] != "NOC":
                    noc_writer.writerow([noc_id, csv_row[0]])
                noc_id += 1
            print("...complete\n")

def create_athlete_noc_csv(athlete_event_file, nocs_file):
    """
        Create a csv linking Athletes and their respective NOCs

        input: athlete_events.csv, noc_regions.csv
        output: None
    """

    athlete_event_csv = athlete_event_file
    noc_csv = nocs_file 

    athlete_id = 0
    noc = ""
    noc_id = 0
    noc_id_dict = {}
    duplicationDict = {}

    #open athlete_events.csv
    with open(athlete_event_csv, mode='r') as open_athlete_event:
        athlete_event_reader = csv.reader(open_athlete_event)
        
        #open noc_regions.csv
        with open(noc_csv, mode='r') as open_noc:
            noc_reader = csv.reader(open_noc)
            
            #create helper dictionary 
            for noc_row in noc_reader:
                if noc_row[0] != "ID" and noc_row[1] != "NOC":
                    noc_id_dict[noc_row[1]] = noc_row[0]

            #open Athletes_NOCs.csv
            with open('Athletes_NOCs.csv', mode='w') as open_athlete_noc:
                athlete_noc_writer = csv.writer(open_athlete_noc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                print("Creating Athletes_NOCs.csv...")

                #populate Athletes_NOCs.csv 
                for id_and_noc in athlete_event_reader:
                    if id_and_noc[0] not in duplicationDict:
                        duplicationDict[id_and_noc[0]] = ""

                        if id_and_noc[0] != "ID" and id_and_noc[7] != "NOC":
                            athlete_id = id_and_noc[0]
                            noc = id_and_noc[7]
                            noc_id = noc_id_dict[noc]

                            athlete_noc_writer.writerow([athlete_id, noc_id])
                print("...complete\n")

def create_medal_csv(athlete_events):
    """
        Gives an id to each medals in athlete_events.csv

        input: athlete_events.csv
        output: None 
    """
    athlete_events_csv = athlete_events

    #open athlete_event.csv
    with open(athlete_events_csv, mode ='r') as file:
        csv_file = csv.reader(file)

        #write into Medals.csv
        with open('Medals.csv', mode='w') as medal_info:
            medal_writer = csv.writer(medal_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            print("Creating Medals.csv file...")

            medal_ID = 0

            #populate Medals.csv 
            for csv_row in csv_file:
                if str(csv_row[14]) == "NA" or csv_row[0] == "ID":
                    continue
                medal_ID += 1
                medal_writer.writerow([medal_ID, csv_row[9], csv_row[13], str(csv_row[14])])
                
            print("...complete\n")

def create_athlete_medal_csv(athlete_event_file, medal_file):
    """
       Create a csv linking athlete to their respective medals 

        input: athlete_events.csv, Medals.csv 
        output: None
    """

    athlete_event_csv = athlete_event_file
    medal_csv = medal_file

    athlete_id = 0
    medal_id = 0

    #open athlete_events.csv
    with open(athlete_event_csv, mode='r') as open_athlete_event:
        athlete_event_reader = csv.reader(open_athlete_event)

        #open Medals.csv
        with open(medal_csv, mode='r') as open_medal:
            medal_reader = csv.reader(open_medal)
            
            #open Athletes_Medals.csv
            with open('Athletes_Medals.csv', mode='w') as open_athlete_medal:
                athlete_medal_writer = csv.writer(open_athlete_medal, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                print("Creating Athletes_Medals.csv...")

                #populate Athletes_Medals.csv
                for row in athlete_event_reader:

                    if row[0] != "ID" and str(row[14]) != "NA":
                        athlete_id = row[0]

                        for medal in medal_reader:
                            if row[9] == medal[1] and row[13] == medal[2] and row[14] == medal[3]:
                                medal_id = medal[0]
                                break

                        athlete_medal_writer.writerow([athlete_id, medal_id])
                print("...complete\n")

def create_noc_medal(athlete_medal, athlete_noc):
    """
        Create a csv linking each country to their respective medals 

        input: Athletes_Medals.csv, Athletes.csv
        output: None 
    """
    athlete_medal_csv = athlete_medal
    athlete_noc_csv = athlete_noc
    athlete_noc_dict = {}

    #open Athlete_Medals.csv
    with open(athlete_medal_csv, mode='r') as open_athlete_medal:
        athlete_medal_reader = csv.reader(open_athlete_medal)

        #open Athletes.csv
        with open(athlete_noc_csv, mode='r') as open_athlete_noc:
            athlete_noc_reader = csv.reader(open_athlete_noc)

            #create a helper dictionary
            for row in athlete_noc_reader:
                athlete_noc_dict[row[0]] = row[1]

            #open NOCs_Medals.csv
            with open('NOCs_Medals.csv', mode='w') as open_noc_medal:
                noc_medal_writer = csv.writer(open_noc_medal, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                print("Creating NOCs_Medals.csv...")
                #populate NOCs_Medals.csv
                for row in athlete_medal_reader:
                    if row[0] != "athlete_id" and row[1] != "medal":
                        noc_medal_writer.writerow([athlete_noc_dict[row[0]], row[1]])
                print("...complete\n")


def main():
    create_athletes_csv('athlete_events.csv')
    create_nocs_csv('noc_regions.csv')
    create_athlete_noc_csv('athlete_events.csv', 'NOCs.csv')
    create_medal_csv('athlete_events.csv')
    create_athlete_medal_csv('athlete_events.csv', 'Medals.csv')
    create_noc_medal('Athletes_Medals.csv', 'Athletes_NOCs.csv')
    
if __name__ == "__main__":
    main()