import google_docs.settings as settings
import google_docs.file as file


def add_text(text, index):
    requests = [
        {
            'insertText': {
                'location': {
                    'index': index,
                },
                'text': text
            }
        },
    ]

    settings.docs_service.documents().batchUpdate(
        documentId=file.doc_id,
        body={'requests': requests}
    ).execute()


def replace_text(string_to_replace, string_to_input):
    requests = [
        {
            'replaceAllText': {
                'containsText': {
                    'text': string_to_replace,
                    'matchCase':  'true'
                },
                'replaceText': string_to_input,
            }
        }
    ]

    settings.docs_service.documents().batchUpdate(
        documentId=file.doc_id,
        body={'requests': requests}
    ).execute()
