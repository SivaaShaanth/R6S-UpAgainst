# Using Google Cloud Vision API to OCR scanned documents to extract structured data

Just a quickie test to see if [Google Cloud Vision](https://cloud.google.com/vision) can be used to effectively OCR a scanned data table, in the way that products like [ABBYY FineReader provide image-ocr-to-Excel](https://github.com/dannguyen/abbyy-finereader-ocr-senate).

__The short answer:__ No. While Cloud Vision provides bounding polygon coordinates in its output, it doesn't provide it at the word or region level, which would be needed to then calculate the data delimiters.

You can [read more about getting started with the Google Cloud Vision API in its official docs](https://cloud.google.com/vision/docs/getting-started). The instructions here are a somewhat simplified version of the official instructions here:

https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/python/text

Set up a Google developer account and get an API key:

https://cloud.google.com/vision/docs/auth-template/cloud-api-auth#set_up_an_api_key



## How to run

The __cloudvisreq.py__ script is included at the bottom of this gist.

~~~sh
$  python cloudvisreq.py API_KEY image1.jpg image2.png
~~~

### Sample image:

[Courtesy of Eli Lilly](http://www.lillyphysicianpaymentregistry.com/Payments-to-Physicians):

![image](https://cloud.githubusercontent.com/assets/121520/14005729/4bf2648e-f123-11e5-84d6-be1c9d84cdcd.png)



### Result:

~~~
Wrote 3021 bytes to jsons/pdftable.png.json
---------------------------------------------
    Bounding Polygon:
{'vertices': [{'y': 272, 'x': 212}, {'y': 272, 'x': 3066}, {'y': 2295, 'x': 3066}, {'y': 2295, 'x': 212}]}
    Text:
Lilly other Health Care Professional Registry
Data updated on Monday, March 3, 2014
Payments Made: Q1-Q4 2013
The Other Health Care Professional Registry reports direct and indirect payments by Lilly, as well as Lilly's portion of alliance partnership paymen
o health care professionals other than physicians serving as faculty
members. When the "Entity Paid
a company, hospital, or university, and there
a different name on the provider of service
reflects an indirect payment which may or may not actually have been received in
whole or in part by the
ted service provider. Copyright 2014 Eli Lilly and Company. All rights reserved
Note: Due to differences in scope and definitions, the data reported in this report may differ from data included in reports submitted by Lilly for compliance with state payment reporting laws
Payments
All Amounts in US Dollars
Provider of Service
*Payments for reimbursed expenses are not compensation
Entity Paid
Patient Education Professional
Education
Education
WARD, JANET
OH ABDALLAH, RITA $14,025 $500 $2,823 S17348
ABDALLAH, RITA
FAIRVIEW PARK
OH AGOSTI, CAROL $1,050 1,631 $355 $3036
AGOSTI, CAROL
TOLEDO
AINSWORTH, ABBY CORPUS CHRISTI AINSWORTH, ABBY $113 $113
AKERS, REBECCA VINCENNES IN AKERS, REBECCA
$2,400 $2,400
IALCHEMIPHARMA LLC, WAYNE PA BELAZI, DEA $11,889 $1.99 $12,088
MEADOW VISTA
ALEMAN, MARY
ALEMAN, MARY
ALEXANDER, LISA
ALEXANDER, LISA
FALLEN, CONNETTE COTTAGE GROVE
MN ALLEN, CONNETTE $6,113 $875 $2,347 $9,335
MALLISON HEINRICH, LL. LUBBOCK HEINRICH, ALLISON $4,200 $1.238 $5.438
ALLISON, CRYSTAL GOODYEAR
AZ ALLISON, CRYSTAL s250 $250
MALLISON, SUSAN
EASTON
PA ALLISON, SUSAN $7950 $2.138 $2.252 $12.340
ALVAREZ, MICHELLE MCALLEN TX ALVAREZ, MICHELLE
S4,650 $750 $244 $5,644
GRANADA HILLS CA ANGELES, ADA
$39,150 $11,456 $938 $9,181 $60,725
ANGELES WORLD, INC.,
ARBOLEDA, JANE
MIAMI FL ARBOLEDA, JANE
S375 $4,875 $549 $5,799
WACO ARMSTRONG, JULIE
$2,400 $750 $3,150
ARMSTRONG, JULIE
S900 $2,006 $657 $3,563
ARNOLD, MARY BETH
AUGUSTA
GA ARNOLD, MARY BETH
ARRAMBIDE, ROBIN KATY TX ARRAMBIDE, ROBIN
$11719 $11719
ARRINGTON, WANDA CHARLOTTE NC ARRINGTON, WANDA
S2,531 $258 $2789
PA ASH FORD, RICHARD
$3,525 S339 $3,864
WILKES BARRE
ASHFORD, RICHARD
ATTANASIO, MICHAEL SEWELL NJ ATTANASIO, MICHAEL
$450 $450
INDIANA PA AvOLIO JOHN $225 $225
AVOLIO JOHN
BABEY, CHRISTINE SCOTTSDALE AZ BABEY, CHRISTINE $5.100 $13,294 $2.135 $20,529
DALLAS BAILEY-GRAY, PATRICK 226 $226
BAILEY-GRAY, PATRICK
DECATUR IL BAKER, BENITA $17.100 S11738 $6,884 $35,722
BAKER, BENITA
~~~