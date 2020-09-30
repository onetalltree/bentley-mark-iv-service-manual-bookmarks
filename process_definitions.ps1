# Powershell script to

Get-Content .\bookmark_definitions.csv | python .\process_definitions.py | Out-File bookmarks.txt -Encoding ASCII