
class Person:
    """
    Represents a person in a social network.

    Attributes:
        name: The person's name.
        friends: A list of Person objects representing their friends.
    """

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """Adds another person to the friends list."""
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """
    Represents a social network using an adjacency list.

    Attributes:
        people: Dictionary mapping names to Person objects.
    """

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """Creates and adds a new person to the network."""
        if name in self.people:
            print(f"Person '{name}' already exists!")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        """Creates a bidirectional friendship between two people."""

        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        if person1 == person2:
            print("Friendship not created. A person cannot be friends with themselves!")
            return

        # Add each person to the other's friends list.
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        """Prints each person and their friends."""

        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]

            if friend_names:
                print(f"{name} is friends with: {', '.join(friend_names)}")
            else:
                print(f"{name} is friends with: No friends")


# ==========================================
# Test Your Social Network
# ==========================================

network = SocialNetwork()

# Add at least 6 people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate person
network.add_person("Alex")

# Create at least 8 friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Test friendship with a person who doesn't exist
network.add_friendship("Jordan", "Johnny")

# Print the complete network
print("\n--- Social Network ---")
network.print_network()

