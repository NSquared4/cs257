CREATE TABLE Athletes (
    id SERIAL,
    name text,
    age integer,
    height integer,
    weight integer,
    sport text
);

CREATE TABLE NOCs (
    id SERIAL,
    name text,
);

CREATE TABLE Medals (
    id SERIAL,
    year integer,
    city text,
    event text
);

CREATE TABLE Athletes_NOCs (
    athlete_id integer,
    NOC_id integer
);
CREATE TABLE Athletes_Medals (
    athlete_id integer,
    medal_id integer
);
