# Defines a group of targets to build when 'docker buildx bake' is run without specifying a target.
group "default" {
    targets = ["python-bakery"]
}

# Defines a specific build target named 'python-bakery'.
target "python-bakery" {
    # Specifies the build context directory (current directory).
    context    = "."
    # Specifies the Dockerfile to use.
    dockerfile = "Dockerfile"
    # IMPORTANT: List the platforms you want to build images for.
    platforms  = ["linux/amd64", "linux/arm64"]
    # IMPORTANT: Define the tags for the built image(s).
    # REPLACE 'yourusername' with your actual Docker Hub username!
    tags       = ["ishika1108/python-bakery:latest"] # <-- USED YOUR USERNAME FROM LOGIN
    # Optional: Add labels to your image
    labels = {
      "org.opencontainers.image.source" = "https:https://github.com/Is-hika/Docker-bake" # Optional: Link to source repo
      "maintainer" = "Ishika Kumari <ishika11082004@gmail.com>" # Optional: Your info
    }
}