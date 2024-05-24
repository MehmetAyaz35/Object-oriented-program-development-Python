"""Vid dynamisk typning kan variabler omfördelas till olika typer av värden under körningen av ett program. Denna flexibilitet möjliggör
mer koncis och flexibel kod, eftersom du kan använda samma variabel för att lagra olika typer av data genom hela programmet."""

"""Jag har definierat två variabler en av stringtyp och en av integertyp. Som du kan se från koden har jag inte definierat datatypen för 
någon variabel och koden ger inget fel, detta beror på att Python är ett dynamiskt skrivet språk. Datatyperna för variabler identifieras
 vid körning så det finns inget behov av att deklarera det i koden.
"""


name = "Mehmet"
age = 33
print(f"The student's name is {name} and {age} years old.")