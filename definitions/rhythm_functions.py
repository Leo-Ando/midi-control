import random
from definitions.chord_definitions import tones_of_McCoy_style_chord, McCoy_style_chords, chromatic_scale_tones
from definitions.midi_definitions import note_name_to_midi_note_number_dict

def generate_rhythm(measure, quarter_front, quarter_back, eighth_back, sixteenth_back, thirty_second_back, min, max):
    total_notes = int(measure * 32)
    rhythm = ['0'] * total_notes

    while True:
        for ii in range(total_notes):
            i = ii + 1
            if i % 2 == 0: 
                if random.random() < thirty_second_back:
                    rhythm[ii] = '1'        
            elif ((i+1) % 4 )== 0:
                if random.random() < sixteenth_back:
                    rhythm[ii] = '1'
            elif ((i-1) % 4) == 0 and (((i-1) / 4 + 1 ) % 2) == 0.0:
                if random.random() < eighth_back:
                    rhythm[ii] = '1'
            elif ((i-1) % 8) == 0 and (((i-1) / 8 +1 ) % 2)  == 0.0:
                if random.random() < quarter_back:
                    rhythm[ii] = '1'
            else:
                if random.random() < quarter_front:
                    rhythm[ii] = '1'
                    
        ones_count = rhythm.count('1')

        # Check if number of '1's is within the specified range
        if min <= ones_count <= max:
            break
        else:
            # Reset rhythm and try again
            rhythm = ['0'] * total_notes

    return rhythm

def generate_rhythms_list(patterns):
    rhythms_list = []
    for pattern in patterns:
        rhythm = generate_rhythm(pattern['measure'], pattern['quarter_front'], pattern['quarter_back'], pattern['eighth_back'], pattern['sixteenth_back'], pattern['thirty_second_back'], pattern['min'], pattern['MAX'])
        rhythms_list.append(rhythm)
    return rhythms_list


# rhythmsをつなげてひと続きのリストにする
def generate_jointed_rhythms( rhythms_list, rhythm_order, rhythm_repetitions ):
    jointed_rhythms = []
    for rhythm_index, repetitions in zip( rhythm_order, rhythm_repetitions ):
        for _ in range(repetitions):
            jointed_rhythms += rhythms_list[rhythm_index]
    return jointed_rhythms

            
# rhythmsの"1"という要素と"1"という要素の間の要素数をリストにする
def generate_distances_list_of_jointed_rhythms( jointed_rhythms ):
    distances_list_of_jointed_rhythms = []
    distance = 0
    for i in reversed ( jointed_rhythms ):
        #print(i,distance)
        if i == '1' :
            distances_list_of_jointed_rhythms.append(distance)
            distance = 0
        elif i == '0':
            distance += 1
            distances_list_of_jointed_rhythms.append(0)
    distances_list_of_jointed_rhythms.reverse()
    return distances_list_of_jointed_rhythms


            
def generate_note_off(distances_list_of_jointed_rhythms):
    rhythms_list_with_note_off = []
    distance_from_last_note = 0
    sustain = 0 #音ののびる長さ
    for distance in  distances_list_of_jointed_rhythms :
        distance_from_last_note += 1
        #note_onの場合
        if distance != 0: 
            if distance_from_last_note == sustain and sustain != 0: #sustain != 0は最初のnote_onの場合を除く  
                rhythms_list_with_note_off.append("on and off")
            else :
                rhythms_list_with_note_off.append("on")
            sustain = random.randint(1, distance + 0) #note_onから次のnote_onまでのうち１つ要素を選ぶ
            distance_from_last_note = 0
        #note_offの場合
        elif distance == 0:
            if distance_from_last_note == sustain:
                rhythms_list_with_note_off.append("off")
            else:
                rhythms_list_with_note_off.append("sustain")
                
    return rhythms_list_with_note_off


def generate_rhythms_list_with_note_off( rhythms, rhythm_order, rhythm_repetitions):
    jointed_rhythms = generate_jointed_rhythms( rhythms, rhythm_order, rhythm_repetitions )
    distances_list_of_jointed_rhythms = generate_distances_list_of_jointed_rhythms( jointed_rhythms )
    rhythms_list_with_note_off = generate_note_off(distances_list_of_jointed_rhythms)
    return rhythms_list_with_note_off 

            
# jointed_rhythmに対応するpitchのひとつづきのリストを生成
def generate_jointed_pitch( patterns, rhythm_order, rhythm_repetitions, pitch_order ):
    jointed_pitch = []
    for rhythm_index, repetitions, pitch in zip( rhythm_order, rhythm_repetitions , pitch_order ):
        for _ in range(repetitions):
            pattern = patterns[rhythm_index]
            for _ in range (int(pattern['measure'] * 32)):
                jointed_pitch.append(pitch)
    return jointed_pitch


def generate_rhythm_send_from_rhythms(patterns, rhythms, pitch_order, rhythm_order, rhythm_repetitions, measure):
    rhythms_list_with_note_off = generate_rhythms_list_with_note_off( rhythms, rhythm_order, rhythm_repetitions)
    jointed_pitch = generate_jointed_pitch( patterns, rhythm_order, rhythm_repetitions, pitch_order )
    total_notes = int(measure * 32)
    rhythm_send = []

    while len(rhythm_send) < total_notes:
        for type, pitch_name in zip( rhythms_list_with_note_off, jointed_pitch ):
           
            notes = []
            if type == 'on':
                for one_pitch in pitch_name: #pitch = [["C", 4], ["E", 4]], one_pich = ["C", 4]
                    note_name = one_pitch[0]
                    octave = one_pitch[1]
                    midi_note_key = f'{note_name}{octave}'
                    midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                    notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes})
                last_notes = notes
            elif type == 'off':
                rhythm_send.append({"action": "note_off", "note": last_notes})
            elif type == 'sustain':
                rhythm_send.append({"action": "sustain"})
            
          
            if len(rhythm_send) >= total_notes:
                break

            if len(rhythm_send) >= total_notes:
                break
                      
    return rhythm_send[:total_notes]

def generate_percussion_rhythm_send(patterns, rhythms, rhythm_order, rhythm_repetitions, measure):
    rhythms_list_with_note_off = generate_rhythms_list_with_note_off( rhythms, rhythm_order, rhythm_repetitions)
    total_notes = int(measure * 32)
    rhythm_send = []

    while len(rhythm_send) < total_notes:
        for type in rhythms_list_with_note_off:
           
            notes = []
            if type == 'on':
                midi_note_key = f'C4'
                midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes})
                last_notes = notes
            elif type == 'off':
                rhythm_send.append({"action": "note_off", "note": last_notes})
            elif type == 'sustain':
                rhythm_send.append({"action": "sustain"})
            
          
            if len(rhythm_send) >= total_notes:
                break

            if len(rhythm_send) >= total_notes:
                break

    return rhythm_send[:total_notes]


def generate_M_random_pitch(chord_name):
    return random.choice(McCoy_style_chords[chord_name])

def generate_M_rhythm_send_from_rhythms(patterns, rhythms, pitch_order, rhythm_order, rhythm_repetitions, measure):
    rhythms_list_with_note_off = generate_rhythms_list_with_note_off( rhythms, rhythm_order, rhythm_repetitions)
    jointed_pitch = generate_jointed_pitch( patterns, rhythm_order, rhythm_repetitions, pitch_order )
    
    total_notes = int(measure * 32)
    rhythm_send = []

    while len(rhythm_send) < total_notes:
        for type, pitch_name in zip( rhythms_list_with_note_off, jointed_pitch ):
          
            # Read the 'tipe' attribute and set the action accordingly
            action_type = "note_on" #if pattern['tipe'] == 'ON' else "note_off"
            notes = []
            if type == "on":
                pitch = generate_M_random_pitch(pitch_name)
                for one_pitch in pitch: #pitch = [["C", 4], ["E", 4]], one_pich = ["C", 4]
                    note_name = one_pitch[0]
                    octave = one_pitch[1]
                    midi_note_key = f'{note_name}{octave}'
                    midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                    notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes})
                last_notes = notes
                
            elif type == "on and off":
                pitch = generate_M_random_pitch(pitch_name)
                for one_pitch in pitch: #pitch = [["C", 4], ["E", 4]], one_pich = ["C", 4]
                    note_name = one_pitch[0]
                    octave = one_pitch[1]
                    midi_note_key = f'{note_name}{octave}'
                    midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                    notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes}, {"action": "note_off", "note": last_notes})
                last_notes = notes
                
            elif type == "off":
                rhythm_send.append({"action": "note_off", "note": last_notes})
                
                
            elif type == "sustain":
                rhythm_send.append({"action": "sustain"})
            
            
            if len(rhythm_send) >= total_notes:
                break

    return rhythm_send[:total_notes]

def generate_random_pitch(chord_name):
    return random.choice(tones_of_McCoy_style_chord[chord_name])
         

def generate_solo_rhythm_send_from_rhythms(patterns, rhythms, pitch_order, rhythm_order, rhythm_repetitions, measure):
    
    rhythms_list_with_note_off = generate_rhythms_list_with_note_off( rhythms, rhythm_order, rhythm_repetitions)
    jointed_pitch = generate_jointed_pitch( patterns, rhythm_order, rhythm_repetitions, pitch_order )

    
    total_notes = int(measure * 32)
    rhythm_send = []
    last_pitch_name = None
    
    # 小節数がmeasureを超えないようにする
    while len(rhythm_send) < total_notes:
        last_octave = 5
        last_last_octave = 0
        
        for type, pitch_name in zip( rhythms_list_with_note_off, jointed_pitch ):
            #キーが変わったら、最初の音をランダムに決定
            if pitch_name != last_pitch_name:
                last_note_name = generate_random_pitch(pitch_name)[0]
                last_last_note_name = generate_random_pitch(pitch_name)[0]
            last_pitch_name = pitch_name    

            notes = []
            
            if type == "on":
                
                max_octave = 5
                min_octave = 4
                last_pitch_index = tones_of_McCoy_style_chord[pitch_name].index([last_note_name,4])
                
                #オクターブが範囲外の場合、やり直し  
                while True:
                    #音名決定
                    choices = [1, -1, 0]
                    weights = [0.45, 0.45, 0]  # 1, -1, 0 の確率はそれぞれ 50%, 30%, 20%
                    pitch_interval = random.choices(choices, weights, k=1)[0]
                    #chord_notesの端まで行ったら、逆方向に変更
                    if last_pitch_index == 0:
                        pitch_interval = random.choice([1,0])
                    elif last_pitch_index == 4:
                        pitch_interval = random.choice([-1,0])      
                    note_name = tones_of_McCoy_style_chord[pitch_name][last_pitch_index + pitch_interval][0]
                    
                    #オクターブ決定
                    octave = last_octave
                    octave_up_down = random.random()
                    if octave_up_down < 0.5: #音程が降下する場合
                        if chromatic_scale_tones.index(note_name) > chromatic_scale_tones.index(last_note_name):
                            octave = last_octave - 1
                    else:#音程が上昇する場合
                        if chromatic_scale_tones.index(note_name) < chromatic_scale_tones.index(last_note_name):
                            octave = last_octave + 1
                                            
                    if octave > max_octave or octave < min_octave:
                        continue
                    elif last_last_note_name == note_name and last_last_octave == octave:
                        continue
                    else:
                        break
                midi_note_key = f'{note_name}{octave}'
                midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes})
                
                last_last_note_name = last_note_name
                last_last_octave = last_octave
                last_note_name = note_name         
                last_octave = octave
                
                last_notes = notes
                
            elif type == "off":
                rhythm_send.append({"action": "note_off", "note": last_notes})
            elif type == "sustain":
                rhythm_send.append({"action": "sustain"})
            
            if len(rhythm_send) >= total_notes:
                break

    return rhythm_send[:total_notes]

def generate_M_base_random_pitch(chord_name):
    M_base = random.choice(McCoy_style_chords[chord_name])
    del M_base[2:]
    if M_base[0][1] ==  M_base[1][1]:
        M_base[0][1] = M_base[1][1] + 1
    elif M_base[0][1] <  M_base[1][1]:
        M_base[0][1] = M_base[1][1]

    return M_base

def generate_M_base_rhythm_send_from_rhythms(patterns, rhythms, pitch_order, rhythm_order, rhythm_repetitions, measure):
    rhythms_list_with_note_off = generate_rhythms_list_with_note_off( rhythms, rhythm_order, rhythm_repetitions)
    jointed_pitch = generate_jointed_pitch( patterns, rhythm_order, rhythm_repetitions, pitch_order )
    
    total_notes = int(measure * 32)
    rhythm_send = []

    while len(rhythm_send) < total_notes:
        for type, pitch_name in zip( rhythms_list_with_note_off, jointed_pitch ):
          
            # Read the 'tipe' attribute and set the action accordingly
            action_type = "note_on" #if pattern['tipe'] == 'ON' else "note_off"
            notes = []
            if type == "on":
                pitch = generate_M_base_random_pitch(pitch_name)
                # print(pitch)
                for one_pitch in pitch: #pitch = [["C", 4], ["E", 4]], one_pich = ["C", 4]
                    note_name = one_pitch[0]
                    octave = one_pitch[1]
                    midi_note_key = f'{note_name}{octave}'
                    midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                    notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes})
                last_notes = notes
                
            elif type == "on and off":
                pitch = generate_M_random_pitch(pitch_name)
                for one_pitch in pitch: #pitch = [["C", 4], ["E", 4]], one_pich = ["C", 4]
                    note_name = one_pitch[0]
                    octave = one_pitch[1]
                    midi_note_key = f'{note_name}{octave}'
                    midi_note = note_name_to_midi_note_number_dict[midi_note_key]
                    notes.append(midi_note)
                rhythm_send.append({"action": "note_on", "note": notes}, {"action": "note_off", "note": last_notes})
                last_notes = notes
                
            elif type == "off":
                rhythm_send.append({"action": "note_off", "note": last_notes})
                
                
            elif type == "sustain":
                rhythm_send.append({"action": "sustain"})
            
            
            if len(rhythm_send) >= total_notes:
                break
            
    return rhythm_send[:total_notes]
