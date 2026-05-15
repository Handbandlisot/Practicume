for hod in range(102, 334):
    mat = hod * 3

    combined_str = str(hod) + str(mat)

    if len(set(combined_str)) == 6:
        print(f"{hod}+{hod}+{hod}={mat}")
