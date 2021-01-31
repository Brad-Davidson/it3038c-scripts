$ipv4= (Get-NetIPAddress).IPv4Address | Select-String "192*" #The IP address of the machine
$user= $env:USERNAME #Gets the user name of the current logged in user
$psversion= $host.version.Major
$myhost= hostname #gets the hostname of the machine
$date= (Get-Date) #gets the current datetime
$body= @"
This machine's IP is $ipv4
User is $user
Hostname is $myhost
Version $psversion
Today's Date is $date
"@
Write-Host($body)
Send-MailMessage -To "davidsbw@mail.uc.edu" -From "davidsbw@mail.uc.edu" -Subject "IT3038C Windows SysInfo" -Body "$body" -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential) #sends an email to davidsbw@mail.uc.edu