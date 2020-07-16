class Item:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def on_take(self) -> None:
        print(f"You have picked up {self.name}.")

    def on_drop(self) -> None:
        print(f"You have dropped {self.name}.")
