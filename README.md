# Retail ETL Pipeline with Airflow, Docker & PostgreSQL

## Overview

This project implements an end-to-end ETL pipeline for processing retail customer data from the Olist dataset.

The pipeline is built to simulate a production-oriented Data Engineering workflow, including:

- Data extraction from raw CSV files
- Data validation and quality checks
- Data transformation
- Loading processed data into PostgreSQL
- Workflow orchestration using Apache Airflow
- Containerized deployment using Docker Compose

The goal of this project is to demonstrate practical Data Engineering skills including ETL development, database integration, orchestration, and containerization.

---

# Architecture

```
                    +----------------+
                    |  Raw CSV Data  |
                    | Olist Dataset  |
                    +-------+--------+
                            |
                            |
                            v

                    +---------------+
                    |    Extract    |
                    | Customer      |
                    | Extractor     |
                    +-------+-------+
                            |
                            v

                    +---------------+
                    |   Validate    |
                    | Data Quality  |
                    +-------+-------+
                            |
                            v

                    +---------------+
                    |  Transform    |
                    | Cleaning &    |
                    | Standardizing |
                    +-------+-------+
                            |
                            v

                    +---------------+
                    |     Load      |
                    | PostgreSQL    |
                    +-------+-------+
                            |
                            v

                    +----------------+
                    | retail schema  |
                    | customers     |
                    +----------------+


                    Apache Airflow
                           |
                           |
                    customer_etl_dag
                           |
                           |
                    PythonOperator
                           |
                           |
                  customer_pipeline.py
```

---

# Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.12 |
| ETL Framework | Python (Pandas) |
| Workflow Orchestration | Apache Airflow |
| Database | PostgreSQL 17 |
| Database Management | pgAdmin 4 |
| Containerization | Docker & Docker Compose |
| ORM / Database Connection | SQLAlchemy |
| Environment Management | uv |

---

# Project Structure

```
retail-etl-pipeline/

│
├── dags/
│   └── customer_etl_dag.py
│
├── src/
│   │
│   ├── extract/
│   │   └── customer_extractor.py
│   │
│   ├── validation/
│   │   └── customer_validator.py
│   │
│   ├── transform/
│   │   └── customer_transformer.py
│   │
│   ├── load/
│   │   └── postgres_loader.py
│   │
│   ├── pipelines/
│   │   └── customer_pipeline.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── utils/
│       └── logger.py
│
├── data/
│   └── raw/
│       └── olist_customers_dataset.csv
│
├── postgres/
│   └── init/
│
├── docker-compose.yml
├── Dockerfile
├── .env
└── README.md
```

---

# Data Pipeline

## 1. Extract

The pipeline reads raw customer data from the Olist dataset.

Input:

```
data/raw/olist_customers_dataset.csv
```

Example:

```
customer_id
customer_unique_id
customer_zip_code_prefix
customer_city
customer_state
```

---

## 2. Validation

Before loading data into PostgreSQL, the pipeline performs data quality checks:

- Dataset is not empty
- Required columns exist
- Missing value checks
- Duplicate checks

Example validation logs:

```
Not empty.
Not missing column.
Customer dataset validation completed.
```

---

## 3. Transformation

Data preprocessing includes:

- Removing leading/trailing spaces
- Standardizing city names
- Standardizing state codes
- Removing duplicate records
- Handling missing values

---

## 4. Load

Processed data is loaded into PostgreSQL.

Database:

```
mydb
```

Schema:

```
retail
```

Table:

```
retail.customers
```

Current data volume:

```
99,441 customer records
```

---

# Airflow DAG

The pipeline is orchestrated by Apache Airflow.

DAG:

```
customer_etl_dag
```

Task:

```
customer_etl
```

Execution flow:

```
customer_etl_dag

        |
        v

PythonOperator

        |
        v

run_customer_pipeline()

        |
        v

Extract
Validate
Transform
Load
```

---

# Running the Project

## 1. Clone repository

```bash
git clone <repository-url>

cd retail-etl-pipeline
```

---

## 2. Configure environment variables

Create `.env`:

```env
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=mydb
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123

POSTGRES_SCHEMA=retail
```

---

## 3. Start services

Build and start Docker containers:

```bash
docker compose up -d --build
```

Services:

```
PostgreSQL
pgAdmin
ETL container
Airflow Scheduler
Airflow API Server
Airflow Worker
Redis
```

---

## 4. Initialize Airflow

```bash
docker compose up airflow-init
```

---

## 5. Access Airflow UI

Open:

```
http://localhost:8080
```

Default credentials:

```
username: airflow
password: airflow
```

Trigger:

```
customer_etl_dag
```

---

## 6. Access PostgreSQL

Using pgAdmin:

```
Host:
postgres

Database:
mydb

Schema:
retail
```

Verify:

```sql
SELECT COUNT(*)
FROM retail.customers;
```

Expected result:

```
99441
```

---

# Database Design

Current schema:

```
mydb

└── retail

    └── customers
```

Future expansion:

```
retail

├── customers
├── orders
├── order_items
├── products
└── payments
```

---

# Key Engineering Practices

This project demonstrates:

- Modular ETL architecture
- Separation of Extract / Transform / Load layers
- Containerized development environment
- Workflow orchestration
- Database schema management
- Logging and monitoring
- Data validation before ingestion

---

# Future Improvements

Potential improvements:

- Add more Olist datasets (orders, products, payments)
- Implement incremental loading
- Add data quality monitoring
- Add warehouse modeling (star schema)
- Deploy pipeline to cloud environment
- Add CI/CD pipeline

---

# Author

Giao Dang

Data Engineering Portfolio Project