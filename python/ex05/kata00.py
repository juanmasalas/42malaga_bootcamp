kata = (19,42,21)
# Te coge tupla y te la convierte str cada uno de sus elementos.
m = map(str, kata)
print(f"The {len(kata)} numbers are: ", ", ".join(m))
