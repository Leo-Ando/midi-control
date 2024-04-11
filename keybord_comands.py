import threading
from pynput.keyboard import Key, Listener

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


# グローバル変数とそのロックを定義
BPM = 120
is_playing = True
BPMLock = threading.Lock()
swing_factor = 0
swingLock = threading.Lock()
rhythm_patterns = generate_rhythm_patterns_dict(instrument_names)
instrumentsLock = threading.Lock()
airphone_shift = 0
airphone_shiftLock = threading.Lock()





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

