# Flipkart RTD Dispatch Optimizer

**Repository description:** AI-assisted dispatch prioritization engine that predicts RTD/SLA risk and ranks marketplace orders by urgency.

> Portfolio demo using synthetic data only. No employer-confidential operational data is included.

## Problem
Marketplace operations teams often manage large order queues with different SLA cut-offs, warehouse constraints, order ages and shipment states. A flat queue makes it easy to miss orders that are most likely to breach RTD commitments.

## Solution
This project scores each order using time-to-SLA, current status, warehouse backlog, order age and operational risk signals, then classifies it into **Dispatch Now**, **Monitor**, or **Safe**.

## Architecture
```text
Synthetic order feed -> Validation -> Risk scoring -> Priority queue -> Ops dashboard / alerts
```

## Features
- RTD/SLA risk score per order
- Warehouse-level backlog risk
- Priority queue sorted by urgency
- Explainable reason codes
- Synthetic demo dataset
- Unit tests + CI

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Portfolio signal
Demonstrates operations automation, prioritization logic, risk modeling and decision-support design for marketplace workflows.
