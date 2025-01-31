document.getElementById('senha').addEventListener('input', function() {
    const senha = this.value;
  
    // Regras de validação
    const requisito1 = senha.length >= 8;
    const requisito2 = /[A-Z]/.test(senha);
    const requisito3 = /\d/.test(senha);
    const requisito4 = /[!@#$%^&*(),.?":{}|<>]/.test(senha);
  
    // Atualiza os requisitos na interface
    document.getElementById('requisito1').classList.toggle('valid', requisito1);
    document.getElementById('requisito2').classList.toggle('valid', requisito2);
    document.getElementById('requisito3').classList.toggle('valid', requisito3);
    document.getElementById('requisito4').classList.toggle('valid', requisito4);
});  