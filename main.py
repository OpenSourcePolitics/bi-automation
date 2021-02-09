import google_docs.settings as settings
import google_docs.file as file
# import matomo
# import metabase


if __name__ == "__main__":
    settings.init()
    title = str(input("Enter file name on remote Google Drive"))
    file.get_file(title)

    # Do the treatment you want on the file: inserting image, text, replacing
    # elements etc.
