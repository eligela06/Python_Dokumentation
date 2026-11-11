# Inverting a one-to-many mapping

# You are given a dictionary mapping each capital city to a population tier, where multiple cities can share a tier:

# capital_pop_tier = {
#   "Paris": "large", "Tokyo": "large", "Rome": "medium",
#   "Bern": "small", "Vienna": "medium", "Reykjavik": "small",
# }

# Invert it into a tier_to_capitals dictionary mapping each tier to a list of capitals sharing that tier.


capital_pop_tier = {
  "Paris": "large", "Tokyo": "large", "Rome": "medium",
  "Bern": "small", "Vienna": "medium", "Reykjavik": "small",
}

tier_to_capitals = {}

for capital, tier in capital_pop_tier.items():
    if tier not in tier_to_capitals:
        tier_to_capitals[tier] = []
    tier_to_capitals[tier].append(capital)

print(tier_to_capitals)