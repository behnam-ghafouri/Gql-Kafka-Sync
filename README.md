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


http://localhost:8000/graphql/

mutation {
  createUser(username: "admin", email: "admin@crm.com", password: "password123", role: "ADMIN") {
    id
  }
}

http://localhost:8001/graphql/

mutation {
  createLead(firstName: "Clark", lastName: "Kent", companyId: 99) {
    id
  }
}

mutation {
  createDeal(name: "Daily Planet Subscription", value: 150.0, leadId: 1) {
    id
    name
  }
}

docker compose logs -f identity-consumer