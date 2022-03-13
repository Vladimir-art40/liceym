a = input() + '%'
qw = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
was = False
b = input()
while b != '':
    scan_poz = 0
    for p in a:
        if scan_poz >= len(b) and p != '%' and p != '*':
            break
        if p == '1':
            if b[scan_poz] in qw:
                break
            scan_poz += 1
        if p == '0':
            if b[scan_poz] not in qw:
                break
            scan_poz += 1
        if p == '?':
            scan_poz += 1
        if p == '%':
            if scan_poz != len(b):
                break
            print(b)
            was = True
            break
        if p == '*':
            if scan_poz == len(b):
                if a.split('*')[1] == '%':
                    print(b)
                    was = True
                    break

            for start_compare in range(scan_poz, len(b) + 1):
                new_b = b[start_compare:]
                new_comp = a.split('*')[1]
                if len(new_b) == len(new_comp) - 1:
                    new_scan_poz = 0
                    for new_p in new_comp:
                        if new_scan_poz >= len(new_b) and new_p != '%':
                            break
                        if new_p == '1':
                            if new_b[new_scan_poz] in qw:
                                break
                            new_scan_poz += 1
                        if new_p == '0':
                            if new_b[new_scan_poz] not in qw:
                                break
                            new_scan_poz += 1
                        if new_p == '?':
                            new_scan_poz += 1
                        if new_p == '%':
                            if new_scan_poz != len(new_b):
                                break
                            print(b)
                            was = True
                            break
            break
    b = input()
if not was:
    print('Есть нечего, значить!')

