# Order-preserving deduplication

# You are given a log of repeated action names:

# log = ["login", "click", "click", "scroll", "login", "purchase", "scroll", "logout", "click"]

# Deduplicate log while preserving the original order of first appearance, using a set as a "seen" tracker alongside a list. Then verify your result matches list(dict.fromkeys(log)).


logs = ["login", "click", "click", "scroll", "login", "purchase", "scroll", "logout", "click"]

seen = set()

logs_new = []

for log in logs:
    if log not in seen:
        seen.add(log)
        logs_new.append(log)
print(logs_new)
print(list(dict.fromkeys(logs)))

print(logs_new == list(dict.fromkeys(logs)))