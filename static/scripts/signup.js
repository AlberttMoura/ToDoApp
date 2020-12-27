const x = document.getElementById('signup')
var inputs = document.getElementsByTagName('input')

x.addEventListener('click', (event)=>{
    
    for(let i = 1; i < inputs.length - 1; i++){

        //Verificando se os campos estão preenchidos
        if(!inputs[i].value){
            document.getElementById('required-field' + [i]).className = 'warning-on'
            event.preventDefault()
        }

        else{
            document.getElementById('required-field' + [i]).className = 'warning-off'

            //Verificando e-mail
            if(inputs[i].name == 'email'){
                if(!inputs[i].value.includes("@")){
                    document.getElementById('invalid-email').className = 'warning-on'
                    event.preventDefault()
                }
                else{
                    if(inputs[i].value.slice(inputs[i].value.length-4).toLocaleLowerCase() != ".com" || inputs[i].value[inputs[i].value.length-5] == '@'){
                        document.getElementById('invalid-email').className = 'warning-on'
                        event.preventDefault()
                    }
                    else{
                        document.getElementById('invalid-email').className = 'warning-off'
                    }

                }
            }
            //Verificando senhas
            else if(inputs[i].name.toLocaleLowerCase() == "password2") {
                if(inputs[i].value != inputs[i-1].value) {
                    document.getElementById('passwords-dont-match').className = 'warning-on'
                    event.preventDefault()
                }
                else{
                    document.getElementById('passwords-dont-match').className = 'warning-off'
                }
            }

        }

    }
    
})