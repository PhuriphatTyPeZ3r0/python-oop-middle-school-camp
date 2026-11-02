# ==============================================================================
# 🎨 CANVA MCP AUTOMATION BRIDGE: CREATE PRESENTATION SLIDE DECK
# ==============================================================================

import subprocess
import json
import time
import sys

# รองรับการแสดงผลภาษาไทยและสัญลักษณ์บน Windows Terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def main():
    print("🚀 เริ่มต้นเชื่อมต่อกับ Canva MCP Server...")
    proc = subprocess.Popen(
        ['cmd.exe', '/c', 'npx', '-y', 'mcp-remote@latest', 'https://mcp.canva.com/mcp'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    def send_rpc(msg):
        proc.stdin.write(json.dumps(msg) + '\n')
        proc.stdin.flush()
        line = proc.stdout.readline()
        if not line:
            return None
        return json.loads(line)

    # 1. Initialize
    init_res = send_rpc({
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'initialize',
        'params': {
            'protocolVersion': '2024-11-05',
            'capabilities': {},
            'clientInfo': {'name': 'Antigravity-Canva-Bridge', 'version': '1.0'}
        }
    })
    print("✅ Initialized with Canva MCP:", init_res.get('result', {}).get('serverInfo', {}))

    # 2. Initialized Notification
    proc.stdin.write(json.dumps({'jsonrpc': '2.0', 'method': 'notifications/initialized'}) + '\n')
    proc.stdin.flush()

    # 3. ตรวจสอบบัญชีผู้ใช้
    user_res = send_rpc({
        'jsonrpc': '2.0',
        'id': 2,
        'method': 'tools/call',
        'params': {
            'name': 'get-logged-in-account-details',
            'arguments': {}
        }
    })
    user_info = user_res.get('result', {}).get('structuredContent', {})
    print(f"👤 บัญชีผู้ใช้ Canva: {user_info.get('name')} (Team ID: {user_info.get('team_id')})")

    # 4. กำหนดโครงสร้างเนื้อหา 15 สไลด์
    sections = [
        {
            "title": "LEVEL UP! ผจญภัยโลก Python และ OOP",
            "description": "แคมป์สร้างฮีโร่ดิจิทัล จากบรรทัดโค้ดแรกสู่ผู้พิทักษ์แห่งการเขียนโปรแกรม",
            "points": [
                "เปลี่ยนผ่านจาก Scratch สู่ภาษา Python",
                "เรียนรู้การคิดเชิงคำนวณผ่านเกม",
                "สร้างตัวละครเกมด้วย Object-Oriented Programming"
            ]
        },
        {
            "title": "อาวุธประจำกาย: Thonny IDE",
            "description": "ทำความรู้จักแท่นตีดาบเวทมนตร์สำหรับนักเรียนมัธยม",
            "points": [
                "Code Editor: สมุดบันทึกคาถาคำสั่ง",
                "Variables Inspector: หน้าต่างตรวจจับหีบสมบัติ",
                "Shell: ลานแสดงผลลัพธ์เวทมนตร์"
            ]
        },
        {
            "title": "Module 1: ตัวแปร (Variables) = หีบเก็บสมบัติ",
            "description": "การเก็บข้อมูลและการเลือกใช้ Data Types ให้เหมาะสม",
            "points": [
                "String: เก็บข้อความ เช่น hero_name = 'Arthur'",
                "Integer: เก็บตัวเลขจำนวนเต็ม เช่น hero_hp = 100",
                "Boolean: สวิตช์จริงเท็จ เช่น is_alive = True"
            ]
        },
        {
            "title": "Module 2: ทางแยกแห่งชะตากรรม (Conditionals)",
            "description": "การตัดสินใจของโปรแกรมด้วย If, Elif, Else",
            "points": [
                "if hero_hp <= 0: Game Over ชุบชีวิตใหม่",
                "elif hero_hp <= 30: เตือนภัยเลือดเหลือน้อย",
                "else: พลังเต็มเปี่ยม พร้อมลุยดันเจี้ยน"
            ]
        },
        {
            "title": "Module 3: ลูปฟาร์มเลเวล (Loops)",
            "description": "การทำซ้ำอย่างมีประสิทธิภาพด้วย While Loop",
            "points": [
                "ทำซ้ำตราบใดที่เงื่อนไขยังเป็นจริง",
                "ลดค่า Stamina ทุกครั้งที่โจมตี",
                "ระวังกับดัก Infinite Loop ลืมลดค่าตัวแปร"
            ]
        },
        {
            "title": "Module 4: คัมภีร์เวทมนตร์ (Functions)",
            "description": "การรวมคำสั่งเป็นฟังก์ชันด้วย def",
            "points": [
                "เขียนครั้งเดียว เรียกใช้กี่รอบก็ได้",
                "การส่ง Parameter เข้าไปในวงเล็บ",
                "การ Return ผลลัพธ์กลับมาใช้งานต่อ"
            ]
        },
        {
            "title": "วิกฤตการณ์ตัวละครล้นจอ! ทำไมต้อง OOP?",
            "description": "ปัญหาของการเขียนโค้ดแบบเดิมเมื่อเกมเริ่มมีขนาดใหญ่",
            "points": [
                "ถ้ามีมอนสเตอร์ 50 ตัว จะประกาศตัวแปร 50 ชุดหรือไม่?",
                "โค้ดรก ยุ่งเหยิง และเกิดบั๊กได้ง่าย",
                "แก้ปัญหาด้วยการรวมข้อมูลและการกระทำไว้ใน Object เดียว"
            ]
        },
        {
            "title": "The Golden Metaphor: แม่พิมพ์ vs ตัวตนจริง",
            "description": "ความแตกต่างที่ชัดเจนระหว่าง Class และ Object",
            "points": [
                "Class คือ แม่พิมพ์คุกกี้ (Blueprint) มีแค่อันเดียว",
                "Object คือ ตัวขนมคุกกี้ที่ปั๊มออกมาจริงในหน่วยความจำ",
                "แม่พิมพ์ 1 อัน สามารถปั๊มตัวละครออกมาได้นับร้อยตัว"
            ]
        },
        {
            "title": "Consumer Stage: สังเกตเครื่องหมายจุด (.)",
            "description": "การเรียกใช้งานออบเจกต์สำเร็จรูปที่มีอยู่แล้วใน Python",
            "points": [
                "text.upper() การเรียก Method ของ String",
                "turtle.forward(100) สั่งให้ออบเจกต์เต่าเดินหน้า",
                "เครื่องหมายจุด (.) คือการเคาะเรียกความสามารถ"
            ]
        },
        {
            "title": "Producer Stage: พิมพ์เขียวคลาสแรกของเรา",
            "description": "การสร้างคลาส Hero ด้วยคำสั่ง class และ __init__",
            "points": [
                "__init__ คือ เมธอดกำเนิดตัวละคร",
                "Attributes คือ ข้อมูลประจำตัว เช่น self.name, self.hp",
                "จัดระเบียบคุณสมบัติทั้งหมดไว้ใต้คลาสเดียว"
            ]
        },
        {
            "title": "ถอดรหัสความลับคำว่า self",
            "description": "self คือสรรพนาม 'ของฉันเอง' เพื่อระบุตัวตนของออบเจกต์",
            "points": [
                "เหมือนนักเรียนทุกคนเปิดกระเป๋าของตัวเอง",
                "self.hp คือ เลือดของตัวฉัน ไม่ใช่เลือดของเพื่อน",
                "Method ในคลาสต้องมี self เป็นพารามิเตอร์ตัวแรกเสมอ"
            ]
        },
        {
            "title": "เพิ่มท่าไม้ตายให้ตัวละคร (Methods)",
            "description": "การสร้างพฤติกรรมและการกระทำให้กับออบเจกต์",
            "points": [
                "def attack(self, enemy): การโจมตีศัตรู",
                "def take_damage(self, damage): การลดเลือดตนเอง",
                "การสื่อสารระหว่าง 2 ออบเจกต์ผ่านเมธอด"
            ]
        },
        {
            "title": "เสกตัวละครเข้าสู่เกม (Instantiation)",
            "description": "การปั๊มฮีโร่และมอนสเตอร์ออกมาดวลกันจริงในเกมลูป",
            "points": [
                "player1 = Hero('Arthur', 120, 22)",
                "boss = Monster('Red Dragon', 90, 18)",
                "การเชื่อมต่อเข้ากับ While Loop สำหรับเทิร์นเบสเกม"
            ]
        },
        {
            "title": "กิจกรรมประลองโค้ด Parsons Problems",
            "description": "การฝึกจัดเรียงลำดับบล็อกโค้ดเพื่อลดภาระทางปัญญา",
            "points": [
                "จัดเรียงแถบการ์ดโค้ดสีบนโต๊ะให้ถูกต้อง",
                "ฝึกคิดเชิงตรรกะโดยไม่ต้องกังวลเรื่องพิมพ์ผิด",
                "นำโค้ดที่เรียงสำเร็จไปทดสอบรันใน Thonny IDE"
            ]
        },
        {
            "title": "ยินดีด้วย! คุณคือ OOP Guild Master",
            "description": "สรุปความรู้และเปิดสังเวียน Live Arena Tournament",
            "points": [
                "เข้าใจแก่นแท้ของ Class, Object, Attributes, และ Methods",
                "พร้อมสำหรับสังเวียนดวลบอสใหญ่บนจอโปรเจกเตอร์",
                "ก้าวต่อไปสู่การสร้างเกม 2D ด้วย Pygame"
            ]
        }
    ]

    brief = (
        "Create an engaging, gamified educational presentation for middle school students (ages 12-15) "
        "teaching Python Programming Fundamentals and Object-Oriented Programming (OOP). "
        "Theme: Fantasy RPG & Cyber-Tech gaming with Pixel art aesthetic, Dark Navy background (#0F172A), "
        "Cyber Cyan (#06B6D4) and Neon Violet (#8B5CF6) accents. Title in Kanit/Prompt Bold, body in Sarabun. "
        "Includes clear code examples, visual metaphors (cookie cutter mold vs cookies, treasure chests, magic spellbook), "
        "and gamified level-up achievements."
    )

    print("🎨 ส่งคำสั่งสร้างสไลด์ไปยัง Canva (create-design)...")
    create_req = {
        'jsonrpc': '2.0',
        'id': 3,
        'method': 'tools/call',
        'params': {
            'name': 'create-design',
            'arguments': {
                'brief': brief,
                'format': 'Presentation',
                'outline': {
                    'sections': sections
                },
                'user_intent': 'Create Python and OOP educational presentation for middle school coding camp'
            }
        }
    }

    create_res = send_rpc(create_req)
    print("📥 ตอบรับจาก Canva:", json.dumps(create_res, ensure_ascii=False, indent=2))

    # ตรวจสอบ async job
    structured = create_res.get('result', {}).get('structuredContent', {})
    job_id = structured.get('job_id')
    continuation_token = structured.get('continuation_token')

    if not job_id:
        # อาจคืนค่าเป็น content ธรรมดา
        content_text = create_res.get('result', {}).get('content', [{}])[0].get('text', '')
        print("📄 ผลลัพธ์ข้อความ:", content_text)
        try:
            parsed = json.loads(content_text)
            job_id = parsed.get('job_id')
            continuation_token = parsed.get('continuation_token')
        except Exception:
            pass

    if job_id:
        print(f"⏳ กำลังประมวลผลการเจนสไลด์ Canva (Job ID: {job_id})...")
        for poll_round in range(1, 30):
            time.sleep(5)
            poll_req = {
                'jsonrpc': '2.0',
                'id': 100 + poll_round,
                'method': 'tools/call',
                'params': {
                    'name': 'get-create-design-async-job',
                    'arguments': {
                        'job_id': job_id,
                        'continuation_token': continuation_token
                    }
                }
            }
            poll_res = send_rpc(poll_req)
            poll_content = poll_res.get('result', {}).get('structuredContent', {})
            if not poll_content:
                text_raw = poll_res.get('result', {}).get('content', [{}])[0].get('text', '')
                try:
                    poll_content = json.loads(text_raw)
                except Exception:
                    pass

            status = poll_content.get('status')
            print(f"   [รอบที่ {poll_round}] สถานะ: {status}")
            if status == 'success':
                design_url = poll_content.get('design', {}).get('url') or poll_content.get('url')
                design_id = poll_content.get('design', {}).get('id')
                print("\n🎉 สร้างสไลด์ Canva สำเร็จเรียบร้อยแล้ว!")
                print(f"🔗 ลิงก์เข้าชมและแก้ไขสไลด์ Canva: {design_url}")
                print(f"🆔 Design ID: {design_id}")
                
                # บันทึกผลลัพธ์ลงไฟล์
                with open("canva_generated_design_link.txt", "w", encoding="utf-8") as f:
                    f.write(f"Canva Presentation URL: {design_url}\nDesign ID: {design_id}\n")
                break
            elif status == 'failed':
                print("❌ การสร้างสไลด์ใน Canva ล้มเหลว:", poll_content.get('error'))
                break
    else:
        print("ℹ️ ไม่พบ job_id หรือ Canva ส่งผลลัพธ์กลับมาทันที")

    proc.terminate()

if __name__ == "__main__":
    main()
