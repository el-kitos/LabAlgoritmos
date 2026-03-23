from pathlib import Path

path = Path("learning_phyton.txt")
content = path.read_text()
lines = content.splitlines()

oraciones = []

for line in lines:
    line = line.replace("Python", "HTML")
    oraciones.append(line)

for i in oraciones:
    print(i)
    print()
