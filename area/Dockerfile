# Use the official Flutter image as a base image
FROM cirrusci/flutter:latest AS build

# Set the working directory
WORKDIR /app

# Create a non-root user and switch to that user
RUN adduser --disabled-password --gecos '' appuser

# Disable Flutter Analytics
RUN flutter config --no-analytics

# Ensure the non-root user has permissions to access the Flutter SDK directory
USER root
RUN chown -R appuser /sdks/flutter

# Add the Flutter SDK directory to the list of safe directories in Git
RUN git config --global --add safe.directory /sdks/flutter

# Switch to the non-root user
USER appuser

# Copy the pubspec files and run flutter pub get
COPY pubspec.* ./
RUN flutter pub get

# Copy the rest of the application
COPY . .

# Build the Flutter web app
RUN flutter build web
