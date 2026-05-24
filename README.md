# 数据分析项目模板

这是一个可复制的 Python 数据分析项目模板，适合用来快速开始新的数据分析或数据可视化项目。

## 目录说明

- `main.py`：项目主入口，包含示例数据生成、数据库连接、保存数据与绘图逻辑。
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
- `main.py`
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

如果你还想让 `main.py` 使用新的数据库名或用户名，请同时确认 `docker-compose.yml` 中的环境变量和 `main.py` 中读取到的值保持一致。

## 新项目初始化 checklist

复制模板并开始新项目时，建议按下面顺序检查：

- [ ] 复制模板文件夹并重命名
- [ ] 修改 `docker-compose.yml` 中的容器名
- [ ] 修改 `docker-compose.yml` 中的数据库名
- [ ] 修改 `docker-compose.yml` 中的用户名和密码
- [ ] 根据需要修改端口映射
- [ ] 修改 `main.py`，替换示例数据逻辑
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

当前模板会启动一个 PostgreSQL 容器，并通过 `main.py` 连接它。

默认数据库配置：

- 主机：`db`
- 端口：`5432`
- 数据库名：`analytics`
- 用户名：`analytics`
- 密码：`analytics`

## 项目运行说明

启动完成后，程序会：

1. 创建必要目录
2. 读取或生成示例数据
3. 打印数据预览和统计摘要
4. 测试数据库连接
5. 将数据保存到 PostgreSQL
6. 生成示例图表

## 同步给同事

建议同步以下内容给同事：

- `Dockerfile`
- `docker-compose.yml`
- `requirements.txt`
- `main.py`
- `.env.example`
- `README.md`

### 同事如何拉取并运行

如果你们使用 Git，建议同事按下面流程操作：

```powershell
git clone <你的仓库地址>
cd <项目文件夹>
docker compose up --build
```

如果同事只是拿到一份已经复制好的项目目录，也可以直接：

```powershell
cd <项目文件夹>
docker compose up --build
```

### 修改后如何提交

如果你在本地改了项目，请按下面方式提交：

```powershell
git status
git add .
git commit -m "更新项目模板或业务逻辑"
git push
```

建议提交前先检查是否有不该提交的本地文件，例如：

- `.env`
- `__pycache__`
- 生成的图表文件
- 数据文件
- 本地临时日志

### 本地开发 vs 同事同步

#### 本地开发

你本地开发时，通常只需要：

- 修改 `main.py`
- 修改 `requirements.txt`
- 修改 `docker-compose.yml`
- 重新运行 `docker compose up --build`

#### 同事同步

同事同步时，建议只同步以下内容：

- 代码
- `Dockerfile`
- `docker-compose.yml`
- `requirements.txt`
- `README.md`

不要直接同步：

- `.env`
- 本地生成的数据文件
- 本地缓存目录
- 不必要的临时输出

## 维护建议

- 每次新增依赖时，请更新 `requirements.txt`
- 每次修改运行逻辑时，请同步更新 `README.md`
- 每次新建项目时，请优先复制这个模板，再按新项目名修改配置

## 常见问题

### 1. `docker` 命令找不到

请先安装 Docker Desktop，并重新打开终端。

### 2. 容器启动失败

先检查 `docker compose version` 是否能正常输出版本信息。

### 3. 数据库连接失败

请确认 `docker-compose.yml` 中的数据库配置和 `main.py` 中读取到的环境变量一致。

## 许可证

本模板仅用于学习、原型开发和内部项目起步，具体使用方式请根据你们的项目规范调整。
