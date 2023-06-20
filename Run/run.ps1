# Clear contents of PID.txt file
echo "" > .\PID.txt

# Start the first Python script in the current console window
$generate_AI_filespy = "generate_AI_files.py"

try {
    $argument = $args[0]  # Retrieve the first command-line argument if available
    if (![string]::IsNullOrEmpty($argument)) {
        $process1 = Start-Process -FilePath "python.exe" -ArgumentList $generate_AI_filespy, $argument -NoNewWindow -PassThru
    } else {
        $process1 = Start-Process -FilePath "python.exe" -ArgumentList $generate_AI_filespy -NoNewWindow -PassThru
    }
} catch {
    Write-Host "An error occurred while starting the Python script: $_"
}


try {
$process1 = Start-Process -FilePath "python.exe" -ArgumentList $generate_AI_filespy, $args[0]  -NoNewWindow -PassThru
}
catch{
write-host "No argument entered, launching default prompt."
}

# Get the PID of the first Python script
$pythonScriptPID1 = $process1.Id
Write-Host "Python script PID: $pythonScriptPID1"
$pythonScriptPID1 >> .\PID.txt

# Start the second Python script in the current console window
$Turn_mediatorpy = "Turn_mediator.py"
$process2 = Start-Process -FilePath "python.exe" -ArgumentList $Turn_mediatorpy -NoNewWindow -PassThru

# Get the PID of the second Python script
$pythonScriptPID2 = $process2.Id
Write-Host "Python script PID: $pythonScriptPID2"
$pythonScriptPID2 >> .\PID.txt
