# Define the directory path and the target string
$directoryPath = "C:\Users\vrdhn\Desktop\CS"
$targetString = "mss"

# Get all Python files in the directory and its subdirectories
$pythonFiles = Get-ChildItem -Path $directoryPath -Recurse -Filter *.py

# Iterate through each Python file
foreach ($file in $pythonFiles) {
    # Read the content of the file
    $fileContent = Get-Content -Path $file.FullName -Raw

    # Check if the target string exists in the file content
    if ($fileContent -match $targetString) {
        # Print the name of the file
        Write-Host "File with target string found: $($file.FullName)"
    }
}
