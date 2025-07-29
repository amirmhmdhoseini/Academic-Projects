from itertools import product

# هر یال با یک عدد از 0 تا 8 شماره‌گذاری شده
# لیست مثلث‌ها: هر مثلث یک لیست شامل شماره 3 یالشه
triangles = [
    [0, 1, 2],  # مثلث بالا
    [3, 4, 5],  # مثلث چپ
    [4, 2, 6],  # مثلث راست
    [6, 7, 8]   # مثلث پایین
]

# تعداد رنگ‌ها: 0 = قرمز، 1 = سبز، 2 = آبی
colors = [0, 1, 2]

valid_count = 0

# همه حالت‌های ممکن رنگ‌آمیزی یال‌ها (تعداد: 3^9 = 19683)
for coloring in product(colors, repeat=9):
    valid = True
    for tri in triangles:
        a, b, c = tri
        if coloring[a] == coloring[b] == coloring[c]:
            valid = False  # این مثلث تک‌رنگه → حالت نامعتبر
            break
    if valid:
        valid_count += 1

print("تعداد حالت‌های مجاز:", valid_count)
