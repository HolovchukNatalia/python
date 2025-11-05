# Розробити програму, яка: 
# а) створює текстовий файл TF11_1 із символьних рядків однакової довжини; 
# б) читає вміст файла TF11_1, вилучає у кожному рядку всі символи крім цифр,
# доповнює його до заданої довжини пробілами і записує у файл TF11_2; 
# в) читає вміст файла TF11_2 і друкує його по рядках.

def open_file(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "was not opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

file1_name = "TF11_1.txt"
file2_name = "TF11_2.txt"

LINE_LENGTH = 20

file1_w = open_file(file1_name, "w")
if file1_w is not None:
    file1_w.write("Room 123 is on level45\n")
    file1_w.write("Call me at number 38099\n")
    file1_w.write("Order ID: 5577438291\n")
    print("Data was successfully written!")
    file1_w.close()
    print("File TF11_1.txt was closed!\n")

file1_r = open_file(file1_name, "r")
file2_w = open_file(file2_name, "w")

if file1_r is not None and file2_w is not None:
    for line in file1_r:
        digits_only = "".join(ch for ch in line if ch.isdigit())
        digits_only = digits_only.ljust(LINE_LENGTH)
        file2_w.write(digits_only + "\n")

    file1_r.close()
    file2_w.close()
    print("Files TF11_1 and TF11_2 were closed!\n")


print("Contents of TF11_2:")
file2_r = open_file(file2_name, "r")
if file2_r is not None:
    for row in file2_r:
        print(row.rstrip()) 
    file2_r.close()
    print("File TF11_2.txt was closed!")
