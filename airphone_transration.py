import mido
import threading

from main import airphone_shift

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
                for interval in [0, 5, 10]:
                    # note_on処理
                    original_note = msg.note
                    transposed_note = original_note + airphone_shift + 8
                    new_msg = msg.copy(note=transposed_note, velocity=100)
                    outport.send(new_msg)
                    playing_notes[original_note] = transposed_note
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                 for interval in [0, 5, 10]:
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

