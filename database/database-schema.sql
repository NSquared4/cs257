CREATE TABLE Athletes (
    id SERIAL,
    athlete_name text,
    age integer,
    height integer,
    athlete_weight integer,
    sport text
);

CREATE TABLE NOCs (
    id SERIAL,
    noc_abbre text,
);

CREATE TABLE Medals (
    id SERIAL,
    year integer,
    sport text,
    medal_type integer
);

CREATE TABLE NOCs_Medals (
    noc_id integer,
    medal_id integer
);

CREATE TABLE Athletes_NOCs (
    athlete_id integer,
    noc_id integer
);
CREATE TABLE Athletes_Medals (
    athlete_id integer,
    medal_id integer
);
