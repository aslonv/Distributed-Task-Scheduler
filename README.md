# Distributed Task Scheduler

This project implements a distributed task scheduler using FastAPI. It provides an API for user authentication, task creation, and task status retrieval.

Along the course, as part of personal research and learning journey, I will technically advance the project.

## File Structure

The main components of this project are:

1. `app/main.py`: Contains the FastAPI application and route definitions.
2. `app/tasks.py`: Implements the task creation and status retrieval logic.

## Main Components

### main.py

This file sets up the FastAPI application and defines the following endpoints:

1. `/token` (POST): Authenticates users and provides access tokens.
2. `/tasks` (POST): Creates a new task for the authenticated user.
3. `/tasks/{task_id}` (GET): Retrieves the status of a specific task.

Key features:
- Uses OAuth2 with Password (and hashing), Bearer with JWT tokens for authentication.
- Implements dependency injection for user authentication.
- Utilizes FastAPI's built-in request validation and documentation generation.

### tasks.py

This file contains the core logic for task management:

1. `create_task(task_data: dict, current_user: dict) -> str`:
   - Creates a new task with a unique ID.
   - Associates the task with the current user.
   - Simulates task processing (async operation).
   - Returns the task ID.

2. `get_task_status(task_id: str) -> str`:
   - Retrieves the status of a task given its ID.
   - Returns "not_found" if the task doesn't exist.

Key features:
- Uses a simple in-memory dictionary to store tasks (simulating a database).
- Implements asynchronous task processing using `asyncio.sleep()`.
- Generates unique task IDs using UUID4.

## Usage

1. Authenticate using the `/token` endpoint to receive an access token.
2. Use the access token in the Authorization header for subsequent requests.
3. Create tasks using the `/tasks` endpoint.
4. Check task status using the `/tasks/{task_id}` endpoint.

## Dependencies

- FastAPI
- Pydantic
- Python-jose (for JWT tokens)
- Passlib (for password hashing)

## Setup

### Prerequisites

- Docker
- Kubernetes

### Running Locally

```sh
docker-compose up --build
