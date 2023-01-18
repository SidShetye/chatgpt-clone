param (
    [Boolean] $pushImage = $false
)

$ErrorActionPreference = "Stop"

$tag = "latest"

# if we're going to push, also tag this locally
if ($pushImage) {
    $image = "crypteron.azurecr.io/chatgpt-clone"   
} else {
    $image = "chatgpt-clone"
}

& docker build -t $image`:$tag .
    
if ($pushImage) {
    # Make sure the az cli is installed: See https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
    & az acr login --name crypteron
    & docker push $image`:$tag
}

# Cleanup *system wide* remove all unused containers, images, networks and volumes:
# docker system prune