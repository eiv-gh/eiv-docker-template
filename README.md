# 数据分析项目模板

这是一个可复制的 Python 数据分析项目模板，适合用来快速开始新的数据分析或数据可视化项目。

## 目录说明

- `check.py`：项目主入口，包含示例数据生成、数据库连接、保存数据与绘图逻辑。
- `Dockerfile`：用于构建 Python 应用容器。
- `docker-compose.yml`：启动数据库与应用的容器编排文件。
- `requirements.txt`：Python 依赖清单。
- `.env.example`：环境变量模板。
- `.gitignore`：忽略不应该提交到版本库的文件。

## 快速开始

### 1. 安装 Docker

请先安装 Docker Desktop，并确保 `docker` 和 `docker compose` 命令可用。

### 2. 复制模板

复制当前项目目录，并将文件夹名称改为你的新项目名称。

### 3. 修改配置

在新项目中，建议先修改以下内容：

- `docker-compose.yml`
  - 修改数据库名
  - 修改容器名称
  - 修改用户名和密码
  - 如需要，修改端口映射
- `check.py`
  - 替换示例数据逻辑
  - 改成你的真实数据读取、清洗、分析与可视化逻辑
- `requirements.txt`
  - 根据项目需要增删依赖

### 4. 启动项目

在项目根目录执行：

```powershell
docker compose up --build
```

如果你本地没有 Docker，可以先安装 Docker Desktop，再重新运行以上命令。

## 项目命名建议

复制模板时，建议统一按下面的规则命名：

- 文件夹名：使用英文小写、中划线或下划线
- 容器名：使用项目名拼接，避免和其他项目冲突
- 数据库名：尽量和项目名相关，且避免特殊字符

推荐示例：

- 项目文件夹：`customer_churn_analysis`
- Postgres 容器名：`customer-churn-analysis-postgres`
- 应用容器名：`customer-churn-analysis-app`
- 数据库名：`customer_churn_analysis`

## 如何替换数据库名

修改 `docker-compose.yml` 时，只需要替换以下几项：

1. `POSTGRES_DB`
2. `POSTGRES_USER`
3. `POSTGRES_PASSWORD`
4. `container_name`
5. 如需要，修改端口映射

示例：

```yaml
services:
  db:
    image: postgres:16
    container_name: customer-churn-analysis-postgres
    environment:
      POSTGRES_DB: customer_churn_analysis
      POSTGRES_USER: customer_churn_analysis_user
      POSTGRES_PASSWORD: your_password
    ports:
      - "5432:5432"
```

如果你还想让 `check.py` 使用新的数据库名或用户名，请同时确认 `docker-compose.yml` 中的环境变量和 `check.py` 中读取到的值保持一致。

## 新项目初始化 checklist

复制模板并开始新项目时，建议按下面顺序检查：

- [ ] 复制模板文件夹并重命名
- [ ] 修改 `docker-compose.yml` 中的容器名
- [ ] 修改 `docker-compose.yml` 中的数据库名
- [ ] 修改 `docker-compose.yml` 中的用户名和密码
- [ ] 根据需要修改端口映射
- [ ] 修改 `check.py`，替换示例数据逻辑
- [ ] 根据新项目需要更新 `requirements.txt`
- [ ] 视情况复制 `.env.example` 为 `.env`
- [ ] 运行 `docker compose up --build`
- [ ] 验证应用输出和数据库连接是否正常

## 环境变量

默认模板里提供了 `.env.example`，你可以复制一份为 `.env`，并按需填写：

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=analytics
POSTGRES_USER=analytics
POSTGRES_PASSWORD=analytics
```

> 当前模板里，`docker-compose.yml` 已经把数据库参数写进容器环境变量中，因此 `.env` 不是必须项，但建议保留用于本地调试和后续扩展。

## 数据库说明

当前模板会启动一个 PostgreSQL 容器，并通过 `check.py` 连接它。

默认数据库配置：

- 主机：`db`
- 端口：`5432`
- 数据库名：`analytics`
- 用户名：`analytics`
- 密码：`analytics`

# 运行 app 服务（执行默认 command）  
docker-compose run app

# 运行 app 服务，但覆盖命令  
docker-compose run app python src/bin/check.py

# 运行 app 服务，进入交互式终端  
docker-compose run app bash

# 运行完后自动删除容器（推荐，避免残留）  
docker-compose run --rm app

# 运行完后自动删除容器，并覆盖命令  
docker-compose run --rm app python src/bin/check.py  
