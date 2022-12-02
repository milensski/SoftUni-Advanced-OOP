from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('anytime', 99, 100.0, 2500.0)
        self.enemy = Hero('enemy', 10, 100.0, 25.0)

    def test_init_method(self):
        self.assertEqual('anytime', self.hero.username)
        self.assertEqual(99, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(2500.0, self.hero.damage)

    def test_battle_with_ourselves_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_or_less_health_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_enemy_zero_or_less_health_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight enemy. He needs to rest", str(ve.exception))

    def test_battle_for_draw(self):
        self.hero.health = 1
        self.enemy.health = 1
        self.hero.level = 1
        self.enemy.level = 1
        self.hero.damage = 1
        self.enemy.damage = 1

        result = self.hero.battle(self.enemy)
        expected = 'Draw'

        self.assertEqual(expected, result)

    def test_for_win_against_enemy(self):
        self.enemy.level = 1
        result = self.hero.battle(self.enemy)
        expected = 'You win'

        self.assertEqual(expected, result)

    def test_for_lose_against_enemy(self):
        self.hero.level = 1
        self.hero.damage = 1

        result = self.hero.battle(self.enemy)
        expected = 'You lose'

        self.assertEqual(expected, result)

    def test_enemy_stats_after_battle_he_won(self):
        self.hero.level = 1
        self.hero.damage = 1
        self.hero.battle(self.enemy)

        self.assertEqual(11,self.enemy.level)
        self.assertEqual(104.0,self.enemy.health)
        self.assertEqual(30.0,self.enemy.damage)

    def test_hero_stats_after_battle_he_won(self):

        self.enemy.level = 1
        self.enemy.damage = 1
        self.hero.battle(self.enemy)

        self.assertEqual(100,self.hero.level)
        self.assertEqual(104.0,self.hero.health)
        self.assertEqual(2505.0,self.hero.damage)


    def test_string_representation(self):
        result = self.hero.__str__()
        expect = "Hero anytime: 99 lvl\n" \
                 "Health: 100.0\n" \
                 "Damage: 2500.0\n"

        self.assertEqual(result, expect)


if __name__ == "__main__":
    main()
