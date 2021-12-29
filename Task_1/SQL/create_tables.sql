DROP TABLE IF EXISTS neighbourhood;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS calendar;
DROP TABLE IF EXISTS listing;

CREATE TABLE listing (
    id int,
    name text,
    host_id int,
    host_name text,
    neighbourhood_group text,
    neighbourhood_name text,
    latitude float,
    longitude float,
    room_type text,
    price float,
    minimum_nights int,
    number_of_reviews int,
    last_review date,
    reviews_per_month float,
    calculated_host_listings_count int,
    availability_365 int,
    number_of_reviews_ltm int,
    licence varchar
);

CREATE TABLE neighbourhood (
    neighbourhood_group varchar(200),
    neighbourhood_name varchar(200)
);

/* If I would plan to update this database I'd define the 'listing_id' columns
   in the following tables as a foreign key but since I just want to read data,
   here it isn't necessary: */

CREATE TABLE review (
    listing_id int,
    review_date date
);

CREATE TABLE calendar (
    listing_id int,
    day date,
    available boolean,
    price text,
    adjusted_price text,
    minimum_nights int,
    maximum_nights int
);