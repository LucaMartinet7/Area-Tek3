# Use the official Flutter image as a base image
FROM ghcr.io/cirruslabs/flutter:latest

# Set the working directory
WORKDIR /app

# Create a non-root user and switch to that user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Ensure the non-root user has permissions to access the Flutter SDK directory
USER root
RUN chown -R appuser /sdks/flutter
USER appuser

# Set the working directory to the area directory
WORKDIR /app/area

# Copy the pubspec files and run flutter pub get
COPY area/pubspec.* ./
RUN flutter pub get

# Copy the rest of the application
COPY area ./

# Ensure the non-root user has permissions to write to the entire project directory
USER root
RUN chown -R appuser /app/area
USER appuser

# Ensure the non-root user has permissions to write to the .dart_tool directory
USER root
RUN mkdir -p /app/area/.dart_tool && chown -R appuser /app/area/.dart_tool
USER appuser

# Build the Flutter web app
RUN flutter build web

# Expose port 8080 (Flutter web default port)
EXPOSE 8080

# Start the Flutter web server
CMD ["flutter", "run", "-d", "web-server", "--web-port", "8080", "--web-hostname", "0.0.0.0"]