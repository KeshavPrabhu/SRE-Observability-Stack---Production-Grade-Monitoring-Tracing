# 🔭 SRE Observability Stack: Production-Grade Monitoring & Tracing

A complete, production-inspired observability stack built to monitor a distributed application. This project demonstrates core Site Reliability Engineering (SRE) principles using the modern open-source observability ecosystem.

## 🏗 Architecture
*(Will  add architecture diagram shortly)*

## 🛠 Tech Stack
* **Application:** Python (Flask), Vanilla JS, Nginx, PostgreSQL
* **Telemetry Collection:** OpenTelemetry (OTel) Collector
* **Metrics:** Prometheus, Node Exporter, Postgres Exporter, Nginx Exporter
* **Logs:** Loki, Promtail
* **Traces:** Tempo
* **Visualization & Alerting:** Grafana, Alertmanager

## 🧠 What This Project Demonstrates
This is not a "Hello World" dashboard. It simulates real-world production chaos and monitors it using SRE best practices:
1. **Four Golden Signals:** Monitoring Latency, Traffic, Errors, and Saturation via Prometheus and OpenTelemetry.
2. **Distributed Tracing:** Every API request is instrumented. Traces flow from Flask -> OTel -> Tempo, allowing deep-dive analysis of slow database queries.
3. **Log Aggregation:** Promtail scrapes Docker logs and ships them to Loki.
4. **Chaos Engineering (Simulated):** The backend intentionally injects random latency spikes and 500 Internal Server Errors to test the alerting pipeline.
5. **Actionable Alerting:** Prometheus rules are configured to trigger Alertmanager when error rates exceed 5% or latency exceeds 1.5s.

## 🚀 Getting Started
1. Clone the repository.
2. Run `docker compose up -d --build`.
3. Access the demo app at `http://localhost:8080`.
4. Generate traffic by clicking through the exam flow.
5. Access Grafana at `http://localhost:3000` (admin/admin) to view the **SRE Command Center**.

## 📊 Screenshots
*(I will add it later)*

## 🚨 Alerting Rules
* **HighErrorRate:** Triggers if the 1-minute error rate exceeds 5%.
* **HighLatency:** Triggers if average request duration exceeds 1.5s.
* **ServiceDown:** Triggers if any scrape target goes offline.
