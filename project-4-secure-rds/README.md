# Project 4: Dynamic Web App with Private RDS 🚀

### Project Overview
In this project, you will build a secure, two-tier application architecture from the ground up to understand how real-world applications are secured. Instead of putting everything in one place, you will create a custom VPC and divide it into two distinct zones:

* **Public Subnet:** We will place the EC2 Web Server here so it can accept traffic from the internet.
* **Private Subnet:** We will place the RDS Database here so it remains hidden and isolated from the outside world for maximum security.

![AWS Secure RDS Architecture](image_04.png)

### 🎯 Key Learning Points:
* **Network Isolation:** You will learn the critical difference between Public Subnets (which have an Internet Gateway) and Private Subnets (which do not), and when to use each.
* **DB Subnet Groups:** You will learn how to configure a DB Subnet Group, a specific requirement for RDS that defines which subnets your database is allowed to use across multiple Availability Zones.
* **Secure Connectivity:** You will learn how to securely connect your Public Web Server to your Private Database using Security Group chaining, ensuring the database only accepts connections from your specific web server.

---

### 🚀 Lab Guide: Step-by-Step

#### Step (1) - Create VPC and Subnets
RDS requires at least 2 Availability Zones (AZs), so we need to create 2 private subnets.

1. Go to **VPC Console**
2. Click **Create VPC**
3. Select **VPC only**
4. Name: `Project4-VPC`
5. CIDR: `10.0.0.0/16`
6. Click **Create VPC**

**Create Subnets:**
1. Go to **Subnets** → **Create subnet**
2. Select `Project4-VPC`

**Subnet 1 (Public):**
* Name: `Public-Subnet-1`
* AZ: `us-east-1a` (choose one you prefer, but remember it)
* CIDR: `10.0.1.0/24`
* Click **Add new subnet**

**Subnet 2 (Private):**
* Name: `Private-Subnet-1`
* AZ: `us-east-1a` (choose same as Public Subnet)
* CIDR: `10.0.2.0/24`
* Click **Add new subnet**

**Subnet 3 (Private Backup):**
* Name: `Private-Subnet-2`
* AZ: `us-east-1b` (must choose different from first one)
* CIDR: `10.0.3.0/24`
* Click **Create subnet**

#### Step (2) - Internet Gateway and Route Table (For Public)
We will only give internet access to the Public Subnet.

1. Go to **Internet Gateways** → **Create internet gateway**
2. Name: `Project4-IGW`
3. Click **Create**
4. After creation, go to **Actions** → **Attach to VPC** → Select `Project4-VPC`
5. Go to **Route Tables** → **Create route table**
6. Name: `Public-RT`
7. VPC: `Project4-VPC`
8. Click **Create**
9. In the new route table, click **Edit routes** → **Add route**
   * Destination: `0.0.0.0/0`
   * Target: **Internet Gateway** → Select `Project4-IGW`
10. Click **Save changes**
11. Go to **Subnet associations** tab → **Edit subnet associations**
12. Check ONLY `Public-Subnet-1` (Do NOT select Private subnets)
13. Click **Save associations**

#### Step (3) - Create Security Groups

**Create Web Server Security Group:**
1. Go to **EC2 Console** → **Security Groups** → **Create security group**
2. Name: `Web-SG`
3. VPC: Select `Project4-VPC` (make sure to select the new one)
4. **Inbound Rules:**
   * Type: **SSH**, Port: **22**, Source: `0.0.0.0/0` (Anywhere)
   * Type: **HTTP**, Port: **80**, Source: `0.0.0.0/0` (Anywhere)
5. Click **Create security group**

**Create Database Security Group:**
1. Click **Create security group** again
2. Name: `DB-SG`
3. VPC: `Project4-VPC`
4. **Inbound Rules:**
   * Type: **MySQL/Aurora**, Port: **3306** (Important to fill the DB port range)
   * Source: Select **Custom** → Type `Web-SG` and select it (This allows only Web-SG to connect)
5. Click **Create security group**

#### Step (4) - Create DB Subnet Group (Special Requirement for RDS)
We need to group the Private Subnets and tell RDS to run only in these locations.

1. Go to **RDS Console**
2. In left menu, scroll down and click **Subnet groups**
3. Click **Create DB Subnet Group**
4. Name: `my-db-subnet-group`
5. VPC: `Project4-VPC`
6. Availability Zones: Select `us-east-1a` and `us-east-1b` (the two AZs where we created subnets)
7. Subnets: In the list below, select the two private subnets with CIDR `10.0.2.0/24` and `10.0.3.0/24`
   > ⚠️ **DO NOT** select the Public subnet (`10.0.1.0/24`)
8. Click **Create**

#### Step (5) - Create RDS Database (Private)
1. In RDS Console, click **Create database**
2. Database creation method: **Full configuration**
3. Engine type: **MySQL**
4. Templates: **Single-AZ DB instance deployment**
5. **Settings:**
   * DB instance identifier: (leave default or give name)
   * Master username: `admin`
   * Master password: `password123` (use secure password in production)
6. **Instance configuration:** Burstable classes, **db.t3.micro** (Free tier eligible)
7. **Storage:** Leave defaults (20 GB gp2)
8. **Connectivity (Most Important Part):**
   * Virtual Private Cloud (VPC): Select `Project4-VPC`
   * DB Subnet group: `my-db-subnet-group` (should appear automatically)
   * Public access: **No** (This is critical for security)
   * VPC security group: Select existing → Choose `DB-SG` 
     *(Remove the default security group if selected)*
9. Database authentication: **Password authentication**
10. Click **Create database**

#### Step (6) - Create EC2 Web Server (Public)
1. Go to **EC2 Console** → **Launch instance**
2. Name: `Web-Server`
3. OS: **Amazon Linux 2023**
4. Instance type: **t2.micro** (Free tier eligible)
5. **Network settings** → **Edit:**
   * VPC: `Project4-VPC`
   * Subnet: `Public-Subnet-1` (Be careful not to choose wrong)
   * Auto-assign Public IP: **Enable** (If not enabled, you won't be able to access)
   * Security group: Select existing → Choose `Web-SG`
6. Key pair: Select your existing key pair
7. Click **Launch instance**

#### Step (7) - Testing
1. Connect to EC2 using **EC2 Instance Connect** or SSH
2. Install MySQL client:
```bash
sudo dnf update -y
sudo dnf install mariadb105 -y
```
3. **Get RDS Endpoint:**
   * Go to **RDS Console** → **Databases** → Click your database
   * Copy the Endpoint (it looks like: `database-1.xxxxxxxx.us-east-1.rds.amazonaws.com`)
4. **Test connection from EC2:**
```bash
mysql -h <RDS-ENDPOINT> -u admin -p
```
5. Enter password: `password123`

If you see the `mysql>` prompt, congratulations! You have successfully built a secure private database architecture! 🎉

---
[⬅️ Back to Main Menu](../README.md)
