# ==============================================================================
# 🧪 UNIT TESTS: TEXT BATTLE ARENA
# Target: starter_battle_arena.py
# Framework: unittest / pytest compatible
# ==============================================================================

import unittest
from unittest.mock import patch
import io
import sys
from starter_battle_arena import Hero, Monster


class TestBattleArena(unittest.TestCase):

    def setUp(self):
        """เตรียมออบเจกต์ตัวละครสำหรับการทดสอบแต่ละกรณี"""
        self.hero = Hero(name="Arthur", hp=100, attack_power=22)
        self.monster = Monster(kind="Red Dragon", hp=90, attack_power=18)

    # --------------------------------------------------------------------------
    # ข้อ 1: การสร้างอินสแตนซ์ Hero และ Monster (Instantiation & Attributes)
    # --------------------------------------------------------------------------
    def test_hero_instantiation(self):
        """ตรวจสอบการกำหนดค่า Attributes เริ่มต้นของ Hero"""
        self.assertEqual(self.hero.name, "Arthur")
        self.assertEqual(self.hero.hp, 100)
        self.assertEqual(self.hero.max_hp, 100)
        self.assertEqual(self.hero.attack_power, 22)

    def test_monster_instantiation(self):
        """ตรวจสอบการกำหนดค่า Attributes เริ่มต้นของ Monster"""
        self.assertEqual(self.monster.name, "Red Dragon")
        self.assertEqual(self.monster.hp, 90)
        self.assertEqual(self.monster.max_hp, 90)
        self.assertEqual(self.monster.attack_power, 18)

    # --------------------------------------------------------------------------
    # ข้อ 2: ฟังก์ชัน take_damage() (Normal & Edge Case เลือดไม่ต่ำกว่า 0)
    # --------------------------------------------------------------------------
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_take_damage_normal(self, mock_stdout):
        """ทดสอบการลดเลือดปกติของ Hero"""
        self.hero.take_damage(30)
        self.assertEqual(self.hero.hp, 70)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_take_damage_cannot_drop_below_zero(self, mock_stdout):
        """ทดสอบ Edge Case เมื่อรับดาเมจเกินเลือดที่เหลือ เลือดต้องหยุดที่ 0 ไม่ติดลบ"""
        self.hero.take_damage(150)
        self.assertEqual(self.hero.hp, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_take_damage_cannot_drop_below_zero(self, mock_stdout):
        """ทดสอบ Monster take_damage เลือดต้องไม่ลดต่ำกว่า 0 เช่นกัน"""
        self.monster.take_damage(200)
        self.assertEqual(self.monster.hp, 0)

    # --------------------------------------------------------------------------
    # ข้อ 3: ฟังก์ชัน heal() (Normal & Boundary Case ไม่เกิน max_hp)
    # --------------------------------------------------------------------------
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_heal_normal(self, mock_stdout):
        """ทดสอบการฮีลเมื่อเลือดลดลงไปมาก (เพิ่มขึ้น 20 หน่วยอย่างถูกต้อง)"""
        self.hero.take_damage(50)  # hp = 50
        self.hero.heal()           # hp + 20 = 70
        self.assertEqual(self.hero.hp, 70)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_heal_boundary_cap_at_max_hp(self, mock_stdout):
        """ทดสอบ Boundary Case เมื่อฮีลแล้วต้องไม่เกิน max_hp (100)"""
        self.hero.take_damage(10)  # hp = 90
        self.hero.heal()           # 90 + 20 = 110 -> ต้องถูก cap ไว้ที่ 100
        self.assertEqual(self.hero.hp, self.hero.max_hp)
        self.assertEqual(self.hero.hp, 100)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_heal_at_full_hp(self, mock_stdout):
        """ทดสอบเมื่อเลือดเต็ม 100 แล้วกดฮีล เลือดต้องยังคงเป็น 100"""
        self.hero.heal()
        self.assertEqual(self.hero.hp, 100)

    # --------------------------------------------------------------------------
    # ข้อ 4: ฟังก์ชัน is_alive() (True เมื่อ hp > 0, False เมื่อ hp == 0)
    # --------------------------------------------------------------------------
    def test_hero_is_alive_when_hp_above_zero(self):
        """ฮีโร่ต้องมีสถานะ is_alive เป็น True เมื่อเลือด > 0"""
        self.assertTrue(self.hero.is_alive())
        self.hero.hp = 1
        self.assertTrue(self.hero.is_alive())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hero_is_alive_false_when_dead(self, mock_stdout):
        """ฮีโร่ต้องมีสถานะ is_alive เป็น False เมื่อเลือด == 0"""
        self.hero.take_damage(100)
        self.assertEqual(self.hero.hp, 0)
        self.assertFalse(self.hero.is_alive())

    def test_monster_is_alive(self):
        """มอนสเตอร์ต้องคืนค่า is_alive ถูกต้องทั้งตอนมีชีวิตและตอนตาย"""
        self.assertTrue(self.monster.is_alive())
        self.monster.hp = 0
        self.assertFalse(self.monster.is_alive())

    # --------------------------------------------------------------------------
    # ข้อ 5: ฟังก์ชัน attack() (ลดเลือดคู่ต่อสู้ได้จริง)
    # --------------------------------------------------------------------------
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=0)
    def test_hero_attack_reduces_monster_hp(self, mock_rand, mock_stdout):
        """ทดสอบว่า Hero โจมตีแล้ว Monster เลือดลดลงตามพลังโจมตีจริง"""
        initial_monster_hp = self.monster.hp  # 90
        self.hero.attack(self.monster)        # damage = 22 + 0 = 22
        expected_hp = initial_monster_hp - self.hero.attack_power
        self.assertEqual(self.monster.hp, expected_hp)
        self.assertEqual(self.monster.hp, 68)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=0)
    def test_monster_attack_reduces_hero_hp(self, mock_rand, mock_stdout):
        """ทดสอบว่า Monster โจมตีแล้ว Hero เลือดลดลงตามพลังโจมตีจริง"""
        initial_hero_hp = self.hero.hp        # 100
        self.monster.attack(self.hero)        # damage = 18 + 0 = 18
        expected_hp = initial_hero_hp - self.monster.attack_power
        self.assertEqual(self.hero.hp, expected_hp)
        self.assertEqual(self.hero.hp, 82)


if __name__ == '__main__':
    unittest.main()
