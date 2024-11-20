class Stack:
    def __init__(self):
        # Skapar en lista för att lagra stackens element
        self.items = []

    def push(self, item):
        # Lägger till ett element överst på stacken
        self.items.append(item)
        print(f"Elementet {item} har lagts till i stacken.")

    def pop(self):
        # Tar bort och returnerar det översta elementet
        if self.is_empty():
            print("Stacken är tom. Kan inte utföra pop.")
            return None
        item = self.items.pop()
        print(f"Elementet {item} har tagits bort från stacken.")
        return item

    def peek(self):
        # Returnerar det översta elementet utan att ta bort det
        if self.is_empty():
            print("Stacken är tom. Det finns inget element att visa.")
            return None
        return self.items[-1]

    def is_empty(self):
        # Kontrollerar om stacken är tom
        return len(self.items) == 0

# Testa stacken
print("Testar stacken med heltal:")
int_stack = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"Pop: {int_stack.pop()}")  # Förväntat resultat: 2
print(f"Är stacken tom? {int_stack.is_empty()}")  # Förväntat resultat: False

print("\nTestar stacken med strängar:")
str_stack = Stack()
str_stack.push("Hello")
str_stack.push("World")
print(f"Peek: {str_stack.peek()}")  # Förväntat resultat: "World"
print(f"Pop: {str_stack.pop()}")  # Förväntat resultat: "World"
print(f"Är stacken tom? {str_stack.is_empty()}")  # Förväntat resultat: False
