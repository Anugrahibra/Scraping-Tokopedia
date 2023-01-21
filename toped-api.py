import requests
import json
import pandas as pd
import openpyxl

search = "Laptop"
url = "https://gql.tokopedia.com/graphql/SearchProductQueryV4"
def get_params():
  params = []
  for i in range (1,101):
    param = "device=desktop&navsource=&ob=23&page={}&q={}&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start={}&topads_bucket=true&unique_id=a172a4a6f96e631e7a5a2a4aeff86da4&user_addressId=182509738&user_cityId=188&user_districtId=2459&user_id=&user_lat=-7.0504602&user_long=110.654989&user_postCode=58164&user_warehouseId=0&variants=".format(i, search, (i-1)*60)
    params.append(param)

  return params

def scrape_data(param):
    payload = [{
        "operationName": "SearchProductQueryV4",
        "variables": {
          "params": param
        },
        "query": "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
      }]

    req = requests.post(url, json=payload).json()
    rows = req[0]["data"]["ace_search_product_v4"]["data"]["products"]

    scrape_data = []
    for i in range(0, len(rows)):
      product_name = rows[i]["name"]
      price = rows[i]["price"]
      rating = rows[i]["ratingAverage"]
      store = rows[i]["shop"]["name"]
      location = rows[i]["shop"]["city"]
      scrape_data.append(
        (product_name, price, rating, store, location)
      )
    return scrape_data



if __name__ == "__main__":
  params = get_params()
  all_data = []
  for i in range(0, len(params)):
    param = params[i]
    data = scrape_data(param)
    all_data.extend(data)

  df = pd.DataFrame(all_data, columns=["product_name", "price", "rating", "store", "location"])
  df.to_excel("Laptop_Tokped.xlsx", index=False)
  print("Your data has been saved")




