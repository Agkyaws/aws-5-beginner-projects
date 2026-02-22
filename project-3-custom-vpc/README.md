# Project 3: Create a Custom VPC 🚀

In this project, you will move away from the "Default VPC" that AWS makes for you. You will build your own private network from scratch! This helps you understand exactly how traffic flows in the cloud.

![AWS Custom VPC Architecture](image_03.png)

### 🎯 What You Will Learn
* **VPC (Virtual Private Cloud):** How to build a private network and choose your own IP address range.
* **Subnets:** How to divide your network into smaller sections.
* **Internet Gateway (IGW):** How to create a "front door" so your network can talk to the internet.
* **Route Tables:** How to create a "map" to direct your network traffic.

---

### 🚀 Step-by-Step Guide

We will build a **10.0.0.0/16** network and create a **10.0.1.0/24** public subnet inside it.

#### Step 1: Create Your VPC
1. Go to the **AWS Console** and search for **VPC**.
2. Click **"Your VPCs"** on the left and then click **"Create VPC"**.
3. Select **"VPC only"**.
4. **Name tag:** `My-Custom-VPC`.
5. **IPv4 CIDR block:** `10.0.0.0/16`.
6. Click **"Create VPC"**.

#### Step 2: Create a Subnet
1. Click **"Subnets"** on the left and click **"Create subnet"**.
2. **VPC ID:** Select your `My-Custom-VPC`.
3. **Subnet name:** `My-Public-Subnet`.
4. **IPv4 CIDR block:** `10.0.1.0/24`.
5. Click **"Create subnet"**.

#### Step 3: Create and Attach an Internet Gateway
1. Click **"Internet gateways"** on the left and click **"Create internet gateway"**.
2. **Name tag:** `My-IGW`.
3. Click **"Create internet gateway"**.
4. Once created, click **"Actions"** -> **"Attach to VPC"**.
5. Select `My-Custom-VPC` and click **"Attach internet gateway"**.

#### Step 4: Configure the Route Table
1. Click **"Route tables"** on the left and click **"Create route table"**.
2. **Name tag:** `My-Public-Route-Table`.
3. **VPC:** Select `My-Custom-VPC` and click **"Create"**.
4. In the **"Routes"** tab, click **"Edit routes"** -> **"Add route"**.
5. **Destination:** `0.0.0.0/0`.
6. **Target:** Select **Internet Gateway** and pick `My-IGW`.
7. Click **"Save changes"**.

#### Step 5: Associate Subnet with Route Table
1. Inside your `My-Public-Route-Table`, click the **"Subnet associations"** tab.
2. Click **"Edit subnet associations"**.
3. Check the box for `My-Public-Subnet` and click **"Save associations"**.

#### Step 6: Test with an EC2 Instance
1. Go to the **EC2 service** and click **"Launch instance"**.
2. **Name:** `VPC-Test-Server`.
3. **Network settings:** Click **"Edit"**.
   * **VPC:** Select `My-Custom-VPC`.
   * **Subnet:** Select `My-Public-Subnet`.
   * **Auto-assign Public IP:** Select **"Enable"**.
4. Launch the instance and try to connect!

---
[⬅️ Back to Main Menu](../README.md)
