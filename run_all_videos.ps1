$pythonScript = "C:\Users\Chinmay\py_tools\main.py"
$videoDir = "C:\Users\Chinmay\Desktop\Test_videos"

Get-ChildItem -Path $videoDir -File | ForEach-Object {
    $videoPath = $_.FullName
    Write-Host "Processing video: $videoPath"
    python "$pythonScript" $videoPath
}