# ==============================================================================
# 🎮 PROJECT: TEXT BATTLE ARENA (ศึกประลองฮีโร่ดิจิทัล)
# วิชา: Python Fundamentals & Object-Oriented Programming (OOP) สำหรับมัธยมต้น
# แนะนำให้เปิดและรันด้วย: Thonny IDE (เปิดแถบ View -> Variables และ Object inspector)
# ==============================================================================

import time
import random
import sys

# รองรับการแสดงผลภาษาไทยและสัญลักษณ์บน Windows Terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ------------------------------------------------------------------------------
# 🧙‍♂️ STEP 1: พิมพ์เขียวคลาส Hero (Blueprint)
# ------------------------------------------------------------------------------
class Hero:
    def __init__(self, name, hp, attack_power):
        """
        เมธอดกำเนิดตัวละคร (Constructor)
        คำสั่ง self.xxx หมายถึงการสร้างคุณสมบัติประจำตัว (Attributes) ของฮีโร่ตัวนั้นๆ
        """
        self.name = name                 # ชื่อตัวละคร (String)
        self.hp = hp                     # พลังชีวิตปัจจุบัน (Integer)
        self.max_hp = hp                 # พลังชีวิตสูงสุด (Integer)
        self.attack_power = attack_power # ค่าพลังโจมตีพื้นฐาน (Integer)

    def attack(self, enemy):
        """
        เมธอดสำหรับสั่งให้ฮีโร่โจมตีศัตรู
        สังเกตว่าพารามิเตอร์ enemy คือตัวแทนของออบเจกต์ศัตรูที่เราจะไปลดเลือดเขา!
        """
        # สุ่มดาเมจเล็กน้อยเพื่อความสนุก (+- 3 หน่วย) โดยต้องไม่ติดลบ
        damage = max(0, self.attack_power + random.randint(-3, 3))

        print(f"⚔️  [{self.name}] พุ่งเข้าโจมตีใส่ [{enemy.name}]!")
        print(f"💥  สร้างความเสียหายได้ {damage} แต้ม!")
        
        # ส่งดาเมจไปให้ศัตรูลดเลือดผ่านเมธอด take_damage ของศัตรู
        enemy.take_damage(damage)

    def take_damage(self, damage):
        """
        เมธอดสำหรับลดพลังชีวิตของตัวเราเอง
        """
        damage = max(0, damage)
        self.hp = max(0, self.hp - damage)
            
        print(f"🛡️  [{self.name}] พลังชีวิตลดลงเหลือ: {self.hp}/{self.max_hp}\n")

    def heal(self):
        """
        TODO (ภารกิจของนักเรียน): เมธอดสำหรับฟื้นฟูพลังชีวิต
        คำใบ้: เพิ่ม self.hp ขึ้นมา 20 หน่วย แต่ต้องไม่เกิน self.max_hp!
        """
        # ป้องกันไม่ให้ตัวละครที่ตายแล้วฟื้นคืนชีพ (Zombie resurrection guard)
        if not self.is_alive():
            print(f"⚠️ [{self.name}] พ่ายแพ้ไปแล้ว ไม่สามารถดื่มยาฟื้นพลังได้!\n")
            return

        heal_amount = 20
        self.hp = min(self.max_hp, self.hp + heal_amount)
        print(f"✨ [{self.name}] ดื่มน้ำยาฟื้นพลัง! พลังชีวิตเพิ่มเป็น {self.hp}/{self.max_hp}\n")

    def is_alive(self):
        """
        ตรวจสอบว่าตัวละครยังมีชีวิตอยู่หรือไม่ (คืนค่า True หรือ False)
        """
        return self.hp > 0


# ------------------------------------------------------------------------------
# 👾 STEP 2: พิมพ์เขียวคลาสมอนสเตอร์ Monster (Blueprint)
# ------------------------------------------------------------------------------
class Monster:
    def __init__(self, name=None, hp=90, attack_power=18, kind=None):
        # รองรับทั้ง name และ kind เพื่อป้องกัน TypeError หากนักเรียนคุ้นเคยกับคำว่า kind
        self.name = name if name is not None else (kind if kind is not None else "Goblin")
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

    def attack(self, enemy):
        damage = max(0, self.attack_power + random.randint(-2, 2))
        print(f"🐾 [{self.name}] พ่นไฟโจมตีใส่ [{enemy.name}]!")
        print(f"🔥 สร้างความเสียหายได้ {damage} แต้ม!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        damage = max(0, damage)
        self.hp = max(0, self.hp - damage)
        print(f"💢 [{self.name}] พลังชีวิตเหลือ: {self.hp}/{self.max_hp}\n")

    def is_alive(self):
        return self.hp > 0


# ------------------------------------------------------------------------------
# 🏟️ STEP 3: ลานประลอง (Game Loop Execution)
# ------------------------------------------------------------------------------
def start_battle():
    print("=" * 55)
    print("      🏆 ยินดีต้อนรับสู่สังเวียน TEXT BATTLE ARENA! 🏆")
    print("=" * 55)

    # 1. ปั๊มออบเจกต์ (Instantiation)
    player = Hero(name="Arthur", hp=100, attack_power=22)
    boss = Monster(name="Red Dragon", hp=90, attack_power=18)

    print(f"ฮีโร่เข้าสู่สนาม: {player.name} (HP: {player.hp}, ATK: {player.attack_power})")
    print(f"บอสสุดโหดปรากฏตัว: {boss.name} (HP: {boss.hp}, ATK: {boss.attack_power})\n")
    print("ระฆังเริ่มการต่อสู้ดังขึ้นใน 3... 2... 1... START!\n")
    time.sleep(1)

    turn = 1
    has_healed = False

    # 2. การต่อสู้แบบเทิร์นเบสด้วย While Loop
    while player.is_alive() and boss.is_alive():
        print(f"--- 🌀 เทิร์นที่ {turn} ---")
        
        # ตัวอย่างกลยุทธ์: ถ้าเลือดเหลือน้อยกว่า 40 และยังไม่เคยฮีล ให้ดื่มโพชั่น
        if player.hp <= 40 and not has_healed:
            player.heal()
            has_healed = True
            time.sleep(1)
        else:
            # เทิร์นของผู้เล่นโจมตี
            player.attack(boss)
            time.sleep(1)

        # ตรวจสอบว่าบอสตายหรือยังก่อนที่จะโจมตีสวนกลับ
        if not boss.is_alive():
            print(f"🎉 ไชโย! [{player.name}] ปราบ [{boss.name}] สำเร็จแล้ว!")
            print("🌟 คุณได้รับ 500 EXP และตราสัญลักษณ์ 'OOP Guild Master'!")
            break

        # เทิร์นของบอสโจมตีสวนกลับ
        boss.attack(player)
        time.sleep(1)

        if not player.is_alive():
            print(f"💀 อนิจจา! [{player.name}] พ่ายแพ้ให้แก่ [{boss.name}]...")
            print("🔄 กลับไปอัปเกรด Class และฝึกซ้อมแล้วกลับมาประลองใหม่นะ!")
            break

        turn = turn + 1

    print("\n" + "=" * 55)
    print("              🏁 จบการประลองในสังเวียน 🏁")
    print("=" * 55)


# เรียกใช้งานฟังก์ชันเริ่มต้นเกมเมื่อรันไฟล์นี้
if __name__ == "__main__":
    start_battle()
