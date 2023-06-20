$pidFilePath = "PID.txt"  # Specify the path to the file containing PIDs

try {
    # Read the file and retrieve the list of PIDs
    $pids = Get-Content -Path $pidFilePath

    # Terminate each process by PID
    foreach ($processId in $pids) {
        try {
            $process = Get-Process -Id $processId -ErrorAction Stop
            Write-Host "Terminating process with PID: $processId"
            $process | Stop-Process -Force
        } catch {
		continue
        }
    }
} catch {
    Write-Host "Error occurred while reading PID file: $_.Exception.Message"
}
