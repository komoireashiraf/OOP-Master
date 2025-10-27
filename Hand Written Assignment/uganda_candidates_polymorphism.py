# Base class
class PoliticalParty:
    def __init__(self, name, candidate_name):
        self.name = name
        self.candidate_name = candidate_name

    def slogan(self):
        pass


# Subclass 1 - NRM
class NRM(PoliticalParty):
    def __init__(self):
        super().__init__("National Resistance Movement (NRM)", "Yoweri Kaguta Museveni")

    def slogan(self):
        return "Protecting The Gains!"


# Subclass 2 - NUP
class NUP(PoliticalParty):
    def __init__(self):
        super().__init__(
            "National Unity Platform (NUP)", "Robert Kyagulanyi Ssentamu (Bobi Wine)"
        )

    def slogan(self):
        return "People Power, Our Power!"


# Subclass 3 - FDC
class FDC(PoliticalParty):
    def __init__(self):
        super().__init__("Forum for Democratic Change (FDC)", "Patrick Oboi Amuriat")

    def slogan(self):
        return "One Uganda, One People, One People, One Uganda!"


# Create candidate objects
candidate1 = NRM()
candidate2 = NUP()
candidate3 = FDC()

# List of candidates
candidates = [candidate1, candidate2, candidate3]

# Display party, candidate, and slogan
for c in candidates:
    print(f"Party: {c.name}")
    print(f"Candidate: {c.candidate_name}")
    print(f"Slogan: {c.slogan()}")
    print("-" * 60)
