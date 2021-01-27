CREATE TABLE Athletes (
    id text,
    athlete_name text,
    age text,
    height text,
    athlete_weight text,
    sport text
);
\copy athletes from 'Athletes.csv' DELIMITER ',' CSV NULL AS 'NULL'

CREATE TABLE NOCs (
    id text,
    noc_abbre text
);
\copy nocs from 'NOCs.csv' DELIMITER ',' CSV NULL AS 'NULL'

CREATE TABLE Medals (
    id text,
    year text,
    sport text,
    medal_type text
);
\copy medals from 'Medals.csv' DELIMITER ',' CSV NULL AS 'NULL'

CREATE TABLE NOCs_Medals (
    noc_id text,
    medal_id text
);
\copy nocs_medals from 'NOCs_Medals.csv' DELIMITER ',' CSV NULL AS 'NULL'

CREATE TABLE Athletes_NOCs (
    athlete_id text,
    noc_id text
);
\copy athletes_nocs from 'Athletes_NOCs.csv' DELIMITER ',' CSV NULL AS 'NULL'

CREATE TABLE Athletes_Medals (
    athlete_id text,
    medal_id text
);
\copy athletes_medals from 'Athletes_Medals.csv' DELIMITER ',' CSV NULL AS 'NULL'
