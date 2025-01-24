import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk1 = runner.Runner("Vasia")
        for i in range(10):
            walk1.walk()
        self.assertEqual(walk1.distance, 50)

    def test_run(self):
        run2 = runner.Runner("Petia")
        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        challenge3 = runner.Runner("Kolia")
        challenge4 = runner.Runner("Misha")
        for i in range(10):
            challenge3.walk()
            challenge4.run()
        self.assertNotEqual(challenge3.distance, challenge4.distance)


if __name__ == '__main__':
    unittest.main()