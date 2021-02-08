import google_docs.settings as settings
import google_docs.file as file


def get_doc_content():
    """
        Return the content of the current file as a dictionnary
    """
    result = settings.service.documents().get(
        documentId=file.doc_id
    ).execute()['body']['content']
    return result


def get_indexes_from_text_anchor(text_anchor):
    """
        Get the start and end index of a searched string. Return None if not
        found.
    """
    doc_content = get_doc_content()
    path = get_path(doc_content, text_anchor)
    if path:
        start_index, end_index = get_indexes(doc_content, path)
        return start_index, end_index
    return None


def get_indexes(doc_content, path):
    nested_obj = doc_content
    for key in path[:-1]:
        nested_obj = nested_obj[key]
    return None, None


def get_path(nested_obj, value, prepath=()):  # refactor
    if isinstance(nested_obj, dict):
        for k, v in nested_obj.items():
            path = prepath + (k,)
            if v == value:  # found value
                return path
            elif isinstance(v, dict):  # v is a dict
                p = get_path(v, value, path)  # recursive call
                if p is not None:
                    return p
            elif isinstance(v, list):
                for index, nested_dic_in_list in enumerate(v):
                    path = path + (index, )
                    return get_path(nested_dic_in_list, value, path)
    elif isinstance(nested_obj, list):
        for index, nested_dic_in_list in enumerate(nested_obj):
            path = prepath + (index, )
            getted_path = get_path(nested_dic_in_list, value, path)
            if getted_path is not None:
                return getted_path
            else:
                continue  # useless ?
