import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient


CONFIG = json.load(open(".venv\seminario\config.json"))
form_creds = CONFIG["credentials"]["doc_intel_rg"]
endpoint = form_creds["endpoint"]
key = form_creds["subskey1"]

print(f"\nConectando con el endpoint en: {endpoint}\n")


# sample document
formUrl = "https://github.com/skycrat/seminario/blob/4263a43b8c702da1196442fd42aca48c6f8bd74d/my_prescription.jpeg?raw=True"


print(f"Analizando documento en el url: {formUrl}\n")

document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", formUrl)
result = poller.result()


print(f"Contenido del documento:\n {result.content}\n")

print("\nAnálisis completo.\n")