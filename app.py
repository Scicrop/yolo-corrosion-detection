import os
import sys
import urllib.request
import zipfile
import subprocess
sys.path.append('yolov7')
from yolov7.simple_detect import detect


def execute_command_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            command = file.readline().strip()
            subprocess.run(command, shell=True, check=True)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error running the command line: {e}")


def download_progress_hook(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    print(f"\rDownloading... {percent}%", end='', flush=True)


def download_and_extract(url, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Download the zip file with progress hook
    zip_file_path = os.path.join(target_dir, 'file.zip')
    urllib.request.urlretrieve(url, zip_file_path, reporthook=download_progress_hook)
    print("\nDownload complete!")

    extract_dir = os.path.join(target_dir, './')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    os.remove(zip_file_path)


def is_valid_folder(folder):
    return os.path.exists(folder) and os.path.isdir(folder)


def find_file(diretorio_base, nome_arquivo):
    for root, dirs, files in os.walk(diretorio_base):
        if nome_arquivo in files:
            return os.path.join(root, nome_arquivo)
    return None


runs_folder = 'runs/'
dataset_folder = 'yolov7/Rust8-2'
if is_valid_folder(runs_folder):
    weights = find_file(runs_folder+'/train', 'best.pt')
    base_folder_test_images = "test_images/"
    files = os.listdir(base_folder_test_images)
    for file in files:
        print("Detecting rust in file: " + file)
        detect(base_folder_test_images+file, weights)
else:
    print('There are no trained model.')
    if is_valid_folder(dataset_folder):
        print('Dataset found.')
    else:
        print('No dataset found.')
        dataset_url = "https://public-scicrop.s3.amazonaws.com/academy/Rust8-2.zip"
        print('Downloading dataset.')
        download_and_extract(dataset_url, 'yolov7/')
    execute_command_from_file('training_cmd.txt')

