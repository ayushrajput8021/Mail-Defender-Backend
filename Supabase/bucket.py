import os
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

# importing db credentials
url = str(os.getenv("SUPABASE_URL"))
key = str(os.getenv("SUPABASE_KEY"))
supabase: Client = create_client(url, key)


def model_deleter():
    supabase.storage.from_('models').remove('trained_model.sav')
    supabase.storage.from_('models').remove('feature_extraction.sav')


def model_exporter():
    with open('./Models/feature_extraction.sav', 'rb') as f:
        supabase.storage.from_("models").upload(file=f, path='feature_extraction.sav')
    with open('./Models/trained_model.sav', 'rb') as f:
        supabase.storage.from_("models").upload(file=f, path='trained_model.sav')
