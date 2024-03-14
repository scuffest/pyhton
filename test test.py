SVENSKA_ALPHABET = "abcdefghijklmnopqrstuvwxyzåäö"

def kryptera(meddelande, shift):
  """Krypterar ett meddelande med Cesarkryptering.

  Args:
    meddelande: Det meddelande som ska krypteras.
    shift: Hur många steg bokstäverna ska flyttas.

  Returns:
    Det krypterade meddelandet.
  """
  krypterat_meddelande = ""
  for bokstav in meddelande.lower():
    if bokstav in SVENSKA_ALPHABET:
      index = SVENSKA_ALPHABET.find(bokstav)
      ny_index = (index + shift) % len(SVENSKA_ALPHABET)
      krypterat_meddelande += SVENSKA_ALPHABET[ny_index]
    else:
      krypterat_meddelande += bokstav
  return krypterat_meddelande

def dekryptera(krypterat_meddelande, shift):
  """Dekrypterar ett krypterat meddelande med Cesarkryptering.

  Args:
    krypterat_meddelande: Det krypterade meddelandet.
    shift: Hur många steg bokstäverna ska flyttas.

  Returns:
    Det dekrypterade meddelandet.
  """
  dekrypterat_meddelande = ""
  for bokstav in krypterat_meddelande.lower():
    if bokstav in SVENSKA_ALPHABET:
      index = SVENSKA_ALPHABET.find(bokstav)
      ny_index = (index - shift) % len(SVENSKA_ALPHABET)
      dekrypterat_meddelande += SVENSKA_ALPHABET[ny_index]
    else:
      dekrypterat_meddelande += bokstav
  return dekrypterat_meddelande

# Exempel på användning
meddelande = "Hello World!"
shift = 5

krypterat_meddelande = kryptera(meddelande, shift)
print(f"Krypterat: {krypterat_meddelande}")

dekrypterat_meddelande = dekryptera(krypterat_meddelande, shift)
print(f"Dekrypterat: {dekrypterat_meddelande}")
