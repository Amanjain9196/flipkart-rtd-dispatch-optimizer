import pandas as pd
from pathlib import Path

DATA = Path('data/orders.csv')


def score_order(row):
    score = 0
    reasons = []
    if row['hours_to_sla'] <= 2:
        score += 50; reasons.append('SLA within 2 hours')
    elif row['hours_to_sla'] <= 6:
        score += 30; reasons.append('SLA within 6 hours')
    if row['status'] in {'packed','ready_to_dispatch'}:
        score += 10
    else:
        score += 20; reasons.append('Order not dispatch-ready')
    if row['warehouse_backlog'] >= 80:
        score += 20; reasons.append('High warehouse backlog')
    if row['order_age_hours'] >= 24:
        score += 10; reasons.append('Order ageing')
    return min(score,100), '; '.join(reasons) or 'No major risk'


def classify(score):
    return 'Dispatch Now' if score >= 70 else 'Monitor' if score >= 40 else 'Safe'


def main():
    df = pd.read_csv(DATA)
    scored = df.apply(lambda r: score_order(r), axis=1, result_type='expand')
    df[['risk_score','reason']] = scored
    df['priority'] = df['risk_score'].map(classify)
    print(df.sort_values('risk_score', ascending=False).to_string(index=False))

if __name__ == '__main__':
    main()
