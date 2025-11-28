# Spotify_project_azure_databricks

##Data Architecture
<img width="1217" height="645" alt="ADF_DataBricks_Data_Architecture drawio" src="https://github.com/user-attachments/assets/dbf82af8-ef01-4a3f-8924-61d281c26b4d" />

##Data Flow
Extract: Raw data ingestion via Azure Data Factory

Bronze Layer: Raw data storage in source format

Silver Layer: Data cleansing and standardization

Gold Layer: Business-level aggregates and models

Serve: Data warehouse for consumption

##Technology Stack
Layer	Technology	Purpose
Orchestration	Azure Data Factory	Data pipeline orchestration
Transformation	Azure Databricks, PySpark	Data processing & transformations
Storage	Azure Data Lake Storage	Raw and processed data storage
Data Warehouse	Azure Synapse Analytics	Analytics and reporting
Version Control	GitHub	CI/CD and collaboration
Data Catalog	Unity Catalog	Metadata management

##Project Structure
text
spotify-data-platform/
├── adf-pipelines/                 # Azure Data Factory pipelines
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── databricks/
│   ├── notebooks/
│   │   ├── bronze_to_silver/
│   │   ├── silver_to_gold/
│   │   └── utilities/
│   ├── scripts/
│   └── config/
├── schemas/                       # Data schemas and DDL
├── cicd/                         # CI/CD pipelines
├── docs/                         # Documentation
└── tests/                        # Unit and integration tests

##Data Pipeline Details
Bronze Layer (Raw Data)
Purpose: Store raw data in original format

Features:

Incremental data loading with backfilling capabilities

Schema validation and error handling

Raw data versioning

Technologies: Azure Data Factory, Auto Loader

Silver Layer (Cleaned Data)
Purpose: Data cleansing and standardization

Transformations:

Data deduplication

Schema enforcement and evolution

Slowly Changing Dimensions (SCD) Type 1/2

Data quality checks

Pyspark transformations (joins, window functions, etc.)

Technologies: Databricks, PySpark, Unity Catalog

Gold Layer (Business Models)
Purpose: Business-ready aggregated data

Features:

Delta Lake tables for ACID transactions

Optimized for query performance

Business domain models

Data mart creation

Technologies: Delta Lake, Azure Synapse

##Key Features
Dynamic Data Pipelines
Metadata-driven pipelines using Jinja templates

Incremental processing with automatic backfilling

Schema evolution handling

Data lineage tracking

Data Quality & Governance
Unity Catalog for centralized governance

Data quality monitoring and alerting

Access control and security groups

Audit logging and compliance

CI/CD Implementation
GitHub-based version control

Automated testing and deployment

Environment promotion (Dev → Staging → Prod)

Infrastructure as Code (Terraform/ARM templates)

##License
This project is licensed under the MIT License - see the LICENSE file for details.
