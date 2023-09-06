# ${{ values.name | dump }}

- [Overview](#overview)
- [Usage](#usage)

## Overview

Use this component to automatically create an Airbyte connection between a source file and a Snowflake instance.

Airbyte will take care of creating the Snowflake table, identifying the data schema based on the Pandas IO Tools.

### What's a Workload

Workload refers to any data processing step (etl, job, transformation etc.) that is applied to data in a Data Product. Workloads can pull data from sources external to the Data Mesh or from an Output Port of a different Data Product or from Storage Areas inside the same Data Product, and persist it for further processing or serving.

### Airbyte

Airbyte is an open-source data integration platform that syncs data from various sources to destinations like data warehouses, databases, and data lakes. It provides data engineering teams with a comprehensive set of tools based on a modular architecture to handle necessary tasks and operations from a single platform.

The main features of Airbyte are as follows:

- Data Stream Selection: Airbyte allows you to select the specific API streams you want to replicate, giving you control over the data you want to integrate.
- Connector Development Kit (CDK): Airbyte's CDK simplifies the process of building connectors, allowing you to create connectors in a short amount of time with minimal code.
- Data Extraction and Loading: Airbyte provides a secure and reliable way to extract data from different tools and load it into your desired data storage.
- Airbyte is self-hosted, giving you full control over your data and associated costs. It offers a cost-effective alternative to other ETL tools, as it is not volume-based in terms of pricing.

Learn more about it on the [official website](https://docs.airbyte.com/).

## Usage

To get information about this component and how to use it, refer to this [document](./docs/index.md).