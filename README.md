# Microservices CRM Challenge

A distributed system consisting of an **Identity Service** and a **CRM Service** using Python, Django, GraphQL, and Kafka.

## Architecture Highlights
- **Service Isolation:** Separate PostgreSQL databases for Identity and CRM to ensure true microservice decoupling.
- **Synchronous Communication:** The CRM service uses REST to fetch Company data from the Identity service during GraphQL execution.
- **Asynchronous Events:** Real-time Deal notifications are sent from CRM to Identity via Kafka.
- **Data Modeling:** - **Company:** Supports hierarchical parent-child relationships.
  - **User:** Multi-tenant design where every user belongs to a company.

## Setup & Execution
Everything is containerized. To start the entire environment:
```bash
docker compose up --build