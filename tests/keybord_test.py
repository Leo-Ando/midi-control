from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        if key.char == 'a':  # 'a' キーが押された場合
            print("あああ")
            
        if key.char.isdigit():
            print("数字が押された！" + key.char) 

    except AttributeError:
        if key == Key.space:  # スペースキーが押された場合
            print("Space pressed!")
            
def on_release(key):
    if key == Key.esc:
        # esc キーが押されたら終了
        return False

# キーボードリスナーの起動
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  
  
