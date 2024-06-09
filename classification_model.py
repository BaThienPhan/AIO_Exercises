def f1_score(tp, fp, fn):
    # Kiểm tra nếu tp,fp,fn không phải là số nguyên (int)
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return
    
    # Kiểm tra nếu bất kỳ giá trị nào trong tp, fp, fn nhỏ hơn hoặc bằng 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    
    # Tính toán Precision (Độ chính xác)
    precision = tp / (tp + fp)
    
    # Tính toán Recall (Độ nhạy)
    recall = tp / (tp + fn)
    
    # Tính toán F1-score
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    # In ra kết quả
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1-score: {f1_score}')

# Ví dụ sử dụng hàm
f1_score(50, 10, 5)
