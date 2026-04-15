# Supabase Setup and Evaluation  
### Deployment on Linux VM using Docker Compose  

---

## Table of Contents
1. Introduction  
2. Deployment Environment Details  
3. Setup Steps  
4. Access Details  
5. Usage Sample  
6. Benefits  
7. Limitations  
8. Conclusion  

---

## 1. Introduction
This document describes the setup and evaluation of Supabase on a Linux Virtual Machine using Docker Compose. It covers deployment, access, usage, and key evaluation aspects.

---

## 2. Deployment Environment Details

| Component            | Details                          |
|---------------------|----------------------------------|
| Operating System    | Ubuntu 22.04 LTS                |
| Environment         | Linux VM (On-prem / Cloud)      |
| CPU                 | Minimum 2 vCPUs                 |
| RAM                 | Minimum 4 GB                    |
| Disk Space          | Minimum 20 GB                   |
| Docker Version      | 24.x or above                  |
| Docker Compose      | v2.x                           |

---

## 3. Setup Steps

### 3.1 Install Docker & Docker Compose
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker
```

### 3.2 Clone Supabase Repository
```bash
git clone https://github.com/supabase/supabase.git
cd supabase/docker
```

### 3.3 Configure Environment Variables
```bash
cp .env.example .env
```
Update the following in `.env`:
- POSTGRES_PASSWORD
- JWT_SECRET
- ANON_KEY
- SERVICE_ROLE_KEY

### 3.4 Start Services
```bash
docker compose up -d
```

### 3.5 Verify Running Containers
```bash
docker ps
```

---

## 4. Access Details

| Service              | URL / Port                  |
|---------------------|---------------------------|
| Supabase Studio     | http://<VM_IP>:3000       |
| REST API            | http://<VM_IP>:8000       |
| PostgreSQL          | Port 5432                 |
| Auth Service        | http://<VM_IP>:9999       |

**Default Credentials:**
- Username: postgres
- Password: Defined in .env

---

## 5. Usage Sample

### Create Table
```sql
create table users (
  id uuid primary key default uuid_generate_v4(),
  name text,
  email text unique
);
```

### Insert Data
```sql
insert into users (name, email)
values ('John Doe', 'john@example.com');
```

### Access via REST API
```bash
curl http://<VM_IP>:8000/rest/v1/users \
  -H "apikey: <API_KEY>" \
  -H "Authorization: Bearer <API_KEY>"
```

### JavaScript Client Example
```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient('http://<VM_IP>:8000', '<API_KEY>')

const { data, error } = await supabase
  .from('users')
  .select('*')
```

---

## 6. Benefits
- Open-source alternative to Firebase  
- Built on PostgreSQL  
- Auto-generated APIs  
- Built-in authentication  
- Real-time support  
- Easy Docker setup  

---

## 7. Limitations
- Manual maintenance required  
- Resource intensive  
- Scaling complexity  
- Limited enterprise support  

---

## 8. Conclusion
Supabase is a powerful backend platform with strong capabilities, but requires proper planning when self-hosted.
