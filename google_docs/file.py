import google_docs.settings as settings


def create_file(title):
    body = {
        'title': title
    }
    doc = settings.docs_service.documents().create(body=body).execute()
    global doc_id
    doc_id = doc.get('documentId')
    with open(title, 'w') as file:
        file.write(id)


def get_file(title):
    # TODO: currently, you need to have the file id in the correctly named
    # file, which is annoying as you need to manually copy paste the file id
    # from google docs
    try:
        with open(title, 'r') as file:
            global doc_id
            doc_id = file.readline()
            settings.docs_service.documents().get(documentId=doc_id).execute()
    except Exception as e:
        print("File not found", e)
    return doc_id


def duplicate_file(title, wanted_name):
    global doc_id
    doc_id = get_file(title)
    body = {
        'title': wanted_name
    }
    try:
        drive_response = settings.drive_service.files().copy(
            fileId=doc_id,
            body=body
        ).execute()
        doc_id = drive_response.get('id')
    except Exception as e:
        print("Can't duplicate file", e)
