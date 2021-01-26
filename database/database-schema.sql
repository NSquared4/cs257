CREATE TABLE Athletes (
    id SERIAL,
    _name text,
    age integer,
    height integer,
    _weight integer,
    sport text
);

CREATE TABLE NOCs (
    id SERIAL,
    noc_abbre text,
);

CREATE TABLE Medals (
    id SERIAL,
    year integer,
    medal_type integer,
    
);

CREATE TABLE NOCs_Medals (
    NOC_id integer,
    medal_id integer
);

CREATE TABLE Athletes_NOCs (
    athlete_id integer,
    NOC_id integer
);
CREATE TABLE Athletes_Medals (
    athlete_id integer,
    medal_id integer
);
