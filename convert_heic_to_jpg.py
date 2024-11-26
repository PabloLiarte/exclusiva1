import os

# Ruta al directorio con las imágenes
UPLOAD_FOLDER = 'static/uploads'

def rename_extensions(directory, old_ext, new_ext):
    for filename in os.listdir(directory):
        if filename.lower().endswith(old_ext):
            old_path = os.path.join(directory, filename)
            new_filename = os.path.splitext(filename)[0] + new_ext
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renombrado: {filename} -> {new_filename}")

if __name__ == '__main__':
    # Cambiar de .heic a .jpg
    rename_extensions(UPLOAD_FOLDER, '.heic', '.jpg')

