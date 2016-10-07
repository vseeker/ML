obuff = []
for ln in open('messages_complete.txt'):
    if ln in obuff:
        continue
    obuff.append(ln)
with open('translate_complete_final.txt', 'w') as handle:
    handle.writelines(obuff)