# Counts all recorded sightings.
def count_sightings(observations):
    return len(observations)


# Counts sightings of a species, ignoring letter case.
def count_species(observations, species):
    count = 0
    for observation in observations:
        if observation.lower() == species.lower():
            count += 1
    return count


# Returns unique species, preserving the spelling of their first occurrence.
def unique_species(observations):
    result = []
    seen = []
    for observation in observations:
        normalized = observation.lower()
        if normalized not in seen:
            result.append(observation)
            seen.append(normalized)
    return result


# Combines the statistics and species list into a report.
def create_report(observations, species):
    unique = unique_species(observations)
    return (
        count_sightings(observations),
        len(unique),
        count_species(observations, species),
        unique,
    )


# Collects the observed species and the species to count.
number_of_sightings = int(input('Number of sightings: '))
observations = []
for sighting_number in range(number_of_sightings):
    name = input(f'Species for sighting {sighting_number + 1}: ')
    observations.append(name)

species_to_count = input('Species to count: ')
total, different_species, species_count, distinct_species = create_report(
    observations, species_to_count
)

# Displays the calculated statistics.
print(f'Total sightings: {total}')
print(f'Different species: {different_species}')
print(f'Sightings of {species_to_count}: {species_count}')
print(f'Unique species: {distinct_species}')
 