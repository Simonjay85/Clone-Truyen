import sys

filename = "tehi-theme/single-truyen.php"
with open(filename, "r") as f:
    lines = f.readlines()

# We want to remove lines from index 825 to 1041 (0-indexed, meaning lines 826 to 1042)
# and replace with the correct closing tags.
closing_tags = """                        </div>
                    </div>
                    <!-- content end -->
                </div>
            </div>
        </div>
        <!-- danh sách chương END -->
"""

new_lines = lines[:825] + [closing_tags] + lines[1042:]

with open(filename, "w") as f:
    f.writelines(new_lines)
