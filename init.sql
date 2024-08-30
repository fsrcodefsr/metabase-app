CREATE TABLE candidates (
    id SERIAL PRIMARY KEY,
    iin VARCHAR(12) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    school VARCHAR(255),
    university VARCHAR(255),
    foreign_university VARCHAR(255),
    bolashak_scholarship VARCHAR(255),
    specialty VARCHAR(255),
    academic_degree VARCHAR(50),
    international_olympiads VARCHAR(255),
    republican_olympiads VARCHAR(255),
    regional_city_olympiads VARCHAR(255),
    republican_sports_competitions VARCHAR(255),
    regional_city_sports_competitions VARCHAR(255)
);