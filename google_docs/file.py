import google_docs.settings as settings


def create_file(title):
    body = {
        'title': title
    }
    doc = settings.service.documents().create(body=body).execute()
    global doc_id
    doc_id = doc.get('documentId')
    with open(title, 'w') as file:
        file.write(id)


def get_file(title):  # TODO: find REALLY with the name, otherwise it's a pita to manually copy paste the file id
    try:
        with open(title, 'r') as file:
            global doc_id
            doc_id = file.readline()
            settings.service.documents().get(documentId=doc_id).execute()
    except Exception as e:
        print("File not found", e)
