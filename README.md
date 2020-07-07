# Medibot: COVID19 Information Bot
A chatterbot dependent web-basesd interactive COVID19 Information Bot designed using Flask.

## Introduction
COVID-19 has grasped the entire world by surprise and lack of vaccine have further deterroriated the condition. Health organisations around the world are constantly trying to reach out to each and everyone around the world to provide heath and precautionary guidelines. From social media to mass communication, health organisations like WHO, CDC, ICMR etc. in collaboration with the governments of the world are leaving no stones unturned when it comes to using technology to reach the global public. This project, open-sourced on 7th July, 2020 aims to provide COVID related information to the people in the form of a smart personal assistant.

## User Guide
1. Open your terminal. Run **pip3 install -requirements.txt** to install the required packages.
2. Run **python3 train_model.py**. The model will train on the textual data and generate *sentence_tokenizer.pickle* and *database.sqlite3*, which stores the trained weights.
3. Run **python3 medibot.py**. The model will load the information bot in the url http://127.0.0.1:5000/

## Language Support
* English 
* Deutsch (in Testing phase)

# References
COVID related information gathered from the official CDC FAQ section.
