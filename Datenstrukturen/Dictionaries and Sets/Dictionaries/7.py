# Stimmen zaehlen und korrigieren

# Gegeben ist eine Liste mit den Namen der Kandidaten, fuer die abgestimmt wurde. Namen koennen mehrfach vorkommen:

# votes = ["red", "blue", "red", "green", "blue", "red", "yellow", "blue", "green", "red"]

# Erstelle ein Dictionary, das die Stimmen fuer jeden Kandidaten zaehlt. Ermittle die beiden Kandidaten mit den meisten Stimmen und gib einen Satz mit dem Gewinner, 
# dem Zweitplatzierten und ihren jeweiligen Stimmenzahlen aus. Ziehe anschliessend die folgenden ungueltigen Stimmen ab:

# invalid = {"red": 2, "blue": 1}

# Ziehe diese Stimmenzahlen von der Auszaehlung ab. Die angepasste Stimmenzahl eines Kandidaten darf dabei nie unter null sinken. Gib danach die angepassten Stimmenzahlen aus.

votes = ["red", "blue", "red", "green", "blue", "red", "yellow", "blue", "green", "red"]
invalid = {"red": 2, "blue": 1}


vote_counts = {}
for vote in votes:
    if vote not in vote_counts:
        vote_counts[vote] = 1
    else:
        vote_counts[vote] += 1


highest_count = max(vote_counts.values())
first_place = [
    candidate for candidate, count in vote_counts.items()
    if count == highest_count
]

second_count = max(
    (count for count in vote_counts.values() if count < highest_count),
    default=None,
)
second_place = [
    candidate for candidate, count in vote_counts.items()
    if count == second_count
]

if len(first_place) > 1:
    print(
        f"Gleichstand auf dem ersten Platz: {', '.join(first_place)} "
        f"haben jeweils {highest_count} Stimmen."
    )
else:
    print(f"{first_place[0]} hat mit {highest_count} Stimmen gewonnen.")

if second_place:
    print(
        f"Auf dem zweiten Platz: {', '.join(second_place)} "
        f"mit jeweils {second_count} Stimmen."
    )
elif len(first_place) == 1:
    print("Es gibt keinen getrennten zweiten Platz.")

for invalid_vote, invalid_count in invalid.items():
    if invalid_vote in vote_counts:
        vote_counts[invalid_vote] = max(
            0, vote_counts[invalid_vote] - invalid_count
        )

print("Angepasste Stimmenzahlen:", vote_counts)