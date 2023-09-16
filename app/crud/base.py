import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=csg1003200288dd9cc6;AccountKey=XdiQV09RRZ4CV8G5YgpmwJE3fJVo2VCGdKb0wK96UUHFvgU3L5mQkWjyzNLNaAWbBHGjueQPrkUD+AStkhCo9w==;EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)



##Create a container in Azure Blob Storage
def create_or_get_container(blob_service_client:str, container_id:str):
    """Create or get an Azure Blob Storage container."""
    try:
        container_client = blob_service_client.create_container(container_id)
        print('Container {0} created'.format(container_id))
        print(container_client)
    except ResourceExistsError:
        container_client = blob_service_client.get_container_client(container_id)
    return container_client
# create_or_get_container(blob_service_client, 'dbt')

# # List containers in Azure Blob Storage
def containers_list(blob_service_client):
    """List containers in Azure Blob Storage."""
    all_containers = blob_service_client.list_containers(include_metadata=True)
    for container in all_containers:
        print(container,"\n")
    return all_containers
# containers_list(blob_service_client)




# # Upload a blob to a container
# blob_root_directory = 'dbt'
# working_dir = os.getcwd()
# file_directory = os.walk(working_dir + '/dbt')
# for folder in file_directory:
#     for file in folder[-1]:
        
#         try:
#             file_path = os.path.join(folder[0], file)      
#             blob_path = '{0}{1}'.format(
#                 blob_root_directory,
#                 file_path.replace(r"C:\Users\Ready_(Azure Storage) Blob Management/dbt", '')
#             )
#             blob_obj = blob_service_client.get_blob_client(container=container_id, blob=blob_path)
#             with open(file_path, mode='rb') as file_data:
#                 blob_obj.upload_blob(file_data)
#         except ResourceExistsError as e:
#             print('Blob (file object) {0} already exists.'.format(file))
#             continue
#         except Exception as e:            
#             raise Exception(e)


# # List blobs (file objects) in a given container
# blobs = container_client.list_blobs()
# # blobs = container_client.list_blobs(name_starts_with='dbt')
# for blob in blobs:
#     print(blob['name'])
#     print(blob['container'])
#     print(blob['snapshot'])
#     print(blob['version_id'])
#     print(blob['is_current_version'])
#     print(blob['blob_type'])
#     print(blob['blob_tier'])
#     print(blob['metadata'])
#     print(blob['creation_time'])
#     print(blob['last_modified'])
#     print(blob['last_accessed_on'])
#     print(blob['size'])
#     print(blob['deleted'])
#     print(blob['deleted_time'])
#     print(blob['tags'])    


# # Download a blob
# file_object_path = 'dbt/2. Build dbt projects/1. Build your DAG/Exposures dbt Developer Hub.pdf'
# file_downloaded = os.path.join(working_dir, 'Exposures dbt Developer Hub.pdf')

# with open(file_downloaded, mode='wb') as download_file:
#     download_file.write(container_client.download_blob(file_object_path).readall())

# # Delete a blob (subfolder in this example)
# blobs = container_client.list_blobs()
# for blob in blobs:
#     if blob.name.startswith('dbt/List of commands/'):
#         container_client.delete_blob(blob.name)
#         print('Blob {0} deleted'.format(blob.name))

# # Delete a container
# container_client.delete_container()