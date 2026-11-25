import unittest
from programm import add, mult, generat_random, Person, Employe

person = Person("Elia","Bischof")

class TestFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,5),7)
    def test_mult(self):
        self.assertEqual(mult(2,3),6)
    def test_generat_random(self):
        a = int(input("Zahl1: "))
        if a<0:
            raise ValueError("Gib bitte eine zahl über 0 ein für den test")
        b = int(input("Zahl2: "))
        
        self.assertGreaterEqual(generat_random(a,b), a)
        self.assertLessEqual(generat_random(a,b),b)

class TestClasses(unittest.TestCase):
    def test_Person(self):
        self.assertIsSubclass(Employe, Person)

suite = unittest.TestSuite()  # Eine TestSuite ist eine Sammlung von Tests, die gemeinsam ausgeführt werden.
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFunc))  # Der TestLoader sucht in TestFunc nach Methoden, deren Name mit "test_" beginnt, erstellt daraus Tests und fügt sie der Suite hinzu.
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClasses))  # Dasselbe für TestClasses: So kommt auch test_Person in die Suite und wird nicht ausgelassen.
runner = unittest.TextTestRunner()  # Der Runner führt die Tests aus und zeigt das Ergebnis im Terminal an; ohne Angabe gilt die Standard-Ausführlichkeit.
result = runner.run(suite)  # Startet alle Tests in der Suite. Das zurückgegebene TestResult enthält z. B. die Anzahl der Tests und mögliche Fehler.

print(f'Tests run: {result.testsRun}')
