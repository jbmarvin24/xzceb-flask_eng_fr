import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

# Loan environment Variables
load_dotenv()

# Get Apikey
# API_KEY = os.environ['apikey']
API_KEY = 'UiM4rJ73LYcShOJX3pUGQW1VtwzT3Uma_ByyYkqasJw_'

# Get Url
# URL = os.environ['url']
URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/dff8e325-9c41-493d-bf53-be560ee3ae7c'

# Initiate Language Translator
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)


# Translate English to French
def english_to_french(english_text):
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']


# Translate French to English
def french_to_english(french_text):
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
