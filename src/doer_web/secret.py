from google.cloud import secretmanager

from doer_web import gcloud


def get(id_: str):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{gcloud.project_id}/secrets/{id_}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
