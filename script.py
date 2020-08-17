import os
import subprocess
import datetime
import dropbox

SCREENSHOT_FOLDER = os.getenv('SCREENSHOT_FOLDER', '~/Docker/Приложения/my_application_for_my_projects')

def generate_file_path(_datetime=None):
    if not _datetime:
        _datetime = datetime.datetime.now()
    datetime_str = _datetime.strftime('%Y-%m-%d-%H:%M')
    filename = f'Screenshot_{datetime_str}.png'
    path = os.path.join(SCREENSHOT_FOLDER, filename)
    return os.path.expanduser(path), filename


screenshot_filepath, screenshot_filename = generate_file_path()
print('Путь к файлу', screenshot_filepath)
print('Название файла', screenshot_filename)

subprocess.call(['gnome-screenshot', '-a', '-f', screenshot_filepath])


dropbox_client = dropbox.Dropbox('here key for dropbox')

shared_link_metadata = dropbox_client.sharing_create_shared_link(f'/{screenshot_filename}', short_url=True)
link = shared_link_metadata.url
print('Получить ссылку', shared_link_metadata)
print('shared_link_metadata', shared_link_metadata)

subprocess.run['xclip', '-selection', 'clipboard'], input=link.encid)