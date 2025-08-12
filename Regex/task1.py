import re

with open("show_version.txt", "r", encoding="utf-8") as f:
    content = f.read()

data_dict = {}
pattern = re.compile(r"^([\w\s()/\-]+):\s+(.+)$", re.MULTILINE)

for match in pattern.finditer(content):
    key = match.group(1).strip()
    value = match.group(2).strip()
    if "reload" not in key.lower() and "reload" not in value.lower():
        data_dict[key] = value

# extracting reload info
reload_info = []
reload_pattern = re.compile(r".*reload.*", re.IGNORECASE)

for line in content.splitlines():
    line_stripped = line.strip()
    if reload_pattern.search(line_stripped) and line_stripped not in reload_info:
        reload_info.append(line_stripped)

for info in reload_info:
    print(info)
