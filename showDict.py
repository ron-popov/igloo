# Actionable commands which are passed into a function for further processing
# Python character limit ignored due to performance concerns with powershell

show_command_set = {
	'show powershell version':'$PSVersionTable | Format-Table -HideTableHeaders',
	'show ip public':'(Invoke-WebRequest https://itomation.ca/mypublicip).content',
	'show ipv6 public':'(Invoke-WebRequest ip6only.me/api/).content',
	'show ip address':'Get-NetIPAddress -AddressFamily IPv4 | Select-Object -Property ifIndex,InterfaceAlias,IPAddress,PrefixLength,PrefixOrigin | Sort-Object -Property IPAddress | Format-Table -AutoSize',
	'show ipv6 address':'Get-NetIPAddress -AddressFamily IPv6 | Select-Object -Property ifIndex,InterfaceAlias,IPAddress,PrefixLength,PrefixOrigin | Sort-Object -Property IPAddress | Format-Table -AutoSize',
	'show crypto':'Get-VpnConnection | Select-Object -Property Name, ServerAddress,TunnelType,AuthenticationMethod, ConnectionStatus',
	'show log app':'Get-EventLog -LogName Application -Newest 300 | Select-Object -Property TimeGenerated, Message',
	'show log sys':'Get-EventLog -LogName System -Newest 300 | Select-Object -Property TimeGenerated, Message',
	'show log sec':'Get-EventLog -LogName Security -Newest 300 | where {$_.timewritten -gt $date} | Select-Object -Property TimeGenerated,UserName | fl *',
	'show log wev':'eventvwr.msc',
	'show gpo':'gpresult /R',
	'show svc':'Get-Service | Sort-Object -Property Status -Descending | Format-Table -AutoSize',
	'show proc':'Get-Process | Sort-Object -Property CPU -Descending',
	'show proc top':'Get-Process | Sort-Object -Property WS | Select-Object -Last 10 | sort-object -Property CPU -Descending',
	'show int':'Get-NetAdapter',
	'show arp':'arp -a',
	'show tcp':'netstat -n',
	'show dns cache':'Get-DnsClientCache | Sort-Object -Property Entry | Format-Table -AutoSize',
	'show dns server':'Get-DnsClientServerAddress | Sort-Object -Property AddressFamily | Format-List',
	'show drives':'Get-Volume | Select-Object -Property DriveLetter, FileSystemLabel,DriveType,FileSystem,Size,HealthStatus, OperationalStatus,Path,ObjectId | Sort-Object -Property DriveLetter -Descending | Format-List',
	'show fwall profile':'Get-NetFirewallProfile',
	'show ip route':'Get-NetRoute -AddressFamily ipv4 | Sort-Object -Property DestinationPrefix | Format-Table -Autosize',
	'show ipv6 route':'Get-NetRoute -AddressFamily ipv6 | Sort-Object -Property DestinationPrefix | Format-Table -Autosize',
}