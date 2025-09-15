# Deployment Guide | 部署指南

[English](#english) | [中文](#中文)

---

## English

### Local Development

#### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

#### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd tonesoul-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**
   ```bash
   python scripts/run_tests.py
   ```

5. **Start the server**
   ```bash
   python scripts/start_server.py
   ```

### Docker Deployment

#### Single Container

1. **Build the image**
   ```bash
   docker build -t tonesoul-system .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 tonesoul-system
   ```

#### Docker Compose

1. **Start services**
   ```bash
   docker-compose up -d
   ```

2. **View logs**
   ```bash
   docker-compose logs -f
   ```

3. **Stop services**
   ```bash
   docker-compose down
   ```

### Production Deployment

#### Environment Variables

Create a `.env` file with the following variables:

```env
# Server Configuration
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=info

# Security
SECRET_KEY=your-secret-key-here

# Database (if applicable)
DATABASE_URL=postgresql://user:password@localhost/tonesoul

# Monitoring
SENTRY_DSN=your-sentry-dsn-here
```

#### Systemd Service (Linux)

Create `/etc/systemd/system/tonesoul.service`:

```ini
[Unit]
Description=ToneSoul System API
After=network.target

[Service]
Type=simple
User=tonesoul
WorkingDirectory=/opt/tonesoul-system
Environment=PATH=/opt/tonesoul-system/venv/bin
ExecStart=/opt/tonesoul-system/venv/bin/python src/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl enable tonesoul
sudo systemctl start tonesoul
sudo systemctl status tonesoul
```

#### Nginx Reverse Proxy

Create `/etc/nginx/sites-available/tonesoul`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/tonesoul /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Cloud Deployment

#### AWS ECS

1. **Build and push to ECR**
   ```bash
   aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-west-2.amazonaws.com
   docker build -t tonesoul-system .
   docker tag tonesoul-system:latest <account-id>.dkr.ecr.us-west-2.amazonaws.com/tonesoul-system:latest
   docker push <account-id>.dkr.ecr.us-west-2.amazonaws.com/tonesoul-system:latest
   ```

2. **Create ECS task definition**
   ```json
   {
     "family": "tonesoul-system",
     "networkMode": "awsvpc",
     "requiresCompatibilities": ["FARGATE"],
     "cpu": "256",
     "memory": "512",
     "executionRoleArn": "arn:aws:iam::<account-id>:role/ecsTaskExecutionRole",
     "containerDefinitions": [
       {
         "name": "tonesoul-system",
         "image": "<account-id>.dkr.ecr.us-west-2.amazonaws.com/tonesoul-system:latest",
         "portMappings": [
           {
             "containerPort": 8000,
             "protocol": "tcp"
           }
         ],
         "logConfiguration": {
           "logDriver": "awslogs",
           "options": {
             "awslogs-group": "/ecs/tonesoul-system",
             "awslogs-region": "us-west-2",
             "awslogs-stream-prefix": "ecs"
           }
         }
       }
     ]
   }
   ```

#### Google Cloud Run

1. **Build and deploy**
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT-ID/tonesoul-system
   gcloud run deploy --image gcr.io/PROJECT-ID/tonesoul-system --platform managed
   ```

#### Heroku

1. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

2. **Add Procfile**
   ```
   web: python src/main.py
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

### Monitoring and Logging

#### Health Checks

The system provides a health check endpoint at `/health`:

```bash
curl http://your-domain.com/health
```

#### Logging

Configure structured logging in production:

```python
import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        return json.dumps(log_entry)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('tonesoul.log')
    ]
)
```

#### Metrics

Consider integrating with monitoring solutions:
- Prometheus + Grafana
- DataDog
- New Relic
- AWS CloudWatch

### Security Considerations

1. **Environment Variables**: Never commit secrets to version control
2. **HTTPS**: Always use HTTPS in production
3. **Rate Limiting**: Implement rate limiting for API endpoints
4. **Input Validation**: All inputs are validated using Pydantic
5. **CORS**: Configure CORS appropriately for your use case
6. **Authentication**: Add authentication if required

### Performance Optimization

1. **Async Processing**: The system supports async processing
2. **Connection Pooling**: Use connection pooling for databases
3. **Caching**: Implement caching for frequently accessed data
4. **Load Balancing**: Use load balancers for high availability

---

## 中文

### 本地開發

#### 先決條件
- Python 3.11 或更高版本
- pip（Python 套件管理器）
- Git

#### 設置步驟

1. **克隆倉庫**
   ```bash
   git clone <your-repository-url>
   cd tonesoul-system
   ```

2. **創建虛擬環境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

4. **運行測試**
   ```bash
   python scripts/run_tests.py
   ```

5. **啟動服務器**
   ```bash
   python scripts/start_server.py
   ```

### Docker 部署

#### 單容器

1. **構建映像**
   ```bash
   docker build -t tonesoul-system .
   ```

2. **運行容器**
   ```bash
   docker run -p 8000:8000 tonesoul-system
   ```

#### Docker Compose

1. **啟動服務**
   ```bash
   docker-compose up -d
   ```

2. **查看日誌**
   ```bash
   docker-compose logs -f
   ```

3. **停止服務**
   ```bash
   docker-compose down
   ```

### 生產部署

#### 環境變量

創建 `.env` 文件，包含以下變量：

```env
# 服務器配置
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=info

# 安全
SECRET_KEY=your-secret-key-here

# 資料庫（如果適用）
DATABASE_URL=postgresql://user:password@localhost/tonesoul

# 監控
SENTRY_DSN=your-sentry-dsn-here
```

### 監控和日誌記錄

#### 健康檢查

系統在 `/health` 提供健康檢查端點：

```bash
curl http://your-domain.com/health
```

### 安全考慮

1. **環境變量**: 永遠不要將機密提交到版本控制
2. **HTTPS**: 在生產中始終使用 HTTPS
3. **速率限制**: 為 API 端點實施速率限制
4. **輸入驗證**: 使用 Pydantic 驗證所有輸入
5. **CORS**: 為您的用例適當配置 CORS
6. **身份驗證**: 如果需要，添加身份驗證

### 性能優化

1. **異步處理**: 系統支援異步處理
2. **連接池**: 為資料庫使用連接池
3. **緩存**: 為頻繁訪問的數據實施緩存
4. **負載平衡**: 使用負載平衡器實現高可用性