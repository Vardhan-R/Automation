def dec(bin_str: str) -> int:
	n = len(bin_str)
	d = 0
	for i in range(n):
		d += 2 ** i * int(bin_str[-i - 1])

	return d

all_controls = {"HALT": 15,
			"RESET_SC": 14,
			"CMP": 13,
			"AO": 12,
			"AI": 11,
			"SUB": 10,
			"YO": 9,
			"YW": 8,
			"XO": 7,
			"XW": 6,
			"IO": 5,
			"IW": 4,
			"RO": 3,
			"RI": 2,
			"PCO": 1,
			"PC_INC": 0}

file_ptr = open("eeprom.txt", 'r')
lst_to_write = file_ptr.readline().split(" ")
file_ptr.close()

for i in range(256):
	lst_to_write[i] = int(lst_to_write[i])

while True:
	cmd = input("cmd no. or -1 to exit: ")
	if cmd == "-1":
		break
	cmd_no = dec(cmd)

	controls = ""
	for step in range(16):
		if controls != ["FILL"]:
			controls = input("Controls: ").upper().split(" ")
		if controls in [[""], ["0"]]:
			break
		elif controls == ["FILL"]:
			lst_to_write[16 * cmd_no + step] = lst_to_write[16 * cmd_no + step - 1]
		else:
			lst_to_write[16 * cmd_no + step] = 0
			for control in controls:
				lst_to_write[16 * cmd_no + step] += 2 ** all_controls[control]

for i in range(256):
	lst_to_write[i] = str(lst_to_write[i])

str_to_write = " ".join(lst_to_write)

file_ptr = open("eeprom.txt", 'w')
file_ptr.write(str_to_write)
file_ptr.close()