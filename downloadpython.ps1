[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$workingdir = (Get-Location).Path
if($PSVersiontable.PSVersion.Major -lt 3)
{
    Write-Warning "Por favor, baixe o Pyhon e o coloque na mesma pasta do script."
    Write-Output "Baixe em: https://www.python.org/ftp/python/3.9.0/python-3.9.0-embed-amd64.zip"
    Write-Output ("Salve nesse diretório: $workingdir `n e renomeie para python.zip" -f (Get-Location).Path)
    Write-Output "Baixe em: https://bootstrap.pypa.io/get-pip.py"
    Write-Output ("Salve nesse diretório: $workingdir" -f (Get-Location).Path)
    Read-Host "Pressione Enter quando estiver pronto!"
}
else
{
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.0/python-3.9.0-embed-amd64.zip -OutFile python.zip
    Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
}
if($PSVersiontable.PSVersion.Major -lt 5)
{
    if((Test-Path "$workingdir\python") -eq $False)
    {
        Add-Type -AssemblyName System.IO.Compression.FileSystem
        [IO.Compression.ZipFile]::ExtractToDirectory('python.zip', 'python\')
    }
    else
    {
        Write-Warning "Diretório $work\python encontrado. Exclua se necessário!"
    }
}
else
{
    Expand-Archive -LiteralPath python.zip -DestinationPath python\ -Force
}

((Get-Content python\python39._pth)) -Replace "#import", "import" | Set-Content python\python39._pth
Set-Content python\python39._pth -value "../", (Get-Content python\python39._pth)

python\python.exe get-pip.py
python\python.exe -m pip install -r requirements.txt

del python.zip
del get-pip.py
