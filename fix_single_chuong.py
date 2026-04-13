filename = "tehi-theme/single-chuong.php"
with open(filename, "r") as f:
    lines = f.readlines()

# Line 1-2 headers
# Line 478 content starts
new_lines = lines[:4] + lines[477:]

with open(filename, "w") as f:
    f.writelines(new_lines)
