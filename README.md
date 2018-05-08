# gigzag

A simple Flask application with user authentication and profiles.

# Run the server using Docker

Install Docker.

Open the terminal and `cd` to this directory. Run the following command.

```
docker build -t gigzag .
docker run --rm -p 8080:8080 gigzag
```

Open your browser to `localhost:8080/`