CREATE TABLE Athletes (
    id text,
    athlete_name text,
    age text,
    height text,
    athlete_weight text,
    sport text
);

CREATE TABLE NOCs (
    id text,
    noc_abbre text
);

CREATE TABLE Medals (
    id text,
    year text,
    sport text,
    medal_type text
);

CREATE TABLE NOCs_Medals (
    noc_id text,
    medal_id text
);

CREATE TABLE Athletes_NOCs (
    athlete_id text,
    noc_id text
);
N
