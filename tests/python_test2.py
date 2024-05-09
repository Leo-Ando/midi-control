total_notes = 12
rhythms = [0, 1, 2,3,4,5]
rhythm_send = []

while len(rhythm_send) < total_notes:
    for i in rhythms:
        rhythm_send.append(i)
        if len(rhythm_send) >= total_notes:
            break

print(rhythm_send)