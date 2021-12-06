#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
from urllib import parse

class UserAgent:

    def __init__(self):
        self.user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/71.0.3542.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/78.0.3882.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4298.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4164.4 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.271',
    'Mozilla/5.0 (Linux; Android 9; JAT-LX1 Build/HONORJAT-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 YaBrowser/17.11.0.542.00 Mobile Safari/537.36',
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    ]

    def myheaders(self):
        user_agent = self.user_agents
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ru,en-US;q=0.7,en;q=0.3',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': random.choice(user_agent)
                  }
        return headers

    def sup_head(self, query):
        """ replace head string """
        user_agent = self.user_agents
        url = 'https://prom.ua/search?search_term={zapros}'
        query = self.encoded_url(query)
        post_head = {
        'Host': 'prom.ua',
        'User-Agent': random.choice(user_agent),
        'Accept': '*/*',
        'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': url.format(zapros=query),
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Forwarded-Proto': 'https',
        'Origin': 'https://prom.ua',
        'DNT': '1',
        'Connection': 'close'
            }
        return post_head


    def encoded_url(self, uri):
        encode = parse.quote(uri)        
        return encode

    def swith(self, q):
        if len(q) >= 73:
            return False
        elif len(q) < 73:
            return True

    def body(self, qure):
        b = [{"variables":{"search_term":"","params":{"delivery_type":"delivery","binary_filters":[]},"limit":40,"offset":0},"extensions":{},"operationName":"SearchListingQuery","query":"query SearchListingQuery($search_term: String!, $offset: Int, $limit: Int, $params: Any, $company_id: Int, $sort: String) {\n  allFavorites {\n    products\n    __typename\n  }\n  context {\n    ...ProductContextFragment\n    promOplataEnabled\n    canBeSlow\n    __typename\n  }\n  listing: searchListing(search_term: $search_term, limit: $limit, offset: $offset, params: $params, company_id: $company_id, sort: $sort) {\n    searchTerm\n    company {\n      id\n      name\n      hasCompanyPortalZone\n      topProductGroups {\n        id\n        name\n        image(width: 200, height: 200)\n        __typename\n      }\n      portalPageURL\n      regionName\n      __typename\n    }\n    page {\n      correctedSearchTerm\n      ...ProductsListFragment\n      __typename\n    }\n    category {\n      id\n      caption\n      path {\n        id\n        caption\n        __typename\n      }\n      url\n      __typename\n    }\n    breadCrumbs {\n      items {\n        url\n        caption\n        __typename\n      }\n      lastItemClickable\n      __typename\n    }\n    searchTerm\n    elasticCats\n    searchTermData {\n      region {\n        id\n        subdomain\n        __typename\n      }\n      wholesale\n      discount\n      productType\n      isAdult\n      mainWord\n      mainEntity\n      attributes\n      searchTermProcessed\n      categoryId\n      possibleCatSource\n      __typename\n    }\n    advSource\n    __typename\n  }\n  region {\n    id\n    name\n    nameF2\n    __typename\n  }\n  proSaleNetwork {\n    ...ProSaleNetworkFragment\n    __typename\n  }\n  country {\n    name\n    nameF2\n    __typename\n  }\n}\n\nfragment ProductsListFragment on ListingPage {\n  total\n  isPaidListing\n  esQueryHash\n  isCpaOnlySearch\n  regionReset\n  topHitsCategory {\n    id\n    path {\n      id\n      caption\n      __typename\n    }\n    __typename\n  }\n  seoTags {\n    name\n    url\n    __typename\n  }\n  seoManufacturers {\n    name\n    url\n    __typename\n  }\n  seoCountries {\n    name\n    url\n    __typename\n  }\n  seoCategories {\n    name\n    url\n    __typename\n  }\n  seoNavigation {\n    name\n    url\n    __typename\n  }\n  seoPromotions {\n    name\n    url\n    __typename\n  }\n  seoTopTags {\n    name\n    url\n    __typename\n  }\n  seoTopLatestTags {\n    name\n    url\n    __typename\n  }\n  tagsBlockIndexes\n  products {\n    product_item_id\n    productModel {\n      model_id\n      product_count\n      min_price\n      max_price\n      model_product_ids\n      company_count\n      __typename\n    }\n    product {\n      ...ProductItemInfoFragment\n      __typename\n    }\n    advert {\n      ...ProductItemAdvertFragment\n      __typename\n    }\n    rp {\n      ...ProductItemRankingParametersFragment\n      __typename\n    }\n    productClickToken\n    advDebug {\n      productWeightEs\n      productScore\n      __typename\n    }\n    __typename\n  }\n  companyIds\n  quickFilters {\n    name\n    title\n    measureUnit\n    values {\n      value\n      title\n      imageUrl(width: 200, height: 200)\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductItemInfoFragment on Product {\n  id\n  ...ProductPresenceFragment\n  ...ProductItemInfoMainFragment\n  __typename\n}\n\nfragment ProductItemInfoMainFragment on Product {\n  id\n  ...ProductGalleryImageFragment\n  name: nameForCatalog\n  company_id\n  signed_id\n  groupId\n  categoryId\n  categoryIds\n  customOrderId\n  customOrderUrl\n  image(width: 200, height: 200)\n  imageAlt: image(width: 640, height: 640)\n  mainImageId\n  buyButtonDisplayType\n  productTypeKey\n  urlForProductCatalog\n  hasDiscount\n  price\n  priceFrom\n  priceUSD\n  priceOriginal\n  priceCurrency\n  priceCurrencyLocalized\n  noPriceText\n  discountedPrice\n  discountPercent\n  discountDays\n  discountDaysLabel\n  measureUnit\n  sellingType\n  wholesalePrices {\n    price\n    __typename\n  }\n  isService\n  comparisonUrl\n  isWholesale\n  isAdult\n  promoLabel {\n    active\n    image\n    __typename\n  }\n  company {\n    id\n    name\n    signedId\n    isChatVisible\n    isContactNowAllowed\n    timedHash\n    regionName(branchFirst: true)\n    opinionPositivePercent\n    opinionTotal\n    opinionTotalInRating\n    companyOpinionsUrl\n    mainLogoUrl(width: 25, height: 25)\n    urlForCompanyProducts\n    achievements\n    companyPromoLabel {\n      active\n      image\n      __typename\n    }\n    __typename\n  }\n  report_start_chat_url\n  oioCategories\n  canShowPrice\n  isOrderable\n  is_delivery_free\n  __typename\n}\n\nfragment ProductGalleryImageFragment on Product {\n  id\n  name: nameForCatalog\n  imageGallery: image(width: 700, height: 500)\n  imagesGallery: images(width: 640, height: 640)\n  imagesAltGallery: images(width: 700, height: 500)\n  __typename\n}\n\nfragment ProductPresenceFragment on Product {\n  presence {\n    title\n    presence\n    isAvailable\n    isEnding\n    isOrderable\n    isWait\n    isPresenceSure\n    __typename\n  }\n  __typename\n}\n\nfragment ProductItemAdvertFragment on Prosale {\n  clickUrl\n  categoryId\n  token\n  campaignId\n  source\n  price\n  ctr\n  otr\n  commission_rate_kind\n  advert_weight_adv\n  hash\n  __typename\n}\n\nfragment ProductItemRankingParametersFragment on RankingParameters {\n  advWeightA\n  advWeightB\n  modelId\n  advWeightBoost\n  variation\n  notAvail\n  adult\n  cats\n  opinion\n  evopay\n  orderSuccess\n  __typename\n}\n\nfragment ProductContextFragment on Context {\n  context_meta\n  countryCode\n  domain\n  currentOrigin\n  langUrlPrefix\n  currentLang\n  defaultCurrencyCode\n  countryCurrency\n  currentUserPersonal {\n    id\n    email\n    __typename\n  }\n  currentRegionId\n  __typename\n}\n\nfragment ProSaleNetworkFragment on ProSaleNetwork {\n  criteo {\n    account\n    __typename\n  }\n  criteoCategory {\n    account\n    __typename\n  }\n  rtbHouse {\n    account\n    regionParam\n    __typename\n  }\n  __typename\n}\n"}]
        b[0]['variables']['search_term'] = qure
        return json.dumps(b)

    def jurl(self) -> str:
        jurl = 'https://prom.ua/graphql'
        return jurl

    def topbody(self, body) -> list:
        body = json.loads(body)
        js_dict = self.clear_js(body)
        topbody = self.get_name_price(js_dict)
        return topbody

    def clear_js(self, js_string):
        js_byte_parse_dict = \
            js_string[0]['data']['listing']['page']['products']
        return js_byte_parse_dict

    def get_name_price(self, array) -> list:
        name, discount = [], []
        for n in range(0, len(array)):
            name_ = array[n]['product']['name']
            discount_ = array[n]['product']['discountedPrice']
            name.append(name_)
            discount.append(discount_)
        spisok = self.glue(name, discount)
        return spisok

    def glue(self, arr_a, arr_b) -> list:
        result = list(zip(arr_a, arr_b))
        return result

    pass











