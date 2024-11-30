# Tasks

## Table of contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running tests](#testing)
- [Running the project](#running)
- [Api Endpoints](#endpoints)

## Prerequisites

1. **Python**: Make sure you have Python installed (preferably 3.11.* or later).
2. **pip**: Python package installer should also be installed.
3. **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/JoaoRicardoSimplicio/tasks.git
cd tasks
```

2. **Create a virtual environment and activate it**:
```bash
python3.11 -m venv env
source env/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Testing

1. **Run tests**:
```bash
python3 manage.py test
```

## Running

1. **Apply the migrations**:
```bash
python3 manage.py migrate
```

2. **Run the app**:
```bash
python3 manage.py runserver
```

## Endpoints

1. Create and list tasks:
- Endpoint `/tasks/`
- Methods:
    - `GET`: Fetch all tasks.
    - `POST` Create a new task.
- Request body:
```json
{
    "title": "Create a new endpoint",
    "description": "Create a new endpoint to set task as done."
}
```

2. Delete a task:
- Endpoint `/tasks/<id>/`
- Methods:
    - `DELETE`: Delete a task.

3. Update a task:
- Endpoint `/tasks/<id>/`
- Methods:
    - `PATCH`: Update a specific task.
- Request body:
Example where the field `title` must be updated.
```json
{
    "title": "Task with title updated",
}
```

4. Set a task as done.
- Endpoint `/tasks/<id>/complete`
- Methods:
    - `POST` Set the given task as done.
