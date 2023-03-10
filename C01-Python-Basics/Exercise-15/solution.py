def gas_stations(distance, tank_size, stations):
    result = []

    stations_target = [ station for station in stations
                             if station < distance] + [distance]
    
    diffs = [stations_target[0]]

    for i in range(0, len(stations_target) - 1):
        diffs.append(stations_target[i + 1]- stations_target[i])
    
    fuel = tank_size

    for index, diff in enumerate(diffs):
        fuel -= diff

        if fuel <= 0:
            fuel = tank_size - diff

            if fuel <= 0:
                return []
            
            result.append(stations[index - 1])

    return result

tests = [
    (320, 90, [50, 80, 140, 180, 220, 290], [80, 140, 220, 290]),
    (390, 80, [70, 90, 140, 210, 240, 280, 350], [70, 140, 210, 280, 350]),
    (100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150], [40, 80]),
    (100, 50, [10, 90], []),
    (100, 101, [200], []),
    (100, 50, [200], [])
]

for distance, tank_size, stations, expected in tests:
    print(gas_stations(distance, tank_size, stations) == expected)