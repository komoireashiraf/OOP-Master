# 3. African Countries
class Country:
    def _init_(self, name, capital, population, language):
        self.name = name
        self.capital = capital
        self.population = population
        self.language = language


country1 = Country("Uganda", "Kampala", "48 million", "English and Luganda")
country2 = Country("Kenya", "Nairobi", "55 million", "Swahili and English")
country3 = Country("Nigeria", "Abuja", "223 million", "English")
country4 = Country("Egypt", "Cairo", "110 million", "Arabic")
country5 = Country(
    "South Africa", "Pretoria", "60 million", "Zulu, Xhosa, Afrikaans, English"
)
