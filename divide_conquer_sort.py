# Daftar mahasiswa
students = [
    ("Andi", 78),
    ("Budi", 65),
    ("Citra", 85),
    ("Dewi", 72),
    ("Eka", 90)
]

# -------------------------------
# MERGE SORT
# -------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# -------------------------------
# QUICK SORT
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][1]
        left = [x for x in arr[1:] if x[1] <= pivot]
        right = [x for x in arr[1:] if x[1] > pivot]
        return quick_sort(left) + [arr[0]] + quick_sort(right)

# -------------------------------
# PROSES
# -------------------------------
students_merge = students.copy()
merge_sort(students_merge)

students_quick = quick_sort(students.copy())

print("Hasil Merge Sort:")
for s in students_merge:
    print(s)

print("\nHasil Quick Sort:")
for s in students_quick:
    print(s)