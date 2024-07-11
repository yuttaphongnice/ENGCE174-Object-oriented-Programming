rows = int(input("กรอกแถว (1-5): "))

# ตรวจสอบความถูกต้องของค่าที่ได้รับ
if rows < 1 :
    print("กรอกเฉพาะ 1 ถึง 5 เท่านั้น")
else:
    # ดาวจากน้อยไปมาก
    for i in range(1, rows + 1):
        print('*' * i)

    print("\n---------------------------------------")

    # ดาวจากมากไปน้อย
    for i in range(rows, 0, -1):
        print('*' * i)

    print("\n---------------------------------------")

    # แบบดาวที่จัดกลาง
    def print_tree(rows):
        for i in range(1, rows + 1):
            print(' ' * (rows - i) + '* ' * i)

    print_tree(rows)

    print("\n---------------------------------------")

    # แบบดาวที่จัดกลางกลับด้าน
    def print_reversed_tree(rows):
        for i in range(rows, 0, -1):
            print(' ' * (rows - i) + '* ' * i)

    print_reversed_tree(rows)
    
    print("\n---------------------------------------")

    # แบบดาวจากน้อยไปมาก 
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * i)
