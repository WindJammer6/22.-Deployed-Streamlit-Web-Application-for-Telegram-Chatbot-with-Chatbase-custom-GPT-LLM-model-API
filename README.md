# 22.-Deployed-Streamlit-Web-Application-for-Telegram-Chatbot-with-Chatbase-API-and-Firebase-with-Figma-for-prototyping ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=streamlit) ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=firebase) ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=figma) 

JUST NEED TO SLOWLY CLEAN UP ALL THE FILES AND UPLOAD THEM HERE!! AND UPDATE WITH THE RELEVANT INFORMATION ABOUT THOSE FILES/FOLDERS!

List of features to add to the UROP Telegram chatbot (if can do all these then not bad alr!! No need try to do more cuz need focus on the other UROP and studies too 😫):

Schedule:
August:
- Try to deploy the Telegram Chatbot and Streamlit website (and firebase)
- Allow teachers of a course to add (manually i guess?) assignments for the programming course (Maybe a seperate page of Programming Question and Test cases), and hopefully it shows up in the streamlit lists of assignment id for the programming course

September:
- Allow the teacher to customise behavior of the chatbot via the details page

November:
- Try to get Telegram bot to instead do conversational with free text input, make it more like limited with text options and fill in the blanks style, with name, courseid,  assignmentid and their answers (basically figure out how the entire conversation with the Telegram chatbot is gonna be like)
- From a conversation with ChatGPT:
Can Telegram bots be programmed to not give the user freedom of text but instead with premade options?
ChatGPT said:
ChatGPT
Yes, Telegram bots can be programmed to offer users a limited set of options instead of allowing free text input. This can be achieved using inline keyboards, custom keyboards, or callback queries.

Inline Keyboards: These are buttons that appear within the chat and can trigger actions or responses when pressed. They don't require user input beyond clicking a button.

Custom Keyboards: These replace the default keyboard with a set of predefined buttons that users can select from.

Callback Queries: These are used with inline keyboards to handle button presses and provide appropriate responses based on the user’s selection.

By using these features, you can create a controlled interaction flow where users only choose from the given options.


Bonus task for even more improvement:
Allow teachers from other courses to add their own course + assignments with the respective ids + get  the 'search course' bar to work, where by you search for a course and all its uploaded assignments will show up at the left side of the streamlit website





This is a project done as part of my University's Undergraduate Research Opportunities Programme (UROP), titled **'UROP: Telegram chatbot for novice programmers to learn coding'**, supervised and initiated by Professor Oka Kurniawan ([here](https://github.com/kurniawano) is his Github account), spanding 8 months of (on-off) work.

Here is the description of the UROP project:  
'''  
Learning coding can be improved significantly when learners have an immediate and personalized feedback. The number of learners for coding make it impossible for human instructors to give an immediate and personalized feedback to learners. The rise of AI gives us the possibility to create a chatbot Tutor that can support learners anywhere and at any time. The purpose of this project is to create a Telegram chatbot where learners can get feedback related to their coding courses. The feedback should be accurate as reflected in the notes or instructor problem set.

The chatbot can be used for any institution that teaches programming.  
'''

This project is made up of 2 Github repositories:  
- [21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase](21.-Deployed-Telegram-Chatbot-integrated-with-Chatbase-custom-GPT-LLM-model-API-and-Firebase)
- [22.-Streamlit-Web-Application-for-Telegram-Chatbot-with-Chatbase-custom-GPT-LLM-model-API-n-Firebase](https://github.com/WindJammer6/22.-Streamlit-Web-Application-for-Telegram-Chatbot-with-Chatbase-custom-GPT-LLM-model-API-n-Firebase) (this Github repository) (hosts the code for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database)

This Github repository is hosting the code for the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database.

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

<br>

## Table of Contents
Here is a directory to explain the purpose of each file in this repository:

1. [Files that are required in the creation of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database](#filesrequiredincreationofstreamlitwebapplication)
    1. '.streamlit' folder  
        1. 'config.toml' file
    2. 'README.md' file
    3. 'firebase_key.json' file
    4. 'requirements.txt' file
    5. 'streamlit_web_application.py' file
2. [Additional files that are not part of the creation of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes the past iterations/versions/prototypes of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database](#filesofpastiterationsofstreamlitwebapplication)
    1. Figma
3. [Additional files that are not part of the creation of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, but includes my learning journey of some of the required technology being used in this project that I was not familiar with](#filesoflearningjourney)
    1. Prompt Engineering learn (from Prompt Engineering course by DeepLearning.AI in collaboration with OpenAI (using ChatGPT as the LLM))
    2. Figma learn
4. [Deployment Process of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database on Streamlit Cloud](#deploymentofstreamlitwebapplication)

<br>

## 1. Files that are required in the creation of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database <a name = "filesrequiredincreationofstreamlitwebapplication"></a>
**1. '.streamlit' folder**  
*i. 'config.toml' file*

The main Python file for the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database itself.

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
streamlit==1.27.2
streamlit_autorefresh==1.0.1
firebase_admin==6.2.0
```
This is a compulsory file, in accordance to the deployment of Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database in [Streamlit Cloud](https://streamlit.io/cloud) as described in the documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud (refer to the section below '4. Deployment Process of the Streamlit Web Application for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database on [Streamlit Cloud](https://streamlit.io/cloud)' for more information on the deployment process of this Streamlit Web Application for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database on [Streamlit Cloud](https://streamlit.io/cloud)): https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud), which allows you to tell Streamlit (Python Framework) to download the necessary external libraries/framework/packages specified in this 'requirements.txt' file in the deployment environment that is required for the deployment of this Streamlit Web Application for the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database. 

Apparently, the 'requirements.txt' file is a common practice across various deployment platforms in Python, not just for [Streamlit Cloud](https://streamlit.io/cloud). Whether you are deploying your applications on platforms like Heroku, AWS, Vercel, or others, specifying dependencies in a 'requirements.txt' file allows the platform to understand and install the necessary packages.

<br>

**5. 'streamlit_web_application.py' file**  
The main Python file for the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database itself.

<br>

Source(s):  
- https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) (Documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud)
- https://www.youtube.com/watch?v=s-Ga8c3toVY&t=336s (Code First with Hala) 
 
<br>

## 2. Past iterations/versions/prototypes of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database <a name = "filesofpastiterationsofstreamlitwebapplication"></a>
https://www.figma.com/community/file/1406323732296662518/telegram-chatbot-website-with-prompt-engineering-prototyping (Figma prototype file link)  

- Here is the link of this deployed Telegram Bot (named 'Telegram_Chatbot_integrated_with_Chatbase_GPT_model_API') using [Vercel](https://vercel.com/) - https://t.me/test_12173_bot

<br>

## 3. My learning journey of some of the required technology being used in this project that I was not familiar with <a name = "filesoflearningjourney"></a>
Due to my lack of knowledge in some of the required technology being used in the Telegram Chatbot integrated with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database, I had to first learn them, which includes:
+ Prompt Engineering learn (from Prompt Engineering course by DeepLearning.AI in collaboration with OpenAI (using ChatGPT as the LLM))
+ Figma learn

<br>

1. *Prompt Engineering learn (from Prompt Engineering course by DeepLearning.AI in collaboration with OpenAI (using ChatGPT as the LLM))*
  
    Consists of my learning journey of the Prompt Engineering paradigm (online course where I learnt the Prompt Engineering paradigm from: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/ by DeepLearning.AI, in collaboration with OpenAI titled 'ChatGPT Prompt Engineering for Developers' (only up till the 7th video in the playlist)
    
    *What is Prompt Engineering?*  
    Prompt Engineering is the process of writing/refining a generative AI prompt to improve its accuracy and effectiveness and obtain desired outputs from AI models.
    
    *What are prompts?*  
    An AI (including Large Language Models (LLM)) prompt is a question, command, or statement that you input into an AI 
    (including Large Language Models (LLM)) model to initiate a response or action, harnessing the power of Natural 
    Language Processing (NLP).
    
    (Note: OpenAI GPT model API (Python Framework) requires monthly payment subscription: The codes in this tutorial require the OpenAI GPT model API (Python Framework) in order to obtain responses from ChatGPT. However, the OpenAI GPT model API (Python Framework) access requires monthly payment subscription. Hence, the codes in this folder will not be able to run, without the OpenAI GPT model API (Python Framework) access, which requires payment. You can do the monthly payment subscription to get the OpenAI GPT model API (Python Framework) access here: https://platform.openai.com/docs/overview (OpenAI Platform)
    
    Hence, most of the 'output' from the code in this tutorial will be the simulated output shown in the videos in this tutorial, written in [Jupyter Notebook](https://jupyter.org/) files)
    
    Source(s):  
    - https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/ (DeepLearning.AI) (online course where I learnt the Prompt Engineering paradigm from)
    - https://www.coursera.org/articles/what-is-prompt-engineering (Coursera) (Definition of Prompt Engineering)
    - https://www.copy.ai/blog/what-are-ai-prompts (copy.ai) (Definition of Prompts)
    - https://platform.openai.com/docs/overview (OpenAI Platform) (link for payment for the OpenAI GPT model API (Python Framework) access)
    - https://jupyter.org/ (Jupyter Notebook)

<br>
  
2. *Figma learn*

    Consists of my learning journey of Figma (main Youtube playlist where I learnt the Prompt Engineering paradigm from: https://www.youtube.com/playlist?list=PLKId0A0XCIbUYx3c_NYn13W9Z_kkIiA2m by Aliena Cai, titled 'Figma UX Tutorial by Aliena' (only up till the 4th video in the playlist)

    *What is Figma?*  
    Figma is a collaborative web application for interface design, with additional offline features enabled by desktop applications for macOS and Windows. The feature set of Figma focuses on user interface (UI) and user experience (UX) design, with an emphasis on real-time collaboration, utilising a variety of vector graphics editor and prototyping tools.

    - Here is the link of my [Figma](https://figma.com/) account of the username: 'WindJammer6' - https://www.figma.com/@windjammer6
   
    Source(s):  
    - https://www.youtube.com/playlist?list=PLKId0A0XCIbUYx3c_NYn13W9Z_kkIiA2m (Aliena Cai) (Youtube playlist titled 'Figma UX Tutorial by Aliena')
     - https://www.youtube.com/watch?v=D4NyQ5iOMF0&list=PLKId0A0XCIbUYx3c_NYn13W9Z_kkIiA2m&index=1 (Aliena Cai) (Youtube video titled 'Figma UX tutorial for beginners - Wireframe')
      - https://www.youtube.com/watch?v=oZAKb_gs2Uo&list=PLKId0A0XCIbUYx3c_NYn13W9Z_kkIiA2m&index=2 (Aliena Cai) (Youtube video titled 'Figma UX tutorial for beginners - Mockup')
      - https://www.youtube.com/watch?v=HwiHqfax7Uk&list=PLKId0A0XCIbUYx3c_NYn13W9Z_kkIiA2m&index=3 (Aliena Cai) (Youtube video titled 'Figma tutorial for beginners - auto layout & components')
      - https://www.youtube.com/watch?v=v1UKB-0EUhQ&list=PLKId0A0XCIbUYx3c_NYn13W9Z_kkIiA2m&index=4 (Aliena Cai) (Youtube video titled 'Figma UX tutorial for beginners - Prototype')
    - https://www.youtube.com/watch?v=FTFaQWZBqQ8 (AJ&Smart) (Youtube video titled 'Figma UI Design Tutorial: Get Started in Just 24 Minutes!')
    - https://loremipsum.io/ (Lorem Ipsum text generator)
    - https://en.wikipedia.org/wiki/Figma (Wikipedia) (What is Figma definition)

<br>

## 4. Deployment Process of the Streamlit Web Application for the Telegram Chatbot with Chatbase custom GPT LLM model API and Firebase (API)'s Realtime Database on Streamlit Cloud <a name = "deploymentofstreamlitwebapplication"></a> ![My Skills](https://go-skill-icons.vercel.app/api/icons?i=streamlit)

*What is [Streamlit Cloud](https://streamlit.io/cloud)?*  
From the official [Streamlit Cloud](https://streamlit.io/cloud) website: 'Streamlit Cloud is a new product that lets you build, deploy, and share data from Streamlit Web Applications in minutes.' 

Honestly, the documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud (link: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app) explains very clearly step by step on how to deploy a Streamlit Web Application on [Streamlit Cloud](https://streamlit.io/cloud). Once deployed correctly, I got a direct 'streamlit.io' link to the Streamlit Web Application, which I can then share with others to try out this Streamlit Web Application.

<br>  

- Here is the link of my [Streamlit Cloud](https://streamlit.io/cloud) account of the username: 'WindJammer6' - https://share.streamlit.io/user/windjammer6
- Here is the link of this deployed Streamlit Web Application using [Streamlit Cloud](https://streamlit.io/cloud) - https://22-app-website-for-telegram-chatbot-hezsqgseuns85wxaqsdfpd.streamlit.app/

Source(s):  
+ https://streamlit.io/cloud (Streamlit Cloud)
+ https://blog.streamlit.io/introducing-streamlit-cloud/ (Streamlit Blog)
+ https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app (Streamlit Cloud) (Documentation on how to deploy a Streamlit (Python Framework) Web Application on Streamlit Cloud)
