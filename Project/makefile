# Variables
PROJECT_ROOT := myYoutube
REQUIRED_DIRS := $(PROJECT_ROOT)\site $(PROJECT_ROOT)\encoding $(PROJECT_ROOT)\mailer $(PROJECT_ROOT)\myAPI $(PROJECT_ROOT)\search
DOCKER_COMPOSE_FILE := docker-compose.yml
DOCKERFILES := $(REQUIRED_DIRS:%=%\Dockerfile)
REQUIRED_FILES := $(PROJECT_ROOT)\myAPI\requirements.txt $(PROJECT_ROOT)\encoding\requirements.txt $(PROJECT_ROOT)\mailer\requirements.txt $(PROJECT_ROOT)\site\package.json

.PHONY: all setup check_dirs check_files generate_files validate_config build_and_run restart_services check_services access_services logs debug_services clean

# Default task: runs all necessary steps
all: setup validate_config build_and_run access_services

# Setup phase: ensure all directories, files, and docker-compose.yml are present
setup: check_dirs check_files generate_files

# Ensure required directories exist (Windows-compatible)
check_dirs:
	@echo "Checking required directories..."
	@for %%D in ($(REQUIRED_DIRS)) do ( \
		if not exist "%%D" ( \
			echo Creating missing directory: %%D; \
			mkdir "%%D"; \
		) \
	)

# Ensure required files (Dockerfiles and docker-compose.yml) exist and create them if missing
check_files: $(DOCKERFILES) $(DOCKER_COMPOSE_FILE)

$(DOCKER_COMPOSE_FILE):
	@echo "Creating missing $(DOCKER_COMPOSE_FILE)..."
	@echo "version: '3.9'" > $(DOCKER_COMPOSE_FILE)
	@echo "services:" >> $(DOCKER_COMPOSE_FILE)
	@echo "  api:" >> $(DOCKER_COMPOSE_FILE)
	@echo "    build:" >> $(DOCKER_COMPOSE_FILE)
	@echo "      context: $(PROJECT_ROOT)\myAPI" >> $(DOCKER_COMPOSE_FILE)
	@echo "      dockerfile: Dockerfile" >> $(DOCKER_COMPOSE_FILE)
	@echo "    ports:" >> $(DOCKER_COMPOSE_FILE)
	@echo "      - '5000:5000'" >> $(DOCKER_COMPOSE_FILE)
	@echo "  site:" >> $(DOCKER_COMPOSE_FILE)
	@echo "    build:" >> $(DOCKER_COMPOSE_FILE)
	@echo "      context: $(PROJECT_ROOT)\site" >> $(DOCKER_COMPOSE_FILE)
	@echo "      dockerfile: Dockerfile" >> $(DOCKER_COMPOSE_FILE)
	@echo "    ports:" >> $(DOCKER_COMPOSE_FILE)
	@echo "      - '3000:3000'" >> $(DOCKER_COMPOSE_FILE)
	@echo "networks:" >> $(DOCKER_COMPOSE_FILE)
	@echo "  default:" >> $(DOCKER_COMPOSE_FILE)
	@echo "    name: project_default" >> $(DOCKER_COMPOSE_FILE)

$(DOCKERFILES):
	@echo "Creating missing Dockerfile in $(@D)..."
	@if $(@D)==$(PROJECT_ROOT)\myAPI ( \
		echo "FROM python:3.9-slim" > $@ && \
		echo "WORKDIR /app" >> $@ && \
		echo "COPY requirements.txt ." >> $@ && \
		echo "RUN pip install --no-cache-dir -r requirements.txt" >> $@ && \
		echo "COPY . ." >> $@ && \
		echo "EXPOSE 5000" >> $@ && \
		echo 'CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]' >> $@; \
	) else if $(@D)==$(PROJECT_ROOT)\site ( \
		echo "FROM node:16" > $@ && \
		echo "WORKDIR /usr/src/app" >> $@ && \
		echo "COPY package*.json ./" >> $@ && \
		echo "RUN npm install" >> $@ && \
		echo "COPY . ." >> $@ && \
		echo "EXPOSE 3000" >> $@ && \
		echo 'CMD ["npm", "run", "dev"]' >> $@; \
	) else if $(@D)==$(PROJECT_ROOT)\encoding ( \
		echo "FROM python:3.9-slim" > $@ && \
		echo "WORKDIR /app" >> $@ && \
		echo "RUN apt-get update && apt-get install -y ffmpeg && apt-get clean" >> $@ && \
		echo "COPY requirements.txt ." >> $@ && \
		echo "RUN pip install --no-cache-dir -r requirements.txt" >> $@ && \
		echo "COPY . ." >> $@ && \
		echo "EXPOSE 5001" >> $@ && \
		echo 'CMD ["python", "app.py"]' >> $@; \
	) else if $(@D)==$(PROJECT_ROOT)\mailer ( \
		echo "FROM python:3.9-slim" > $@ && \
		echo "WORKDIR /app" >> $@ && \
		echo "COPY requirements.txt ." >> $@ && \
		echo "RUN pip install --no-cache-dir -r requirements.txt" >> $@ && \
		echo "COPY . ." >> $@ && \
		echo "EXPOSE 5002" >> $@ && \
		echo 'CMD ["python", "mailer.py"]' >> $@; \
	)

# Generate missing requirements.txt and package.json files
generate_files: $(REQUIRED_FILES)

$(PROJECT_ROOT)\myAPI\requirements.txt:
	@echo "Generating myAPI requirements.txt..."
	@echo "django==4.2\ndjangorestframework==3.14.0" > $@

$(PROJECT_ROOT)\encoding\requirements.txt:
	@echo "Generating encoding requirements.txt..."
	@echo "ffmpeg-python==0.2.0\nrequests==2.31.0" > $@

$(PROJECT_ROOT)\mailer\requirements.txt:
	@echo "Generating mailer requirements.txt..."
	@echo "flask==2.3.2\nflask-mail==0.9.1\nrequests==2.31.0" > $@

$(PROJECT_ROOT)\site\package.json:
	@echo "Generating site package.json..."
	@echo "{\"name\": \"myyoutube-site\",\"version\": \"1.0.0\",\"dependencies\": {\"react\": \"^18.2.0\",\"react-dom\": \"^18.2.0\",\"axios\": \"^1.4.0\"}}" > $@

# Validate the Docker Compose configuration
validate_config:
	@echo "Validating Docker Compose configuration..."
	@docker-compose -f $(DOCKER_COMPOSE_FILE) config

# Build and run all services
build_and_run:
	@echo "Building and starting all services..."
	@docker-compose -f $(DOCKER_COMPOSE_FILE) up --build -d

# Restart services
restart_services:
	@echo "Restarting all services..."
	@docker-compose down
	@docker-compose up --build -d

# Check running containers
check_services:
	@echo "Checking running containers..."
	@docker ps

# Access services
access_services:
	@echo "You can access the services as follows:"
	@echo "Frontend (React app): http://localhost:3000"
	@echo "Backend API: http://localhost:5000"
	@echo "Database: PostgreSQL running on localhost:5432"
	@echo "Use a database client with username: 'postgres', password: 'password', database: 'myyoutube'."

# View logs for a specific service
logs:
	@echo "Usage: make logs SERVICE=<service-name>"
	@if [ "$(SERVICE)" ]; then \
		docker-compose logs $(SERVICE); \
	else \
		echo "Please specify a service name, e.g., 'make logs SERVICE=api'."; \
	fi

# Debug services if errors occur
debug_services:
	@echo "Checking service statuses and logs..."
	@docker-compose ps | findstr "Exit" && docker-compose logs || echo "All services are running fine."

# Clean up the project
clean:
	@echo "Stopping and removing services, cleaning up..."
	@docker-compose down -v
