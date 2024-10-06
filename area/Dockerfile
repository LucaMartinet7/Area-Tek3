# Use the official Flutter image as a base image
FROM cirrusci/flutter:stable as build

# Set the working directory
WORKDIR /app

# Create a non-root user and switch to that user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Copy the pubspec files and run flutter pub get
COPY pubspec.* ./
RUN flutter pub get

# Copy the rest of the application
COPY . .

# Build the Flutter web app
RUN flutter build web

# Use a lightweight web server to serve the built Flutter web app
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the built web files from the build stage
COPY --from=build /app/build/web .

# Expose the application port
EXPOSE 80
# Start a simple HTTP server to serve the Flutter web app
CMD ["dart", "-m", "webdev", "serve", "index.html", "--hostname=0.0.0.0", "--port=8080"]