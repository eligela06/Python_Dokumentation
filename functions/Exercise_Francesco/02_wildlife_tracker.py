def count_sightings(observations):
    return len(observations)


def count_species(observations, species):
    count = 0
    for observation in observations:
        if observation.lower() == species.lower():
            count += 1
    return count


def unique_species(observations):
    result = []
    seen = []
    for observation in observations:
        normalized = observation.lower()
        if normalized not in seen:
            result.append(observation)
            seen.append(normalized)
    return result


def create_report(observations, species):
    unique = unique_species(observations)
    return (
        count_sightings(observations),
        len(unique),
        count_species(observations, species),
        unique,
    )


number_of_sightings = int(input('Number of sightings: '))
observations = []
for sighting_number in range(number_of_sightings):
    name = input(f'Species for sighting {sighting_number + 1}: ')
    observations.append(name)

species_to_count = input('Species to count: ')
total, different_species, species_count, distinct_species = create_report(
    observations, species_to_count
)

print(f'Total sightings: {total}')
print(f'Different species: {different_species}')
print(f'Sightings of {species_to_count}: {species_count}')
print(f'Unique species: {distinct_species}')
 