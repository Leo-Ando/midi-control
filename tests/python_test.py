import itertools

def configure_iterators(*lists):
    """
    複数のリストを受け取り、最も長いリストを除いて、他のリストを無限ループするイテレータに変換します。
    
    Args:
        *lists: 可変長のリスト引数
    
    Returns:
        tuple: 各リストまたはそのイテレータのタプル
    """
    # 各リストの長さを取得
    lengths = [len(lst) for lst in lists]
    
    # 最も長いリストを特定
    max_length_index = lengths.index(max(lengths))
    
    # イテレータを設定e
    iterators = []
    for i, lst in enumerate(lists):
        if i == max_length_index:
            # 最も長いリストはそのまま返す
            iterators.append(lst)
        else:
            # それ以外は無限ループするイテレータに変換
            iterators.append(itertools.cycle(lst))
    
    return tuple(iterators)

# 使用例:
rhythm_order = [0, 1, 2]
rhythm_repetitions = [3, 1]
pitch_order = [60, 62, 64, 65]
patterns = [{'measure': 1}, {'measure': 0.5}, {'measure': 1.5}]

# イテレータを設定
rhythm_order_iter, rhythm_repetitions_iter, pitch_order_iter = configure_iterators(rhythm_order, rhythm_repetitions, pitch_order)

# サンプル使用
for ro, rr, po in zip(rhythm_order_iter, rhythm_repetitions_iter, pitch_order_iter):
    print(f"Rhythm Index: {ro}, Repetitions: {rr}, Pitch: {po}")
    if ro == rhythm_order[-1]:  # サンプルで無限ループを防ぐための条件
        break

