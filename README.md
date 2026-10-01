# cloud_project_3
docker

docker build -t cloud-proj-3 .  
docker run --name cloud-proj-3 cloud-proj-3 

see image size  
docker images cloud-proj-3

turn into tar  
docker save -o cloud-proj-3.tar cloud-proj-3

load tar  
docker load -i cloud-proj-3.tar  