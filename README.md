# README
This script is for scraping product data from Tokopedia, an Indonesian e-commerce platform.
It uses the requests and json library to make GET requests to the Tokopedia's search graphql endpoint, and pandas and openpyxl to store and export the data.

## How to Use
1. Install the required libraries: requests, json, pandas and openpyxl
2. Modify the search variable to the desired search term.
3. Run the script
4. The resulting data will be stored in a Pandas DataFrame and exported to an Excel file.

## Code Explanation
The script does the following:

1. Defines the search term and the URL for the graphql endpoint
2. Defines a function get_params() that creates a list of query parameters for pagination, with a range from 1 to 100.
3. Defines a function scrape_data(param) that makes a GET request to the graphql endpoint with the specified parameter and returns the JSON response.
4. Iterates through the params list, passing each parameter to the scrape_data() function to retrieve the data
5. The data is processed and stored in a Pandas DataFrame
6. The DataFrame is then exported to an Excel file.

Please note that the script is using the endpoint https://gql.tokopedia.com/graphql/SearchProductQueryV4, which is specific to the Search Product page, and also it is using some parameter specific to the endpoint like device=desktop, rows=60, scheme=https and start={} etc.
Also, this script may not work as is because of the change in the endpoint, the parameters or the structure of the data returned by the endpoint.
