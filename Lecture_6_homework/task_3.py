location: list[tuple[str, float, float]] = [("Tbilisi", 41.71, 44.82),
            ("Batumi", 41.64, 41.63),
            ("Kutaisi", 42.26, 42.71)
            ]
for city, latitude, longitude in location:
    print(f"city: {city}, latitude: {latitude}, longitude: {longitude}")

city_names: list[str] = [city for city, latitude, longitude in location]
print(city_names)

