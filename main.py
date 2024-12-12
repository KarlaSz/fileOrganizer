# Importujemy niezbędne biblioteki
import os  # Biblioteka do pracy z systemem plików i systemem operacyjnym
import shutil  # Biblioteka do operacji na plikach, np. przenoszenia plików

# Ustalamy folder, który chcemy posortować (folder "Documents" w domowym katalogu użytkownika)
directory = r"C:\Users\karos\Documents"  # Można zmienić na inny folder, który chcesz posortować

# Słownik rozszerzeń plików i odpowiadających im folderów, do których będą przenoszone
extensions = {
    ".jpg": "Images",  # Pliki .jpg będą przenoszone do folderu "Images"
    ".png": "Images",  # Pliki .png będą przenoszone do folderu "Images"
    ".gif": "Images",  # Pliki .gif będą przenoszone do folderu "Images"
    ".mp4": "Videos",  # Pliki .mp4 będą przenoszone do folderu "Videos"
    ".mov": "Videos",  # Pliki .mov będą przenoszone do folderu "Videos"
    ".doc": "Documents",  # Pliki .doc będą przenoszone do folderu "Documents"
    ".pdf": "Documents",  # Pliki .pdf będą przenoszone do folderu "Documents"
    ".txt": "Documents",  # Pliki .txt będą przenoszone do folderu "Documents"
    ".mp3": "Music",  # Pliki .mp3 będą przenoszone do folderu "Music"
    ".wav": "Music"  # Pliki .wav będą przenoszone do folderu "Music"
}

# Wyświetlamy komunikat o tym, w jakim folderze będą organizowane pliki
print(f"Organizing files in: {directory}")

# Rozpoczynamy iterację po wszystkich plikach i folderach w zadanym katalogu
for filename in os.listdir(directory):
    # Tworzymy pełną ścieżkę do pliku lub folderu
    file_path = os.path.join(directory, filename)

    # Sprawdzamy, czy to jest plik, a nie folder
    if os.path.isfile(file_path):
        # Wyodrębniamy rozszerzenie pliku i konwertujemy na małe litery
        extension = os.path.splitext(filename)[1].lower()

        # Logowanie: wyświetlamy nazwę przetwarzanego pliku
        print(f"Processing file: {filename}")

        # Sprawdzamy, czy rozszerzenie pliku jest zdefiniowane w naszym słowniku
        if extension in extensions:
            # Pobieramy nazwę folderu, do którego ma zostać przeniesiony plik
            folder_name = extensions[extension]

            # Tworzymy pełną ścieżkę do folderu (jeśli folder nie istnieje, zostanie utworzony)
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)  # exist_ok=True zapobiega błędowi, gdy folder już istnieje

            # Tworzymy pełną ścieżkę do miejsca docelowego, gdzie plik ma zostać przeniesiony
            destination_path = os.path.join(folder_path, filename)

            # Przenosimy plik do odpowiedniego folderu
            shutil.move(file_path, destination_path)

            # Logowanie: wyświetlamy komunikat o przeniesieniu pliku
            print(f"Moved {filename} to {folder_name} folder")
        else:
            # Logowanie: jeśli rozszerzenie pliku nie jest obsługiwane, informujemy o tym
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        # Logowanie: jeśli napotkaliśmy folder, a nie plik, informujemy o tym
        print(f"Skipped {filename}. It's a directory.")

# Po zakończeniu przetwarzania wszystkich plików wyświetlamy komunikat
print("File organization completed.")
