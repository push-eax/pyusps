#!/usr/bin/python

# pyusps

import requests, json

endpoint = "https://tools.usps.com/tools/app/ziplookup/zipByAddress"

headers = {
        "Accept":           "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":  "gzip,deflate,br",
        "Content-Type":     "application/x-www-form-urlencoded; charset=UTF-8",
        "Host":             "tools.usps.com",
        "Referer":          "https://tools.usps.com/go/ZipLookupAction!input.action",
        "User-Agent":       "pyusps",
        "Connection":       "keep-alive"
}

# USPS ZIP lookup API parameters
'''
data = {
    "address1":     "",
    "address2":     "",
    "city":         "",
    "companyName":  "",
    "state":        ""
}
'''

with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        for line in input:
            addressArray = [elements.strip() for elements in line.split(",")]
            try:
                lookup = json.loads(requests.post(endpoint, headers=headers, data={"address1":addressArray[0], "address2":"", "city":addressArray[1], "companyName":"", "state":addressArray[2]}).text)
                postalCode = lookup["addressList"][0]["zip5"] + "-" + lookup["addressList"][0]["zip4"]
                print("Found " + line.strip() + " in ZIP code " + postalCode)
                output.write(line.strip() + "\t\t" + postalCode + "\n")
            except:
                print("No ZIP found for " + line.strip())
