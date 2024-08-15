# 22.-Streamlit-Web-Application-for-Telegram-Chatbot-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase 

JUST NEED TO SLOWLY CLEAN UP ALL THE FILES AND UPLOAD THEM HERE!! AND UPDATE WITH THE RELEVANT INFORMATION ABOUT THOSE FILES/FOLDERS!

This is a project done as part of my University's Undergraduate Research Opportunities Programme (UROP), titled **'UROP: Telegram chatbot for novice programmers to learn coding'**, supervised and initiated by Professor Oka Kurniawan ([here](https://github.com/kurniawano) is his Github account), spanding 8 months of (on-off) work.

Here is the description of the UROP project:  
'''  
Learning coding can be improved significantly when learners have an immediate and personalized feedback. The number of learners for coding make it impossible for human instructors to give an immediate and personalized feedback to learners. The rise of AI gives us the possibility to create a chatbot Tutor that can support learners anywhere and at any time. The purpose of this project is to create a Telegram chatbot where learners can get feedback related to their coding courses. The feedback should be accurate as reflected in the notes or instructor problem set.

The chatbot can be used for any institution that teaches programming.  
'''

This project is made up of 2 Github repositories:  
- [21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase](21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase) (this Github repository) (hosts the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database)
- Streamlit website (the other repository)

This Github repository is hosting the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database.

<br>

## My Approach to developing this UROP project:  
The approach to developing this UROP project is split into 2 components:  
1. **Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database**
  - Create a regular Telegram Bot -> integrating a Chatbase custom GPT LLM model to generate the Telegram Bot's responses to incoming texts/prompts from students (which basically gives the Telegram Bot the 'chatbot' functionality) -> incoming texts/prompts from students and the Chatbase custom GPT LLM model's responses will be saved into a database

2. **Streamlit website** 
  - There will be a separate website application containing 2 pages
    1. the first 'Details' page where it can take inputs from human instructors to manipulate the setting/behaviour of the Chatbase custom GPT LLM model via Prompt Engineering, and train the Chatbase custom GPT LLM model with their own course materials and notes without having to worry about their own course materials and notes leaking to the public
    2. the second 'Database' page where it displays the incoming texts/prompts from students and the Chatbase custom GPT LLM model's responses for the human instructors to evaluate the students' incoming texts/prompts (which the data is retrieved from the database)

*This project's deployed Telegram Bot, Chatbase custom GPT LLM model, Streamlit (Python Framework)'s Website Application and Firebase (API) links:*
+ https://t.me/test_12173_bot (Telegram Bot named 'Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API') 
+ https://www.chatbase.co/dashboard/goh-jet-wei-team-91859289/chatbot/wGS8ehg-39TolweihWY3w (Direct link to this project's Chatbase custom GPT LLM model, but only accessible by me through email)
+ https://22-app-website-for-telegram-chatbot-hezsqgseuns85wxaqsdfpd.streamlit.app/ (Streamlit (Python Framework)'s Website Application)
+ https://console.firebase.google.com/u/0/project/urop-telegram-chatbot/database/urop-telegram-chatbot-default-rtdb/data (Direct link to this project's Firebase (API) Realtime database, but only accessible by me through email)


Maybe add a how to use section? Saying that the Chatbase API part might require money to get access to the API key... and hence otherwise cannot be used??

<br>

## Table of Contents
Here is a directory to explain the purpose of each file in this repository:

1. [Files that are required in the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database](#filesrequiredincreationoftelegramchatbot)
    1. 'api' folder  
        1. 'index.py' file
    2. 'README.md' file
    3. 'firebase_key.json' file
    4. 'requirements.txt' file
2. [Additional files that are not part of the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes the past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database](#filesofpastiterationsoftelegramchatbot)
    1. telegram bot with openai (ultimately didnt choose to work with it since it exposes the instructors' materials to public, that chatbase managed to achieve fortunately to keep them private)
    2. telegram bot with chatbase (but no database) (first iteration) (can refer from the deployment one to this one cuz this one uses long polling, but the final uploaded one in index.py uses webhook instead in order to get it to work with vercel for deployment)
    3. telegram bot with chatbase and mysql (second iteration) (wanted to do this initially, but I bumped into issues trying to find somewhere to deploy my MySQL server, such as Heroku, ClearDB, PlanetScale, etc. but all required billing info so I decided to abandon using MySQL as the database and use firebase instead)
    4. telegram bot with chatbase and firebase (third iteration)
3. [Additional files that are not part of the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes my learning journey of some of the required technology being used in this project that I was not familiar with](#filesoflearningjourney)
    1. Telegram Bot API (Python Framework) learn folder (uses the test_12171 bot)
    2. OpenAI API learn folder (uses the test_12172 bot)
    3. Chatbase API learn folder (uses the test_12173_bot)
4. [Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other application) on Vercel](#deploymentoftelegramchatbot)

<br>

## 1. Files that are required in the creation of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database <a name = "filesrequiredincreationoftelegramchatbot"></a>
**1. 'api' folder**  
*i. 'index.py' file*

The main Python file for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database itself.

<br>

**2. 'README.md' file**  
The 'README.md' file.

<br>

**3. 'firebase_key.json' file**
```python
{
  "type": "service_account",
  "project_id": "urop-telegram-chatbot",
  "private_key_id": "d370c3cff86ea75089c60973d19105f90d84fdc7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC2Yqgt09bJB335\nbN61dlqWY0yFcLv8DPqvHKtpUqzSAvQGdK00zaPlezkd4SKGfohd8z4o0srpUPt9\n0fLhIPJJJhTjRN7rZpvJOPWiECQfHFXc2OJhOdabDnJoIeth+29RfD5D4t2HUdWO\n/OiSKJfNYNAf2sKELJLlPOnXwpa/wfzNhHap50WLjed8OzF+Y57ucFHut/USlsWp\n3uiRdjHod3Sfs0eL+jKfeOdkni7o/E1ytN1Ascvc1OLpbi9h6GyoLLZf8g2O1Nyn\nfe26tfRnkYvT1viErxnhQBGUh3hz3SVIsZ4FYyVrlWVwH+U8CJg2foBtbtOZjmEK\nPNAC0fi3AgMBAAECggEATMs0iftA3CtJ6Rxkl55qXRkZbrQ9is7CPLpDGFlFyDWT\nHybAiVOu12Cvd3vEiEG91GUnfpPm+R9ujRc5/33aVl9w+xKUFCUDolHX5zGJrAnH\nw3IUu6BZUrdeB6eEjyCJyhMYuofLA/+6fnbRzDzIUiMZ7tezAGkuPtSLl5vo0ns5\n1Mw13sSlssc3bjd+bCa23xDamzKWpMFlHJztnbsRVjKXfzMx2f45+snT1Lqo4kk/\ncCpM8QFlMHxLgei7JOKSkEj6LYM9Xn1dRmPJGGSAtlx/2W0/DFrVD4GCLXReKNsz\n4afFN42cZB88pKT/8YB3KoH3o/wA79k4AdsagccGbQKBgQDz3p5Yi1YgvmxWPKxd\npO1cYek2itrpH9YUZirehU01rrdHJvyufFVEoUHoeoXcDHVt++1iHZvZPwt/ZgZq\nP2tM5XWY1hlgdDgOb5J2td8jdMJuKBkzGLpnSg0qSEVlsBEsJhajvGIzBIz2Ervk\nhz1F3pIwXDZNEFS5ywMrW55WgwKBgQC/dRym9V3g0Y6g2mjAqIANRZ605R3MZpst\nN5r9GFSBB/JXo22shLCA0/RL0A3Q8aGblVv9VwHVOi1qaeU8DIcQqJvdKfspIi0J\nL8mp3ZraGzknCEHkj0oKGqNCE2Nsfx+dQ6du+u7UOecb22pjqV2UeL6gMerAMf16\nX1ZTL7hevQKBgFyIVObd/9Euz+as4O4rXVEXaakjaMraJJ3a4ltKkzBSWgKqfWgr\njyMaWOrASrhjFc+krr7y4ya8cD1n1flMlQc5bbSPUFOz5W080oMuoTtP21J27pDf\nyiLVC0fG4mYiN3HcBe0c1tnq2R2poBenZQ101V16L7RwBOX2bP5vphXHAoGBALX1\nCncOqNr6rm/nQzkeqxxx9yR6v7g8J+xwdWdm0SEUOVjbJGeab9jwF7RZllfm3S1t\nZNC/+Sj6MqF45PkN+ut1IzStKltsdJrPhPxgdUQmLUoQSfd7yuURbellXc+GfbhL\nzPvnlkWyhhduj40KMLrjil/bMPzaRcogg31p0/KNAoGBAKNTzPgZSif0PGXPEvhK\nzEi5ojwvC9iOIKvmjgXLu+e0zAI27PiiryrfrpQW6CK7RpK9KO2lQ2NUdyOi0MVI\nkqMGPLzjVwBKtWMhIwvaZxFJBvCNIg6nE5RSKoXFSYKWqmLPp+2ydPLXGPgAzNL/\n/7+TBiy9OmEkqIbNmwzgiYgR\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-rvtdl@urop-telegram-chatbot.iam.gserviceaccount.com",
  "client_id": "108928779375842545414",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rvtdl%40urop-telegram-chatbot.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```
This file represents the authetication key. Apparently, when accessing to APIs (such as the Firebase API), you will need to have a sort of, authentication key, which is what this file is to ensure that only authorized users can access the API. Refer to this video to understand how the Firebase API authentication key is used with your Python code: https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) 

<br>

**4. 'requirements.txt' file**
```python
fastapi==0.95.2
pydantic==1.10.9  # or another compatible 1.x version
python-telegram-bot==13.3
requests==2.28.2
firebase_admin==6.2.0
```
This is a compulsory file, in accordance to the deployment of Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database in [Vercel](https://vercel.com/) as described in this 'Deploy telegram bot on Vercel(Python)' website blog by Chapi Menge (refer to the section below '4. Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other application) on Vercel' for more information on the deployment process of this Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database on [Vercel](https://vercel.com/)): https://blog.chapimenge.com/blog/programming/deploying-on-vercel/ (Blog), which allows you to tell Streamlit (Python Framework) to download the necessary external libraries/framework/packages specified in this 'requirements.txt' file in the deployment environment that is required for the deployment of this Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database. 

Apparently,the 'requirements.txt' file is a common practice across various deployment platforms in Python, not just for [Vercel](https://vercel.com/). Whether you are deploying your applications on platforms like Heroku, AWS, Streamlit, or others, specifying dependencies in a 'requirements.txt' file allows the platform to understand and install the necessary packages.

Source(s):  
https://blog.chapimenge.com/blog/programming/deploying-on-vercel/ (Blog) ('Deploy telegram bot on Vercel(Python)' website blog by Chapi Menge)
https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) 
 
<br>

## 2. Past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database <a name = "filesofpastiterationsoftelegramchatbot"></a>
Telegram_bot.py is not required and is just merely for local running as long polling. (refer to the deployment process)

*Why did I choose Firebase's Realtime Database instead of MySQL databases?*  
There are various platforms where you can deploy your Telegram Bot, including [Heroku](https://heroku.com/), [Back4app](https://containers.back4app.com/), [Amazon Web Services](https://aws.amazon.com/) etc. However, nowadays most of these deployment platforms require your billing information in order to start deploying applications on them. I did not want to take the risk of being overcharged as I will most likely not maintain my built application since I only created them for education purposes and not for production. Hence, I decided to use [Vercel](https://vercel.com/) instead since it is the only deployment platform that did not require billing information. (This is the same reason why I chose Firebase's Realtime database as the database instead of MySQL databases (refer to the section above '2. Past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database' for more information on the reason why I chose Firebase's Realtime database as the database instead of MySQL databases) Same for the firebase, which caused me to ultimately changed to it from MySQL server since basically all platforms I found to host my MYSQL server in the cloud required me to put billing information (I didnt want to spend moneyy) unfortunately, while only firebase didnt need

<br>

## 3. My learning journey of some of the required technology being used in this project that I was not familiar with <a name = "filesoflearningjourney"></a>
Due to my lack of knowledge in some of the required technology being used in the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, I had to first learn them, which includes:
- Building a Telegram Bot in Python (using the 'telegram.ext' (Python Framework) Telegram Bot API)
- Using Chatbase API (requires money)
- OpenAI API (but ended up not using it)

What is [Chatbase](https://www.chatbase.co/)?  
'Chatbase is an AI chatbot builder that allows companies and other users to create their own chatbot trained on their specific data, such as documentation or website content.'    
Source: https://www.techopedia.com/definition/chatbase (Techopedia)  

<br>

## 4. Deployment Process of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database (or any other application) on Vercel <a name = "deploymentoftelegramchatbot"></a> ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=vercel)

RMB ONCE ALL THE FIRST ITERATION OF THE TELEGRAM BOT IS ADDED THEN ADD A LINK TO IT IN THE DESCRIPTION IN THIS SECTION!!! FOR THE FIRST ITERATION OF THE TELEGRAM BOT

*What is [Vercel](https://vercel.com/)?*  
From the official [Vercel](https://vercel.com/) website: 'Vercel lets teams deploy and run the user facing parts of their applications easily, separately from their backend.' 

*Why did I choose [Vercel](https://vercel.com/)?*  
There are various platforms where you can deploy your Telegram Bot, including [Heroku](https://heroku.com/), [Back4app](https://containers.back4app.com/), [Amazon Web Services](https://aws.amazon.com/) etc. However, nowadays most of these deployment platforms require your billing information in order to start deploying applications on them. I did not want to take the risk of being overcharged as I will most likely not maintain my built application since I only created them for education purposes and not for production. Hence, I decided to use [Vercel](https://vercel.com/) instead since it is the only deployment platform that did not require billing information. (This is the same reason why I chose Firebase's Realtime database as the database instead of MySQL databases (refer to the section above '2. Past iterations/versions/prototypes of the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database' for more information on the reason why I chose Firebase's Realtime database as the database instead of MySQL databases)

Honestly, the 'Deploy telegram bot on Vercel(Python)' website blog by Chapi Menge (link: https://blog.chapimenge.com/blog/programming/deploying-on-vercel/) explains clearly step by step on how to deploy a Telegram Bot, built in Python on [Vercel](https://vercel.com/) (I believe that if you build the Telegram Bot using other programming languages such as JavaScript, the deployment process on [Vercel](https://vercel.com/) and the required code in the files will differ). Once deployed correctly, rather than getting a link for your application, the Telegram Bot should start to work as expected. 

<br>

**I did run into quite a few difficulties deploying the Telegram Bot on Vercel, which I spent a great deal of time trying to debug, even while following the website blog by Chapi Menge due to my lack of knowledge in deploying on [Vercel](https://vercel.com/), and that the website blog by Chapi Menge is not the clearest. Here are some of the background knowledge and additional information that I found helpful to deploying on [Vercel](https://vercel.com/):**
- What is a Webhook and what is Long Polling? (that is mentioned in the website blog by Chapi Menge)
  - What is a Webhook?  
    A webhook is a way for an application to send real-time data to another system when triggered by certain events. It only sends HTTP requests to the system when triggered by a (certain) event. (hence more efficient than Long Polling)

    What is Long Polling?  
    Long Polling is a way for an application to send real-time data to another system by maintaining a constant connection to constantly check for updates between the application and the system. It constantly sends HTTP requests to the system. (hence less efficient than Long Polling)

    However, for [Vercel](https://vercel.com/), it only works with applications that uses Webhooks instead of Long Polling due to its architecture (its just like that). And unfortunately, when I first built the Telegram Bot locally on my laptop (see the first iteration in the prototype folder?), the code I used to build the Telegram Bot was using Long Polling instead. You can tell that the Telegram Bot is using Long Polling from the following code in the first iteration of the Telegram Bot:
    ```
    updater.start_polling()
    updater.idle()
    ```
    and hence caused my Telegram Bot to be unable to be deployed on [Vercel](https://vercel.com/), which the website blog by Chapi Menge did not warn very clearly and took me a great deal of time trying to debug. This is when I realised I need to change the code of the Telegram Bot to use Webhooks instead!

  - What is the 'index.py' file in the 'api' folder for? (that is mentioned in the website blog by Chapi Menge)  
    It was unfortunately not mentioned very clearly in the website blog by Chapi Menge, but 'index.py' (and the name has to be 'index.py' for some reason and not anything else) basically is supposed to hold the main code of the application, and the application must include code that allows it to handle Webhooks. I thought it was a little weird to put the main code of the application in the 'index.py' file in the 'api' folder... but it works for some reason.

    **IMPORTANT**  
    For this Telegram Bot, in order to get the Telegram Bot to use Webhooks instead of Long Polling, I simply just took reference from the provided 'index.py' file in the website blog by Chapi Menge, which used a sample Telegram Bot code built by Chapi Menge, and used [ChatGPT](https://chatgpt.com/) to adapt my first iteration of the Telegram Bot using Long Polling (with minor changes to my code, you can compare the 'index.py' file in this Github repository to the first iteration in the prototype folder file), to use Webhooks instead in order to deploy the Telegram Bot on [Vercel](https://vercel.com/). From what I observed, [ChatGPT](https://chatgpt.com/) used various other Python libraries that I am not familiar with, which are the 'FastAPI', 'pydantic', 'typing' and 'os' Python libraries that were not initially in my first iteration of the Telegram Bot to adapt it to use Webhooks instead of Long Polling.
    
  - According to the website blog by Chapi Menge, I needed to 'go to vercel and see the deployment is happening. After the deployment is finished, you can go to the Settings tab and click on Environment Variables. Add the 'TOKEN' variable and add the token of your bot.' What is this part talking about? (that is mentioned in the website blog by Chapi Menge)  
    The website blog by Chapi Menge is referring to adding the 'TOKEN' Environment variable and the corresponding Telegram Bot's token value/data/information to the application in [Vercel](https://vercel.com/). 

    Environment variables are key-value pairs that are stored outside the application's code and are used by the operating system and applications to configure behavior. These variables are accessible to the application at runtime and are typically used to store configuration settings and important information such as:
    - API keys
    - Database connection strings
    - Credentials (e.g. username/password)
    - Paths (e.g. file system locations)
    - Application modes (e.g. development, production)
   
    In this Telegram Bot, variables that are used as Environment variables include those containing the value/data/information of the Telegram Bot Token, Chatbase API key, Firebase Realtime Database URL, etc. You can see the Environment variables being used in the Telegram Bot's main code in the 'index.py' file here:
    ```python
    # Configuration for Chatbase, Telegram Bot and Firebase
    FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL')
    CHATBASE_API_URL = 'https://www.chatbase.co/api/v1/chat'
    CHATBASE_API_KEY = os.environ.get('CHATBASE_API_KEY')
    CHATBASE_CHATBOT_ID = os.environ.get('CHATBASE_CHATBOT_ID')
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')  # Make sure to set this in your environment variables
    ```
    What the website blog by Chapi Menge is saying is that we need to manually add the data for these Environment variables (since they should be stored outside of the application's code) in [Vercel](https://vercel.com/) like so:
    1. Go to the settings of the application in Telegram Bot's main code in the 'index.py' file, and click on 'Environment variables'. There is a text box titled 'Key' and another text box titiled 'Value'. The 'Key' represent the name of Environment variable and the 'Value' represent the value/data/information of the Environment variable.
![Screenshot 2024-08-16 002526](https://github.com/user-attachments/assets/b9bd2c59-25e4-43cd-b6d7-5ea6f084885f)

    2. Lets say we added the 'TOKEN' Environment variable into the text box titled 'Key' and the Telegram Bot's token value/data/information into the text box titled 'Value'. It should show the list of added Environment variables and their corresponding value/data/information below here. Notice that the exact same names of these Environment variables are used in the Telegram Bot's main code in the 'index.py' file (make sure the Environment variable name manually added in the application in [Vercel](https://vercel.com/) and the main code of the application are the same in order to use it properly!), this is because the Environment variables and their corresponding value/data/information that you manually added in [Vercel](https://vercel.com/) are indeed being read/extracted and used in the Telegram Bot's main code in the 'index.py' file
![Screenshot 2024-08-16 002547](https://github.com/user-attachments/assets/366a70eb-33c0-4719-aefb-67c342cfc8c1)

    Not super sure why the value/data/information of the Environment variables can't be manually inputted into the main code of the application, but needed to be separated from the main code of the application and be manually added into the application in [Vercel](https://vercel.com/)... but it works.
    
  - I got the error 'The Serverless Function has crashed' in [Vercel](https://vercel.com/). What does it mean and what do I do?  
    It means there is some issue with the main code of the application. You can check the 'Logs' of the application in [Vercel](https://vercel.com/) to see the full error.

    Due to my lack of knowledge in deploying applications in [Vercel](https://vercel.com/), I repeatedly copied the full error that showed in the 'Logs' of the application in [Vercel](https://vercel.com/), and asked [ChatGPT](https://chatgpt.com/) to tell me about the error and how to fix them, until I stopped getting errors and the application started to work.
  
  - What is this command 'curl 'https://api.telegram.org/bot<token>/setWebhook?url=https://telegram-bot.vercel.app/webhook' for? Where do I run it? (that is mentioned in the website blog by Chapi Menge)  
    The last thing that we need to do to deploy an application in [Vercel](https://vercel.com/) is to apparently run this command to 'set the Webhook' (idk what exactly this means, but you need to do this step in order to deploy an application in [Vercel](https://vercel.com/)):
    ```
    curl https://api.telegram.org/bot<token>/setWebhook?url=https://telegram-bot.vercel.app/webhook
    ```
    with '\<token>' replaced with the Telegram Bot token.
 
    However, since I am using Windows with Powershell in my VS code, this did not work for me as I had to go through the extra trouble of downloading the [curl](https://curl.se/download.html) software as well to run this command. So I used [ChatGPT](https://chatgpt.com/) to offer any alternative commands that works for Windows with Powershell in my VS code, in which it suggested I try this command, which works for me:
    ```
    $url = "https://api.telegram.org/bot<token>/setWebhook"
    $body = @{ url = "https://<your-vercel-app-url>/webhook" }
    Invoke-RestMethod -Method Post -Uri $url -Body $body
    ```
    with '\<token>' replaced with the Telegram Bot token and '\<your-vercel-app-url>' replaced with the URL of the application in [Vercel](https://vercel.com/).
 
    You can tell that the command works if it returns the following message:
    ```
    {"ok":true,"result":true,"description":"Webhook was set"}
    ```
    
    According to the website blog by Chapi Menge, you can run this command anywhere, including the terminal and VS code, but running it in VS code worked for me. 
      

- Here is the link of my [Vercel](https://vercel.com/) account of the username: 'WindJammer6' - https://vercel.com/windjammer6s-projects
- Here is the link of this deployed Telegram Bot (named 'Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API') using [Vercel](https://vercel.com/) - https://t.me/test_12173_bot

Source(s):  
https://vercel.com/ (Vercel)
https://vercel.com/blog/what-is-vercel (Vercel Blog)
https://blog.chapimenge.com/blog/programming/deploying-on-vercel/ (Blog) ('Deploy telegram bot on Vercel(Python)' website blog by Chapi Menge)
https://chatgpt.com/ (ChatGPT)
