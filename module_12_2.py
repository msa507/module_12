import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_and_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner2, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

if __name__ == '__main__':
    unittest.main()