# Real-Time Pollution Incident Intelligence (Delhi PM2.5)

This project demonstrates a real-time pollution incident detection system.
Instead of static dashboards, pollution readings are processed as a stream
and evaluated immediately to detect unsafe air quality events.

## Problem
Air pollution in cities like Delhi can spike rapidly.
Most systems focus on historical charts, which delays awareness and response.

## Solution
A streaming-based incident intelligence pipeline that:
- Processes pollution readings one by one
- Applies simple, explainable decision logic
- Flags PM2.5 incidents instantly when thresholds are crossed

## Why Real-Time Matters
Real-time detection enables faster alerts, public awareness,
and policy or safety responses during severe pollution events.

## Scope and Assumptions
For reliability and hackathon constraints, the submission uses
simulated pollution data. The same design supports live data
integration when external sources are available.

This project focuses on clarity of logic and system design,
not production deployment.
## Dashboard
The project includes a lightweight live console dashboard.
It displays current pollution readings and highlights incidents
in real time when PM2.5 exceeds safe levels.
## How It Works (30-second view)

1. Pollution readings arrive as a continuous stream
2. Each reading is evaluated immediately
3. If PM2.5 crosses a safe threshold, an incident is flagged
4. The system prioritizes decision-making over visualization

The project uses simulated data to ensure reliability during evaluation.
