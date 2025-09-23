class Resident:
    def _init_(self, name, room_no):
        self.name = name
        self.room = room_no


class Visitor:
    def __init__(self, name, Visitor_ID):
        self.name = name
        self.Visitor_ID


class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []


def record_visit(self, visitor: Visitor, resident: Resident):
    entry = visitor.name, +"is visiting" + resident.name + "in room" + resident.room_no
    self.visits.append(entry)


def show_visits(self):
    print(f"Visit records for {self.name} Hostel:")
    if not self.visits:
        print("No visits recorded yet.")
    for visit in self.visits:
        print("-" + visit)


Hostel = Hostel("Rubongoya")
Resident = Resident("Ashiraf", "12B")
Visitor1 = Visitor("Favour", "V15")
Visitor2 = Visitor("Amooti", "V32")
Visitor3 = Visitor("Sarah", "V220")
Visitor4 = Visitor("Diana", "V145")
Visitor5 = Visitor("Zauma", "v234")

hostel.record_visit()
