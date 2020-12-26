$(document).ready(function() {


  $('section.song > header.song-header > h2.song-title > a').each(function () {
    var href = $(this).attr("href");
    href = href.replace("canciones", "cancionesAjax");
    $(this).qtip({
       content: {
          url: href,
          method: 'get'
       }
    }); 
  });

});