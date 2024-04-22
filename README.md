rhythm_orderとrhythm_repetitionsから求められる小節数をリズムの長さとする
song_pitch_measuresから求められる小節数をピッチの長さとする

## main.pyでのrhythm_orderとrhythm_repetitionsの定義について
- patternsの要素数よりもorderとrepetitionsの要素数の方が多いとどうなるか
  - `問題ない。多い分だけpatternsのリズムが繰り返される`
  
- orderの要素数とrepetittionsの要素数が違うとどうなるか
  - `リストの長さが短い方に合わせてリズムが作られ、長い方の長い分は無視される。`
 
- rhythm_orderとrhythm_repetitionsから求められる小節数がmeasureと異なるとどうなるか
  - `求められる小説数の方が短い場合は、measureと同じ長さになるまで繰り返される。`
  - `求められる小節数の方が長い場合は、measureの長さの分だけ生成され、残りは無視される。`

- orderとrepetitionsの決め方のルールを書くべき

## rhythms_list_with_note_offの生成
- **rhythm_orderとrhythm_repetitionsの長さが違う時にどうなるか**
   - `短い方のリストに合わせてrhyths_list_with_note_offが生成される`
     `長い方のリストの長い分は無視される`
  `generate_jointed_rhythmsのfor文でzipを使っているから`


## jointed_pitchの生成
- **rhythm_orderとrhythm_repetitionsとpitch_orderの長さが違う時にどうなるか**
- リズムの長さの方がpitchの長さより長い場合
  - `リズムの長さの長い分は無視される`
- pitchの長さの方がリズムの長さより長い場合
  - `ピッチの長さに達するまでリズムの長さをループする`  


## rhythm_sendの生成
- **rhythms_list_with_note_offとjointed_pitchの長さが違う時にどうなるか**
  
  - rhythmの方がpitchより長い場合
  - `rhythmの長い部分は無視される`
  - pitchの方がrhythmより長い場合
  - `pitchの長さに達するまでrhythmがループする`
 
- rhythm_sendはmeasureの正数倍か、jointed_pitchの正数倍か
  - `measureの長さと等しい。jointed_pitchの整数倍とは限らない。`
  - `ピッチの長さがmeasureより短い場合は、measureと同じ長さになるまで繰り返される`
  - `ピッチの長さがmeasureより長い場合は、measureの長さの分だけ生成され、残りは無視される`

## pitchの定義方法
- 曲全体を通してpitchを定義できる様にするべき
- pitchを定義するときに、pitchごとの小説数も定義するべきか?
  - その場合、rhythm_orderとrhythm_repetitionsはどうなるか
  - `リズムとピッチを別のものとして生成し、その後ピッチの長さに合わせてリズムの長さを変える様にした。`

## pitchのある楽器のpatternsについて
- patternsの要素数をもっと少なくする
- patternsは固定で、pitchだけ変えていく
    - 一つのpatternsの要素から一つだけのリズムを生成するのか
    - 一つのpatternsの要素から複数のリズムを生成する様にするのか
   
- その場合rhythm_orderとrhythm_repetitionsはどうなるか

