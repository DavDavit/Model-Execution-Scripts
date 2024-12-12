# Model-Execution-Scripts

This repository provides a framework for executing machine learning models using data stored in Hadoop Distributed File System (HDFS). The workflow includes retrieving data, filtering it based on user input, processing the data, and running the model.

## Features

- **Dockerized Environment**: Encapsulate the scripts and dependencies for easy deployment.
- **HDFS Interaction**: Read CSV files and retrieve FITS files from Hadoop.
- **Data Processing**: Filter rows from the CSV based on user-defined parameters.
- **Model Execution**: Run an external script or model using system commands.

## Prerequisites

- Python 3.9 or higher
- Docker
- HDFS with the necessary data uploaded
- FITS file handling capabilities

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/model_execution_scripts.git
cd model_execution_scripts
