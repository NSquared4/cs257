SELECT * FROM NOCs ORDER BY NOC ASC; 

SELECT Athletes.athlete_name FROM Athletes WHERE Athletes.id = Athletes_NOCs.athlete_id AND Athletes_NOCs.noc_id = "107";

SELECT Athletes.athlete_name, Medals.year, Medals.sport, Medals.medal_type 
FROM Athletes, Medals 
WHERE Athletes.id = "71665"
AND Athletes.id = Athletes_Medals.athlete_id
ORDER BY Medals.year ASC; 

SELECT NOCs.noc_abbre, COUNT(NOCs_Medals.medal_id) FROM NOCs, NOCs_Medals 
WHERE NOCs.id = NOCs_Medals.noc_id
AND NOCs_Medals.noc_id = Medals.id
AND Medals.medal_type = "Gold" 
ORDER BY COUNT(NOCs_Medals.medal_id) DESC; 