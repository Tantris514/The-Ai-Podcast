$FilePath = $args[0]
$Gender = $args[1]
$text = Get-Content -Path $FilePath -Raw
Write-Host `n
if ($Gender -eq "f") {
    Write-Host $text -ForegroundColor Magenta
}
elseif ($Gender -eq "m") {
    Write-Host $text -ForegroundColor Blue
}
else {
    Write-Host "Invalid gender argument. Please use 'f' for female or 'm' for male." -ForegroundColor Red
}
