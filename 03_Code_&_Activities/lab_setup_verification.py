# ==============================================================================
# 🛠️ LAB ENVIRONMENT DIAGNOSTIC & VERIFICATION SCRIPT
# สำหรับ: ครูผู้สอน / ผู้ช่วยสอน ใช้รันตรวจเช็กความพร้อมเครื่องคอมพิวเตอร์ก่อนเปิดค่าย
# ==============================================================================

import sys
import os
import subprocess

# รองรับการแสดงผลภาษาไทยและสัญลักษณ์บน Windows Terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_diagnostics():
    print("=" * 60)
    print(" 🔍 YOUNG PYTHON & OOP CODING CAMP: LAB READINESS CHECK")
    print("=" * 60)

    all_passed = True

    # 1. เช็กเวอร์ชัน Python
    py_version = sys.version_info
    print(f"\n[1] ตรวจสอบ Python Version: {py_version.major}.{py_version.minor}.{py_version.micro}")
    if py_version.major >= 3 and py_version.minor >= 8:
        print("    ✅ ผ่าน: รองรับ Python 3.8+ ตามมาตรฐาน")
    else:
        print("    ❌ ไม่ผ่าน: แนะนำให้อัปเดตเป็น Python 3.8 ขึ้นไป")
        all_passed = False

    # 2. เช็กการรองรับ UTF-8 Output
    print("\n[2] ตรวจสอบ Terminal Encoding:")
    enc = sys.stdout.encoding
    print(f"    - Current stdout encoding: {enc}")
    if enc and 'utf' in enc.lower():
        print("    ✅ ผ่าน: รองรับ UTF-8 แสดงผลภาษาไทยและอีโมจิได้สมบูรณ์")
    else:
        print("    ⚠️ ข้อควรระวัง: ไม่ใช่ UTF-8 (แต่ระบบมี sys.stdout.reconfigure fallback รองรับ)")

    # 3. เช็กไฟล์โค้ดของนักเรียน
    print("\n[3] ตรวจสอบไฟล์ประกอบการสอนในเครื่อง:")
    required_files = [
        "starter_battle_arena.py",
        "test_battle_arena.py"
    ]
    for filename in required_files:
        exists = os.path.exists(filename)
        if exists:
            print(f"    ✅ พบไฟล์: {filename}")
        else:
            print(f"    ❌ ไม่พบไฟล์: {filename} (กรุณาคัดลอกมาวางในโฟลเดอร์นี้)")
            all_passed = False

    # 4. รัน Unit Tests ยืนยันความสมบูรณ์ของโค้ดเกม
    print("\n[4] ตรวจสอบความถูกต้องของโมเดล OOP ด้วย Unit Tests:")
    if os.path.exists("test_battle_arena.py"):
        try:
            res = subprocess.run(
                [sys.executable, "-m", "unittest", "test_battle_arena.py"],
                capture_output=True,
                text=True
            )
            if res.returncode == 0:
                print("    ✅ ผ่าน: Unit Tests ทั้งหมด 13 ข้อผ่าน 100% (Ready to Battle!)")
            else:
                print("    ❌ ไม่ผ่าน: มีบาง Test Error หรือล้มเหลว")
                print(res.stderr)
                all_passed = False
        except Exception as e:
            print(f"    ❌ ไม่สามารถรันการทดสอบได้: {e}")
            all_passed = False
    else:
        print("    ⚠️ ข้ามการรัน Unit Tests เนื่องจากไม่พบไฟล์ทดสอบ")

    print("\n" + "=" * 60)
    if all_passed:
        print(" 🎉 ผลการประเมิน: เครื่องคอมพิวเตอร์พร้อมเปิดค่าย 100% (LAB READY!)")
    else:
        print(" ⚠️ ผลการประเมิน: พบข้อควรปรับปรุง กรุณาตรวจสอบตามรายการด้านบน")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_diagnostics()
