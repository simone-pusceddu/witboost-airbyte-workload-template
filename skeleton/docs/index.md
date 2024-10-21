{% set dataProductMajorVersion = values.identifier.split(".")[2] %}

## Component Information

| Field Name               | Value                                                                                                                  |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| **Name**                 | ${{ values.name }}                                                                                                     |
| **Fully Qualified Name** | ${{ values.domainName }} - ${{ values.dataproductName }} - version ${{ dataProductMajorVersion }} - ${{ values.name }} |
| **Description**          | ${{ values.description }}                                                                                              |
| **Domain**               | ${{ values.domain }}                                                                                                   |
| **Data Product**         | ${{ values.dataproduct }}                                                                                              |
| **Identifier**           | ${{ values.identifier }}                                                                                               |
| **Depends On**           | ${{ values.dependsOn }}                                                                                                |


## Source File Details

| Field Name           | Value                      |
|:---------------------|:---------------------------|
| **Source Name**      | ${{ values.sourceName }}   |
| **URL**              | ${{ values.url }}          |
| **File Format**      | ${{ values.format }}       |
| **Storage Provider** | ${{ values.storage }}      |
| **User-Agent**       | ${{ values.user_agent }}   |
| **Dataset Name**     | ${{ values.dataset_name }} |


## Snowflake Destination Details

| Field Name           | Value                         |
|:---------------------|:------------------------------|
| **Destination Name** | ${{ values.destinationName }} |
| **Database**         | ${{ values.database }}        |
| **Schema**           | ${{ values.schema }}          |


## Connection

| Field Name          | Value                        |
|:--------------------|:-----------------------------|
| **Connection Name** | ${{ values.connectionName }} |
