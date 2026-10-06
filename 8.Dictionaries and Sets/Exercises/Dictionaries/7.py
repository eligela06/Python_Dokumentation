# Stimmen zaehlen und korrigieren

# Gegeben ist eine Liste mit den Namen der Kandidaten, fuer die abgestimmt wurde. Namen koennen mehrfach vorkommen:

# votes = ["red", "blue", "red", "green", "blue", "red", "yellow", "blue", "green", "red"]

# Erstelle ein Dictionary, das die Stimmen fuer jeden Kandidaten zaehlt. Ermittle die beiden Kandidaten mit den meisten Stimmen und gib einen Satz mit dem Gewinner, dem Zweitplatzierten und ihren jeweiligen Stimmenzahlen aus. Ziehe anschliessend die folgenden ungueltigen Stimmen ab:

# invalid = {"red": 2, "blue": 1}

# Ziehe diese Stimmenzahlen von der Auszaehlung ab. Die angepasste Stimmenzahl eines Kandidaten darf dabei nie unter null sinken. Gib danach die angepassten Stimmenzahlen aus.

votes = ["red", "blue", "red", "green", "blue", "red", "yellow", "blue", "green", "red"]
invalid = {"red": 2, "blue": 1}


votes_dict = {}
for vote in votes:
    if vote not in votes_dict:
        votes_dict[vote] = 1
    else:
        votes_dict[vote] += 1


first_place = max(votes_dict, key=votes_dict.get)
other_candidates = {}

for candidate, count in votes_dict.items():
    if candidate == first_place:
        continue
    else:
        other_candidates[candidate] = count

second_place = max(other_candidates, key=other_candidates.get)

if votes_dict[first_place] == votes_dict[second_place]:
    tied_candidates = [
        candidate for candidate, count in votes_dict.items()
        if count == votes_dict[first_place]
    ]
    print(f"Gleichstand: {', '.join(tied_candidates)} haben jeweils {votes_dict[first_place]} Stimmen.")
else:
    print(
        f"{first_place} hat mit {votes_dict[first_place]} Stimmen gewonnen; "
        f"{second_place} ist mit {votes_dict[second_place]} Stimmen Zweiter."
    )

for invalid_vote, invalid_count in invalid.items():
    if invalid_vote in votes_dict:
        votes_dict[invalid_vote] = max(0, votes_dict[invalid_vote] - invalid_count)

print("Angepasste Stimmenzahlen:", votes_dict)