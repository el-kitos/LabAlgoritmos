from pathlib import Path

path = Path("learning_phyton.txt")
content = path.read_text()
lines = content.splitlines()
oraciones = []
for line in lines:
    oraciones.append(line)

for j in range(2):    
    for i in oraciones:
        print(i)
        print()