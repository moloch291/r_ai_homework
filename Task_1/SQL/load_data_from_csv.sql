-- After setting up read permissions:
COPY neighbourhood(
            neighbourhood_group,
            neighbourhood_name
    )
FROM 'C:\Users\moloch\Code\RevenueAI_Homework\Task_1\CSVs\neighbourhoods.csv'
DELIMITER ','
-- Specify encoding to avoid messing up characters from spanish alphabet:
ENCODING 'UTF-8'
CSV HEADER;

COPY review(
        listing_id,
        review_date
    )
FROM 'C:\Users\moloch\Code\RevenueAI_Homework\Task_1\CSVs\reviews.csv'
DELIMITER ','
CSV HEADER;

COPY calendar(
         listing_id,
         day,
         available,
         price,
         adjusted_price,
         minimum_nights,
         maximum_nights
    )
FROM 'C:\Users\moloch\Code\RevenueAI_Homework\Task_1\CSVs\calendar.csv'
DELIMITER ','
CSV HEADER;

COPY listing(
        id, name, host_id, host_name, neighbourhood_group, neighbourhood_name, latitude, longitude,
        room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month,
        calculated_host_listings_count,availability_365,number_of_reviews_ltm, licence
    )
FROM 'C:\Users\moloch\Code\RevenueAI_Homework\Task_1\CSVs\listings.csv'
DELIMITER ','
ENCODING 'UTF-8'
CSV HEADER;