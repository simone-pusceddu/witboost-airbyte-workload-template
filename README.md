<br/>
<p align="center">
    <a href="https://www.witboost.com/">
        <img src="docs/img/witboost_logo.svg" alt="witboost" width=600 >
    </a>
</p>
<br/>

Designed by [Agile Lab](https://www.agilelab.it/), Witboost is a versatile platform that addresses a wide range of sophisticated data engineering challenges. It enables businesses to discover, enhance, and productize their data, fostering the creation of automated data platforms that adhere to the highest standards of data governance. Want to know more about Witboost? Check it out [here](https://www.witboost.com/) or [contact us!](https://witboost.com/contact-us)

This repository is part of our [Starter Kit](https://github.com/agile-lab-dev/witboost-starter-kit) meant to showcase Witboost's integration capabilities and provide a "batteries-included" product.


# Airbyte Workload Template

- [Overview](#overview)
- [Usage](#usage)

## Overview

Use this template to automatically create an Airbyte connection between a source file and a Snowflake instance.

Airbyte will take care of creating the Snowflake table, identifying the data schema based on the Pandas IO Tools.

![Provisioning](docs/img/hld-Provisioning.png)

Refer to the [witboost Starter Kit repository](https://github.com/agile-lab-dev/witboost-starter-kit) for information on the Tech Adapter that can be used to deploy components created with this Template.


### What's a Template

A Template is a tool that helps create components inside a Data Mesh. Templates help establish a standard across the organization. This standard leads to easier understanding, management and maintenance of components. Templates provide a predefined structure so that developers don't have to start from scratch each time, which leads to faster development and allows them to focus on other aspects, such as testing and business logic.

For more information, please refer to the [official documentation](https://docs.witboost.agilelab.it/docs/p1_user/p6_advanced/p6_1_templates/#getting-started).


### What's a Workload

Workload refers to any data processing step (etl, job, transformation etc.) that is applied to data in a Data Product. Workloads can pull data from sources external to the Data Mesh or from an Output Port of a different Data Product or from Storage Areas inside the same Data Product, and persist it for further processing or serving.


### Airbyte

Airbyte is an open-source data integration platform that syncs data from various sources to destinations like data warehouses, databases, and data lakes. It provides data engineering teams with a comprehensive set of tools based on a modular architecture to handle necessary tasks and operations from a single platform.

The main features of Airbyte are as follows:

- Data Stream Selection: Airbyte allows you to select the specific API streams you want to replicate, giving you control over the data you want to integrate.
- Connector Development Kit (CDK): Airbyte's CDK simplifies the process of building connectors, allowing you to create connectors in a short amount of time with minimal code.
- Data Extraction and Loading: Airbyte provides a secure and reliable way to extract data from different tools and load it into your desired data storage.
- Airbyte is self-hosted, giving you full control over your data and associated costs. It offers a cost-effective alternative to other ETL tools, as it is not volume-based in terms of pricing.

Learn more about it on the [official website](https://docs.airbyte.com/)


## Usage

To get information on how to use this template, refer to this [document](./docs/index.md).

### Component Testing

To verify the component before deploying it along with the Data Product, the component needs to be tested against a CUE Policy defined for [Airbyte Workload](./policies/airbyte.cue). This policy needs to be defined inside the **Governance** section of the Witboost Platform.

For more information, please refer to the [official documentation](https://docs.witboost.agilelab.it/docs/p1_user/p5_managing_policies/p5_1_overview).


## License

This project is available under the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0); see [LICENSE](LICENSE) for full details.

## About Witboost

[Witboost](https://witboost.com/) is a cutting-edge Data Experience platform, that streamlines complex data projects across various platforms, enabling seamless data production and consumption. This unified approach empowers you to fully utilize your data without platform-specific hurdles, fostering smoother collaboration across teams.

It seamlessly blends business-relevant information, data governance processes, and IT delivery, ensuring technically sound data projects aligned with strategic objectives. Witboost facilitates data-driven decision-making while maintaining data security, ethics, and regulatory compliance.

Moreover, Witboost maximizes data potential through automation, freeing resources for strategic initiatives. Apply your data for growth, innovation and competitive advantage.

[Contact us](https://witboost.com/contact-us) or follow us on:

- [LinkedIn](https://www.linkedin.com/showcase/witboost/)
- [YouTube](https://www.youtube.com/@witboost-platform)