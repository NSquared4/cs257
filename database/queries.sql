SELECT nocs.noc_abbre 
FROM nocs 
ORDER BY noc_abbre ASC; 

SELECT Athletes.athlete_name 
FROM Athletes, Athletes_NOCs
WHERE Athletes.id = Athletes_NOCs.athlete_id 
AND Athletes_NOCs.noc_id = CAST(107 AS text);


SELECT Athletes.athlete_name, Medals.year, Medals.sport, Medals.medal_type 
FROM Athletes, Medals, Athletes_Medals
WHERE Athletes.id = CAST(71665 AS text)
AND Athletes.id = Athletes_Medals.athlete_id
ORDER BY Medals.year ASC; 


SELECT NOCs.noc_abbre, COUNT(NOCs_Medals.medal_id) 
FROM NOCs, NOCs_Medals, Medals
WHERE NOCs.id = NOCs_Medals.noc_id
AND NOCs_Medals.noc_id = Medals.id
AND Medals.medal_type = CAST("Gold" AS text) 
ORDER BY COUNT(NOCs_Medals.medal_id) DESC; 
