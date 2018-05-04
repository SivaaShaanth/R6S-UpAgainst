<<<<<<< HEAD
<<<<<<< HEAD
# Using Python 3 + Google Cloud Vision API's OCR to extract text from photos and scanned documents

Just a quickie test in Python 3 (using Requests) to see if [Google Cloud Vision](https://cloud.google.com/vision) can be used to effectively OCR a scanned data table and preserve its structure, in the way that products such as [ABBYY FineReader can OCR an image and provide Excel-ready output](https://github.com/dannguyen/abbyy-finereader-ocr-senate).

__The short answer:__ No. While Cloud Vision provides bounding polygon coordinates in its output, it doesn't provide it at the word or region level, which would be needed to then calculate the data delimiters.

On the other hand, the OCR quality is pretty good, if you just need to identify text anywhere in an image, without regards to its physical coordinates. I've included two examples: 

####### 1. A low-resolution photo of road signs

[Courtesy of SPUI on Wikicommons](https://commons.wikimedia.org/wiki/File:Jughandle_signage.jpg):

![Jughandle_signage](https://upload.wikimedia.org/wikipedia/commons/e/e4/Jughandle_signage.jpg)


###### 1a. Google GMail CAPTCHA (circa 2009)

Added this out of curiousity: a sample taken from Google's 2009 research paper, [What’s Up CAPTCHA?; A CAPTCHA Based On Image Orientation](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35157.pdf)

![captcha](http://i.imgur.com/3lu00lM.jpg)


####### 2. An image (PDF to PNG) of a spreadsheet

[Courtesy of Eli Lilly](http://www.lillyphysicianpaymentregistry.com/Payments-to-Physicians):

![image](https://cloud.githubusercontent.com/assets/121520/14005729/4bf2648e-f123-11e5-84d6-be1c9d84cdcd.png)




You can [read more about getting started with the Google Cloud Vision API in its official docs](https://cloud.google.com/vision/docs/getting-started). My Python script is a somewhat simplified version of the official instructions here:

https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/python/text

You first have to set up a Google developer account and get an API key (the API allows 1000 free requests a month):

https://cloud.google.com/vision/docs/auth-template/cloud-api-auth#set_up_an_api_key



## How to run

The __cloudvisreq.py__ script is included at the bottom of this gist.

~~~sh
$  python cloudvisreq.py API_KEY image1.jpg image2.png
~~~




## Results

### Road signs

~~~
    Bounding Polygon:
{'vertices': [{'x': 16, 'y': 21}, {'x': 772, 'y': 21}, {'x': 772, 'y': 322}, {'x': 16, 'y': 322}]}
    Text:
WARRENVILLE RD
NORTH
SOUTH
ALL TURNS
FROM
WASHINGTON AVE
RIGHT LANE
GREEN BROOK
U AND LEFT
DUNELLEN
TURNS
ALL TURNS f
A

~~~

### GMail Captcha

Sorry spammers, you probably won't get far using Google's API against its old CAPTCHA system (nevermind its [current one](https://www.google.com/recaptcha/intro/index.html)):

~~~py
    Bounding Polygon:
{'vertices': [{'y': 73, 'x': 142}, {'y': 73, 'x': 339}, {'y': 173, 'x': 339}, {'y': 173, 'x': 142}]}
    Text:
ngly:h
~~~


### Spreadsheet




~~~
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

### Tesseract comparison 

__Tesseract (version 3.04 as of Feb. 2016)__, [the open-source OCR tool currently maintained by Google](https://github.com/tesseract-ocr/tesseract), doesn't perform meaningfully in the photo of the road signs, but it is generally pretty strong in the case of screenshotted text. For comparison's sake, here is its output of the tabular data example -- unlike the Cloud Vision API, it *does* attempt to preserve some of the line layout -- and it has the option of [providing HOCR output which can then be used to further define spatial layout](https://github.com/jsfenfen/whatwordwhere).

(note: I've preserved the whitespace in the output, so there are a few dozen blank lines at the bottom...keep scrolling to get to the next section...)

~~~
 

o Lilly Other Health Care Professional Registry
Payments Made: Q1-Q4 2013 Data updated on Monday, March 3, 2014

 

The Other Health Care Professional Registry reports direct and indirect payments by Lilly, as well as Lilly's portion of alliance partnership payments to health care professionals other than physicians serving as faculty
members. When the "Entity Paid" is a company, hospital, or university, and there is a different name on the provider of service, it reﬂects an indirect payment which may or may not actually have been received in
whole or in part by the listed service provider. Copyright © 2014 Eli Lilly and Company. All rights reserved.

Note: Due to differences in scope and deﬁnitions, the data reported in this report may differ from data included in reports submitted by Lilly for compliance with state payment reporting laws.

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Payments*
(All Amounts in US Dollars)
Provider of Service *Payments for re u bursed expenses are not compensatio
Advising]
H
Patient Education “2:13:33 consulting & Certain
Name Location State Name . International Travel-Related 2013 Total
Programs Education .
Programs Education Expenses
Programs
A1 CERTIFIED DIABETES EDUCATORS,
LLC GILBERT AZ WARD, JAN ET $300 $1,631 $129 $2,060
ABDALLAH, RITA FAIRVIEW PARK OH ABDALLAH, RITA $14,025 $500 $2,823 $17,348
ADAMS, MARY ELLEN CINCINNATI OH ADAMS, MARY ELLEN $3,450 $1,594 $5,044
AGOSTI, CAROL TOLEDO OH AGOSTI, CAROL $1,050 $1,631 $355 $3,036
AINSWORTH, ABBY CORPUS CHRISTI TX AINSWORTH, ABBY $113 $113
AKERS, REBECCA VINCENNES IN AKERS, REBECCA $2,400 $2,400
ALCHEMIPHARMA LLC, WAYNE PA BELAZI, DEA $11,889 $199 $12,088
ALEMAN, MARY MEADOW VISTA CA ALEMAN, MARY $3,300 $1,294 $346 $4,940
ALEXANDER, LISA EVANSVILLE IN ALEXANDER, LISA $3,000 $1,988 $1,077 $6,065
ALLEN, CONNETI'E COTTAGE GROVE MN ALLEN, CONNETI'E $6,113 $875 $2,347 $9,335
ALLISON HEINRICH, L.L. LUBBOCK TX HEINRICH, ALLISON $4,200 $1,238 $5,438
ALLISON, CRYSTAL GOODYEAR AZ ALLISON, CRYSTAL $250 $250
ALLISON, SUSAN EASTON PA ALLISON, SUSAN $7,950 $2,138 $2,252 $12,340
ALVAREZ, MICHELLE MCALLEN TX ALVAREZ, MICHELLE $4,650 $750 $244 $5,644
ANDARIESE, JUDITH BROOKLYN NY AN DARIESE, JUDITH $12,450 $338 $1,029 $13,817
ANGELES WORLD, INC., GRANADA HILLS CA ANGELES, ADA $39,150 $11,456 $938 $9,181 $60,725
ARBOLEDA, JANE MIAMI FL ARBOLEDA, JANE $375 $4,875 $549 $5,799
ARMSTRONG, JULIE WACO TX ARMSTRONG, JULIE $2,400 $750 $3,150
ARNOLD, MARY BETH AUGUSTA GA ARNOLD, MARY BETH $900 $2,006 $657 $3,563
ARRAMBIDE, ROBIN KATY TX ARRAMBIDE, ROBIN $1,719 $1,719
ARRINGTON, WANDA CHARLOTTE NC ARRINGTON, WANDA $2,531 $258 $2,789
ASHFORD, RICHARD WILKES BARRE PA ASHFORD, RICHARD $3,525 $339 $3,864
ATTANASIO, MICHAEL SEWELL NJ AlTANASIO, MICHAEL $450 $450
AVOLIO, JOHN INDIANA PA AVOLIO, JOHN $225 $225
BABEY, CHRISTINE SCOTTSDALE AZ BABEY, CHRISTINE $5,100 $13,294 $2,135 $20,529
BAILEY-G RAY, PATRICK DALLAS TX BAILEY-G RAY, PATRICK $226 $226
BAIRD, DENISE LANCASTER PA BAIRD, DENISE $3,000 $638 $176 $3,814
BAKER, BENITA DECATUR IL BAKER, BENITA $17,100 $11,738 $6,884 $35,722

 

 

~~~


# Performance and latency

I didn't rigorously test this so these are just rough averages/medians of how long it took for the entire script (including any network latency) to complete:

* __Road signs:__ 2.1 seconds
* __Spreadsheet:__ 6.8 seconds
* __Spreadsheet (using Tesseract)__: 4.1 seconds

Cloud Vision probably isn't intended for picking apart text documents. Occasionally, the API would fail on the spreadsheet image with this result:

~~~json
{
  "error": {
    "code": 4,
    "message": "image-annotator::RPC deadline exceeded.: Backend timeout!"
  }
}
~~~


For a more robust experience, you probably want to follow the example linked from the API's official docs:

https://github.com/GoogleCloudPlatform/cloud-vision/tree/master/python/text

It includes using the __googleapiclient__ library, which has various conveniences including a `num_retries` argument.

#### Authenticating via oauth2 JSON credentials

If you want to use the __googleapiclient__, which includes authenticating via oauth2 credentials, here's a variation of how to authenticate a service request as shown in the official docs, except from a given filename (i.e. as opposed to setting an environment variable and calling `GoogleCredentials.get_application_default()`):

~~~py
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
def get_vision(oauth2_creds_filename, service_url=DISCOVERY_URL):
    """
    Read oauth2 credentials and return a Google service object,
      which you can then invoke like this:

    ("vision" is the service object)
    request = vision.images().annotate(body={'requests': img_requests_data})
    vision_response_dict = request.execute(num_retries=5)

    """
    creds = GoogleCredentials.from_stream(oauth2_creds_filename)
    service = discovery.build('vision', 'v1', credentials=creds,
                              discoveryServiceUrl=DISCOVERY_URL)
    return service
~~~
=======
# R6S-UpAgainst
>>>>>>> 6dab65e7331611736b41e1c7ef847912b40dfac2
=======
Scripts to read names of a screenshot from in-game, recognize player names using Gcloud Vision, hit https://r6db.com/ and search for their maximum ranks through all seasons and display it on https://sivaashaanth.github.io/
>>>>>>> ba6218b696844811b67e45a50dae46f45597c08c
