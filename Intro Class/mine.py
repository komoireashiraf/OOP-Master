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
        print("+" + "-" * 50 + "+")
        print(f"| Name: {self.name:<42} |")
        print(f"| Favorite Language: {self.favorite_language:<28} |")
        print(f"| Hobby: {self.hobby:<39} |")
        print(f"| Fun Fact: {self.fun_fact:<34} |")
        print("+" + "-" * 50 + "+")

    def show_stack(self):
        print("\n" + "+" + "-" * 50 + "+")
        print(f"| {self.name}'s Tech Stack:{' '*28} |")
        print("+" + "-" * 50 + "+")
        for i, tool in enumerate(self.tech_stack, start=1):
            print(f"| {i}. {tool:<45} |")
        print("+" + "-" * 50 + "+")

    def github_link(self):
        link = f"https://github.com/{self.github_username}"
        print(f"\nGitHub Profile: {link}")


# Create your profile
my_profile = Profile(
    name="Ashiraf",
    favorite_language="JavaScript",
    hobby="playing chess",
    tech_stack=["JavaScript", "HTML", "CSS", "Git", "VS Code"],
    github_username="komoireashiraf",
    fun_fact="I can solve a Rubik's cube in under 2 minutes!",
)

# Call the methods
my_profile.introduce()
my_profile.show_stack()
my_profile.github_link()
