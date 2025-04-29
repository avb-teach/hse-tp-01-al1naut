import os
import sys

def save(from_d, out):
    for root, i, items in os.walk(from_d):
        for ent in items:
            orig = os.path.join(root, ent)
            new_pl = os.path.join(out, ent)
            rep = 1
            while os.path.exists(new_pl):
                name, ext = os.path.splitext(ent)
                new_pl = os.path.join(out, f"{name}{rep}{ext}")
                rep += 1
            with open(orig, 'rb') as source_file:
                with open(new_pl, 'wb') as target_file:
                    target_file.write(source_file.read())

st_path = sys.argv[1]
drop = sys.argv[2]
save(st_path, drop)
