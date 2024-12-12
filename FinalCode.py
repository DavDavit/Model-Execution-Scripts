!pip install docker


import docker

docker_url = 'https://654e-5-77-201-114.ngrok-free.app:2375'


client = docker.DockerClient(base_url=docker_url)


try:
    print(client.version())
    print("Successfully connected to Docker!")
except Exception as e:
    print(f"Error: {e}")



container_name = "docker-hadoop"

image_name = "hadoop_ml_model:latest"

container = client.containers.get(container_name)
image = container.commit(repository=image_name)

!docker login -u 'root' -p 'docker-pass'


!docker tag hadoop_ml_model:latest root/hadoop_ml_model:latest
!docker push root/hadoop_ml_model:latest
import osimport pandas as pd
import pyhdfs
# Step 1: Read CSV from Hadoop (same as before)def read_csv_from_hadoop(hdfs_host, hdfs_port, file_path):
    fs = pyhdfs.HdfsClient(hosts=f"{hdfs_host}:{hdfs_port}")    if fs.exists(file_path):
        with fs.open(file_path) as f:            df = pd.read_csv(f)
        return df    else:
        raise FileNotFoundError(f"File not found: {file_path}")
# Step 2: Filter IDs (same as before)def filter_ids(df, x, y, z):
    filtered_df = df[(df['x_col'] == x) & (df['y_col'] == y) & (df['z_col'] == z)]    return filtered_df['id'].tolist()
# Step 3: Retrieve FITS Files
def retrieve_fits_files(hdfs_host, hdfs_port, folder_path, ids, local_save_dir):    """
    Retrieve FITS files from Hadoop HDFS corresponding to the given IDs.    """
    fs = pyhdfs.HdfsClient(hosts=f"{hdfs_host}:{hdfs_port}")
    # Ensure the local directory exists    os.makedirs(local_save_dir, exist_ok=True)
    retrieved_files = []
    for id in ids:
        # Construct the FITS file name (pad ID to 4 digits)        file_name = f"fbs{id:04d}_cor.fits"
        hdfs_file_path = os.path.join(folder_path, file_name)
        if fs.exists(hdfs_file_path):            local_file_path = os.path.join(local_save_dir, file_name)
            # Download the file from Hadoop            with fs.open(hdfs_file_path) as remote_file, open(local_file_path, 'wb') as local_file:
                local_file.write(remote_file.read())            retrieved_files.append(local_file_path)
        else:            print(f"File not found in Hadoop: {hdfs_file_path}")
    return retrieved_files
# Step 4: Main Execution
if name == "__main__":    # HDFS Configuration
    HDFS_HOST = "localhost"  # Replace with your Hadoop container's hostname    HDFS_PORT = 9870         # Default HDFS web UI port
    CSV_FILE_PATH = "/path/to/your/file.csv"  # Replace with the actual file path in Hadoop    FITS_FOLDER_PATH = "/path/to/fits/folder"  # Folder in Hadoop where FITS files are located
    LOCAL_SAVE_DIR = "./fits_files"  # Local directory to save the retrieved files
    try:        # Read the CSV file and filter IDs
        df = read_csv_from_hadoop(HDFS_HOST, HDFS_PORT, CSV_FILE_PATH)        print("CSV file loaded successfully!")
        # Prompt user for parameters
        x = int(input("Enter value for x: "))        y = int(input("Enter value for y: "))
        z = int(input("Enter value for z: "))        ids = filter_ids(df, x, y, z)
        if ids:
            print(f"Filtered IDs: {ids}")
            # Retrieve FITS files based on the filtered IDs
            files = retrieve_fits_files(HDFS_HOST, HDFS_PORT, FITS_FOLDER_PATH, ids, LOCAL_SAVE_DIR)            if files:
                print(f"Successfully retrieved FITS files: {files}")            else:
                print("No FITS files retrieved. Check if the files exist in Hadoop.")        else:
            print("No IDs matched the criteria.")    except Exception as e:
        print(f"Error: {e}")
result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:        print(f"Error running main.py: {result.stderr}")
    else:        print(f"Model run successful: {result.stdout}")
# Step 6: Main Execution
if name == "__main__":    # HDFS Configuration
    HDFS_HOST = "localhost"  # Replace with your Hadoop container's hostname    HDFS_PORT = 9870         # Default HDFS web UI port
    CSV_FILE_PATH = "/path/to/your/file.csv"  # Replace with actual CSV path in Hadoop    FITS_FOLDER_PATH = "/path/to/fits/folder"  # Replace with actual FITS files path in Hadoop
    LOCAL_SAVE_DIR = "./fits_files"  # Local directory to save the retrieved files
    try:        # Read the CSV file and filter IDs
        df = read_csv_from_hadoop(HDFS_HOST, HDFS_PORT, CSV_FILE_PATH)        print("CSV file loaded successfully!")
        # Prompt user for parameters
        x = int(input("Enter value for x: "))        y = int(input("Enter value for y: "))
        z = int(input("Enter value for z: "))        ids = filter_ids(df, x, y, z)
        if ids:
            print(f"Filtered IDs: {ids}")
            # Retrieve FITS files based on the filtered IDs
            files = retrieve_fits_files(HDFS_HOST, HDFS_PORT, FITS_FOLDER_PATH, ids, LOCAL_SAVE_DIR)            if files:
                print(f"Successfully retrieved FITS files: {files}")
                # Extract objects from the FITS files using the extractobjectsindataset.py script                extract_objects(ids, CSV_FILE_PATH, LOCAL_SAVE_DIR)
                # Run the model for inference
                run_model()            else:
                print("No FITS files retrieved. Check if the files exist in Hadoop.")        else:
            print("No IDs matched the criteria.")    except Exception as e:
        print(f"Error: {e}")
