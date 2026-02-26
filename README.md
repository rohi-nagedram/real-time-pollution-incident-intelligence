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
