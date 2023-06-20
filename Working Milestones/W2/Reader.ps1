$ScriptPID = $PID
$PID >> PID.txt


# Add the System.speech assembly
Add-Type -AssemblyName System.speech

# Create a new SpeechSynthesizer object
$speech = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer
$speech.Rate = 2

# Check the second command line argument to determine the gender of the voice
if ($args[1] -eq "m") {
    $speech.SelectVoiceByHints([System.Speech.Synthesis.VoiceGender]::Male)
}
elseif ($args[1] -eq "f") {
    $speech.SelectVoiceByHints([System.Speech.Synthesis.VoiceGender]::Female)
}

# Read the text file (provided as the first command line argument) line by line
Get-Content -Path ".\\discussion\\$($args[0]).txt" | ForEach-Object {
    # Speak each line
    $speech.Speak($_)
}

# Dispose the SpeechSynthesizer object
$speech.Dispose()
