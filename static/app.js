// Código para gerenciar a mudança de arquivos e exibir a imagem no <figure>
$('form input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length === 0) {
        console.log('Sem imagem para mostrar');
    } else {
        // Lista de tipos de arquivo permitidos
        const tiposAceitos = ['image/jpeg', 'image/png', 'image/svg+xml'];

        // Verifica se o tipo do arquivo está na lista de tipos permitidos
        if (tiposAceitos.includes(arquivos[0].type)) {
            $('img').remove();  // Remove imagens antigas
            let imagem = $('<img class="img-fluid">');
            imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
            $('figure').prepend(imagem);
        } else {
            alert('Formato não suportado');
        }
    }
});

// Código para ocultar automaticamente os alertas após 3 segundos
$(document).ready(() => {
    const tempoParaOcultar = 3000;  // 3 segundos

    // Encontra todos os elementos com a classe 'alert' e define um temporizador para escondê-los
    $('.alert').each(function () {
        const alerta = $(this);
        setTimeout(() => {
            alerta.fadeOut();  // Oculta suavemente o alerta após 3 segundos
        }, tempoParaOcultar);
    });
});
