# Final Presentation Stuff

# Project Name: Aggregated Feed Audio Player

---

Source: ProjectIdeas.pdf, page 11.

[**https://github.com/Scalable-NYU**](https://github.com/Scalable-NYU) 

# Idea

**Imagine that you are driving and want to listen to a personalized radio.**

Create a mobile phone application that tells you political, social, geeky stories that your friends have posted via audio or a facebook news paper.

Cloud angle: browser your friends feeds, gather links
posted by them, group them into topics, covert them into
audio headlines (or news paper feed)

# Project Proposal

---

Social media produces a huge amount of information in modern society. People use social media to receive messages from their friends, followed celebrities and public organizations. However, people nowadays do not usually have enough time for all the blast of information, or rather they cannot digest the most essence of every day information. Since the trend of this era is all about massive data, we want to build a cloud application that can not only help us digest the most of every day information across all the social media platforms, but also reduce the size of the information to the most important, outstanding, and maybe interesting ones. Even further, we propose our application to have extra accessibility feature, which enable our users to listen to the stories and news happened on their social media accounts. 

We think that being able to produce audible information from written text is the ultimate convenience for such information extraction application. In order to leverage most leisure time when reading is impractical; i.e., driving, riding packed subways, our users can simply put on headphone and skim through all the summaries of their daily social broadcast. 

On the technical side, such project demands good setups for data mining and machine learning as well as cloud computing architecture as the overall backbone. We need to ensure intact information scrapping, accurate data classification, and understandable text summarization. 

**A) Operational monitoring and business metric**

1. Regular bash jobs to monitor how much data has been scrapped for the past hour, notify admin/developers when in extreme low or extreme high.
  - When no data is collected, our user will not have anything to watch/listen to. No good user experience.
  - When too much data is poured in, we need to watch out for our server stability/scale-ability.
2. Regular bash jobs to monitor user active time. When user open our app or website, we should count the following attributes:
  - How much time the user spend on our app overall
  - How much time the user spend on a certain feedcast
  - In what percentage the user finish a certain feedcast  (25%, 50%, 75%, 100%)
  - ~~How much time they skip a certain article, etc.~~
  - Basically, we need to analyze their behavior of usage so as to improve our app.
3. Our user will be presented with a web/app client with the following choice:
4. Pages
  1. Menu
    - Click [Essence] - to play deliberate feedcast collect by past hour
    - Click [Facebook] - to play deliberate feedcast from facebook news feed
    - Click [FB Friend] - to play deliberate feedcast from facebook friends news feed
    - Click [FB Fanpage] - to play deliberate feedcast from facebook fan page news feed
    - Click [Twitter] - to play deliberate feedcast from twitter following tweet
  2. Play Dashboard
    - Click [Play] - to play deliberate feedcast. Continue from the last play or today's new feed, whatever is sooner.
    - Click [Next] - to skip the current article and jump to play the next one.
    - Click [Menu] - to go back to menu
    - Click [Look-up] -to  jump to the original article link on FB or TWTR.
    - Further feature to be added.

**B) API Integration**

In addition, since there are other systems that are using the data, we want to have an API that those application can call and receive the data without considering specific platform.

**C) Health & Diagnostics Services**

1. Period notification of new deliberate feedcast. e.g. per hour
2. A user's friend is no longer active in twitter (6 months), send notification to user.
3. Facebook or Twitter server is down, send alert message to notify the user of the cause. *(Basically we do not want our user to blame us, instead they should argue its FB and Twtr's responsibility.)*
4. Suitability testing (important): one of the other tests is to see to what extent the needs of the customer is appropriately served by the business node. For example, send "Rating us" survey to users.
5. AutoSys the QA process periodically - bash jobs that runs automatically every other time and send diagnostic report to the admin/developers. 

**D) Data Preprocess and Machine Learning**

1. Data Preprocess (Collect public user feed from twitter and facebook)
  - Feed is JSON
  - Feed is Unstructured Text
  - Feed is Image
  - Feed is Website
  - (option) Feed is other multimedia, i.e., Video.

  At the final stage of Data Mining, we should have all processed data in JSON format

  Also, to ease the process of running machine learning algorithms, we need to think of having all data stored in **two formats:**

  1. Easy to parse and search.
  2. Easy for machine learning training. 
2. Machine Learning (*opt to change*) @Haoran Ma @Jimmy Yang @Cody Wang
  - Aggregate similar topics together. (By key words, metadata, time of publication, etc)
  - Article/Text summation. (GloVe, Sequence-to-Sequence, Attention, etc)
  - (option) Image to Text. (Describe the theme of an image, code on github.)
    - *We can choose to not do this, or simply grab the image and post in our feed for the user.*
3. Result Deliverable
  1. Transfer processed data into **audio** data. 
  2. Web or Mobile client.

# Data Flow Chart

![](https://static.notion-static.com/be242541-ea29-41bb-b47d-5e013d64a65c/data_flow.png)

# Metadata Schema

    {
    	"user_id":
    		{
    			"user_ID":"fsdkljf94nf",
    			"account":"Lizi"
    			"password":"cloudcomputing"
    			"city":"new york",
    			"gender":"male",
    			"register_date":"2017-09-16",
    			"register_via":"website"
    			"secrets":{
    				"consumer_key" : "kdKy36cs6CqeflKAG8Cdjlk6h",
    		    "consumer_secret" : "W3SqFq5XpqGSfIFV41S",
    		    "access_token_key" : "7940jn50fawDZn2ZS97UywS24y1",
    		    "access_token_secret" : "qXRXR2x9ckCpQWC7Ns"
    				}
    		} 
    }

# Twitter Schema

    [
    	"user_id":"andy",
    	"datetime":"051002"  // MONTH/DAY/HOUR
    	"tweets":[
    			{
    				"category":"0",
    				"created_at":"Thu May 10 02:45:02 +0000 2018",
    				"favorate_count":"3",
            "quote_count":"6",
    				"reply_count":"2",
    				"retweet_count":"10",
    				"screenNanme":"The Wall Street Journal",
    				"text":"David Mayman has helped make sci-fi a reality",
    				"tweet_id":"994407939959148546"
    			},
    			...
    		] <!--END OF TWEEt LIST-->
    			...
    	} <!--END OF USER LISt-->
    ]					

# Audio Schema (Hourly Basis)

    {
    	"user_id":"andy",
    	"category":{
    			"business":
    					[
    						{
    							"time":"0",
    							"url":"https://s3.amazonaws.com/cc-project-s3/andy/23_business.mp3",
    							"next_url":"https://s3.amazonaws.com/cc-project-s3/andy/23_business.mp3"
    						},
    						...
    					], <!--END OF LIST-->
    					"sport":
    					[
    						{
    							"time":"0",
    							"url":"https://s3.amazonaws.com/cc-project-s3/andy/23_business.mp3",
    							"next_url":"https://s3.amazonaws.com/cc-project-s3/andy/23_business.mp3"
    						},
    						...
    					] <!--END OF LIST-->
    					...
    		}

# APP Stream Data Schema

    [
    	[ 
    	"IP": "140.115.50.67", 
    	"user_ID": "vjjkrndsm0d74n", 
    	"Date": "2018-04-07", 
    	"Time": "00:00:00", 
    	"Longitude": "xxx", 
    	"Latitude": "xxx", 
    	"Page": "1", // which page send request to (menu/play dashboard)
    	"Crawler": "0" // if bot or not
    	] , 
    	...
    ] <!--END OF User Request List-->

# APP Statistic Data Schema (Daily Basis)

    {
    	"users":[
    	  "user_ID":{
    	    "total_time":346,
    	    "history":[
    	        {"category": "Essence","percentage":"75","time":35},
    	        {"category": "Twitter","percentage":"100","time":83}
    	      ]<!--END OF USER HISTORY-->
    		 },
    		 "user_ID":{
    	    "total_time":346,
    	    "history":[
    					{"category":"FB","percentage": "100","time":126},
    	        {"category":"FB_fanpage","percentage":"25","time":8},
    	        {"category":"Essence","percentage":"100","time":77}
    				]<!--END OF USER HISTORY-->
    		 }
    	]<!--END OF USERS LIST-->
    }<!--END OF JSON OBJECT-->

# Client Interface: (opt to change)

![](https://static.notion-static.com/625aad15-28f0-41d8-b33c-19daff1756ef/Untitled)

## Weekly Progress (4/25)

Jimmy: 

Implemented a **Twitter API wrapper**, read timeline tweets from users.

**Parse** information into JSON format.

Lizi: 

Managed to programmatically **create** Amazon DynamoDB, **load** JSON data into DynamoDB, **query** data from DynamoDB. 

Tried to provide **RESTful request** to DynamoDB, WIP.

Cody:

Still working hard on deploying applications on multiple could computing platform. After a few tries, I find it was barely helpful to follow instructions on PDF. In this week and the next week, I'll try to deploy it on my own Linux desktop and document in a project report format.

There were also a few issues raised when setting up Glassfish 3.1.22 and I'm trying for figure out the problem.