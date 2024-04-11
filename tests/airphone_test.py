import mido
print(mido.get_input_names())

inport = mido.open_input('Aerophone')

        # MIDI出力ポートを開く
outport = mido.open_output('1 8')

with inport as port:
    for msg in port:
        if msg.type == 'note_on':
            # 受け取ったノートの音程を半音上げる
            new_note = msg.note  
            # 新しい音程で新しいMIDIメッセージを作成
            new_msg = mido.Message('note_on', note=new_note, velocity=msg.velocity, time=msg.time)
            # 新しいMIDIメッセージを送信
            outport.send(new_msg)
            
            new_note = msg.note  + 5
            new_msg = mido.Message('note_on', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)
            
            new_note = msg.note  + 10
            new_msg = mido.Message('note_on', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)
            
            new_note = msg.note  + 15
            new_msg = mido.Message('note_on', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)
            
            new_note = msg.note  + 20
            new_msg = mido.Message('note_on', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)
            
        elif msg.type == 'note_off':
            new_note = msg.note 
            new_msg = mido.Message('note_off', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)
            
            new_note = msg.note  + 5
            new_msg = mido.Message('note_off', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)

            new_note = msg.note  + 10
            new_msg = mido.Message('note_off', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)
            
            new_note = msg.note  + 15
            new_msg = mido.Message('note_off', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)

            new_note = msg.note  + 20
            new_msg = mido.Message('note_off', note=new_note, velocity=msg.velocity, time=msg.time)
            outport.send(new_msg)

