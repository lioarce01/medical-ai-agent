$Url = "http://localhost:8000/api/predict"
$PatientId = "test123"

For ($i = 1; $i -le 10; $i++) {
    If ($i % 3 -eq 0) {
        $HeartRate = Get-Random -Minimum 130 -Maximum 140 
    } else {
        $HeartRate = Get-Random -Minimum 60 -Maximum 80    
    }

    Write-Output "[$i] Sending heart_rate=$HeartRate"

    $Payload = @{
        patient_id = $PatientId
        vitals = @{
            heart_rate = $HeartRate
        }
    } | ConvertTo-Json -Depth 3

    $Response = Invoke-RestMethod -Uri $Url -Method Post -Body $Payload -ContentType "application/json"

    Write-Output "Response: $($Response | ConvertTo-Json -Depth 3)"

    Start-Sleep -Seconds 2
}
