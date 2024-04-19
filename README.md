## main.pyでのrhythm_orderとrhythm_repetitionsの定義について
- patternsの要素数よりもorderとrepetitionsの要素数の方が多いとどうなるか
  
- orderの要素数とrepetittionsの要素数が違うとどうなるか

- orderとrepetitionsの決め方のルールを書くべき

## rhythms_list_with_note_offの生成
- **rhythm_orderとrhythm_repetitionsの長さが違う時にどうなるか**
   - → `短い方のリストに合わせてrhyths_list_with_note_offが生成される`
     `長い方のリストの長い分は無視される`
  `generate_jointed_rhythmsのfor文でzipを使っているから`
  
  - orderの方がrepetitionsより長い場合
  - repetitionsの方がorderより長い場合


## jointed_pitchの生成
- **rhythm_orderとrhythm_repetitionsとpitch_orderの長さが違う時にどうなるか**
  
  - order,repetitionsの方がpitchより長い場合
  - pitchの方がorder,repetitionsより長い場合


## rhythm_sendの生成
- **rhythms_list_with_note_offとjointed_pitchの長さが違う時にどうなるか**
  
  - rhythmの方がpitchより長い場合
  - pitchの方がrhythmより長い場合

## pitchの定義方法
- 曲全体を通してpitchを定義できる様にするべき

- pitchを定義するときに、pitchごとの小説数も定義するべきか?
  - その場合、rhythm_orderとrhythm_repetitionsはどうなるか

## pitchのある楽器のpatternsについて
- patternsの要素数をもっと少なくする
- patternsは固定で、pitchだけ変えていく
    - 一つのpatternsの要素から一つだけのリズムを生成するのか
    - 一つのpatternsの要素から複数のリズムを生成する様にするのか
   
- その場合rhythm_orderとrhythm_repetitionsはどうなるか

