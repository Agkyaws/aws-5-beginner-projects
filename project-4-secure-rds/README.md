# Project 4: Secure Web App with a Private Database 🚀

In this project, you will build a secure, two-tier application architecture. Instead of putting everything in one place, you will create a custom VPC and divide it into two distinct zones:

1. **Public Subnet:** For the EC2 Web Server so it can accept traffic from the internet.
2. **Private Subnet:** For the RDS Database so it stays hidden and safe from the outside world.

![AWS Secure RDS Architecture](image_04.png)

### 🎯 What You Will Learn
* **Network Isolation:** The critical difference between Public Subnets (with an Internet Gateway) and Private Subnets (without one).
* **DB Subnet Groups:** A special requirement for RDS to define which subnets your database can use.
* **Secure Connectivity:** How to use "Security Group chaining" so the database only accepts connections from your specific web server.

---

### 🚀 Step-by-Step Guide

#### Step 1: Create VPC and Subnets
RDS requires at least 2 Availability Zones (AZs), so we need to create 2 private subnets.
1. Go to **VPC Console** -> **Create VPC**.
2. Select **VPC only**.
3. **Name:** `Project4-VPC` | **CIDR:** `10.0.0.0/16`.
4. Create **3 Subnets**:
   * **Subnet 1 (Public):** Name: `Public-Subnet-1`, AZ: `us-east-1a`, CIDR: `10.0.1.0/24`.
   * **Subnet 2 (Private):** Name: `Private-Subnet-1`, AZ: `us-east-1a` (Same as public), CIDR: `10.0.2.0/24`.
   * **Subnet 3 (Private Backup):** Name: `Private-Subnet-2`, AZ: `us-east-1b` (Must be different), CIDR: `10.0.3.0/24`.

#### Step 2: Internet Gateway and Route Table (For Public)
1. Go to **Internet Gateways** -> **Create internet gateway**.
2. **Name:** `Project4-IGW`. After creating, go to **Actions** -> **Attach to VPC** -> Select `Project4-VPC`.
3. Go to **Route Tables** -> **Create route table**.
4. **Name:** `Public-RT` | **VPC:** `Project4-VPC`.
5. In the new route table, click **Edit routes** -> **Add route**.
   * **Destination:** `0.0.0.0/0` | **Target:** `Internet Gateway` -> `Project4-IGW`.
6. Go to **Subnet associations** tab -> **Edit subnet associations**.
7. Check **ONLY** `Public-Subnet-1`. (Do NOT select private subnets).

#### Step 3: Create Security Groups
1. **Web-SG**: 
   * Allow **SSH (22)** from `0.0.0.0/0`.
   * Allow **HTTP (80)** from `0.0.0.0/0`.
2. **DB-SG**: 
   * Type: **MySQL/Aurora (3306)**.
   * **Source:** Select **Custom** -> Type `Web-SG` and select it. (This allows ONLY the Web-SG to connect).

#### Step 4: Create DB Subnet Group
1. Go to **RDS Console** -> **Subnet groups** -> **Create DB Subnet Group**.
2. **Name:** `my-db-subnet-group`.
3. **VPC:** `Project4-VPC`.
4. **Availability Zones:** Select `us-east-1a` and `us-east-1b`.
5. **Subnets:** Select the two private subnets (`10.0.2.0/24` and `10.0.3.0/24`).

#### Step 5: Create RDS Database (Private)
1. Go to **RDS Console** -> **Create database**.
2. **Method:** Full configuration | **Engine:** MySQL | **Template:** Free tier.
3. **Settings:** User: `admin` | Password: `password123`.
4. **Connectivity**:
   * **VPC:** `Project4-VPC`.
   * **DB Subnet group:** `my-db-subnet-group`.
   * **Public access:** **No**.
   * **VPC security group:** Choose `DB-SG`. (Remove the default group).

#### Step 6: Create EC2 Web Server (Public)
1. Go to **EC2 Console** -> **Launch instance**.
2. **Name:** `Web-Server` | **OS:** Amazon Linux 2023.
3. **Network settings** -> **Edit**:
   * **VPC:** `Project4-VPC` | **Subnet:** `Public-Subnet-1`.
   * **Auto-assign Public IP:** **Enable**.
   * **Security group:** Choose `Web-SG`.

#### Step 7: Testing
1. Connect to EC2 using **EC2 Instance Connect**.
2. Install MySQL client:
   ```bash
   sudo dnf update -y
   sudo dnf install mariadb105 -y
   ```
3. Get your **RDS Endpoint** from the RDS Console and test the connection:
   ```bash
   mysql -h <RDS-ENDPOINT> -u admin -p
   ```
4. Enter password: `password123`. If you see `mysql>`, you succeeded! 🎉

---
[⬅️ Back to Main Menu](../README.md)
