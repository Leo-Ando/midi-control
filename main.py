import mido
import random
import time
from pynput.keyboard import Key, Listener
import threading 

from definitions.midi_definitions import send_midi_data
from definitions.chord_definitions import  root_notes, chromatic_scale_tones
from definitions.rhythm_functions import generate_rhythms_list, generate_rhythm_send_from_rhythms, generate_percussion_rhythm_send,  generate_solo_rhythm_send_from_rhythms, generate_M_rhythm_send_from_rhythms, generate_M_base_rhythm_send_from_rhythms

chord_notes = 1



#リズムの生成
#original
M = 32 * 4 * 4
C = [["C", 4]]

#kick
kick_patterns = [
    {'measure': 1,     'min': 0, 'MAX': 6,  'quarter_front': 0.8, 'quarter_back': 0.3, 'eighth_back': 0.3, 'sixteenth_back': 0.3, 'thirty_second_back': 0},
    {'measure': 0.75,  'min': 2, 'MAX': 3,  'quarter_front': 0.5, 'quarter_back': 0.8, 'eighth_back': 0.3, 'sixteenth_back': 0,   'thirty_second_back': 0},
    {'measure': 0.25,  'min': 1, 'MAX': 1,  'quarter_front': 0.5, 'quarter_back': 0.4, 'eighth_back': 0.3, 'sixteenth_back': 0,   'thirty_second_back': 0},
]
kick_rhythms_list = generate_rhythms_list(kick_patterns) # patternsの１行ずつに対応するリズムが入ったリスト
kick_rhythm_order =       [ 0, 1, 2, 1, 2, 1, 2, 1, 2]
kick_rhythm_repetitions = [ 4, 1, 1, 1, 1, 1, 1, 1, 1]
kick_rhythm_send = generate_percussion_rhythm_send(kick_patterns, kick_rhythms_list, kick_rhythm_order, kick_rhythm_repetitions, M)

#snare
snare_patterns = [
    {'measure': 1, 'tipe': 'ON', 'min': 0, 'MAX': 60, 'quarter_front': 0, 'quarter_back': 0, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 0.5, 'tipe': 'ON', 'min': 1, 'MAX': 3, 'quarter_front': 0, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 0.5, 'tipe': 'ON', 'min': 4, 'MAX': 4, 'quarter_front': 0, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.5, 'thirty_second_back': 0}
]
snare_rhythms_list = generate_rhythms_list(snare_patterns)
# print("snare")
# print(snare_rhythms)
snare_rhythm_order =       [ 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
snare_rhythm_repetitions = [ 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1,3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 1]
snare_rhythm_send = generate_percussion_rhythm_send(snare_patterns, snare_rhythms_list, snare_rhythm_order, snare_rhythm_repetitions, M)

#click
click_patterns = [
    {'measure': 1, 'min': 0, 'MAX': 60, 'quarter_front': 0, 'quarter_back': 0, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 0.25, 'min': 1, 'MAX': 2, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 0.25, 'min': 1, 'MAX': 3, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0.8, 'thirty_second_back': 0},
    {'measure': 0.25, 'min': 1, 'MAX': 3, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 0.25, 'min': 1, 'MAX': 4, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0.8, 'thirty_second_back': 0}
]
click_rhythms_list = generate_rhythms_list(click_patterns)
# print("click")
# print(click_rhythms)
click_rhythm_order = [ 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3 , 4, 3, 4, 3, 4, 3, 4, 3, 4]
click_rhythm_repetitions = [ 3, 1, 3, 1, 3, 1, 3, 1 , 3, 1, 3, 1, 3, 1, 3, 1,3, 1, 3, 1, 3, 1, 3, 1,3, 1, 3, 1, 3, 1, 3, 1 , 3, 1, 3, 1, 3, 1 , 3, 1, 3, 1, 3, 1, 3, 1,3, 1, 3, 1, 3, 1, 3, 1]
click_rhythm_send = generate_percussion_rhythm_send(click_patterns, click_rhythms_list, click_rhythm_order, click_rhythm_repetitions, M )


#high
high_patterns = [
    {'measure': 1, 'min': 3, 'MAX': 5, 'quarter_front': 0, 'quarter_back': 1, 'eighth_back': 0.6, 'sixteenth_back': 0, 'thirty_second_back': 0}]
   
high_rhythms_list = generate_rhythms_list(high_patterns)
# print("high")
# print(high_rhythms)
high_rhythm_order = [0, 0, 0]
high_rhythm_repetitions = [4, 8, 1]
high_rhythm_send = generate_percussion_rhythm_send(high_patterns, high_rhythms_list, high_rhythm_order, high_rhythm_repetitions, M)

#chord1
m = 20/2 
mm = 20/2
l = 30/2
solo_patterns = [
    {'measure': 1, 'tipe': 'ON', 'min': mm, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': mm, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': mm, 'MAX':l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': mm, 'MAX':l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.7, 'eighth_back': 0.6, 'sixteenth_back': 0.4, 'thirty_second_back': 0},
]
solo_rhythms_list = generate_rhythms_list(solo_patterns)
# print("chord2")
# print(chord1_rhythms)
solo_pitch_order = [    
    "E",
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
    random.choice(root_notes),
]


for i in solo_pitch_order:
    print(chromatic_scale_tones[(chromatic_scale_tones.index(i) + 8) % len(chromatic_scale_tones)])



solo_rhythm_order =       [0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]
solo_rhythm_repetitions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
solo_rhythm_send = generate_solo_rhythm_send_from_rhythms(solo_patterns, solo_rhythms_list, solo_pitch_order, solo_rhythm_order, solo_rhythm_repetitions, M)

#chord2
m = 4
l = 60/5
chord2_patterns = [
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},    
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.3, 'quarter_back': 0.5, 'eighth_back': 0.5, 'sixteenth_back': 0, 'thirty_second_back': 0},    
]
chord2_rhythms_list = generate_rhythms_list(chord2_patterns)
# print("chord2")
# print(cord2_rhythms)
chord2_pitch_order = solo_pitch_order

# for i in chord2_pitch_order:
#     print(i)
chord2_rhythm_order =       [0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]
chord2_rhythm_repetitions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
chord2_rhythm_send = generate_M_rhythm_send_from_rhythms(chord2_patterns, chord2_rhythms_list, chord2_pitch_order, chord2_rhythm_order, chord2_rhythm_repetitions, M)

#base
m = 2
l = 4
base_patterns = [
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},    
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},
    {'measure': 1, 'tipe': 'ON', 'min': m, 'MAX': l, 'quarter_front': 0.5, 'quarter_back': 0.5, 'eighth_back': 0, 'sixteenth_back': 0, 'thirty_second_back': 0},    
]
base_rhythms_list = generate_rhythms_list(base_patterns)
# print("chord2")
# print(chord1_rhythms)
base_pitch_order =  solo_pitch_order

base_rhythm_order =       [0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]
base_rhythm_repetitions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
base_rhythm_send = generate_M_base_rhythm_send_from_rhythms(base_patterns, base_rhythms_list, base_pitch_order, base_rhythm_order, base_rhythm_repetitions, M)



instrument_names = ["kick", "snare", "click", "high", "solo", "chord2", "base"]
removed_instrument_names = []
instrument_numbers = {
    1: "kick",
    2: "snare",
    3: "click",
    4: "high",
    5: "solo",
    6: "chord2",
    7: "base"
}


midi_port_names ={
"kick" : "1",
"click" : "1 2",
"snare" : "1 3",
"high": "1 4",
"chord2" : "1 5",
"solo" : "1 6",
"base" : "1 7"
}

# [["kick", kick_rhythm_send], ["chord", chord_rhythm_send]] といったリストを作成
def generate_rhythm_patterns_dict(instrument_names):
    rhythm_patterns = []
    for instrument_name in instrument_names:
        rhythm_pattern = []
        rhythm_pattern.append(instrument_name)
        rhythm_pattern.append(eval(f'{instrument_name}_rhythm_send'))
        rhythm_patterns.append(rhythm_pattern)
    return rhythm_patterns

# instrument_namesから要素を取り出したり元に戻したりする関数
def remove_instrument(instrument_names, instrument_number):
    #instrument_number -= 1
    instrument_name = instrument_numbers[instrument_number]
    if instrument_name in instrument_names:
        instrument_names.remove(instrument_name)
        removed_instrument_names.append(instrument_name)
    elif instrument_name in removed_instrument_names:
        removed_instrument_names.remove(instrument_name)
        instrument_names.append(instrument_name)
    return instrument_names, removed_instrument_names
    
# BPMに基づいた待ち時間を計算する関数
def calculate_wait_times(BPM):
    time_between_32th = 60 / (BPM * 8)   #待ち時間
    swing_time_between_32th = time_between_32th * swing_factor / 3  # スイングのずれ幅、基本は2/3
    return time_between_32th, swing_time_between_32th

# グローバル変数とそのロックを定義
BPM = 120
is_playing = True
BPMLock = threading.Lock()
swing_factor =1.6
swingLock = threading.Lock()
rhythm_patterns = generate_rhythm_patterns_dict(instrument_names)
instrumentsLock = threading.Lock()
airphone_shift = 0
airphone_shiftLock = threading.Lock()


import mido
import threading
import time

# MIDIメッセージを受信して処理する関数
def process_midi_input():
    print(mido.get_input_names())
    inport = mido.open_input('Aerophone')
    outport = mido.open_output('1 8')  # 出力ポートは適宜調整してください

    # 鳴っている音のリストを保持する辞書
    # キーは元のnote値、値は転調後のnote値
    playing_notes = {}

    while True:  # 無限ループでMIDIメッセージを受信し続ける
        for msg in inport.iter_pending():
            if msg.type == 'note_on' and msg.velocity > 0:
                # note_on処理
                original_note = msg.note
                transposed_note = original_note + airphone_shift + 8
                new_msg = msg.copy(note=transposed_note, velocity=100)
                outport.send(new_msg)
                playing_notes[original_note] = transposed_note
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                # note_off処理
                original_note = msg.note
                if original_note in playing_notes:
                    # 転調後のnote_offを送信
                    transposed_note = playing_notes[original_note]
                    new_msg = msg.copy(note=transposed_note, velocity=0)
                    outport.send(new_msg)
                    del playing_notes[original_note]
            # 転調が変更された場合（例：キーボード操作による）は、
            # すべての鳴っている音のnote_offを送信する処理が必要です
            # これは別の場所（例：キーボードイベントハンドラ）で行う必要があります

# MIDI処理のスレッドを開始
midi_thread = threading.Thread(target=process_midi_input)
midi_thread.daemon = True  # メインスレッドが終了したら、このスレッドも自動的に終了するようにする
midi_thread.start()



#キーボードによる操作
def on_press(key):
    
    try:
        #キーボードの数字キーで楽器をミュート、もう一度押すとミュート解除
        global instrument_names, removed_instrument_names
        if key.char.isdigit(): #押されたキーがchar属性を持ち、数字なら
            if 1 <= int(key.char) <= len(instrument_numbers): #押された数字が1以上楽器の数以下なら
                instrument_number = int(key.char)
                with instrumentsLock:
                    instrument_names, removed_instrument_names = remove_instrument(instrument_names, instrument_number)
                    print(instrument_names)
                    
    except AttributeError:   
              
        #スペースキーを押すと再生、もう一度押すと停止
        global is_playing
        if key == Key.space:
            is_playing = not is_playing #再生と停止を切り替える     
            
        #矢印上下キーでBPMを変更 
        global BPM
        if key == Key.up:
            with BPMLock: 
                BPM += 5
                print(BPM)
        if key == Key.down and BPM > 5:
            with BPMLock:
                BPM -= 5 
                print(BPM)
                
        #矢印左右キーでswingの強さを変更
        global swing_factor  
        if key == key.left and swing_factor > 0.3:
            with swingLock:
                swing_factor -= 0.3
                print(swing_factor)
        if key == key.right and swing_factor < 2.6:
            with swingLock:
                swing_factor += 0.3
                print(swing_factor)
                
   
 
      
listener =Listener(on_press=on_press)
listener.start()





# AerophoneからMIDIメッセージを受信して処理する関数
# def process_midi_input():
#     print(mido.get_input_names())
#     inport = mido.open_input('Aerophone')
#     outport = mido.open_output('1 8')  # 出力ポートは適宜調整してください

#     while True:  # 無限ループでMIDIメッセージを受信し続ける
#         for msg in inport.iter_pending():
#             if msg.type == 'note_on' or msg.type == 'note_off':
#                 with airphone_shiftLock:
#                     for interval in [0]:
#                         new_note = msg.note + interval + airphone_shift + 8
#                         new_msg = msg.copy(note=new_note, velocity=100)
#                         outport.send(new_msg)







#再生
# BPM = 120
# time_between_32th =  60 / (BPM * 8) #待ち時間
# swing_time_between_32th = time_between_32th * 1.3/3  # スイングのずれ幅、基本は2/3

from contextlib import ExitStack
midi_ports = {}


with ExitStack() as stack: #開くmidiポートを定義
    for instrument in instrument_names:
        # MIDIポート名を取得
        midi_port_name = midi_port_names[instrument]
        # MIDIポートを開く
        midi_port = stack.enter_context(mido.open_output(midi_port_name))
        # 開いたMIDIポートを辞書に格納
        midi_ports[instrument] = midi_port
            
   
    for x in range(8): #曲を繰り返す回数
            
        for i in range(len(chord2_rhythm_send)):
            
            while not is_playing: #スペースキーで再生と停止を切り替える
                time.sleep(0.1)
             
            for instrument_and_pattern in rhythm_patterns:
                instrument = instrument_and_pattern[0]
                pattern = instrument_and_pattern[1]
                send_midi_data(pattern[i]["action"], pattern[i].get("note", None), midi_ports[instrument])

            # Wait for the next action
            # if (i/4) % 2 == 1:
            #     time.sleep( t - st)    
            # elif ((i+1)/4) % 2 == 1:
            #     time.sleep( t + st )
            # else:
            #     time.sleep(t)
        
        
            # instrument_namesに基づいてrhythm_patternsを更新
            with instrumentsLock:
                rhythm_patterns = generate_rhythm_patterns_dict(instrument_names)
        
            # BPMに基づいて待ち時間を計算
            with BPMLock and swingLock:
                time_between_32th, swing_time_between_32th = calculate_wait_times(BPM)
                
            # キーに基づいてairphoneを転調
            with airphone_shiftLock:
                index = i // (32 * 1)
                key = solo_pitch_order[index]
                print(key)
                airphone_shift = chromatic_scale_tones.index(key)
                 
                
                
            #　待つ
            if (i-2) % 4 == 0:
                time.sleep( time_between_32th - swing_time_between_32th)
            elif (i-1) % 4 == 0:
                time.sleep( time_between_32th + swing_time_between_32th )
            else:
                time.sleep(time_between_32th)
            
            
            
        
    

# python "c:/Users/Leo/VS code python/音楽生成/midi再生.py"


