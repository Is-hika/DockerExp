🚀 Deploying a Streamlit App in Docker on AWS EC2
📌 Overview
This guide provides a step-by-step approach to deploying a Streamlit app inside a Docker container on an AWS EC2 instance with a custom network setup. It covers:

✅ Setting up a VPC, Subnet, Route Table, and Internet Gateway
✅ Launching and configuring an EC2 instance
✅ Installing and configuring Docker
✅ Transferring project files to EC2
✅ Running the Streamlit app inside a Docker container
✅ Managing the Docker container

📖 Table of Contents-

1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway
2️⃣ Launching and Configuring an EC2 Instance
3️⃣ Connecting to EC2
4️⃣ Setting Permissions for the PEM Key
5️⃣ Installing and Configuring Docker
6️⃣ Copying Project Files to EC2
7️⃣ Building and Running the Docker Container
8️⃣ Accessing the Streamlit App
9️⃣ Managing the Docker Container

1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway
🔹 Create a New VPC
Go to AWS Console → VPC Dashboard → Create VPC

Name: MyCustomVPC
IPv4 CIDR block: 10.0.0.0/16
![1](1.jpg)

🔹 Create a Subnet
Go to VPC Dashboard → Subnets → Create Subnet

Select: MyCustomVPC
Subnet name: MyPublicSubnet
CIDR block: 10.0.1.0/24
Enable Auto-assign Public IPv4
![1](2.jpg)


🔹 Create an Internet Gateway and Attach to VPC
Name: MyIGW
Attach it to: MyCustomVPC
![1](3.jpg)


🔹 Create and Associate a Route Table
Name: MyPublicRouteTable
Destination: 0.0.0.0/0
Target: MyIGW
Associate with: MyPublicSubnet
![1](4.jpg)


2️⃣ Launching and Configuring an EC2 Instance
🔹 Launch an EC2 Instance
Name: Streamlit-EC2
AMI: Amazon Linux 2023
Instance Type: t2.micro (Free Tier)
Key Pair: Select/Create a key pair
Network: MyCustomVPC
Subnet: MyPublicSubnet
Enable Auto-assign Public IP
Security Group: Allow SSH (22), HTTP (80), Streamlit (8501)
![1](5.jpg)


3️⃣ Connecting to EC2
🔹 Via EC2 Instance Connect
Go to EC2 Dashboard → Select Instance → Click Connect

Choose: EC2 Instance Connect
Click: Connect
![1](6.jpg)


4️⃣ Setting Permissions for the PEM Key
mv /path/to/your-key.pem ~/your-work-directory/
chmod 600 your-key.pem


5️⃣ Installing and Configuring Docker
sudo yum update -y
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
![1](7.jpg)



6️⃣ Copying Project Files to EC2
scp -i your-key.pem app.py Dockerfile requirements.txt mushrooms.csv ec2-user@your-ec2-public-ip:/home/ec2-user/
![1](8.jpg)



7️⃣ Building and Running the Docker Container
🔹 Connect to EC2 and navigate to project directory
cd /home/ec2-user
🔹 Build the Docker image
sudo docker build -t streamlit-app .
![1](9.jpg)



🔹 Run the container
sudo docker run -d -p 8501:8501 --name streamlit_container streamlit-app
![1](10.jpg)



8️⃣ Accessing the Streamlit App
🌐 Open your browser and visit:

http://your-ec2-public-ip:8501
![1](11.jpg)

9️⃣ Managing the Docker Container

🔹 Check running containers

sudo docker ps
🔹 Stop the container

sudo docker stop streamlit_container
🔹 Remove the container

sudo docker rm streamlit_container
🔹 Restart the container

sudo docker start streamlit_container
🎯 Conclusion
This guide helps you deploy a Streamlit app inside a Docker container on AWS EC2 with a custom VPC setup. The deployment ensures scalability, security, and high availability for your application. 🚀🎉

✅ Happy Deploying! 🖥️🐳☁️
           -ishika!!