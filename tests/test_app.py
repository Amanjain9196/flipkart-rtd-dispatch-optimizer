from app import classify, score_order


def test_urgent_order_scores_high():
    row = {
        'hours_to_sla': 1,
        'status': 'processing',
        'warehouse_backlog': 90,
        'order_age_hours': 30,
    }
    score, _ = score_order(row)
    assert score >= 70
    assert classify(score) == 'Dispatch Now'


def test_safe_order_classification():
    assert classify(20) == 'Safe'
