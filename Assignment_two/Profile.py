class Profile:
    def __init__(
        self, name, favorite_language, hobby, tech_stack, github_username, fun_fact
    ):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(
            f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}."
        )
        print(f"Fun fact about me: {self.fun_fact}")

    def show_stack(self):
        print(f"{self.name}'s Tech Stack:")
        for i, tool in enumerate(self.tech_stack, start=1):
            print(f"{i}. {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# Creating my profile
my_profile = Profile(
    name="Komoire Ashiraf",
    favorite_language="JavaScript",
    hobby="playing chess",
    tech_stack=["JavaScript", "HTML", "CSS", "Git", "React", "Node.js", "Figma"],
    github_username="komoireashiraf",
    fun_fact="I know but I can't speak my mother tongue!",
)

# Calling the methods
my_profile.introduce()
print()
my_profile.show_stack()
print()
print("GitHub Profile:", my_profile.github_link())
