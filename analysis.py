New feature analysis code.

# === 追加機能 ===
def calculate_statistics(data):
    """データの基本統計量を計算する"""
    import statistics
    return {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'stdev': statistics.stdev(data) if len(data) > 1 else 0
    }
