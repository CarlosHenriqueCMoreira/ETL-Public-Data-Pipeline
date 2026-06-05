# ETL-Public-Data-Pipeline

ETL Public Data Pipeline
This project implements a complete ETL (Extract, Transform, Load) pipeline using public data from the Brazilian Central Bank API (PTAX). The goal is to demonstrate in practice the three core stages of data engineering: data extraction via API, transformation and cleaning, and loading into a relational database.
About the Project
The pipeline consumes daily USD exchange rates made available through the Brazilian Central Bank's public API. Data is extracted via HTTP requests with error handling and retry logic, transformed and standardized using Pandas, and loaded into a PostgreSQL database via SQLAlchemy.
The architecture was designed to be modular and easy to maintain, separating each pipeline stage into an independent module: extract.py for extraction, transform.py for transformation, and load.py for loading. The main.py file orchestrates the entire flow end to end.
Pipeline Stages
Extract — HTTP requests are made to the PTAX API with support for multiple retry attempts on timeout. Dates are validated before the call and raw data is returned in JSON format.
Transform — raw data is converted into a structured DataFrame, with column renaming to the project standard, datetime type conversion, null record removal, and chronological sorting.
Load — the transformed DataFrame is persisted into a PostgreSQL table. The connection is managed by SQLAlchemy and credentials are securely loaded through environment variables.
Technologies

Python 3.14
Requests for HTTP calls
Pandas for data manipulation and transformation
SQLAlchemy for database connection and loading
PostgreSQL 18 for data storage
python-dotenv for secure credential management

Data Source
PTAX API from the Brazilian Central Bank, which provides daily foreign exchange rates publicly and for free, with no authentication required. Documentation available at https://olinda.bcb.gov.br.
Data Structure
Data is stored in the cotacao_dolar table containing the buy rate, sell rate, and timestamp fields.
Author
Carlos Henrique
