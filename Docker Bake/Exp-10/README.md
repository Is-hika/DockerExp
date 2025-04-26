# Docker Bake Multi-Platform Python Image Example (Docker-bake)

This repository (`Is-hika/Docker-bake`) demonstrates how to use `docker buildx bake` to efficiently build multi-platform Docker images. It provides a simple example creating a Python 3.9 image (based on Ubuntu 20.04) targeting both `linux/amd64` (standard PCs/servers) and `linux/arm64` (Raspberry Pi, AWS Graviton, Apple Silicon VMs, etc.) architectures.

The final multi-platform image is pushed to Docker Hub.

## Key Features Demonstrated

*   **Parallel Builds:** `docker buildx bake` can build multiple targets or platforms simultaneously.
*   **Multi-Platform Support:** Easily build images for different CPU architectures using Buildx.
*   **Centralized Configuration:** Manage build definitions declaratively in a single `docker-bake.hcl` file (JSON or YAML are also supported).
*   **Efficient Pushing:** Push the multi-platform manifest list and associated images to a registry with one command.

## Project Structure

*(Assuming the files are inside the `Exp-10` directory within this repository)*



*(If your `Dockerfile` and `docker-bake.hcl` are in the repository root, update this structure diagram and remove `Exp-10/` from paths below)*

## Prerequisites

*   **Docker:** Version 20.10 or later. ([Install Docker](https://docs.docker.com/engine/install/))
*   **Docker Buildx:** Usually included with recent Docker versions. Verify with `docker buildx version`.
*   **Docker Hub Account:** To push the built images. ([Sign up for Docker Hub](https://hub.docker.com/signup)) - The example uses the username `ishika1108`.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Is-hika/Docker-bake.git
    cd Docker-bake # Navigate into the cloned repository root
    ```

2.  **Ensure Buildx Builder is Ready:**
    While the default builder might work, creating a dedicated `docker-container` based builder is often recommended for multi-platform builds:
    ```bash
    # Create and switch to a new builder (only needs to be done once)
    docker buildx create --use --name mybuilder

    # Verify the active builder supports the target platforms
    docker buildx ls
    ```
    Look for the builder with `*` next to its name and check its listed platforms.

## Usage

1.  **Navigate to Project Directory:**
    Make sure you are in the directory containing the `docker-bake.hcl` file. If you followed the structure above:
    ```bash
    cd Exp-10
    ```
    *(If your files are in the root, skip this `cd` command)*

2.  **Check/Customize Bake File:**
    *   Open `docker-bake.hcl`.
    *   The `tags` line should already be set to use the Docker Hub username `ishika1108`:
        ```hcl
        target "python-bakery" {
            # ... other settings
            tags       = ["ishika1108/python-bakery:latest"] # Uses ishika1108 Docker Hub account
            # ... other settings
             labels = {
               "org.opencontainers.image.source" = "https://github.com/Is-hika/Docker-bake" # Updated source repo
               "maintainer" = "Is-hika" # Updated maintainer
            }
        }
        ```
    *   *(Optional)* Update the `maintainer` or source URL in the `labels` section if desired.

3.  **Login to Docker Hub:**
    Authenticate your Docker client with the Docker Hub account you intend to push to (e.g., `ishika1108`):
    ```bash
    docker login --username ishika1108
    ```
    Enter the password or access token for the `ishika1108` Docker Hub account when prompted. If you want to push to a *different* account, log in with that username instead and update the `tags` line in `docker-bake.hcl` accordingly.

4.  **Build and Push:**
    Ensure you are in the directory containing `docker-bake.hcl` (e.g., `Exp-10`) and run:
    ```bash
    # Build images for all platforms defined and push to Docker Hub
    docker buildx bake --push

    # --- OR ---

    # To build locally without pushing (for testing):
    # docker buildx bake
    ```
    This command reads `docker-bake.hcl`, builds the image for all specified platforms (`linux/amd64`, `linux/arm64`), and pushes the resulting manifest list and images to the `ishika1108/python-bakery` repository on Docker Hub.

## Verification

1.  **Check Docker Hub:**
    *   Go to the repository page on Docker Hub: `https://hub.docker.com/r/ishika1108/python-bakery/tags`.
    *   Verify that the `latest` tag exists and ideally shows support for multiple architectures (`linux/amd64`, `linux/arm64`).

2.  **Inspect Locally:**
    *   Use the `imagetools` command to inspect the manifest list directly from the registry:
        ```bash
        docker buildx imagetools inspect ishika1108/python-bakery:latest
        ```
    *   Confirm the output lists manifests for both `Platform: linux/amd64` and `Platform: linux/arm64`.

## File Descriptions

*   **`Exp-10/Dockerfile`**: A standard Dockerfile defining the steps to create an Ubuntu 20.04 image with Python 3.9 installed via `apt-get`.
*   **`Exp-10/docker-bake.hcl`**: The Docker Bake configuration file written in HCL (HashiCorp Configuration Language).
    *   `group "default"`: Defines the default target(s) to build if none are specified on the command line.
    *   `target "python-bakery"`: Defines a specific build job.
        *   `context`: The build context directory.
        *   `dockerfile`: The Dockerfile to use.
        *   `platforms`: A list of target platforms (OS/Architecture) to build for.
        *   `tags`: The Docker image tag(s) to apply to the built image(s).
        *   `labels`: Optional metadata labels for the image (updated for this repo).

## Concepts

*   **Docker Bake:** A command (`docker buildx bake`) that allows you to build Docker images based on definitions in a file instead of complex command-line flags. It simplifies building multiple images, variants, or platforms from a single command.
*   **Multi-Platform Builds:** The process of creating Docker images that can run natively on different CPU architectures. `docker buildx` leverages QEMU emulation (when building on a different architecture than the target) or native nodes to build these images efficiently. The final result pushed to the registry is typically a *manifest list* (or *image index*) that points to the platform-specific image layers. Docker clients automatically pull the correct layers for their architecture.




## Next Steps

*   Experiment with adding more build targets in `docker-bake.hcl`.
*   Explore build caching options (`cache-from`, `cache-to`) within the bake file for faster subsequent builds.
*   Integrate `docker buildx bake` into a CI/CD pipeline (e.g., GitHub Actions, GitLab CI) for automated multi-platform builds.


![image](https://github.com/user-attachments/assets/f2473dbf-3152-4735-9563-641a509e4198)


![image](https://github.com/user-attachments/assets/a8b5e1ba-bed8-41fd-ace4-d93bcf7e713f)


![image](https://github.com/user-attachments/assets/1d002a69-4ccf-43eb-a6ae-6e34427f2d74)

![image](https://github.com/user-attachments/assets/6e8c6516-7120-4cb6-9475-fee80de2cdc2)


![image](https://github.com/user-attachments/assets/68e19a71-dcce-4caf-961f-108c9d022dc0)

![image](https://github.com/user-attachments/assets/97ef16be-5e84-4b6c-a340-2b70d94505e5)
