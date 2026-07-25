FROM ubuntu:22.04

# Install Flutter dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    zip \
    libgconf-2-4 \
    libxss1 \
    fonts-liberation \
    libappindicator1 \
    libindicator7 \
    lsb-release \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY . .

# Get Flutter
RUN git clone https://github.com/flutter/flutter.git -b stable /flutter
ENV PATH="/flutter/bin:/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Download Flutter dependencies
RUN flutter pub get

# Build web
RUN flutter build web --release

# Use nginx to serve
FROM nginx:latest
COPY --from=0 /app/build/web /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
