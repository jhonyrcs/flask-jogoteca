$('form input[type="file"]').change(event => {
  let arquivos = event.target.files;
  if (arquivos.length === 0) {
      console.log('Sem imagem para mostrar');
  } else {
      // Definindo uma lista de tipos de arquivo permitidos
      const tiposAceitos = ['image/jpeg', 'image/png', 'image/svg+xml'];
      
      // Verificando se o tipo do primeiro arquivo está na lista de tipos permitidos
      if (tiposAceitos.includes(arquivos[0].type)) {
          $('img').remove();
          let imagem = $('<img class="img-fluid">');
          imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
          $('figure').prepend(imagem);
      } else {
          alert('Formato não suportado');
      }
  }
});
