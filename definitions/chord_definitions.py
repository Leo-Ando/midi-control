chromatic_scale_tones = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
root_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


#和音の構成音定義
def generate_tones_of_McCoy_style_chord(root_note, octave):
    # 音階のリスト
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    # ルート音のインデックスを見つける
    root_index = notes.index(root_note)
    # 完全四度の間隔で和音の構成音を見つける
    first_note = notes[root_index]  # ルート音
    second_note = notes[(root_index + 5) % len(notes)]  # 完全四度上
    third_note = notes[(root_index + 10) % len(notes)]  # もう一つの完全四度上
    forth_note = notes[(root_index + 15) % len(notes)]  # もう一つの完全四度上
    fifth_note = notes[(root_index + 20) % len(notes)]  # もう一つの完全四度上

    # 和音のリストを作成（オクターブ付き）
    chord = [[first_note, octave], [second_note, octave], [third_note, octave], [forth_note, octave], [fifth_note, octave]]

    return chord

# C4からB4までの和音を定義
tones_of_McCoy_style_chord = {}
for note in chromatic_scale_tones:
    chord_name = f"{note}"
    tones_of_McCoy_style_chord[chord_name] = generate_tones_of_McCoy_style_chord(note, 4)


#和音定義
McCoy_style_chords = {}

#キーの決定
for root_note in chromatic_scale_tones:
    
    chord_tones = []
    root_index = chromatic_scale_tones.index(root_note)
    chord_name = f"{root_note}"

    #基本の音程の決定
    for degree in range(5):
                
        chord_tone = chromatic_scale_tones[(root_index + degree * 5 ) % len(chromatic_scale_tones)]               
        chord_tones.append(chord_tone)
        mchords = []

    #基本の型をタイプごとに回転
    for type in range(5):
        
        zure = type* 3 % 5
        notes = chord_tones[zure:] + chord_tones[:zure]
        chord = []
        totalIndex = 0
        lastIndex = 0
        octave = 2  
        #一音ずつオクターブを決定、和音を生成
        for degree2 in range(5):
            
            note = notes[degree2]
            noteIndex = chromatic_scale_tones.index(note)
            if noteIndex < lastIndex:
                octave += 1
            lastIndex = noteIndex
                            
            chord.append([note, octave])
        
        mchords.append(chord)
   
    McCoy_style_chords[chord_name] = mchords
    