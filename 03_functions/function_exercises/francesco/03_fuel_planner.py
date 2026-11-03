def calculate_stage_fuel(distance, fuel_per_unit):
    return distance * fuel_per_unit

def calculate_reserve(required_fuel, reserve_percent):
    return required_fuel * reserve_percent / 100

def calculate_total_fuel(stage_fuels, reserve_percent):
    required_fuel = 0
    for stage_fuel in stage_fuels:
        required_fuel += stage_fuel

    reserve_fuel = calculate_reserve(required_fuel, reserve_percent)
    return required_fuel + reserve_fuel

def mission_summary(distances, fuel_rates, reserve_percent):
    stage_fuels = []
    for index in range(len(distances)):
        stage_fuels.append(calculate_stage_fuel(distances[index], fuel_rates[index]))
    return calculate_total_fuel(stage_fuels, reserve_percent)


number_of_stages = int(input('Number of stages: '))
distances = []
fuel_rates = []
stage_fuels = []

for stage in range(1, number_of_stages + 1):
    distance = float(input(f'Distance of stage {stage}: '))
    fuel_per_unit = float(input(f'Fuel per unit for stage {stage}: '))
    distances.append(distance)
    fuel_rates.append(fuel_per_unit)

    stage_fuel = calculate_stage_fuel(distance, fuel_per_unit)
    stage_fuels.append(stage_fuel)

reserve_percent = float(input('Reserve percentage: '))
for stage, stage_fuel in enumerate(stage_fuels, start=1):
    print(f'Stage {stage} fuel: {stage_fuel}')

fuel_before_reserve = 0
for stage_fuel in stage_fuels:
    fuel_before_reserve += stage_fuel

reserve_fuel = calculate_reserve(fuel_before_reserve, reserve_percent)
total_fuel = mission_summary(distances, fuel_rates, reserve_percent)

print(f'Fuel before reserve: {fuel_before_reserve}')
print(f'Reserve fuel: {reserve_fuel}')
print(f'Total fuel required: {total_fuel}')