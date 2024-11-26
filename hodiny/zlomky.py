from math import gcd  # Pro zjednodušení zlomků


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Jmenovatel nemůže být nula.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()  # Automaticky zjednoduší zlomek při vytvoření

    def simplify(self):
        """Zjednodušení zlomku pomocí NSD."""
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __str__(self):
        """Reprezentace zlomku jako řetězce."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Sčítání dvou zlomků."""
        if not isinstance(other, Fraction):
            raise TypeError("Lze sčítat pouze instance třídy Fraction.")

        # Výpočet společného jmenovatele a nového čitatele
        common_denominator = self.denominator * other.denominator
        new_numerator = (
                self.numerator * other.denominator + other.numerator * self.denominator
        )

        # Vrácení nového zjednodušeného zlomku
        return Fraction(new_numerator, common_denominator)


class ExtendedFraction(Fraction):
    def to_mixed_number(self):
        """Převod na smíšené číslo."""
        whole_part = self.numerator // self.denominator  # Celá část
        remainder = self.numerator % self.denominator  # Zbytek (zlomkový čitatel)

        if remainder == 0:
            # Pokud zbytek není, máme celé číslo
            return f"{whole_part}"
        elif whole_part == 0:
            # Pokud je celá část 0, je to jen zlomek
            return f"{remainder}/{self.denominator}"
        else:
            # Kombinace celé části a zlomkové části
            return f"{whole_part} {remainder}/{self.denominator}"
# Vytvoření zlomků
zlomek1 = Fraction(1, 3)
zlomek2 = Fraction(2, 5)

# Sčítání
soucet = zlomek1 + zlomek2

print(f"První zlomek: {zlomek1}")
print(f"Druhý zlomek: {zlomek2}")
print(f"Součet: {soucet}")

rozsireny_zlomek = ExtendedFraction(10, 3)
print(f"Zlomek: {rozsireny_zlomek}")
print(f"Smíšené číslo: {rozsireny_zlomek.to_mixed_number()}")