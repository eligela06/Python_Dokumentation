# Extracting unique values from parsed strings

# You are given a list of email addresses:

# emails = ["ana@example.com", "ben@school.edu", "cid@example.com",
#          "dea@work.org", "eli@school.edu", "fay@example.com"]

# Build a set of the unique domains (the part after @) across all addresses. Then build a second set containing just the organization name in uppercase, without the top-level domain (e.g., "example.com" → "EXAMPLE").




emails = ["ana@example.com", "ben@school.edu", "cid@example.com",
         "dea@work.org", "eli@school.edu", "fay@example.com"]

domains = set()
organizations = set()

for email in emails:
    at = email.find("@")
    domain = email[at+1:]
    domains.add(domain)

for domain in domains:
    point = domain.find(".")
    organization = domain[0:point].upper()
    organizations.add(organization)

print("Domains: ",domains)
print("Organizations: ",organizations)
