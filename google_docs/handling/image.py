import google_docs.settings as settings
import google_docs.file as file
from google_docs.handling.search import get_indexes_from_text_anchor


def add_image(image_uri, index, objectSize={}):
    requests = [{
        'insertInlineImage': {
            'location': {
                'index': 1
            },
            'uri':
                image_uri,
            'objectSize': {
                'height': {
                    'magnitude': 50,
                    'unit': 'PT'
                },
                'width': {
                    'magnitude': 50,
                    'unit': 'PT'
                }
            }
        }
    }]
    body = {'requests': requests}
    settings.docs_service.documents().batchUpdate(
        documentId=file.doc_id,
        body=body
    ).execute()


def insert_image_by_anchor(text_anchor, image_uri):
    start_index, _ = get_indexes_from_text_anchor(text_anchor)
    add_image(image_uri, start_index)
