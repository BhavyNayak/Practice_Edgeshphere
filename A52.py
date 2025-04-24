# 52. Extract domain names from a list of email addresses
def domain_extractor(emails):
    return [email.split('@')[1].split('.')[0] for email in emails if '@' in email ]

emails = [
    "alice@example.com",
    "bob@company.org",
    "carol@sub.domain.co",
    "invalidemail.com"
]
print(domain_extractor(emails))