from typing import List


class Perfume:
    """Represents a perfume with a name, brand and optional scent notes."""

    def __init__(self, name: str, brand: str, notes: List[str] | None = None) -> None:
        self.name = name
        self.brand = brand
        self.notes = notes or []

    def __repr__(self) -> str:
        return (
            f"Perfume(name={self.name!r}, brand={self.brand!r}, notes={self.notes!r})"
        )


class PerfumeCollection:
    """A simple manager for a collection (list) of Perfume instances.

    Methods:
    - add(perfume): add a Perfume instance
    - remove_by_name(name): remove first perfume matching name, return True/False
    - list_all(): return a shallow copy of the perfumes list
    - find_by_brand(brand): return list of perfumes matching brand
    """

    def __init__(self) -> None:
        self._perfumes: List[Perfume] = []

    def add(self, perfume: Perfume) -> None:
        if not isinstance(perfume, Perfume):
            raise TypeError("only Perfume instances can be added to the collection")
        self._perfumes.append(perfume)

    def remove_by_name(self, name: str) -> bool:
        """Remove the first perfume with the given name.

        Returns True if removed, False if not found.
        """
        for i, p in enumerate(self._perfumes):
            if p.name == name:
                del self._perfumes[i]
                return True
        return False

    def list_all(self) -> List[Perfume]:
        return list(self._perfumes)

    def find_by_brand(self, brand: str) -> List[Perfume]:
        return [p for p in self._perfumes if p.brand == brand]

    def __str__(self) -> str:
        if not self._perfumes:
            return "<empty perfume collection>"
        return "\n".join(f"- {p.name} ({p.brand})" for p in self._perfumes)


if __name__ == "__main__":
    # Demo: create collection, add perfumes, append one, remove one
    coll = PerfumeCollection()

    p1 = Perfume("La Vie Est Belle", "Lancôme", ["iris", "patchouli"])
    p2 = Perfume("Light Blue", "Dolce & Gabbana", ["apple", "cedar"])
    p3 = Perfume("Acqua Di Gio", "Giorgio Armani", ["marine", "bergamot"])

    coll.add(p1)
    coll.add(p2)
    coll.add(p3)

    print("Initial collection:")
    print(coll)

    # Append a new perfume
    new_perfume = Perfume("Santal 33", "Le Labo", ["sandalwood", "cardamom"])
    print("\nAppending:", new_perfume)
    coll.add(new_perfume)

    print("\nCollection after append:")
    print(coll)

    # Remove by name
    to_remove = "Light Blue"
    removed = coll.remove_by_name(to_remove)
    print(f"\nAttempted to remove '{to_remove}':", removed)

    print("\nFinal collection:")
    print(coll)

    # --- Lists vs Tuples demo ---
    print("\n--- Lists vs Tuples demo ---")

    # tuples are immutable
    notes_tuple = ("bergamot", "marine")
    print("Tuple of notes:", notes_tuple)

    try:
        # this will raise, tuples don't have append
        notes_tuple.append("jasmine")
    except Exception as e:
        print("Cannot append to tuple:", type(e).__name__, e)

    # convert to list to mutate, then back to tuple
    notes_list = list(notes_tuple)
    notes_list.append("jasmine")
    print("Converted to list and appended:", notes_list)
    notes_tuple2 = tuple(notes_list)
    print("Converted back to tuple:", notes_tuple2)

    # store tuple as perfume notes to show immutability in practice
    p_tuple_notes = Perfume("Immutable Notes Example", "DemoBrand", list(notes_tuple2))
    # overwrite with the tuple to simulate immutable storage
    p_tuple_notes.notes = notes_tuple2
    print("\nPerfume with tuple notes (immutable):", p_tuple_notes)

    try:
        p_tuple_notes.notes.append("vanilla")
    except Exception as e:
        print(
            "Cannot append to perfume.notes because it's a tuple:", type(e).__name__, e
        )
