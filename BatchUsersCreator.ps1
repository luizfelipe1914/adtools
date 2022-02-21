# SCRIPT DE CRIAÇÃO DE USUÁRIOS EM LOTE NO ACTIVE DIRECTORY

Import-Module ActiveDirectory

$dataSource = Import-Csv -Path ".\users.csv" -Delimiter : -Encoding utf8
$domain = "parnamirim.rn"
$log = ".\BatchUser.log"
Function AddUserInDomain{
    param(
        $User
    )
    New-ADUser `
        -SamAccountName "$user.Login" ` #
        -Name "$user.GivenName $user.Surname" ` #
        -GivenName "$user.Givenname" ` #
        -Surname "$user.Surname" ` #
        -Enabled $True ` #
        -ChangePasswordAtLogon $True ` #
        -EmailAddress "$user.Email" ` #
        -AccountPassword $(ConvertTo-SecureString "$user.Password" -AsPlainText -Force) ` #
        -Path "$user.OU" `
        -UserPrincipalName "$user.Login@$domain"
    if($?)
    {
        return $True
    }
    return $False
}

Function SearchUser{
    param
    (
        [string[]] $Login,
        [string[]] $Name 
    )
    $user = Get-AdUser -Filter "UserPrincipalName -eq '$login@$domain'"
    if($user.Name -eq $name ){
        return 1
    }
    elseif ($user.Name -ne $name) {
        return 2
    }
    return 0
}

foreach ($user in $dataSource) {
    $logins = $user.login1, $user.login2, $user.login3
    $emails = $user.email1, $user.email2, $user.email3
    for($i = 1; $i -lt 3;$i++){
        switch ($(SearchUser -Login $logins[$i] -Name $user.name){
            0 
            {
                $usuario = [PSCustomObject]@{
                    Login = $logins[$i]
                    GivenName = $user.givenname
                    Surname = $user.surname
                    Password = $user.password
                    OU = $user.ou
                    Email = $emails[$i]
                }
                if($(AddUserInDomain -User $usuario)){
                    echo "--------------------------------------------------------------------------" | Tee-Object -FilePath $log
                    Write-Host -Message "Usuário de $usuario.GivenName $usuario.Surname foi criado com sucesso! " | Tee-Object -FilePath $log
                    Write-Host -Message "login: $usuario.Login" | Tee-Object -FilePath $log
                    Write-Host -Message "e-mail: $usuario.Email" | Tee-Object -FilePath $log
                }
                else 
                {
                    Write-Warning -Message "Erro ao criar o usuário de $usuario.GivenName $usuario.Surname" | Tee-Object -FilePath $log
                }
            }
            2 
            {
                $i++
            }
        
            1 
            {
                Write-Warning -Message "$usuario.GivenName $usuario.Surname já possui usuário!" | Tee-Object -FilePath $log  
                
            }
    }
}

