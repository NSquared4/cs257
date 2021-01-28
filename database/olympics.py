import sys
import psycopg2


def connect_to_database():
    """
        Connect to the 'olympic' databse

        input: none
        output: none
        return: connection, which is connected to the 'olympic' databse 
    """

    database = "olympics"
    user = ""
    password = ""

    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    return connection


def make_cursor(connect_to_database, query_statement):
    """
        Create the cursor that'll excute query_statements

        input: connect_to_databse, query_statement
        output: none
        return: data in cursor as a tuple
    """
    connection = connect_to_database

    try:
        cursor = connection.cursor()
        query = query_statement
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    
    return cursor.fetchall()


def find_id(noc_abbre):
    """
        Find the NOC ID when given a NOC abbreviation 
        
        input: NOC abbreviation
        output: none
        return: noc_id
    """
    noc_id = ""
    query = """SELECT id FROM NOCs WHERE noc_abbre = %s"""
    connection = connect_to_database()
    
    try:
        cursor = connection.cursor()
        cursor.execute(query, (noc_abbre,))
    except Exception as e:
        print(e)
        exit()
    
    noc_id = cursor.fetchone()

    #returns nothing if id is not found 
    if noc_id == None:
        return None
    else:
        return noc_id[0]


def list_athlete(noc_abbre):
    """
        Lists all athletes from the specified noc

        input: NOC abbreviation
        output: none
        return: none
    """
    
    search_noc = find_id(noc_abbre)
    connection = connect_to_database()
    query = '''SELECT Athletes.*, NOCs.noc_abbre
            FROM Athletes, Athletes_NOCs, NOCs 
            WHERE Athletes.id = Athletes_NOCs.athlete_id
            AND Athletes_NOCs.noc_id = NOCs.id 
            AND Athletes_NOCs.noc_id = CAST(%s AS text);
            '''
    
    try:
        cursor = connection.cursor()
        cursor.execute(query, (search_noc,))
    except Exception as e:
        print(e)
        exit()
    
    if search_noc == None:
        print("Country not found")
        exit()

    print('===== Athletes from {0} ====='.format(noc_abbre))
    for row in cursor:
        print(row[0], row[1])
    print()


def list_golds():
    """
        Lists all the country with gold medals in descending order of the number of gold medals
        
        input: none
        output: none
        return: none 
    """

    query = """SELECT NOCs.noc_abbre, COUNT(NOCs_Medals.noc_id) 
        FROM NOCs, NOCs_Medals, Medals 
        WHERE NOCs.id = NOCs_Medals.noc_id 
        AND NOCs_Medals.medal_id = Medals.id 
        AND Medals.medal_type = 'Gold' 
        GROUP BY NOCs.noc_abbre 
        ORDER BY COUNT(NOCs_Medals.noc_id) DESC;"""
    connection = connect_to_database()
    cursor = make_cursor(connection, query)

    print('===== Countries with Gold Medal =====')
    for row in cursor:
        print(row[0], row[1])


def list_events():
    """
        List all the events of the olympics
        
        input: none
        output: none
        return: none
    """
    query = """SELECT DISTINCT sport FROM athletes ORDER BY sport ASC;"""
    connection = connect_to_database()
    cursor = make_cursor(connection, query)
    
    print('===== List All Events =====')
    for row in cursor:
        print(row[0])
    print()


def main():
    #List of possible command line arguments
    argument_list = ["--help", "-h", "--list_noc_athletes", "-lna", "--list_golds", "-lg", "--events", "-e"]

    #open and reads the usage statement from usage.txt
    usage_txt = open('usage.txt', 'r')
    usage_statements = usage_txt.read()


    if len(sys.argv) < 2:
        print("-h or --help to get usage statement")
    else:
        if "--help" and "-h" not in str(sys.argv):
            index = 1
            while index < len(sys.argv):
                command = str(sys.argv[index])
                
                #checks to make sure the command is possible
                if command in argument_list: 

                    #lists the countries with gold medals from greatest to least 
                    if command == "--list_golds" or command == "-lg":
                        list_golds()
                    
                    #lists all the events in the olympics in alphabetical order
                    elif(command == "--events" or command == "-e"):
                        list_events()
                    
                    #lists all athletes from a specified NOC 
                    elif (command == "--list_noc_athletes" or command == "-lna" 
                        and index + 1 < len(sys.argv) 
                        and str(sys.argv[index + 1]) not in argument_list
                        and len(str(sys.argv[index +1])) <= 3):

                        noc = str(sys.argv[index + 1]).upper()
                        list_athlete(noc)
                        index += 1

                    #catches possible error with --list_noc_atheltes or -lna arguments
                    else:
                        if len(str(sys.argv[index +1])) > 3:
                            print("NOC abbreviation too long")
                        else:
                            print("Please enter a NOC abbrevation after", str(sys.argv[index]))
                        break
                    index += 1

                else:
                    print("-h or --help to get possible arguments")
                    break
                
        else:
            print(usage_statements)

if __name__ == "__main__":
    main()